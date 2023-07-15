def vowels(word):
    for char in word:
        if char in "aeiou":
            print(char)
    return char

word = input('enter any word: ')
vowels(word)