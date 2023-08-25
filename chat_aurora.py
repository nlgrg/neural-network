import requests
import sys
chat_history = []


max_chat_history = 8

url = sys.argv[1]
system_prompt = sys.argv[2]

def respond(prompt):
    prompt = prompt.strip()
    global chat_history
    chat_history=chat_history[-max_chat_history:]
    if prompt=="clear conversation":
        chat_history = []
        return "Cleared Conversation."
    else:
        chat_history.append(prompt if len(chat_history) < 2 else "# User Instruction: " + prompt)
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
        data = response["data"][0] 
        chat_history.append("# You gave this response: " + data)
        print()
        return "(Aurora): " + data

username = input("Username: ")
while True:
    print()
    print(respond(input(f'({username}): ')))
