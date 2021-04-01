#coding=utf-8

while True:
    while True:
        text1 = str(input("请输入对比文案1: "))
        print(text1)
        if len(text1.strip()) > 0:
           break
    while True:
        text2 = str(input("请输入对比文案2: "))
        print(text2)
        if len(text2.strip()) > 0:
            break
    if  text1.strip() == text2.strip():
        print("两文案对比结果一致...")
        print("=="*50)
    else:
        print("文案bug...请注意")
