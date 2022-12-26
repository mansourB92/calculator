num1 = int(input("input frist number = \t"))
op = input("\ninput operator : \t")
num2 = int(input("\ninput secound number = \t"))
out = ""
if op == "+":
	out = num1 + num2
elif op == "-":
	out = num1 - num2
elif op == "*":
	out = num1 * num2
elif op == "/":
	out = num1 / num2
elif op == "**":
	out = num1 ** num2
elif op == "%":
	out = num1 % num2
else:
	out="warning inputs"

#if out != ""
#	print(out)
print("your result is : " + str(out))
