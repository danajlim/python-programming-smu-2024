def count_characters_in_file(file_path):
    char_count = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            for char in content:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        print("Character frequencies in the file:")
        for char, count in char_count.items():
            print(f"'{char}': {count}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 예시 파일 경로
file_path = 'example.txt'
count_characters_in_file(file_path)
