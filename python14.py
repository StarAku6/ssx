alphabet = "abcdefghijklmnopqrstuvwxyz"

inverse_matrix = [[1, 24],
                  [25, 3]]

text = input("Введите зашифрованный текст: ").lower()

decrypted = ""

for i in range(0, len(text), 2):
	y1 = alphabet.index(text[i])
	y2 = alphabet.index(text[i + 1])

	x1 = (inverse_matrix[0][0] * y1 + inverse_matrix[0][1] * y2) % 26
	x2 = (inverse_matrix[1][0] * y1 + inverse_matrix[1][1] * y2) % 26

	decrypted += alphabet[x1] + alphabet[x2]

print("Расшифрованный текст:", decrypted)
