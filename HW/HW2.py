from collections import Counter


words = 0
letters = 0
lines = 0
words_ls = []


with open('C:/Users/Faruh/Desktop/book.txt', mode='r+', encoding='utf8') as f:

    # замените во всём тексте 'Анна Павловна' на 'Anna Pavlovna' (сохраните изменения в этот же файл)
    book = f.read().replace('Анна Павловна', 'Anna Pavlovna')
    f.seek(0)
    f.write(book)
    f.seek(0)

    # количество строк, букв, слов
    for line in f:
        lines += 1
        letters += len(line)
        words_ls += line.split()

        position = 'out'
        for letter in line:
            if letter != ' ' and position == 'out':
                words += 1
                position = 'in'
            elif letter == ' ':
                position = 'out'


longest_words = sorted(words_ls, key=len)[::-1][:10]
most_letters = Counter(''.join(words_ls)).most_common(10)

print(f"Количество слов: {words}")
print(f"Средняя длина слова в тексте: {int(letters/words)}")
print(f"Количество символов: {letters}")
print(f"Топ 10 слов по длине: {longest_words}")
print(f"Топ 10 самых частых букв: {most_letters}")
print(f"Количество строк: {lines}")
