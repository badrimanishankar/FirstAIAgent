# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# class TestGetFiles(unittest.TestCase):
#     def test_file_calculator(self):
#         result = get_files_info(working_directory="calculator", directory=".")
#         self.assertIn("main.py", result)
#         self.assertIn("tests.py", result)
#         self.assertIn("pkg", result)
#         self.assertIn("is_dir=False", result)
#         self.assertIn("is_dir=True", result)

#     def test_file_pkg(self):
#         result = get_files_info(working_directory="calculator", directory="pkg")
#         self.assertIn("calculator.py", result)
#         self.assertIn("render.py", result)
#         self.assertIn("is_dir=False", result)

#     def test_file_bin(self):
#         result = get_files_info(working_directory="calculator", directory="/bin")
#         self.assertIn("Error:", result)

#     def test_file_info(self):
#         result = get_files_info(working_directory="calculator", directory="../")
#         self.assertIn("Error:", result)


if __name__ == "__main__":

    # print("Result for current directory:")
    # print(get_files_info("calculator", "."))

    # print("Result for 'pkg' directory:")
    # print(get_files_info("calculator", "pkg"))

    # print("Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"))

    # print("Result for '../' directory:")
    # print(get_files_info("calculator", "../"))

    # print(get_file_content("calculator", "lorem.txt"))
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    # print(run_python_file("calculator", "main.py"))
    # print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # print(run_python_file("calculator", "tests.py"))
    # print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
