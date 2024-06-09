def is_palindrome(text):
  text = text.lower().replace(" ", "")
  return text == text[::-1]

frase = input("Digite uma frase: ")

if is_palindrome(frase):
  print("A frase é um palíndromo.")
else:
  print("A frase não é um palíndromo.")
