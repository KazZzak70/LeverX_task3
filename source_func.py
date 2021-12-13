from exceptions import InputFileError
from pathlib import Path
import json
import pymysql


def json_file_exists(path: Path) -> bool:
    return True if (path.exists() and path.suffix == ".json") else False


def get_data(file: Path):
    if json_file_exists(file):
        with open(file) as file:
            data_list = json.load(file)
        if data_list:
            return data_list
        else:
            raise InputFileError("Expected data in source JSON file")
    else:
        raise InputFileError("Check the input file path/type")


def db_manipulation(connect_dict: dict, sql: str):
    try:
        connection = pymysql.connect(**connect_dict)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)
