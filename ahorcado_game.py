import random

#Leyendo el archivo
def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)

    global random_word
    random_word = words[random.randint(0,len(words)-1)]
    print(random_word)
    return random_word
    

#Solicitando letras
def input_characters():
    global character_user
    character_user = input("Ingresa una letra: ")
    return character_user

#Comparación
random_word_characters = []
rigth_word_characters = []
def compare():
    for character in random_word:
        random_word_characters.append(character)
        rigth_word_characters.append("-")

    for character in random_word_characters:
        if input_characters() in random_word_characters:
            #position_characters = random_word_characters.index(character_user)
            position_characters = list(enumerate(random_word_characters, 0))
            guess_characters = [(x) for x,i in position_characters if i == character_user]
            for x in guess_characters:
                rigth_word_characters[x] = character_user
            print(position_characters)
            print(guess_characters)
            print(rigth_word_characters)
    print(random_word_characters)


def run():
    read()
    compare()

if __name__=='__main__':
    run()
