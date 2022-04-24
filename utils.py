import json


def load_candidates_from_json():
    """
    Функция для получения списка кандидатов из json-файла
    :return: возвращает список кандидатов из json-файла
    """
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidate_from_id(candidate_id):
    """
    Функция для формирования информации о кандидате по шаблону в зависимости от выбранной позиции
    :param candidate_id: получает номер позиции кандидата
    :return: возвращает информацию о кандидате
    """
    candidates = load_candidates_from_json()
    try:
        return next(filter(lambda spi: spi['id'] == candidate_id, candidates))
    except StopIteration:
        return None


def get_candidates_by_name(candidate_name):
    """
    Функция для формирования информации о кандидате по шаблону в зависимости от выбранного имени
    :param candidate_name: получает имя кандидата
    :return: возвращает информацию о кандидате
    """
    candidates = load_candidates_from_json()
    return [candidate for candidate in candidates if candidate_name.lower() in candidate['name'].lower()]


def get_candidate_from_skills(candidate_skill):
    """
    Функция для формирования списка кандидатов по шаблону в зависимости от выбранных навыков
    :param candidate_skill: получает навык кандидата
    :return: возвращает список кандидатов по указанным навыкам
    """
    candidates = load_candidates_from_json()
    return list(filter(lambda x: candidate_skill.lower() in x['skills'].lower().split(', '), candidates))
