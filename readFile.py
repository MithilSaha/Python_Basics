# Command to run theis file from Python Shell - exec(open(r"D:\Python Books\readFile.py").read())
import glob
def main():
    filePath = input("Please Enter the File Path of Log Files: ")
    keyword = input("Please Enter Your Keyword: ")
    for f in glob.glob(f"{filePath}\*.txt"):
        with open(f) as file_object:
            contents = file_object.read()
            if keyword in contents:
                print(f"You Keyword is found in {f}")

if __name__ == "__main__":
    main()