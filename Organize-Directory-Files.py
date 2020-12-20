import os
import shutil


dir_path = os.path.dirname(os.path.realpath(__file__))
img = 0
musc = 0
vid = 0
ext = 0
arch = 0
doc = 0
cod = 0
try:
    print("Organising your files intro [ images - music - video -executable - archive - torrent - document - code - design files]")
    for filename in os.listdir(dir_path):
        #check if files are images
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")):
            #if images folder doesnt exist then create new folder
            if not os.path.exists("images"):
                os.makedirs("images")
            shutil.copy2(filename, "images")
            print(f'done file named: {filename}')
            os.remove(filename)
            img+=1

        #check if files are music
        if filename.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw", ".rm")):
            #if music folder doesnt exist then create new folder
            if not os.path.exists("music"):
                os.makedirs("music")
            shutil.copy2(filename, "music")
            print(f'done file named: {filename}')
            os.remove(filename)
            musc+=1

        #check if files are videos
        if filename.lower().endswith((".webm", ".mp4", ".mkv")):
            #if videos folder doesnt exist then create new folder
            if not os.path.exists("videos"):
                os.makedirs("videos")
            shutil.copy2(filename, "videos")
            print(f'done file named: {filename}')
            os.remove(filename)
            vid+=1

        #check if files are executables
        if filename.lower().endswith((".exe", ".msi", ".deb" , "dmg")):
            #if executables folder doesnt exist then create new folder
            if not os.path.exists("executables"):
                os.makedirs("executables")
            shutil.copy2(filename, "executables")
            print(f'done file named: {filename}')
            os.remove(filename)
            ext+=1

        #check if files are archive files
        if filename.lower().endswith((".rar", ".tar" , ".zip" , ".gz")):
            #if archives folder doesnt exist then create new folder
            if not os.path.exists("archives"):
                os.makedirs("archives")
            shutil.copy2(filename, "archives")
            print(f'done file named: {filename}')
            os.remove(filename)
            arch+=1

        #check if files are documents
        if filename.lower().endswith((".txt", ".pdf", ".docx" , ".doc", ".csv", ".xls", ".xlsx")):
            #if documents folder doesnt exist then create new folder
            if not os.path.exists("documents"):
                os.makedirs("documents")
            shutil.copy2(filename, "documents")
            print(f'done file named: {filename}')
            os.remove(filename)
            doc+=1

        #check if files are code files
        if filename.lower().endswith((".py", ".php", ".html" , ".css" , ".js")):
            #if code folder doesnt exist then create new folder
            if not os.path.exists("code"):
                os.makedirs("code")
            shutil.copy2(filename, "code")
            print(f'done file named: {filename}')
            os.remove(filename)
            cod+=1               
except OSError:
    print("Error!!...... please try again")

finally:
    # When script is finished clear screen and display message
    os.system("cls" if os.name == "nt" else "clear")
    
print("Finshed orgnaizing your files : ")
print(f"{img} >> Imges")
print(f"{musc} >> Music") 
print(f"{vid} >> Videos")
print(f"{ext} >> Executables")
print(f"{arch} >> Archive files")
print(f"{doc} >> Documents")
print(f"{cod} >> Code files")     