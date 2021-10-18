# Crie um programa que tenha uma tupla com várias palavras ( sem acentuações ). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais

words = ('BUSINESS', 'PROGRAMMING', 'STUDYING',
         'BRENDA', 'CURSO', 'VIDEO', 'PYTHON',
         'PRATICE', 'FUTURE', 'MARKETPLACE',
         'FREE', 'LANGUAGE', 'LEARN')

# At the time of each of the vowels, the loop will run showing each words
for vowels in words:
    print(f'\n\033[1;34mNa palavra: \033[1;30m{vowels},\033[m', end=' ')
    print(f'\033[1;33mas vogais são:\033[m', end=' ')
    # Each letters in vowel will be validated, if it be in global vowels system (aeiou)
    for l in vowels:
        if l.lower() in "aeiou":
            print(l, end=' ')
    
