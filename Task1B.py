class SimpleChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hi there! How can I help you today?",
            "hi": "Hello! How can I assist you?",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "what is your name": "I'm a simple chatbot created by a Python script.",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm not sure how to respond to that. Can you please rephrase?"
        }
    
    def respond(self, user_input):
        user_input = user_input.lower()
        for key in self.rules:
            if key in user_input:
                return self.rules[key]
        return self.rules["default"]

# Create an instance of the chatbot
chatbot = SimpleChatbot()

# Simulate a conversation
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")
