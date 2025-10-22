import os
import shutil

def organize_files(folder_path):
    # Dictionary for folder categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Spreadsheets": [".xlsx", ".csv"],
        "Scripts": [".py", ".js", ".sh"],
        "Archives": [".zip", ".rar"],
        "Others": []
    }

    # Create category folders if not exist
    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Go through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Move file to its category folder
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                print(f"Moved {filename} → {folder}/")
                moved = True
                break

        # If no match found
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))
            print(f"Moved {filename} → Others/")

    print("\n✅ All files organized successfully!")

if __name__ == "__main__":
    target_folder = input("Enter folder path to organize: ").strip()
    if os.path.exists(target_folder):
        organize_files(target_folder)
    else:
        print("❌ Invalid folder path. Please check and try again.")
