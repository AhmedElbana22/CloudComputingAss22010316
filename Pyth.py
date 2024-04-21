import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_txt = [word.lower() for word in words if word.lower() not in stop_words and word.isalnum()]
    return filtered_txt

def display_word_freq(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

 
file_path = "C:\\dockerimages\\random_paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()
    filtered_txt = remove_stopwords(text)
    word_freq = Counter(filtered_txt)
    display_word_freq(word_freq)
