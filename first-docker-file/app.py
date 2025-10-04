import os

name = os.getenv("NAME", "World")
print(f"Hello {name}! Welcome to Docker")
