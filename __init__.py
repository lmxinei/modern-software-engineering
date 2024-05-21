def count_characters(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        char_count = sum(1 for _ in file.read())
    return char_count
#utf-8

def count_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        words = file.read().split()  # 默认在空白处分割，包括空格、换行符、制表符等
    return len(words)


def main():
    param = input("请输入参数（-c 或 -w）：")
    file_name = input("请输入文件名：")

    if param == '-c':
        char_count = count_characters(file_name)
        print("字符数：", char_count)
    elif param == '-w':
        word_count = count_words(file_name)
        print("单词数：", word_count)
    else:
        print("错误：无效的参数")


if __name__ == "__main__":
    main()