sentences = [
    "movie was good",
    "movie was bad",
    "movie was not good"
]

labels = [1,0,0]

for sentence , label in zip(sentences, labels):
    print("sentence : ",sentence)
    print("Label : ",label)

    if label == 1:
        print("Meaning : Positive sentiment")
    else:
        print("Meaning : Negative sentiment")

    print("----------------------------------")