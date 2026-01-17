from dotenv import load_dotenv
import os

load_dotenv()
print('Hello from repository!')
def print_author():
    author = os.getenv('AUTHOR')# Допишите здесь ваш код
    print(f"Автор проекта: {author}")
print_author()