def get_password(file_name: str) -> str:
    """Открывает файл, возвращает содержимое"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
