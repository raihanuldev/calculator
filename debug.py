import math

def calculator():
    print("Best Calculator")
    print("Operations -> +, -, *, /, %, ^ (power), √ (square root)")
    
    try:
        result = float(input("Enter your first number: "))
        
        while True:
            operator = input("Enter operator (+, -, *, /, %, ^, √) or 'q' to quit: ").strip()
            
            if operator.lower() == 'q':
                print("Final Result:", result)
                break
            
            if operator == '√':  # Square root
                if result < 0:
                    print("Error: Cannot calculate square root of a negative number!")
                    continue
                result = math.sqrt(result)
            
            else:
                num = float(input("Enter next number: "))
                
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    if num == 0:
                        print("Error: Cannot divide by zero!")
                        continue
                    result /= num
                elif operator == '%':
                    if num == 0:
                        print("Error: Modulus by zero is not allowed!")
                        continue
                    result %= num  # ✅ Correct modulus operation
                elif operator == '^':  # Power operation
                    result = result ** num  # ✅ Fixed exponentiation
                else:
                    print("Invalid Operator! Please enter a valid one.")
                    continue
            
            print("Current Result:", result)

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")

calculator()
