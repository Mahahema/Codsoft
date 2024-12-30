import re

def chatbot_response(user_input):
    
    user_input = user_input.lower()

   
    if re.match(r'.*(hi|hello|hey|hola).*', user_input):
        return "Hello! How can I assist you today?"

   
    elif re.match(r'.*(your name|who are you).*', user_input):
        return "I am a chatbot created to help you with your queries."

    
    elif re.match(r'.*(what can you do|what is your purpose).*', user_input):
        return "I can answer simple questions, give information, or just chat with you!"

    
    elif re.match(r'.*(help|assist|support).*', user_input):
        return "Sure! How can I help you?"

   
    elif re.match(r'.*(weather|forecast).*', user_input):
        return "Sorry, I can't provide the weather forecast right now. Please check your favorite weather app!"

   
    elif re.match(r'.*(bye|goodbye|see you).*', user_input):
        return "Goodbye! Have a nice day!"

    
    else:
        return "Sorry, I didn't quite understand that. Can you please rephrase?"


def chat():
    print("Chatbot: Hi, I'm here to help you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        
        if re.match(r'.*(bye|goodbye|exit).*', user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chat()
