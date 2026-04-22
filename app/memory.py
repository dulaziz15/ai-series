import json

chat_history = []


def save_message(role, content):

    chat_history.append({
        "role": role,
        "parts": [content]
    })


def get_history():

    return chat_history


def save_to_file():

    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=2)


def load_from_file():

    global chat_history

    try:
        with open("chat_history.json", "r") as f:
            chat_history = json.load(f)
    except:
        chat_history = []