from agent.validator import validate_state, ValidationError
from tiktok.api import submit_ad
from tiktok.errors import explain_api_error

class ConversationAgent:
    def __init__(self):
        self.state = {
            "campaign_name": None,
            "objective": None,
            "ad_text": None,
            "cta": None,
            "music": {
                "type": None,
                "music_id": None
            }
        }
        self.is_finished = False

    def handle_input(self, user_input: str) -> str:
        self._update_state(user_input)

        # Check what's missing FIRST
        missing = self._next_missing_field()
        if missing:
            return self._ask_for_field(missing)

        # Now validate
        try:
            validate_state(self.state)
            result = submit_ad(self.state)
            self.is_finished = True
            return f"✅ Ad submitted successfully:\n{result}"

        except ValidationError as ve:
            # IMPORTANT FIX: re-ask the problematic field
            return (
                f"{ve.message}\n\n"
                "Please choose one of the following:\n"
                "- Enter a music ID\n"
                "- Type 'upload' to upload custom music"
            )

        except Exception as api_error:
            return explain_api_error(api_error)

    def _update_state(self, user_input: str):
        if not self.state["campaign_name"]:
            self.state["campaign_name"] = user_input
            return

        if not self.state["objective"]:
            self.state["objective"] = user_input
            return

        if not self.state["ad_text"]:
            self.state["ad_text"] = user_input
            return

        if not self.state["cta"]:
            self.state["cta"] = user_input
            return

        if self.state["music"]["type"] in (None, "none"):
            if user_input.lower() == "none":
                self.state["music"]["type"] = "none"
                self.state["music"]["music_id"] = None
            elif user_input.lower() == "upload":
                self.state["music"]["type"] = "uploaded"
                self.state["music"]["music_id"] = "mock_uploaded_music_id"
            else:
                self.state["music"]["type"] = "existing"
                self.state["music"]["music_id"] = user_input

    def _next_missing_field(self):
        if not self.state["campaign_name"]:
            return "campaign_name"
        if not self.state["objective"]:
            return "objective"
        if not self.state["ad_text"]:
            return "ad_text"
        if not self.state["cta"]:
            return "cta"
        if not self.state["music"]["type"]:
            return "music"
        return None
        
    def _ask_for_field(self, field: str) -> str:
        questions = {
            "campaign_name": "What should we name the campaign?",
            "objective": "What is the campaign objective? (Traffic or Conversions)",
            "ad_text": "What is the ad text? (Max 100 characters)",
            "cta": "What is the call-to-action?",
            "music": (
                "Do you want to use music?\n"
                "- Type a music ID\n"
                "- Type 'upload' to upload custom music\n"
                "- Type 'none' for no music"
            )
        }
        return questions[field]
