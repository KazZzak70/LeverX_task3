from source_func import db_manipulation


class Student:

    def __init__(self, id, name, birthday, room, sex):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.room = room
        self.sex = sex
        self.db = StudentDB()

    def __str__(self):
        return f"STUDENT:\nID: {self.id}\nNAME: {self.name}\nBIRTHDAY: {self.birthday}\n" \
               f"ROOM: {self.room}\nSEX: {self.sex}\n"

    def save(self, connect_dict: dict):
        return self.db.save(self, connect_dict)


class StudentDB:

    @staticmethod
    def save(student: Student, connect_dict: dict):
        sql = "INSERT INTO students (id, name, birthday, room_id, sex) " \
              "VALUES ({}, '{}', '{}', {}, '{}');". \
              format(student.id, student.name, student.birthday, student.room, student.sex)
        db_manipulation(connect_dict, sql)
