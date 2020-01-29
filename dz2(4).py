text = input('Введите строку из нескольких слов: ')
text = list((text).split())

for i, n in enumerate(text):
    print(i, n[:10])