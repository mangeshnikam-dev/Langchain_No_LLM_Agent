from app.agent.agent import NoLLMAgent

def main():
    agent = NoLLMAgent()
    print("================================")
    print(" LangChain No-LLM Agent")
    print(" Type 'exit' to quit")
    print("================================")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() == "exit":
            break
        response = agent.invoke(user_input)
        print(f"\nAgent: {response}")

if __name__ == "__main__":
    main()
