word = input("Dame una palabra\n")

letter_counter = {}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1 
    else:
        letter_counter[letter] = 1
print(f"tu palabra tiene{len(word)} letras") 
for letter in letter_counter:
    print           