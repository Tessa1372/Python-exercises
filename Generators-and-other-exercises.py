#Generator Problems

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b       
fibon = fibonacci_generator()
print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(next(fibon), end=' ')


def range_generator(n):
    current = 1
    while current <= n:
        yield current
        current += 1
print("\nGenerating numbers from 1 to 5:")
range_gen = range_generator(5)
for num in range_gen:
    print(num, end=' ')


def prime_generator():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
prime_gen = prime_generator()
print("\nFirst 10 prime numbers:")
for _ in range(10):
    print(next(prime_gen), end=' ')



def char_counter(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in sorted(char_counts.items()):
        yield (char, count)
print("\nCounting characters in 'hello world':")
text = "hello world"
for char, count in char_counter(text):
    print(f"'{char}': {count}")


#List Comprehension problems

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = [num * num for row in matrix for num in row if num % 2 == 0]
print(result)  


words = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]
result = [word.upper() for row in words for word in row if len(word) > 3]
print(result)  
