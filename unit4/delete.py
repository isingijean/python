import os

if os.path.exists("newfile1.txt"):
    os.remove("newfile1.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
