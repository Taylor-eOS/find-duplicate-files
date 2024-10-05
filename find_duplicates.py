import os

def find_duplicate_files(folder):
    files = os.listdir(folder)
    file_word_map = {}

    for file in files:
        if os.path.isfile(os.path.join(folder, file)):
            words = [word.lower() for word in file.split() if len(word) > 3]
            for word in words:
                if word not in file_word_map:
                    file_word_map[word] = []
                file_word_map[word].append(file)

    for word, associated_files in file_word_map.items():
        if len(associated_files) > 1:
            for file in associated_files:
                print(file)
            print()

if __name__ == "__main__":
    find_duplicate_files(".")

