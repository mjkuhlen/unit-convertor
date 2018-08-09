running = True
while running == True:
	decision1 = False
	while decision1 == False:
		print('Would you like to convert [K]ilometers, [M]iles or [Q]uit?')
		unit_type = input().lower()
		if unit_type[0] == 'k':
			decision1 = True
			print('Input the amount kilometers to convert')
			kms = input()
			miles = float(kms)/1.60934
			miles = round(miles,2)
			print(f'{kms} kilometers is equal to {miles} miles.')
		elif unit_type[0] == 'm':
			decision1 = True
			print('Input the amount of miles to convert')
			mi = input()
			km = float(mi)*1.60934
			km = round(km,2)
			print(f'{mi} miles is equal to {km} kilometers.')
		elif unit_type[0] == 'q':
			decision1 = True
			running = False
			break
		else:
			print('Please choose [K]ilometers, [M]iles or [Q]uit')
	decision2 = False
	while decision2 == False and unit_type[0] != 'q':
		print('Would you like to convert another value, [Y]es or [N]o?')
		answer = input().lower()
		if answer[0] == 'n':
			running = False
			decision2 = True
			break
		elif answer[0] == 'y':
			running  = True
			decision2 = True
		else:
			print('Please choose either [Y]es or [N]o.')

