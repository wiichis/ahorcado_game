import random

#Leyendo el archivo
def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)

    global random_word
    random_word = words[random.randint(0,len(words))]
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
            position_character = random_word_characters.index(character_user)
            rigth_word_characters[position_character] = character_user
            print(rigth_word_characters)
    print(random_word_characters)



def run():
    read()
    compare()

if __name__=='__main__':
    run()
