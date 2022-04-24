from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def main():
    """
    Функция, которая выводит на главную страницу список кандидатов

    :return: возвращаем список кандидатов
    """
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id_candidate>")
def id_candidates(id_candidate):
    """
    Функция, которая выводит кандидата по номеру позиции
    :param id_candidate: номер позиции кандидата
    :return: возвращает информацию о кандидате, который соответсвует указанной позиции
    """
    candidate = utils.get_candidate_from_id(id_candidate)
    if candidate is None:
        return render_template('error.html')
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def name_candidates(candidate_name):
    """
    Функция, которая выводит кандидата по имени
    :param candidate_name: имя кандидата
    :return: возвращает информацию о кандидате, который соответсвует указанному имени
    """
    candidate = utils.get_candidates_by_name(candidate_name)
    if len(candidate) == 0:
        return render_template('error.html')

    return render_template('search.html', candidates=candidate, candidates_len=len(candidate))


@app.route("/skills/<skill>")
def get_candidate_from_skills(skill):
    """
    Функция, которая выводит кандидатов в зависимости от указанного навыка (skill)
    :param skill: навык кандидата
    :return: возвращает список кандидатов, у которых имеются соответствующие навыки
    """
    candidate = utils.get_candidate_from_skills(skill)
    if len(candidate) == 0:
        return render_template('error.html')

    return render_template('skill.html', candidates=candidate, skill_name=skill.lower().title(),
                           len_skill=len(candidate))


app.run()
