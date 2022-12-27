
out = ""
while out == "":
	txt = str(input('''
 |\t - : tafrigh\t\t|
 |\t + : jame\t\t|
 |\t * : zarb\t\t|
 |\t / : taqsim\t\t|
 |\t ^ : tavan\t\t|
 |\t % : baghimande\t\t|
 
lotfan amaliat mord nazar khod ra var konid
( mesal: 10 + 20 ): '''))

	if 2 != txt.count(" "):
		print("\n !!! lotfan sakhtar amaliat khod ra be surat sahih vared koin !!!")
		continue
	inp = txt.split(" ")
	if not(inp[0]) and not(inp[1]) and not(inp[2]):
		continue
	if inp[0][0] == "-":
		if not(inp[0][1:].isnumeric()):
			continue
	elif not(inp[0].isnumeric()):
		continue
	if inp[2][0] == "-":
		if not(inp[2][1:].isnumeric()):
			continue
	elif not(inp[2].isnumeric()):
		continue
	inp[0] = int(inp[0])
	inp[2] = int(inp[2])
	if inp[1] == "+":
		out = inp[0] + inp[2]
	elif inp[1] == "-":
		out = inp[0] - inp[2]
	elif inp[1] == "*":
		out = inp[0] * inp[2]
	elif inp[1] == "/":
		out = inp[0] / inp[2]
	elif inp[1] == "^":
		out = inp[0] ** inp[2]
	elif inp[1] == "%":
		out = inp[0] % inp[2]
	else:
		print("\n !!! lotfan sakhtar amaliat khod ra be surat sahih vared koin !!!")
		continue

print(f"your result is : {inp[0]} {inp[1]} {inp[2]} = " + str(out))
