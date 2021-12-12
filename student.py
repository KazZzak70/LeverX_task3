class Student:

    def __init__(self, id, name, birthday, room, sex):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.room = room
        self.sex = sex
        self.db = StudentDB()


class StudentDB:

    def get(self, id) -> Student:
        pass

    def save(self, student: Student):
        pass

