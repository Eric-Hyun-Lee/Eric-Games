import time
x=0
s=1
while True:
	for i in range(999999999999):
		x=i
		candies = 0+x
		if x == 1:
			print("You have " + str(candies) + " candy!")
		else:
			print("You have " + str(candies) + " candies!")
		time.sleep(1)
		print("\033c")



