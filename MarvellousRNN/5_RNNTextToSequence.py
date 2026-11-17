from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "movie was good",
    "movie was bad",
    "movie was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)

for sentence,sequence in zip(sentences,sequences):
    print("Sentence : ",sentence)
    print("Sequence : ",sequence)
    print("-------------------------")