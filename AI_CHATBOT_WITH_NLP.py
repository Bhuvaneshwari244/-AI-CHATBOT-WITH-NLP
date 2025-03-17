import nltk
import random
import spacy
from nltk.chat.util import Chat, reflections

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses using pattern-matching
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]),
    (r"how are you", ["I'm doing well, thank you!", "I'm great! How about you?"]),
    (r"what (.*) name", ["I'm a chatbot created to assist you!", "You can call me AI bot."]),
    (r"what (.*) do", ["I can answer questions and chat with you! Try asking me something."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care! Come back soon!"]),
    (r"(.*)", ["I'm not sure how to answer that. Could you rephrase?"])
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def process_input(user_input):
    """Process user input using spaCy NLP"""
    doc = nlp(user_input)  # Tokenization and NLP processing
    return " ".join([token.text.lower() for token in doc])  # Normalization

def chatbot_response(user_input):
    """Generate a response from the chatbot"""
    processed_input = process_input(user_input)
    print(f"[DEBUG] Processed Input: {processed_input}")  # Debugging step
    response = chatbot.respond(processed_input)
    return response if response else "I'm not sure how to answer that. Can you clarify?"

def main():
    """Main function to run the chatbot"""
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["bye", "exit", "quit"]:
                print("Chatbot: Goodbye! Have a great day!")
                break
            print("Chatbot:", chatbot_response(user_input))
        except Exception as e:
            print(f"Chatbot: Oops! Something went wrong. Error: {e}")

if __name__ == "__main__":
    main()
