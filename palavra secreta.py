letter = ""
amount = 1
formated_word = ""
list_words = ""
secret_word = "mundo"

for letters in secret_word:
    letters = "*"
    formated_word += letter
    
while True:
    if secret_word == letter or formated_word == secret_word:
        print("Parabens!!! Voce acertou a palavra secreta")
        break
    
    letter = input("Insira apenas uma letra:").lower()
    qtd_letters = len(letter)
    
    if qtd_letters > 1:
        print("Voce digitou um ou mais caracteres")
        continue
    if letter.isnumeric():
        print("Voce digitou um caractere nao permitido. Digite apenas uma letra")
        continue

    if letter in secret_word:
        if letter == "m":
            formated_word = f"m{formated_word[1:]}"
        elif letter == "u":
            formated_word = f"{formated_word[0:1]}u{formated_word[2:]}"
        elif letter == "n":
            formated_word = f"{formated_word[0:2]}n{formated_word[3:]}"
        elif letter == "d":
            formated_word = f"{formated_word[0:3]}d{formated_word[4:]}"
        elif letter == "o":
            formated_word = f"{formated_word[0:4]}o"
        print(f"{formated_word}! sua {amount} tentativa!")
    else:
        print(f"essa letra nao esta presente!! sua {amount} tentativa!")
    amount += 1