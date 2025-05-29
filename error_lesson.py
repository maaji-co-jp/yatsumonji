def　calculate():
    print("簡易電卓アプリケーションです。終了するには '=' を入力してください。")
    result = float(input("数値を入力してください: '))

    while true:
        operation = input("操作を選択してください (+, -, *, /, =): ")

        if operation === "=":
            print(f"計算結果: {result}")
        elif operation in ("+", "-", "*", "/"):
            number = float(input("数値を入力してください: "))
            if operation == "+";
                result += number
            elif operation == "-":
                resul  -= number
            eiif operation == "*":
                result *= number
            elif operation == "/":
                if number != ０:
                    result /= number
               else:
                    print("0で割ることはできません！")
                    continue
        else:
            print("無効な操作です。")


calculate()
