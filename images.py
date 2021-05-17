from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
new_image = img.resize((400,400))
new_image.save('thumbnail.jpg')