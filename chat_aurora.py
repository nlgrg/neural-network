import requests
import sys

# Initialize chat history and set the maximum chat history length
chat_history = []
max_chat_history = 8

# Get the URL and system prompt from command-line arguments
url = sys.argv[1]
system_prompt = sys.argv[2]

# Function to respond to user input
def respond(prompt):
    prompt = prompt.strip()
    global chat_history
    chat_history = chat_history[-max_chat_history:]  # Truncate chat history to maintain maximum length
    if prompt == "clear conversation":
        chat_history = []  # Clear the conversation history
        return "Cleared Conversation."
    else:
        # Append user input to chat history, including system prompt if necessary
        chat_history.append(prompt if len(chat_history) < 2 else "# User Instruction: " + prompt)
        
        # Prepare data for API request
        response = requests.post(url, json={
            "data": [
                system_prompt,
                "\n".join(chat_history),
                "",
                "",
                0.77,
                0.9,
                22,
                192,
                True,
                0.0,
                1.11,
                "\n\n",
            ]
        }).json()
        
        data = response["data"][0]  # Extract the generated response
        chat_history.append("# You gave this response: " + data)  # Append generated response to chat history
        print()  # Print an empty line for formatting
        return "(Aurora): " + data  # Return the generated response with a prompt label

# Get the username from the user
username = input("Username: ")

# Main loop for user interaction
while True:
    print()  # Print an empty line for formatting
    user_input = input(f'({username}): ')  # Get user input
    print(respond(user_input))  # Call the respond function and print the generated response
