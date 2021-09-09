import random
def lotto():
	print('6 aus 49')
	tip = []
	i = 0
	while i < 6:
		usrin = input('Zahl zwischen 1 und 49 eingeben: ')
		try:
			usrin = int(usrin)
		except ValueError:
			print("Ungültige Eingabe")
		while (usrin not in range(1, 50)) or (usrin in tip):
			print('Zahl nicht im gültigen Bereich oder doppelte Eingabe! Eingabe wiederholen')
			usrin = input('Zahl zwischen 1 und 49 eingeben: ')
			try:
				usrin = int(usrin)
			except ValueError:
				print("Ungültige Eingabe")
		tip.append(usrin)
		i += 1
	print()
	lottozahlen = []
	lottozahlen.extend(range(1, 50))
	# Alternative zu .extend
	#for i in range(1, 50):
	#	lottozahlen.append(i)
	gewinner = random.sample(lottozahlen, 6)
	#print(tip)
	#tip = sorted(tip)
	#gewinner = sorted(gewinner)
	tip.sort()
	gewinner.sort()
	count = 0
	for i in tip:
		for j in gewinner:
			if i == j:
				print(i, '- Treffer!')
				count += 1
	print('Du hast', count, 'Richtige!')
	print()
	print('Deine Zahlen waren:')
	print(tip)
	print()
	print('Alle Gewinnzahlen sind:')
	print(gewinner)
if __name__ == "__main__":
	lotto()
