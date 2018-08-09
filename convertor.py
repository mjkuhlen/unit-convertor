running = True
while running == True:
	print('Would you like to convert [K]ilometers or [M]iles?')
	unit_type = input()
	if unit_type[0] == 'k':
		print('Input kilometers')
		kms = input()
		miles = float(kms)/1.60934
		miles = round(miles,2)
		print(f'{kms} kilometers is equal to {miles} miles')
	elif unit_type[0] == 'm':
		print('Input miles')
		mi = input()
		km = float(mi)*1.60934
		km = round(km,2)
		print(f'{mi} miles is equal to {km} kilometers')
	else:
		print('Please choose either [K]ilometers or [M]iles')
	decision = False
	while decision == False:
		print('Would you like to convert another value, [Y]es or [N]o?')
		answer = input()
		if answer[0] == 'n':
			running = False
			decision = True
			break
		elif answer[0] == 'y':
			running  = True
			decision = True
		else:
			print('Please choose either [Y]es or [N]o.')
