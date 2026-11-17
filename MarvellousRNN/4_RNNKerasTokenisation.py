from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "movie was good",
    "movie was bad",
    "movie was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

for word, index in word_index.items():
    print("Position ",index+1,":",word)