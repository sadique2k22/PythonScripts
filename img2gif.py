from PIL import Image, ImageSequence

# Set the duration for each image in seconds
image_duration = 0.01

# Create a list to store the images
images = []

# Load and append each image to the list
for i in range(1, 1179):
    image_path = f"image/{i}.jpg"
    img = Image.open(image_path)
    images.append(img)

# Create a new image with the first frame
output_img = images[0]

# Save the concatenated image with the specified duration
output_img.save("output2.gif", save_all=True, append_images=images[1:], duration=int(image_duration * 1000), loop=0)