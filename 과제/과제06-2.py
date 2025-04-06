def findChar(cList, ch):
    for sublist in cList:
        if sublist[0] == ch:
            return sublist
    return None

def countChars(txt):
    if not txt:
        return None
    txt = txt.lower()  # 모든 문자를 소문자로 변환
    result = []
    for char in txt:
        char_list = findChar(result, char)
        if char_list:
            char_list[1] += 1
        else:
            result.append([char, 1])
    return result

def printList(cList):
    for sublist in cList:
        print(f"{sublist[0]}: {sublist[1]}")

def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."
    frequency_list = countChars(text)
    if frequency_list:
        printList(frequency_list)
    else:
        print("입력된 텍스트가 없습니다.")

if __name__ == "__main__":
    main()
