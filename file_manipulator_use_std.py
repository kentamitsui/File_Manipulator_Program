import sys,os

# ファイル選択の関数
# 関数にセットする変数の設定
path_inputfile = "inputpath_use_std.txt"
path_outputfile = "outputpath_use_std.txt"

def file_operation(command, path_input, path_output):
    ##### 入力先ファイルの内容を逆順にして、出力先ファイルに書き込む処理 #####
    # 入力先ファイルが存在しなかった場合の処理
    # 入力値が小文字の場合も想定して、upper()で大文字化する
    if command.upper() == "R":
        # outputpath.txtが存在しなかった場合、空ファイルを作成する
        # 出力先のファイルが存在しない場合、入力用ファイルへの入力後に空ファイルを作成する
        if not os.path.exists(path_output):
            with open(path_output, "w") as file:
                pass
        # 入力先ファイルの内容を逆順に並び替え、出力先ファイルに書き込む
        with open(path_input, "r") as file_input:
            content = file_input.readline().strip()

        reversed_content = content[::-1]
        
        with open(path_output, "w") as file_output_reversed:
            file_output_reversed.write(reversed_content)
        
        sys.stdout.write(f"{file_output_reversed}に{file_input}の内容を、逆順にして保存しました。\n")
        sys.stdout.flush()
        pass
    ##### 入力先ファイルの内容を、出力先ファイルにコピーする処理 #####
    # 入力先ファイルが存在しなかった場合の処理
    # 入力値が小文字の場合も想定して、upper()で大文字化する
    elif command.upper() == "C":
        # 出力先のファイルが存在しない場合、入力用ファイルへの入力後に空ファイルを作成する
        if not os.path.exists(path_output):
            with open(path_output, "w") as file:
                pass
        # 入力先ファイルを読み込み、出力先ファイルにcontentの内容(入力先ファイル)を書き込む
        with open(path_input, "r") as file_input:
            content = file_input.readline().strip()

        with open(path_output, "w") as file_output_copy:
            file_output_copy.write(content)

        sys.stdout.write(f"{file_input}の内容を{file_output_copy}にコピーしました。\n")
        sys.stdout.flush()
        pass
    ##### 入力先ファイルの内容を読み込み、指定回数分元ファイルにコピーする処理 #####
    # 入力先ファイルが存在しなかった場合の処理
    # 入力値が小文字の場合も想定して、upper()で大文字化する
    elif command.upper() == "D":
        if not os.path.exists(path_output):
            with open(path_output, "w") as file:
                pass
    # read()を用いて入力先ファイル[全体]を読み込み、指定回数分元ファイルにcontentの内容を書き込む
        with open(path_input, "r") as file_input:
            content = file_input.read().strip()

        sys.stdout.write(f"{path_input}の内容を何回複製しますか。\n")
        sys.stdout.flush()

        count_duplicate = int(sys.stdin.readline().strip())

        with open(path_input, "w") as file_output_duplicate:
            for i in range(count_duplicate):
                if i < count_duplicate - 1:
                    file_output_duplicate.write(content + "\n")
                # 最後の行だけ改行をしない
                else:
                    file_output_duplicate.write(content)
            
        sys.stdout.write(f"{path_input}に保存済みの内容を、{count_duplicate}回複製・上書きしました。\n")
        sys.stdout.flush()
        pass
    ##### 入力先ファイルの内容に[needle]が含まれているかを読み込み、 #####
    ##### 全ての[needle]を[newstring]に置き換える処理 #####
    # 入力先ファイルが存在しなかった場合の処理
    # 入力値が小文字の場合も想定して、upper()で大文字化する
    elif command.upper() == "P":
        if not os.path.exists(path_output):
            with open(path_output, "w") as file:
                pass
    # read()を用いて入力先ファイルを読み込み、置き換え処理を行う
        with open(path_input, "r") as file_input:
            content = file_input.read().strip()

        with open(path_output, "w") as file_output_replace:
            file_output_replace.write(content.replace("needle", "newstring"))
    
        sys.stdout.write(f"{file_input}内の[needle]を、[newstring]に置き換えました。\n")
        sys.stdout.flush()
        pass

def choose_commands(prompt):
        # プロンプトがtrueである限り、ターミナルに出力を行う
    while True:
        sys.stdout.write(prompt + "\n")
        sys.stdout.flush()

        try:
            # strip()を使用して、文字列から改行文字列の[\n]を除去
            return str(sys.stdin.readline().strip())
        except ValueError:
            sys.stdout.write("操作したいコマンドを選択して下さい。\n")
            sys.stdout.flush()

if not os.path.exists(path_inputfile):
    sys.stdout.write("保存したい文字を入力して下さい。\n")
    sys.stdout.flush()

    with open(path_inputfile, "w") as file:
        # strip()を用いて、末尾の空白文字を削除する
        file.write(sys.stdin.readline().strip())

    sys.stdout.write(f"[{path_inputfile}]ファイルを作成し、先程の入力内容を保存しました。\n")
    sys.stdout.flush()
else:
    sys.stdout.write(f"[{path_inputfile}]の内容を変更しますか？\n変更する場合は[Y]、\n変更せず終了する場合は[N]、\nその他の操作を行う場合は[E]を入力して下さい。\n")
    sys.stdin.flush()

    user_input = sys.stdin.readline().strip().upper()
    
    if user_input == "Y":
        sys.stdout.write("保存したい文字を入力して下さい。\n")
        sys.stdout.flush()
        # strip()を用いて、末尾の空白文字を削除する
        content_new = sys.stdin.readline().strip()
        
        with open(path_inputfile, "w") as file:
            file.write(content_new)

        sys.stdout.write("先程の入力内容を保存しました。\n")
        sys.stdout.flush()
    elif user_input == "E":
        prompt_choose = choose_commands("ファイル内容を逆順にしたい場合は[R]、\n" +
        "ファイル内容をコピーしたい場合は[C]、\n" +
        "ファイル内容を指定回数コピーしたい場合は[D]、\n" +
        "ファイル内容を置き換えしたい場合は[P]を入力して下さい。")

        file_operation(prompt_choose, path_inputfile, path_outputfile)
        pass

    elif user_input == "N":
        sys.stdout.write(f"{path_inputfile}の内容は変更せず、プログラムを終了します。\n")
        sys.stdout.flush()
        pass