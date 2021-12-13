from hostel import Hostel
from source_func import get_data
from pathlib import Path
from args import configure_parser
from pymysql.cursors import DictCursor


def main():
    args = configure_parser().parse_args()
    connect_dict = {
        "host": args.host,
        "port": int(args.port),
        "user": args.user,
        "password": args.password,
        "cursorclass": DictCursor
    }
    # output_path = Path(args.to_path)
    hostel = Hostel(connect_dict)

    rooms_file = Path(args.rooms_file_path)
    rooms_data = get_data(file=rooms_file)
    hostel.load_rooms(rooms_data)

    students_file = Path(args.students_file_path)
    students_data = get_data(file=students_file)
    hostel.load_students(students_data)


if __name__ == '__main__':
    main()
