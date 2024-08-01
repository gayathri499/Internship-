# Simple rule-based chatbot

# Define the rules for the chatbot
rules = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "how are you": "I'm just a bunch of code, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to help you with your queries. You can call me Chatbot.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! If you have any more questions, feel free to ask.",
}

def chatbot_response(user_input):
    # Convert the user input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Check if the user input matches any of the predefined rules
    for key in rules:
        if key in user_input:
            return rules[key]
    
    # Default response if no rules match
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Chatbot: Hello! I am a simple rule-based chatbot. How can I assist you?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
