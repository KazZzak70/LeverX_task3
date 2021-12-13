import argparse
import pathlib


def configure_parser():
    parser = argparse.ArgumentParser(description="Student Data Serializer")
    parser.add_argument("students_file_path", help="Path to students source file")
    parser.add_argument("rooms_file_path", help="Path to rooms source file")
    parser.add_argument("host", help="MySQL Database connection host")
    parser.add_argument("port", help="MySQL Database connection port")
    parser.add_argument("user", help="MySQL Database user")
    parser.add_argument("password", help="MySQL Database user password")
    parser.add_argument("--to-xml", dest="output_formats", help="Export result to .xml file format",
                        action="append_const", const="XML")
    parser.add_argument("--to-json", dest="output_formats", help="Export result to .json file format",
                        action="append_const", const="JSON")
    parser.add_argument("--to-path", help="Setting the output path for files",
                        default=str(pathlib.Path.cwd()))
    parser.add_argument("-rooms", "--get-rooms", help="Get a list of rooms with the number of students in them",
                        action="store_true")
    parser.add_argument("--get-top-min-age", help="Get 5 rooms with the smallest average age of students",
                        action="store_true")
    parser.add_argument("--get-top-age-diff", help="Get 5 rooms with the biggest difference in student ages",
                        action="store_true")
    parser.add_argument("--get-rooms-diff-sex", help="Get a list of rooms where students of different sexes live",
                        action="store_true")
    return parser
