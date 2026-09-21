def clean_text(text):
    text = text.lower()
    punctuation = ".,:;!?-—\"'()[]{}"
    result_text = ""
    for char in text:
        if char not in punctuation:
            result_text += char
        else:
            result_text += " "
    return result_text


def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def vowels_counter(text):
    vowels = "аеёиоуыэюя"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_word_frequency(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


# Подготовка введенного текста
text = input("Введите текст: ")
cleaned_text = clean_text(text)
words = cleaned_text.split()

# 1 Количество слов
count_words = len(words)
print(f"Количество слов: {count_words}")

# 2 Самое длинное слово
longest_word = find_longest_word(words)
print(f"Самое длинное слово: {longest_word}")

# 3 Количество гласных
vowels_count = vowels_counter(cleaned_text)
print(f"Количество гласных: {vowels_count}")

# 4 Частота слов
frequency = count_word_frequency(words)
print("Количество раз, которое каждое слово встречается в тексте:")
for word, count in frequency.items():
    print(f"{word}: {count}")
