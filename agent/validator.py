class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def validate_state(state: dict):
    if not state["campaign_name"] or len(state["campaign_name"]) < 3:
        raise ValidationError("Campaign name must be at least 3 characters.")

    if state["objective"] not in ("Traffic", "Conversions"):
        raise ValidationError("Objective must be Traffic or Conversions.")

    if not state["ad_text"] or len(state["ad_text"]) > 100:
        raise ValidationError("Ad text is required and must be under 100 characters.")

    if not state["cta"]:
        raise ValidationError("CTA is required.")

    music = state["music"]

    if music["type"] == "none" and state["objective"] == "Conversions":
        raise ValidationError(
            "Music is required for Conversion campaigns. "
            "Please choose existing or upload custom music."
        )
