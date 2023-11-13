try:
    with open("TF18_1.txt", "w") as file1:
        file1.write("Це текст з першого файлу. This is the text from the first file.")

    with open("TF18_2.txt", "w") as file2:
        file2.write("Це текст з другого файлу.This is the text from the second file.")

    with open("TF18_1.txt", "r") as file1, open("TF18_2.txt", "r") as file2, open("TF18_3.txt", "w") as file3:
        content1 = file1.read()
        content2 = file2.read()
        for i in range(0, len(content1), 20):
            file3.write(content1[i:i + 20] + "\n")

    with open("TF18_2.txt", "w") as file2, open("TF18_3.txt", "r") as file3:
        file2.write(file3.read())

    with open("TF18_2.txt", "r") as file2, open("TF18_1.txt", "w") as file1, open("TF18_3.txt", "w") as file3:
        for i in range(0, len(content2), 20):
            file3.write(content2[i:i + 20] + "\n")

    with open("TF18_1.txt", "w") as file1, open("TF18_3.txt", "r") as file3:
        file1.write(file3.read())

    with open("TF18_1.txt", "r") as file1:
        print("Зміст файлу TF18_1:")
        print(file1.read())

    with open("TF18_2.txt", "r") as file2:
        print("\nЗміст файлу TF18_2:")
        print(file2.read())

except FileNotFoundError:
    print("Помилка: Файл не знайдено.")
except Exception as e:
    print(f"Помилка: {e}")
