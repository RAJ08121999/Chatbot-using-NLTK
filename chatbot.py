from nltk.chat.util import Chat, reflections

patterns_responses = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?']),
    (r'good morning',['very good morning dear']),
    (r'what is your name?|who are you?', ['I am a chatbot created for demo purposes.']),
    (r'how are you?', ['I am just a program, but I am functioning as expected!']),
    (r'quit|exit|bye', ['Goodbye!', 'See you later!']),
    (r'(.*)', ['I am not sure how to respond to that.'])
]

class SimpleChatbot:
    def __init__(self):
        self.chatbot = Chat(patterns_responses, reflections)

    def get_response(self, user_input):
        return self.chatbot.respond(user_input)

def start_chat():
    bot = SimpleChatbot()
    print("Chatbot: Hi! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
