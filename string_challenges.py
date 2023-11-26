# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
vowels = set("айуеыоэяию")
for letter in word.lower():
    if letter in vowels:
        count += 1
print(f"Количество гласных букв: {count}")
print()

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
num_words = len(words)
print(num_words)
print()

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for i in words:
    print(i[0])
print()

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
lenght=0
for i in words:
    lenght+=len(i)
print(lenght/len(words))