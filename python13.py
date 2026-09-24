alphabet = "abcdefghijklmnopqrstuvwxyz"

matrix = [[3, 2],
          [1, 1]]

text = input("Введите текст: ").lower()

text = text.replace(" ", "")


if len(text) % 2 != 0:
	text += "x"

encrypted = ""

for i in range(0, len(text), 2):
	x1 = alphabet.index(text[i])
	x2 = alphabet.index(text[i + 1])

	y1 = (matrix[0][0] * x1 + matrix[0][1] * x2) % 26
	y2 = (matrix[1][0] * x1 + matrix[1][1] * x2) % 26

	encrypted += alphabet[y1] + alphabet[y2]

print("Зашифрованный текст:", encrypted)
