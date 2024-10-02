import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression) 
    return expression, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()
    
for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1
        
end_time = time.time()
total_time = round(end_time - start_time, 2)
            
print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")