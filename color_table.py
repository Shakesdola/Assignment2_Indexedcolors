#!/usr/bin/env python
# coding: utf-8

# In[10]:


from PIL import Image
import numpy as np

# Create a 16x16 grid of colors (256 colors)
num_colors = 256
colors_per_row = 16
colors_per_column = num_colors // colors_per_row

# Initialize an array to store the colors
color_table = np.zeros((num_colors, 3), dtype=np.uint8)

# Generate a table of 256 different colors
for i in range(num_colors):
    red = i % colors_per_row * 16  # Vary the red component from 0 to 255
    green = (i // colors_per_row) * 16  # Vary the green component from 0 to 255
    blue = 128  # You can customize the blue component as needed
    color_table[i] = [red, green, blue]

# Create an image from the color table
color_table_image = Image.fromarray(color_table.reshape(colors_per_column, colors_per_row, 3))

# Save the color table image
color_table_image.save('color_table.png')

# Load the original image________________________________
original_image = Image.open('lena.png')

# Convert the original image to grayscale
original_image = original_image.convert('L')



# Function to map pixel values to the color table
def map_pixels_to_color_table(image, color_table):
    width, height = image.size
    pixel_data = np.array(image)
    
    # Create a blank image for the result
    result_image = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            pixel_value = pixel_data[y, x]
            # Scale the pixel value to fit within the color table range
            scaled_pixel_value = int(pixel_value * (num_colors / 256))
            if scaled_pixel_value >= num_colors:
                scaled_pixel_value = num_colors - 1
            mapped_color = tuple(color_table[scaled_pixel_value])
            result_image.putpixel((x, y), mapped_color)

    return result_image

# Transform the original image using the color table
transformed_image = map_pixels_to_color_table(original_image, color_table)

# Save the transformed image
transformed_image.save('transformed_lena.png')



