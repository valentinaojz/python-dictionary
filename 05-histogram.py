#Un histograma de frecuencia sirve para representar cuantas veces aparece cierto elemento en una colección o más general sirve para resumir resultados.
#Supongamos que nos dan una palabra y necesitamos contar cuantas veces aparece cada letra en la palabra.

word = input("Dame una palabra\n")
letter_counter = {}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1 
    else:
        letter_counter[letter] = 1
print(letter_counter)            