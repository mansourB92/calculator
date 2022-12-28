
def calc():
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
def Zoj_Fard():
	while True:
		ZJnum = input('\nadad mored nazar ra vared konid: ')
		if ZJnum[0] == "-":
			if not(ZJnum[1:].isnumeric()):
				continue
		elif not(ZJnum.isnumeric()):
			continue
		break
	if 0 == (int(ZJnum) % 2):
		print("add vared shode zoj ast")
	else:
		print("add vared shode fard ast")
def Jadval_Zarb():
	print(" ")
	for x in range(1,11):
		print(" *", end="\t")
		for y in range(1,11):
			print(x * y, end="\t")
		print("*")
def Baze_adad_fard():
	while True:
		num_1 = input("az adade: ")
		if num_1[0] == "-":
			if not(num_1[1:].isnumeric()):
				continue
		elif not(num_1.isnumeric()):
			continue
		break
	while True:
		num_2 = input("ta adade: ")
		if num_2[0] == "-":
			if not(num_2[1:].isnumeric()):
				continue
		elif not(num_2.isnumeric()):
			continue
		break
	if int(num_1) >= int(num_2):
		print(" !!! adade dovom az adade aval bozrgtar nist lotfan ba deghat vared konid  !!!")
		Baze_adad_fard()
	for i in range(int(num_1), int(num_2)):
		if 1 == (i % 2):
			print(i, end=", ")
def Factoriel():
	while True:
		fc = input("lotfan adade mored nazar ra vared konid: ")
		if fc[0] == "-":
			if not(fc[1:].isnumeric()):
				continue
		elif not(fc.isnumeric()):
			continue
		out = 1
		for i in range(1, int(fc) + 1):
			out *= i
		print("factoriel adade shoma = ", out)
		break
while True:
	select = input('''
 _______________________________
|\t\t\t\t|
|\t 1. mashin hesab\t|
|\t 2. zoj va fard\t\t|
|\t 3. baze adad fard\t|
|\t 4. jadval zarb\t\t|
|\t 5. factoriel\t\t|
|\t 0. khoruj\t\t|
|_______________________________|
lotfan gozineye mored nazar ra vared konid: ''')
	if select == "1":
		print("\n 1. tmashin hesan:\n")
		calc()
	elif select == "2":
		print("\n 2. zoj va fard:\n")
		Zoj_Fard()
	elif select == "3":
		print("\n 3. baze adad fard:\n")
		Baze_adad_fard()
	elif select == "4":
		print("\n 4. jadval zarb:\n")
		Jadval_Zarb()
	elif select == "5":
		print("\n 5. factoriel:\n")
		Factoriel()
	elif select == "0":
		break
	else:
		continue