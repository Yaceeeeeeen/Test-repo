while True:
   
  
  while True:
   try:
  
     first_number = float(input("enter first number: "))
     break
   except ValueError:
     print("invalid input. please enter a numeric value")

  while True:
    try:
      
    
      operation = input("enter operation type: ")
      if operation in ("/","*","+","-"):
        break
      else:
        raise ValueError
    except ValueError:
      print("invalid operator , please use *,-,+,/")
  
  
  while True:
    try:
        second_number = float(input("enter second number: "))
        if second_number == 0 and operation == "/":
          raise ZeroDivisionError 
    
        
        break
    except ZeroDivisionError:
      print("cannot divide by zero , try another number")
    except ValueError:
       print("invalid input. please enter a numeric value")
    
  
  match operation:
    case"*":
      result = first_number * second_number
    case"+":
      result = first_number + second_number
    case"/":
      result = first_number / second_number
    case"-":
      result = first_number - second_number
    case _:
      result = None
    
  if result != None:
    print("your result is:",result)
  else: 
    print("invalid operator")
  repeat = input("do you want to perform another operation (yes/no): ")
  if repeat == "no":
    break
  print("program exited")