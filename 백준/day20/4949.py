import sys
while True :
    # text =sys.stdin.readline() -> \n을 포함하고 있어서 text=="."을 처리할 수 없음 (출력초과)
    text=sys.stdin.readline().rstrip()
    stack = []

    if text == "." :
        break

    for i in text :
        if i == "[" or i == "(" :
            stack.append(i)
        elif i == "]" :
            if stack and stack[-1] == "[":
                stack.pop()
            else : 
                stack.append("]")
                break
        elif i == ")" :
            if stack and stack[-1] == "(":
                stack.pop()
            else :
                stack.append(")")
                break
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
