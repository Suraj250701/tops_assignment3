# Write a Python program to check the current position of the file cursor using tell().

def check_file_cursor_position():
    with open(".\\Reading and Writing Files\\Practical Examples\\quesion1.txt", "r") as file:
        print("Current file cursor position:", file.tell())
        # Move the cursor to the end of the file
        file.seek(0, 2)
        print("File cursor position after moving to the end:", file.tell())

check_file_cursor_position()