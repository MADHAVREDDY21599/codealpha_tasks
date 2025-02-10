
import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Hey!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Microsoft. You can call me Copilot.",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you! How can I help you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem!", "It's okay, no worries.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a nice day!", "See you later!",]
    ],
    [
        r"(.*)",
        ["I’m here to help you with anything you need.",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chatbot():
    print("Hi! I'm your friendly chatbot. Type something to start a conversation.")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Goodbye! Have a nice day!")
            break
        else:
            response = chatbot.respond(user_input)
            print(response)

# Start the chatbot
if __name__ == "__main__":
    nltk.download('punkt')
    start_chatbot()
