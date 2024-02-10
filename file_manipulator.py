# create_file: python3 file_manipulator.py create_inputfile inputpath.txt
# reverse: python3 file_manipulator.py reverse inputpath.txt outputpath.txt
# Copying: python3 file_manipulator.py copy inputpath.txt outputpath.txt
# Duplicating Contents: python3 file_manipulator.py duplicate-contents inputpath.txt 3
# Replacing Strings: python3 file_manipulator.py replace-string inputpath.txt needle newstring

import sys
import os

# 入力先ファイル(inputpath.txt)が存在しなかった場合、ファイル作成を行う関数
def create_file(input_path):
    if not os.path.exists(input_path):
        sys.stdout.write(f"入力先ファイルを作成します。\n" +
                         "作成にあたり、自身で文字列を入力する場合は[Y]、\n" +
                         "サンプルを自動で入力・保存する場合は[A]を入力して下さい。\n" +
                         "==>サンプルテキスト:test input sentence/replace word is [needle]\n")
        sys.stdout.flush()
        # ユーザーが入力した文字列を、空行を除いて大文字化
        input_string = sys.stdin.readline().strip().upper()

        if input_string == "Y":
            sys.stdout.write(f"文字列を入力して下さい。\n")
            sys.stdout.flush()
            content = sys.stdin.readline().strip()

            with open(input_path, "w") as file_input:
                file_input.write(content)
            
            sys.stdout.write(f"入力内容を保存しました。\n" +
                             "入力内容：" + content)
            sys.stdout.flush()
        elif input_string == "A":
            with open(input_path, "w") as file_input:
                file_input.write(f"test input sentence/replace word is [needle]")

            sys.stdout.write(f"サンプルテキストを保存しました。")
            sys.stdout.flush()

def reverse_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していないので、先に入力先ファイルを作成します。")
        create_file(input_path)
        return
    
    with open(input_path, "r") as file_input:
        content = file_input.read()
    
    with open(output_path, "w") as file_output:
        file_output.write(content[::-1])
    sys.stdout.write(f"{input_path}の内容を、{output_path}に逆順にして出力・保存しました。")
    pass

def copy_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していないので、先に入力先ファイルを作成します。")
        create_file(input_path)
        return
    
    with open(input_path, "r") as file_input:
        content = file_input.read()
    
    with open(output_path, "w") as file_output:
        file_output.write(content)
    sys.stdout.write(f"{input_path}の内容を、{output_path}に出力・保存しました。")
    pass

def duplicate_contents(input_path, times):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していないので、先に入力先ファイルを作成します。")
        create_file(input_path)
        return
    
    with open(input_path, "r") as file_input:
        content = file_input.read().strip()
        sys.stdout.write(f"{input_path}の内容を、指定した回数分コピーしたい場合は[P]を入力、\n" +
                            "また、コマンド内で指定済みの回数分コピーしたい場合は[D]を入力して下さい。")
        sys.stdout.flush()
        input = sys.stdin.readline().strip().upper()
    
    if input == "P":
        sys.stdout.write(f"何回コピーを行いますか。\n")
        sys.stdout.flush()
        input_num = int(sys.stdin.readline().strip())

        with open(input_path, "w") as file_output:
            times = input_num
            for i in range(times):
                if i < times -1:
                    file_output.write(content + "\n")
                else:
                    file_output.write(content)
        sys.stdout.write(f"{input_path}に{times}回コピーし、上書きを行いました。")

    else:
        with open(input_path, "w") as file_output:
            for i in range(times):
                if i < times -1:
                    file_output.write(content + "\n")
                else:
                    file_output.write(content)
        sys.stdout.write(f"{input_path}に{times}回コピーし、上書きを行いました。")
    pass

def replace_string(input_path, needle, newstring):
    if not os.path.exists(input_path):
        print(f"{input_path}が存在していないので、先に入力先ファイルを作成します。")
        create_file(input_path)
        return
    with open(input_path, "r") as file_input:
        content = file_input.read()
    with open(input_path, "w") as file_output:
        file_output.write(content.replace(needle, newstring))
    sys.stdout.write(f"{input_path}内の全ての[needle]という文字列を\n" +
                     "[newstring]に置き換え・上書きを行いました。")
    pass

def main():
    if len(sys.argv) < 3:
        print("下記のコマンドを、ターミナル上で入力して下さい。\n" +
              "また、ディレクトリがきちんと実行ファイル上に移動しているか、確認をして下さい。\n" +
              "python3 file_manipulator.py <operation> <inputpath> [<outputpath>/n/<needle> <newstring>]")
        return

    operation = sys.argv[1]
    input_path = sys.argv[2]

    if operation == "create_inputfile" and len(sys.argv) == 3:
        create_file(input_path)
    elif operation == "reverse" and len(sys.argv) == 4:
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