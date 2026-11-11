import ollama

MODEL = "llama3.2:3b"

messages = [
        {"role": "system", "content": "Ты дружелюбный помощник. Отвечай кратко, на русском."},
]

print("Чат запущен. Напиши \"выход\" для завершения.")

while True:
    user_input = input("Ты: ")

    if user_input.lower() in ("выход", "exit", "quit"):
        print("Чат завершен.")
        break

    if user_input.lower() in ("сброс", "reset"):
        messages = messages[:1]
        print("История чата сброшена.")
        continue

    messages.append({"role": "user", "content": user_input})
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )
    answer = response["message"]["content"]
    messages.append({"role": "assistant", "content": answer})

    print(f"Бот: {answer}\n")