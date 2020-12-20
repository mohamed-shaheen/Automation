import os
from PIL import Image 


LOGO_NAME = input("Enter The Logo Name With Extension: ")
NEW_FOLDER_NAME = input("Enter The New Folder Name : ")
#open logo image and get logo width and logo height
logo_image = Image.open(LOGO_NAME)
logoWidth, logoHeight = logo_image.size
done_images = 0
#make new folder and not make error if it exist.
os.makedirs(NEW_FOLDER_NAME, exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_NAME:
        continue # skip non-image files and the logo file itself

    img = Image.open(filename)
    width, height = img.size

    # Add logo.
    print('Adding logo to %s...' %(filename))
    position = (width - logoWidth, height - logoHeight)
    img.paste(logo_image, position, logo_image)
    #adding logo in the end to paste the opaque portion of the image but not its transparent background.


    # Save changes.
    img.save(os.path.join(NEW_FOLDER_NAME, filename))
    done_images+=1

print("Done Adding Logo To All Images ")
print(f"Total images : {done_images}")