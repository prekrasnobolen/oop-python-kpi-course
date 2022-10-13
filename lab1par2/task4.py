class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, "r")
        except:
            raise FileNotFoundError("File not found")

    def count_char(self):
        count = 0
        for line in self.file:
            count += len(line)
        return count

    def count_words(self):
        count = 0
        for line in self.file:
            count += len(line.split())
        return count

    def count_sentences(self):
        count = 0
        for line in self.file:
            count += len(line.split('.'))
        return count

    def count_strings(self):
        count = 0
        for line in file:
            count += 1
        return count

    def count_special(self, char):
        count = 0
        for line in self.file:
            for ch in line:
                if char == ch:
                    count += 1
        return count


handler = FileHandler("4task4")
print(handler.count_char())
