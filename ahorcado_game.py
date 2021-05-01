import random
import os
from functools import reduce

#Leyendo el archivo
def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)

    #Seleccionado Palabra
    global random_word_uper
    random_word = words[random.randint(0,len(words)-1)]
    traslate_vocals = random_word.maketrans('áéíóú\n', 'aeiou ')
    random_word_uper = random_word.translate(traslate_vocals).upper().strip()
    print(random_word_uper)
    print(len(random_word_uper))
    return random_word
    

#Solicitando letras al jugador
def input_characters():
    global character_user
    character_user = input("Ingresa una letra: ").upper()
    return character_user

random_word_characters = []
rigth_word_characters = []
#print_rigth_word_characters = []


def words_to_play():
    for character in random_word_uper:
        random_word_characters.append(character)
        rigth_word_characters.append("-")
    

#Comparación

def compare():
    global print_rigth_word_characters
    if input_characters() in random_word_characters:
        position_characters = list(enumerate(random_word_characters, 0))
        guess_characters = [(x) for x,i in position_characters if i == character_user]
            
        #Llenando las letras correctas
        for x in guess_characters:
            rigth_word_characters[x] = character_user
            print_rigth_word_characters = reduce(lambda a,b: a + b, rigth_word_characters)
            os.system("clear")
            print(print_rigth_word_characters)     

    else:
        os.system("clear")
        print_rigth_word_characters = reduce(lambda a,b: a + b, rigth_word_characters)
        print(print_rigth_word_characters)
    

def chances():
    lives_value = 10
    words_to_play()
    for _ in range(lives_value):
        print("¡Adivina la Palabra!")
        print('💚 '*lives_value)
        lives_value -= 1
        compare()
        if random_word_uper == print_rigth_word_characters:
            print("GANASTE")
            break

def run():
    os.system("clear")
    read()
    chances()

if __name__=='__main__':

    run()
