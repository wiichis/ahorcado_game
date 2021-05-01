import random
import os
from functools import reduce

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

random_word_characters = []
rigth_word_characters = []
print_rigth_word_characters = []

def words_to_play():
    for character in random_word:
        random_word_characters.append(character)
        rigth_word_characters.append("-")
    rigth_word_characters.pop()
    

#Comparación
def compare():
    if input_characters() in random_word_characters:
        position_characters = list(enumerate(random_word_characters, 0))
        guess_characters = [(x) for x,i in position_characters if i == character_user]
            
        #Llenando las letras correctas
        for x in guess_characters:
            rigth_word_characters[x] = character_user
            print_rigth_word_characters = reduce(lambda a,b: a + b, rigth_word_characters)
            os.system("clear")
            print(print_rigth_word_characters)
        print(random_word_characters)
    else:
        os.system("clear")
        print_rigth_word_characters = reduce(lambda a,b: a + b, rigth_word_characters)
        print(print_rigth_word_characters)
        
        

def chances():
    words_to_play()
    for _ in range(7):
        print("¡Adivina la Palabra!")
        compare()
        
        


def run():
    os.system("clear")
    read()
    chances()

if __name__=='__main__':

    run()
