import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string


with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

# cleaning text from punctuations
clean_text = text.translate(str.maketrans('', '', string.punctuation)).lower()

# downloading Turkish stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('turkish'))

# tokenization
words = word_tokenize(clean_text)

# creating a frequency table to keep the score of each word, also cleaning stopwords
word_count = 0
frequency_table = dict()
for word in words:
    word_count += 1
    word = word.lower()
    if word in stop_words:
        continue
    if word in frequency_table:
        frequency_table[word] += 1
    else:
        frequency_table[word] = 1

# creating a dict to keep the score of each sentence
sentences = sent_tokenize(text)
sentence_value = dict()
counter = 0
for sentence in sentences:
    for word, freq in frequency_table.items():
        if word in sentence.lower():
            counter += 1
            if sentence in sentence_value:
                sentence_value[sentence] += freq
            else:
                sentence_value[sentence] = freq

sum_values = 0
for sentence in sentence_value:
    sum_values += sentence_value[sentence]

# average value of a sentence from the original text
average = int(sum_values/len(sentence_value))
# storing sentences into our summary
summary = ''
for sentence in sentence_value:
    if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
        summary += " " + sentence

print(" ORIGINAL TEXT ".center(174, "-"))
print(text)
print(" SUMMARIZED TEXT ".center(174, "-"))
print(summary)
