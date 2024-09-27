import json


def get_conf(parameter: str) -> str:
    """Преобразует project_config.json в словарь, возвращает значение по ключу parameter.
    Ключи: DATABASE_PASSWORD, EMAIL_HOST_PASSWORD, ADMIN_PASSWORD"""
    with open('project_config.json', 'r', encoding='utf-8') as file:
        parameter_dict = json.loads(file.read())
        return parameter_dict[parameter]
