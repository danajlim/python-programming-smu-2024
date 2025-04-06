import os

def remove_comments(input_filename):
    # 파일이 존재하는지 확인
    if not os.path.exists(input_filename):
        print("입력한 파일이 존재하지 않습니다. 다시 시도하세요.")
        return

    # 새 파일 이름 생성
    output_filename = "cr_" + input_filename

    # 주석 제거하여 새 파일에 쓰기
    with open(input_filename, "r", encoding="utf-8") as input_file:
        with open(output_filename, "w", encoding="utf-8") as output_file:
            for line in input_file:
                # 주석 제거
                line_without_comment = line.split("#")[0]
                output_file.write(line_without_comment)

    print(f"새로운 파일 '{output_filename}'이 생성되었습니다.")

def main():
    while True:
        # 파일 이름 입력 받기
        input_filename = input("파일 이름을 입력하세요: ")

        # 주석 제거 함수 호출
        remove_comments(input_filename)

if __name__ == "__main__":
    main()
