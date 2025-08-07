import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

class TestFunctions(unittest.TestCase):

    def test_get_files_info_current_directory(self):
        result = get_files_info("calculator", ".")
        self.assertEqual(
            result, 
            "Result for current directory:\n- lorem.txt: file_size=28 bytes, is_dir=False\n- main.py: file_size=575 bytes, is_dir=False\n- pkg: file_size=192 bytes, is_dir=True\n- tests.py: file_size=1342 bytes, is_dir=False"
        )
        print(f"{result}\n")

    def test_get_files_info_sub_directory(self):
        result = get_files_info("calculator", "pkg")
        self.assertEqual(
            result, 
            "Result for 'pkg' directory:\n- calculator.py: file_size=1737 bytes, is_dir=False\n- morelorem.txt: file_size=26 bytes, is_dir=False\n- render.py: file_size=766 bytes, is_dir=False"
        )
        print(f"{result}\n")

    def test_get_files_info_error_directory(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(
            result,
            "Result for '/bin' directory:\nError: Cannot list '/bin' as it is outside the permitted working directory"
        )
        print(f"{result}\n")

    def test_get_files_info_error_directory_two(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(
            result, 
            "Result for '../' directory:\nError: Cannot list '../' as it is outside the permitted working directory"
        )
        print(f"{result}\n")

    def test_get_file_content(self):
        result_one = get_file_content("calculator", "main.py")
        result_two = get_file_content("calculator", "pkg/calculator.py")
        result_three = get_file_content("calculator", "./bin/cat")
        result_four = get_file_content("calculator", "pkg/does_not_exist.py")

        print(f"{result_one}\n")
        print(f"{result_two}\n")
        print(f"{result_three}\n")
        print(f"{result_four}\n")

    def test_write_file(self):
        result_one = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        result_two = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        result_three = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

        print(f"{result_one}\n")
        print(f"{result_two}\n")
        print(f"{result_three}\n")

if __name__ == "__main__":
    unittest.main()

    