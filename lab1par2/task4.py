class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, "r")
        except:
            raise FileNotFoundError("File not found")


    def count_char(self):
        return len(self.file.read())

    def count_words(self):
        return len(self.file.read().split())

    def count_sentences(self):
        return len(self.file.read().split("."))

    def count_strings(self):
        return len(self.file.read().split("\n"))

    def count_special(self, char):
        return self.file.read().count(char)


handler = FileHandler("4task4")
print(handler.count_char())
