x = int(input("numero\n"))
Fizz = x % 5;
Buzz = x % 3;
if(Fizz == 0 and Buzz == 0):
    print("FizzBuzz")
else:
    print(x)