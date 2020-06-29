

def RoN(number):
	num = number
	nS = str(num)
	if num % 7 == 0:  # 7???
		return True
	elif str(7) in nS:  # 7????????
		return True
	else:
		return False
		
for i in range(1,101):
	if not RoN(i):
		print(i)
	pass

