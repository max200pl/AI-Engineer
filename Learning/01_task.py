def stats(numbers):
    if not numbers:
        return None
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "len": len(numbers),
        "avg": sum(numbers) / len(numbers),
        "evens": [n for n in numbers if n % 2 == 0],
    }

print(stats([4, 8, 15, 16, 23, 42]))
print(stats([]))