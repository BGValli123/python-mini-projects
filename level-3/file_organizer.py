import os
import shutil

print("="*50)
print("📁 File Organizer")
print("="*50)

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("❌ Invalid path!")
else:
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]

            if ext in ["jpg", "png"]:
                folder = "images"
            elif ext in ["pdf", "docx", "txt"]:
                folder = "documents"
            elif ext in ["py"]:
                folder = "scripts"
            else:
                folder = "others"

            target_folder = os.path.join(folder_path, folder)

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            shutil.move(file_path, os.path.join(target_folder, file))

    print("✅ Files organized successfully!")
