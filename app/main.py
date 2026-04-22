from memory import save_message, get_history, save_to_file, load_from_file
from llm_client import model
from prompt import research_prompt

load_from_file()

while True:

    question = input("\nTanya: ")

    if question == "exit":
        save_to_file()
        break

    save_message("user", question)

    messages = get_history()

    response = model.generate_content(research_prompt(question))

    answer = response.text

    save_message("model", answer)

    print("\nJawaban:\n")
    print(answer)