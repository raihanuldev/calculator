def calculator():
    print("Hello World");
    print("Operations: +, -, *, /")
    
    try:
        result = float(input("Enter Frist Number=> "));
        
        while True:
            operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
            if operator.lower()=='q':
                print("Final Result ",result);
                break;
            num = float(input("Enter next number: "))
            if operator=='+':
                result += num;
            elif operator=='-':
                result -= num;
            elif operator == '*':
                result *= num;
            elif operator == '/':
                if num == 0:
                    print("Error! Division by zero.")
                    continue
                result /= num
            else:
                print("Invaild Operator");
                continue
            print("Current Result:", result)
            
        
    except ValueError:
        print("Error")
        


calculator();