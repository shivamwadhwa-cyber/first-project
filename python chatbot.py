import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"\bhi\b|\bhello\b|\bhey\b", user_input):
        return "Hello! How can I help you today?"

    elif re.search(r"\bhow are you\b", user_input):
        return "I'm doing great! Thanks for asking 😊"

    elif re.search(r"\byour name\b", user_input):
        return "I am a simple Python Chatbot."

    elif re.search(r"\bhelp\b", user_input):
        return "Sure! Tell me what you need help with."

    elif re.search(r"\bbye\b|\bexit\b", user_input):
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Chatbot:", response)

    if user.lower() in ["bye", "exit"]:
        break
