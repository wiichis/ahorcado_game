import random

def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)

    random_word = words[random.randint(0,len(words))]
    print(random_word)


def run():
    read()


if __name__=='__main__':
    run()
