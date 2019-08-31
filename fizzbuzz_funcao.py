def fizzbuzz(x):
		Fizz = x % 5;
		Buzz = x % 3;
		if(Fizz == 0 and Buzz == 0):
   		 return("FizzBuzz")
		else:
				paridade = x % 3
				if paridade == 0:
						return("Fizz")
				else:
						paridade = x % 5;
						if(paridade == 0):
								return("Buzz")
						else:
								return(x)