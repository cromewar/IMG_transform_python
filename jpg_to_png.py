from PIL import Image
import sys
import os

# grab arguments here
img_folder = sys.argv[1]
output_folder = sys.argv[2]
file_format = sys.argv[3]

#checks if the primary folder exists
if not os.path.exists(img_folder):
    print(f'the folder {img_folder} does not exists')
    quit()
# check if folder exists, if not create a new open
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through folder and transform to png
for file in os.listdir(img_folder):
    try:
        img = Image.open(f'{img_folder}{file}')
        remove_file_extension = os.path.splitext(file)[0]
        img.save(f'{output_folder}{remove_file_extension}.{file_format}', file_format)
    except OSError as err:
        print('One or more files can\'t be transformed')



print('all images has been processed')

