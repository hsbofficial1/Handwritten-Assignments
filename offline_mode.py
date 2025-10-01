from PIL import Image, ImageDraw, ImageFont

text_to_convert = """
I’m Harsharaj Shetty B, someone who finds joy in building things that combine creativity and logic. 
From coding websites to designing visuals to experimenting with tech projects, I see each 
challenge as a chance to learn and create something meaningful. 
I started out exploring design and development just out of curiosity, but over time it turned
 into a passion that shaped my work and businesses. 
Today, I run ventures like SparkBee Technologies, Cucoon, and Aquatic.In, while also diving
 deep into side projects ranging from IoT systems to AI-based solutions.
"""

# Create a blank white image
img = Image.new("RGB", (1200, 1600), color="white")

# Choose a handwriting-style font (you need a .ttf file)
font = ImageFont.truetype("IndieFlower-Regular.ttf", 28)  # you can swap with any handwriting font
draw = ImageDraw.Draw(img)# Add text
draw.multiline_text((50, 50), text_to_convert, font=font, fill=(0, 0, 0), spacing=10)

# Save as image
img.save("demo.png")

print("Converted to handwriting-style image!")
