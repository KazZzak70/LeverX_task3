from source_func import db_manipulation


class Room:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.db = RoomDB()

    def __str__(self):
        return f"ROOM:\nID: {self.id}\nNAME: {self.name}\n"

    def save(self, connect_dict: dict):
        return self.db.save(self, connect_dict)


class RoomDB:

    @staticmethod
    def save(room: Room, connect_dict: dict):
        sql = """INSERT INTO rooms (id, name)
                 VALUES (%d, '%s');""" % (room.id, room.name)
        db_manipulation(connect_dict, sql)
