def findChar(cList, ch):
    for sublist in cList:
        if sublist[0] == ch:
            return sublist
    return None

def countChars(txt):
    if not txt:
        return None
    txt = txt.lower()  
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
    with open('lorem.txt', 'r') as file:
        text = file.read().replace('\n', '')  
    frequency_list = countChars(text)
    if frequency_list:
        printList(frequency_list)
    else:
        print("입력된 텍스트가 없습니다.")

if __name__ == "__main__":
    main()
