class Student:
    def __init__(self, surname, name, book_id, grades):
        self.surname = surname
        self.name = name
        self.book_id = book_id
        self.grades = grades

    def get_surname(self):
        return self.surname

    def my_average(self):
        summ = []
        for grade in self.grades.values():
            summ.append(grade)
        return sum(summ)/len(summ)

    def get_name(self):
        return self.name


class Group:
    def __init__(self):
        self.students = []
        self.number = 0

    def add_student(self, surname, name, book_id, grades):
        if self.number < 20:
            for i in self.students:
                if surname == i.get_surname() or name == i.get_name():
                    return
            self.students.append(Student(surname, name, book_id, grades))
            self.number += 1

    def top(self):
        array = self.students
        for j in range(len(array) - 1):
            for i in range(len(array) - j - 1):
                if array[i].my_average() < array[i+1].my_average():
                    buff = array[i+1]
                    array[i+1] = array[i]
                    array[i] = buff
        print("***Top***")
        for i in range(5):
            print(f"{i+1}. {array[i].get_surname()} {array[i].get_name()}    Average:{array[i].my_average()}")


    def average_score(self):
        allgrades = []
        for student in self.students:
            for sub, grade in student.grades:
                allgrades.append(grade)
            return sum(allgrades)/len(allgrades)


tv12 = Group()
tv12.add_student("Danylo", "Konovalenko", 21454, { "Math" : 65, "OOP" : 65, "Polyana" : 102})
tv12.add_student("Bogdan", "Bogdanovych", 21454, { "Math" : 90, "OOP" : 90, "Polyana" : 65})
tv12.add_student("Semen", "Semenovych", 21454, { "Math" : 74, "OOP" : 75, "Polyana" : 77})
tv12.add_student("Kateryna", "Mda", 21454, { "Math" : 60, "OOP" : 60, "Polyana" : 60})
tv12.add_student("ElomMusk", "Sucks", 21454, { "Math" : 85, "OOP" : 77, "Polyana" : 90})
tv12.add_student("Volodymyr", "Zelensky", 21454, { "Math" : 100, "OOP" : 100, "Polyana" : 100})
tv12.top()