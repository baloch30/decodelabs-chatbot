responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm just code, but I'm running great!",
    "what is your name": "I'm DecodeBot, your first AI chatbot.",
    "what can you do": "I can chat using simple rules. Try greeting me!",
    "help": "Try: hello, how are you, what is your name, or bye.",
}

print("DecodeBot: Hi! Type 'bye' or 'exit' to quit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ("bye", "exit"):
        print("DecodeBot: Goodbye! See you soon.")
        break

    reply = responses.get(user_input, "Sorry, I do not understand that.")
    print("DecodeBot: ", reply)