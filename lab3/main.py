import re

ipv4_pattern = re.compile(
    r"\b(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b"
)


# Проверка IP-адреса
def is_valid_ipv4(ip):
    return bool(re.fullmatch(ipv4_pattern, ip))


# Поиск всех корректных IP-адресов в тексте
def find_all_ipv4(text):
    return ipv4_pattern.findall(text)


# Чтение содержимого файла
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Основная функция с match-case
def main():
    print("Выберите опцию:")
    print("1 - Проверка IP-адреса")
    print("2 - Поиск IP в файле")

    option = input("Введите номер опции: ")

    match option:
        case "1":  # Проверка IP-адреса
            ip = input("Введите IP-адрес: ")
            if is_valid_ipv4(ip):
                print(f"IP-адрес {ip} корректен.")
            else:
                print(f"IP-адрес {ip} некорректен.")

        case "2":  # Поиск IP-адресов в файле
            try:
                content = read_file("IPv4.txt")
                ips = find_all_ipv4(content)
                if ips:
                    print(f"Найденные IP-адреса: {ips}")
                else:
                    print("IP-адреса не найдены.")
            except FileNotFoundError:
                print("Файл не найден.")

        case _:  # Обработка некорректного выбора
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()
