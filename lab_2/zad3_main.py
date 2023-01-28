dictionary = {"czerwony": "red", "niebieski": "blue", "czarny": "black", "fioletowy": "purple", "wolno": "slow",
              "szybko": "fast", "kaczka": "duck", "butelka": "bottle", "muzyka": "music", "kot": "cat"}


def translate(word: str) -> str:
    return dictionary.get(word)


def main():
    while True:
        word = input("Wpisz słowo do przetłumaczenia (wpisz 'x' aby wyjść z programu): ")
        if word == 'x':
            print("Do zobaczenia!")
            break
        translation = translate(word)
        if translation:
            print(translation)
        else:
            print("Nie mam tego tlumaczenia :c")

main()