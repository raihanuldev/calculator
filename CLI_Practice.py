import math

# //write a function for Airthmatic Opreator
def calculetor():
    print("Best Calculetor")
    print("Operationss-> +,-,*,%")
    # error handleing 
    try:
        result = float(input("Enter Your Frist Number: "))
        while(True):
            operator = input("enter your Opratior=> +,-,*,^,sq,% 'q' to quit:")
            if(operator.lower()=='q'):
                print("Result is => ",result);
                break;
            if operator =='sq':
                if result <0:
                    print("Error:  cannot calculate Square Root of negative number")
                    continue;
                result = math.sqrt(result);
            num = float(input("Enter next number: "))
            if operator=='+':
                result +=num;
            elif operator=='-':
                result -= num;
            elif operator == '*':
                result *= num;
            elif operator =='/':
                if(num==0):
                    print("Can't divide by Zero");
                    continue;
                result/=num;
            elif operator == '%':
                result %= num
            elif operator == '^':
                result = result ** num;
            else:
                print("Invaild Oprarrtor");
                continue;
            print("Current Result is ",result);
            
        
    except ValueError:
        print("Value Error")
    

calculetor();