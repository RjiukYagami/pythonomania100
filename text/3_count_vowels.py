str = raw_input()

total = 0
vowels = ['e','a','y','i','u','o']
for letter in str:
	if letter in vowels:
		total += 1

print total
