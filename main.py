from agent.conversation import ConversationAgent

def main():
    agent = ConversationAgent()
    print("🎯 TikTok Ad Creation Agent\n")

    while not agent.is_finished:
        user_input = input("You: ")
        response = agent.handle_input(user_input)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    main()
