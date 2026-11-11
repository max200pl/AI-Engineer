import ollama

MODEL = "llama3.2:3b"

response = ollama.chat(
    model=MODEL,
    messages=[
       {"role": "system", "content": "Отвечай как пират"},
       {"role": "user", "content": "Чем list отличается от tuple?"}
    ]
)

print(response["message"]["content"])