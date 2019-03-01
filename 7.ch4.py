ans = [7, 25, 97]

while True:
    print("qを入力して終了。")
    a = input("入力してください。：" )
    try:
        a = int(a)
    except ValueError:
        print("数字を入力するか、ｑで終了します。\n")
        continue
    if a == "q":
        print("終了します。\n")
        break
    elif a in ans:
        print("正解です！\n")
    elif a not in ans :
        print("不正解です。\n")



        
    
