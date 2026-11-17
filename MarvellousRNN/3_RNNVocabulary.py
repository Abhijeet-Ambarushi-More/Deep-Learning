sentences = [
    "movie was good",
    "movie was bad",
    "movie was not good"
]

vocabulary = []

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

for index, uniqueword in enumerate(vocabulary):
    print("Position ",index+1,":",uniqueword)