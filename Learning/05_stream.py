import ollama

MODEL = "llama3.2:3b"

stream = ollama.chat(
    model=MODEL,
      messages=[{"role": "user", "content": "Расскажи короткую историю про кота-программиста."}],
    stream=True,
)

full_answer = ""
for chunk in stream:
    piece = chunk["message"]["content"]
    full_answer += piece
    print(piece, end="", flush=True)

print()  # Печатаем перевод строки после завершения потока
print("Полный ответ:", full_answer)

