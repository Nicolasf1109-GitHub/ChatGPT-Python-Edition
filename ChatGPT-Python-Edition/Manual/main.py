import openai
import os

# Set your OpenAI API key here (ensure it's stored securely)
openai.api_key = "nuh uh your not having my API key, use your own :D"

def chat_with_gpt():
    print("ChatGPT Command-Line Interface")
    print("Type 'exit' to quit the conversation.")
    
    conversation = []
    
    while True:
        # User input
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Append user input to conversation history
        conversation.append({"role": "user", "content": user_input})
        
        try:
            # Make a request to OpenAI API for a response
            response = openai.ChatCompletion.create(
                model="Model here",  # You can change to other models, like 'gpt-3.5-turbo'
                messages=conversation
            )
            
            # Extract and print the bot's reply
            bot_reply = response['choices'][0]['message']['content']
            print("ChatGPT: " + bot_reply)
            
            # Append bot's reply to conversation history
            conversation.append({"role": "assistant", "content": bot_reply})
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_gpt()
