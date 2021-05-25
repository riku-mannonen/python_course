def bmi(weight, height):
    return weight / height ** 2

if __name__ == "__main__":
	weight = float(input('enter weight (kg): ' ))
	height = float(input('enter height (m): '))
	print(f'you\'re bmi is {bmi(weight, height)}')
