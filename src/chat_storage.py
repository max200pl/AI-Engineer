import json
from pathlib import Path

import ollama

DEFAULT_SYSTEM = "Твой дружелюбный помощник. Отвечай кратко, на русском."

def load_chat_history(path: Path, system_prompt: str = DEFAULT_SYSTEM) -> list:
    """ Загрузить историю чата из файла.

    Если файл не существует или пуст, возвращает список с системным сообщением.
    """
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    return [{"role": "system", "content": system_prompt}]

def save_chat_history(path: Path, messages: list) -> None:
    """ Сохранить историю чата в файл.

    Создает файл, если он не существует.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
        
def reset_chat_history(path: Path, messages: list) -> None:
    messages[:] = messages[:1]
    if path.exists():
        path.unlink()
        
def print_chat_history(messages: list) -> None:
    for message in messages[1:]:
        role = "Ты" if message["role"] == "user" else "Бот"
        print(f"{role}: {message['content']}")
        
def  ask_model(messages: list, MODEL: str) -> str:
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

