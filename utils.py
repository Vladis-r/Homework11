import json

def load_candidates_from_json(candidates):
    """
    Функция выводит список кандидатов
    """
    list_of_candidates = []
    for candidate in candidates:
        list_of_candidates.append(candidate["name"])
    return list_of_candidates


def get_candidate(candidate_id, candidates):
    """
    Функция выводит кандидата по его id
    """
    for candidate in candidates:
        if candidate["id"] == int(candidate_id):
            return candidate


def get_candidates_by_name(candidate_name, candidates):
    """
    Функция выводит список кандидатов по имени
    """
    list_of_candidates = []
    for candidate in candidates:
        if candidate["name"].split()[0].lower() == candidate_name.lower() or candidate["name"].split()[1].lower() == candidate_name.lower():
            list_of_candidates.append(candidate)
    return list_of_candidates


def get_candidates_by_skill(skill_name, candidates):
    """
    Функция выводит список кандидатов по скиллу
    """
    list_of_candidates = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            list_of_candidates.append(candidate)
    return list_of_candidates
