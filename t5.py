# Basic Chatbot

def chatbot_response(user_input):
    """Return chatbot reply based on user input."""
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! 😊"
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a nice day!"
    elif "your name" in user_input:
        return "I'm ChatBot 1.0 🤖"
    else:
        return "Sorry, I didn't understand that."

def main():
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if "bye" in user_input.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    main()
