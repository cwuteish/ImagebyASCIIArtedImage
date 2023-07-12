from PIL import Image, ImageDraw, ImageFont

# Set the width and height of the ASCII art (adjust as needed)
ASCII_WIDTH = 280
ASCII_HEIGHT = 110

# Define the ASCII characters to represent the gradient (adjust as needed)
ASCII_CHARS = '@%#*+=-:. '

# Prompt the user to enter the image file location
image_location = input("Enter the location of the image file: ")

# Load the image and resize it
image = Image.open(image_location)
image = image.resize((ASCII_WIDTH, ASCII_HEIGHT), resample=Image.LANCZOS)

# Convert the image to grayscale
image = image.convert('L')

# Calculate the pixel width and height for each ASCII character
pixel_width = image.width / ASCII_WIDTH
pixel_height = image.height / ASCII_HEIGHT

ascii_art = ''
for y in range(ASCII_HEIGHT):
    for x in range(ASCII_WIDTH):
        # Calculate the region of the image to sample
        left = x * pixel_width
        top = y * pixel_height
        right = left + pixel_width
        bottom = top + pixel_height

        # Get the pixel values in the region and calculate the average
        pixels = image.crop((left, top, right, bottom)).getdata()
        average = sum(pixels) / len(pixels)

        # Map the average pixel value to an ASCII character
        char_index = int((average / 255) * (len(ASCII_CHARS) - 1))
        ascii_art += ASCII_CHARS[char_index]

    ascii_art += '\n'

# Create a new image with white background
output_image = Image.new('RGB', (image.width * 10, image.height * 10), (255, 255, 255))
draw = ImageDraw.Draw(output_image)

# Set the font size and type (adjust as needed)
font_size = 10
font = ImageFont.truetype('arial.ttf', font_size)

# Draw the ASCII characters onto the image
x_pos = 0
y_pos = 0
for char in ascii_art:
    if char == '\n':
        y_pos += font_size
        x_pos = 0
    else:
        draw.text((x_pos, y_pos), char, font=font, fill=(0, 0, 0))
        x_pos += font_size

# Save the output image
output_image.save('output_image.png')  # Specify the desired output image filename

# Display the output image
output_image.show()