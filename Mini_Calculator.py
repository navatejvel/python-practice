num_value = input("Enter in first number and second number: ")

first_num = float(input("Enter first number given: "))
second_num = float(input("Enter second number given: "))

if second_num == 0:
  print("Division ==> Undefined")
else:
    print("Valid")
    print("Division => ",first_num/second_num)

print("Addition => ",first_num + second_num)
print("Subtraction => ",first_num - second_num)
print("Multiplication => ",first_num*second_num)
