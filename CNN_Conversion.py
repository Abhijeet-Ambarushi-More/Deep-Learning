from PIL import Image

img = Image.open("digit.png")
print(img.size) # Resolution or number of pixels

img = img.convert("L")  # Convert it into greyscale
img = img.resize((28,28))

img.save("digit_28x28.png")

print(img.size)
