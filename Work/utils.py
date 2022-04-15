import json

__data = []


def file_(path):
    global __data
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for i in __data:
        if i["id"] == candidate_id:
            return {
                "name": i["name"],
                "position": i["position"],
                "picture": i["picture"],
                "skills": i["skills"]
            }
    return {"not_found": "Мы за таких не в теме"}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __data:
        skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
