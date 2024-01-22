result = {}

with open("1.txt", "r", encoding="utf-8") as file:
    line_count_file_1 = sum(1 for line in file)
    result.setdefault("1.txt", line_count_file_1)

with open("2.txt", "r", encoding="utf-8") as file:
    line_count_file_2 = sum(1 for line in file)
    result.setdefault("2.txt", line_count_file_2)

with open("3.txt", "r", encoding="utf-8") as file:
    line_count_file_3 = sum(1 for line in file)
    result.setdefault("3.txt", line_count_file_3)

sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
for key, value in sorted_result.items():
    with open("result_text_1", "a", encoding="utf-8") as file_result:
        file_result.writelines(f"{key}\n")
    with open(key, "r", encoding="utf-8") as file:
        for i in range(sorted_result[key]):
            stroka = file.readline().strip()
            with open("result_text_1", "a", encoding="utf-8") as file_result:
                file_result.writelines(f"{stroka}\n")







