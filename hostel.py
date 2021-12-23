from hostel_serializer import HostelSerializer
from source_func import db_manipulation
from pathlib import Path
from student import Student
from room import Room


class Hostel:

    serializer = HostelSerializer()

    def __init__(self, db_connect_dict: dict, path: Path, forms: list):
        self.connect_dict = db_connect_dict
        self.file_path = path
        self.file_forms = forms
        self.create_db()
        self.create_tables()

    def create_db(self):
        sql = "CREATE DATABASE hostel_db;"
        db_manipulation(self.connect_dict, sql)
        self.connect_dict["database"] = "hostel_db"

    def create_tables(self):
        sql_list = ["""CREATE TABLE rooms (id int NOT NULL,
                                           name varchar(32) NOT NULL, 
                                           PRIMARY KEY (id))
                                           ENGINE=InnoDB 
                                           DEFAULT CHARSET=utf8mb3;""",
                    """CREATE TABLE students (id int NOT NULL,
                                              name varchar(32) NOT NULL, 
                                              birthday datetime NOT NULL,
                                              room_id int REFERENCES rooms(id), 
                                              sex varchar(1) NOT NULL,
                                              PRIMARY KEY (id)) 
                                              ENGINE=InnoDB 
                                              DEFAULT CHARSET=utf8mb3;"""]
        for sql in sql_list:
            db_manipulation(self.connect_dict, sql)

    def get_rooms_with_student_amount(self):
        sql = """SELECT rooms.id AS ID,
                        rooms.name AS NAME,
                        COUNT(*) AS QUANTITY
                 FROM students
                 LEFT JOIN rooms ON students.room_id=rooms.id
                 GROUP BY students.room_id
                 ORDER BY ID;"""
        result = db_manipulation(self.connect_dict, sql)
        for form in self.file_forms:
            Hostel.serializer.serialize(result, form, self.file_path, "rooms_list")

    def get_top_min_age(self):
        sql = """SELECT rooms.ID AS ID,
                        rooms.name AS NAME,
                        CEILING(AVG(DATEDIFF(NOW(), students.birthday))) AS AVERAGE_AGE
                 FROM students
                 LEFT JOIN rooms ON students.room_id=rooms.id
                 GROUP BY students.room_id
                 ORDER BY AVERAGE_AGE
                 LIMIT 5;"""
        result = db_manipulation(self.connect_dict, sql)
        for form in self.file_forms:
            Hostel.serializer.serialize(result, form, self.file_path, "rooms_min_age")

    def get_top_age_diff(self):
        sql = """SELECT rooms.id AS ID,
                        rooms.name AS NAME,
                        (MAX(DATEDIFF(NOW(), students.birthday))-MIN(DATEDIFF(NOW(), students.birthday))) AS AGE_DIFF
                 FROM students
                 LEFT JOIN rooms ON students.room_id=rooms.id
                 GROUP BY students.room_id
                 ORDER BY AGE_DIFF DESC
                 LIMIT 5;"""
        result = db_manipulation(self.connect_dict, sql)
        for form in self.file_forms:
            Hostel.serializer.serialize(result, form, self.file_path, "rooms_age_diff")

    def get_rooms_diff_sex(self):
        sql = """WITH cte AS
                   (SELECT rooms.id AS ID,
                           rooms.name AS NAME,
                           COUNT(DISTINCT sex) uniq
                    FROM students
                    LEFT JOIN rooms ON students.room_id=rooms.id
                    GROUP BY students.room_id
                    ORDER BY ID)
                 SELECT ID,
                        NAME
                 FROM cte
                 WHERE uniq=2
                 ORDER BY ID;"""
        result = db_manipulation(self.connect_dict, sql)
        for form in self.file_forms:
            Hostel.serializer.serialize(result, form, self.file_path, "rooms_diff_sex")

    def load_students(self, data: list[dict]):
        for source_dict in data:
            student = Student(**source_dict)
            student.save(self.connect_dict)

    def load_rooms(self, data: list[dict]):
        for source_dict in data:
            room = Room(**source_dict)
            room.save(self.connect_dict)
