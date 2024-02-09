# reverse: python3 file_manipulator.py reverse inputpath.txt outputpath.txt
# Copying: python3 file_manipulator.py copy inputpath.txt outputpath.txt
# Duplicating Contents: python3 file_manipulator.py duplicate-contents inputpath.txt 3
# Replacing Strings: python3 file_manipulator.py replace-string inputpath.txt needle newstring

import sys
import os

def reverse_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していません。")
        return
    with open(input_path, "r") as file_input:
        content = file_input.read()
    with open(output_path, "w") as file_output:
        file_output.write(content[::-1])

def copy_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していません。")
        return
    with open(input_path, "r") as file_input:
        content = file_input.read()
    with open(output_path, "w") as file_output:
        file_output.write(content)

def duplicate_contents(input_path, times):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していません。")
        return
    with open(input_path, "r") as file_input:
        content = file_input.read()
    with open(input_path, "w") as file_output:
        for _ in range(times):
            file_output.write(content)

def replace_string(input_path, needle, newstring):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していません。")
        return
    with open(input_path, "r") as file_input:
        content = file_input.read()
    with open(input_path, "w") as file_output:
        file_output.write(content.replace(needle, newstring))

def main():
    if len(sys.argv) < 3:
        print("下記のコマンドを、ターミナル上で入力して下さい。\nまた、: python3 file_manipulator.py <operation> <inputpath> [<outputpath>/n/<needle> <newstring>]")
        return

    operation = sys.argv[1]
    input_path = sys.argv[2]

    if operation == "reverse" and len(sys.argv) == 4:
        output_path = sys.argv[3]
        reverse_file(input_path, output_path)
    elif operation == "copy" and len(sys.argv) == 4:
        output_path = sys.argv[3]
        copy_file(input_path, output_path)
    elif operation == "duplicate-contents" and len(sys.argv) == 4:
        times = int(sys.argv[3])
        duplicate_contents(input_path, times)
    elif operation == "replace-string" and len(sys.argv) == 5:
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(input_path, needle, newstring)
    else:
        print("コマンド、または引数の数が無効です。")

if __name__ == "__main__":
    main()