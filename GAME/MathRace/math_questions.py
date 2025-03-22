import random

def generate_question():
    """Generates a simple math problem."""
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])
    
    if operator == "/":  
        num1 = num2 * random.randint(1, 5)  # Ensure whole number division

    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)
    
    if operator == "/":
        correct_answer = int(correct_answer)  # Convert float to int

    return question, str(correct_answer)
