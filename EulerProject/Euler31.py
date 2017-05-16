possible = 0
for p200 in range(0,2):
	for p100 in range(0,3):
		for p50 in range(0,5):
			for p20 in range(0,11):
				for p10 in range(0,21):
					for p5 in range(0,41):
						for p2 in range(0,101):
							if 2*p2+5*p5+10*p10+20*p20+50*p50+100*p100+200*p200 <= 200:
									possible += 1
									print possible
print possible