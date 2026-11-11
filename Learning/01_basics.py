age = 30
price = 19.99
name = "John"
is_dev = True
nothing = None

print(type(age), type(price), type(name), type(is_dev), type(nothing))

langs = ["Python", "JavaScript", "C++"]
langs.append("Java")
print(langs[0], langs[-1])
print(len(langs))

user = {"name": "John", "age": 30}
print(user["name"], user["age"])

if age > 18 and is_dev:
    print("Adult developer")
else:
    print("Not an adult developer")

for lang in langs:
    print(lang)

for i in langs:
    print(i)

for i in range(3):
    print(i)

for key, value in user.items():
    print(f"{key}: {value}") # f-string for formatted output

# --- Functions ---

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}!")

print(greet("Alice"))
print(greet("Bob", "Hi"))

# -- List Comprehensions

nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]          # map each number to its square
evens = [n for n in nums if n % 2 == 0]  # filter even numbers
print(squares, evens)

