import ollama
from pathlib import Path
import json

MODEL = "llama3.2:3b"

messages = [
        {"role": "system", "content": "Ты дружелюбный помощник. Отвечай кратко, на русском."},
]

print("Чат запущен. Напиши \"выход\" для завершения.")

# Variables for chat history file and directory
name_file = "chat_history.json"
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
chat_history_path = data_dir / name_file

# Function to save chat history to file
def save_chat_history():
    with open(chat_history_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def load_chat_history():
    global messages
    if chat_history_path.exists():
        with open(chat_history_path, "r", encoding="utf-8") as f:
            chat_history = json.load(f)
        if chat_history:
            messages = chat_history

def reset_chat_history():
    global messages
    messages = messages[:1]
    if chat_history_path.exists():
        chat_history_path.unlink()
        
def print_chat_history():
    for message in messages[1:]:
        role = "Ты" if message["role"] == "user" else "Бот"
        print(f"{role}: {message['content']}")
        
def  ask_model(messages) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        stream=True
    )
    full_answer = ""
    for chunk in response:
        piece = chunk["message"]["content"]
        full_answer += piece
        print(piece, end="", flush=True)
    print()
    return full_answer

load_chat_history()

# Main chat loop
while True:
    user_input = input("Ты: ")
# Check for exit command
    if user_input.lower() in ("выход", "exit", "quit"):
        print("Чат завершен.")
        break
# Handle chat reset command
    if user_input.lower() in ("сброс", "reset"):
        reset_chat_history()
        print("История чата сброшена.")
        print_chat_history()
        continue
# Append user message and get assistant response
    messages.append({"role": "user", "content": user_input})
    print("Бот: ", end="", flush=True)
    full_answer = ask_model(messages)
        
# Print a newline after streaming the assistant's response
    print()  # Печатаем перевод строки после завершения потока
# Append assistant response to chat history and save it
    messages.append({"role": "assistant", "content": full_answer})

    save_chat_history()

print("История чата сохранена.")
    