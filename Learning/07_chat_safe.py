import sys
from pathlib import Path

import httpx
from matplotlib.pylab import rint
import ollama

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # корень проекта
from src.chat_storage import load_chat_history, save_chat_history, reset_chat_history, print_chat_history, ask_model

MODEL = "llama3.2:3b"
HISTORY_PATH = Path("data") / "chat_history.json"


def main():
        
    messages = load_chat_history(HISTORY_PATH)

    try:
    # Main chat loop
        while True:
            user_input = input("Ты: ")
            # Check for exit command
            if user_input.lower() in ("выход", "exit", "quit"):
                print("Чат завершен.")
                break
            # Handle chat reset command
            if user_input.lower() in ("сброс", "reset"):
                reset_chat_history(HISTORY_PATH, messages)
                print("История чата сброшена.")
                print_chat_history(messages)
                continue
            # Append user message and get assistant response
            messages.append({"role": "user", "content": user_input})
            print("Бот: ", end="", flush=True)
            try:
                full_answer = ask_model(messages, MODEL)
            except httpx.ConnectError as e:
                print(f"\nОшибка при подключении к модели: {e}")
                messages.pop()
                continue
            except ollama.ResponseError as e:
                print(f"\nОшибка при обращении к модели: {e}")
                messages.pop()
                continue

            # Print a newline after streaming the assistant's response
            print()  # Печатаем перевод строки после завершения потока
            # Append assistant response to chat history and save it
            messages.append({"role": "assistant", "content": full_answer})

          
    except (KeyboardInterrupt, EOFError): #
        if messages[-1]["role"] == "user":     # последний вопрос остался без ответа
            messages.pop()
        print("\nЧат завершен пользователем.")
    finally:
        save_chat_history(HISTORY_PATH, messages) 
        print("История чата сохранена.")
if __name__ == "__main__":
    main()
    