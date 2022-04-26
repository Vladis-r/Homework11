from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
from flask import Flask, render_template
import json


with open("candidates.json", encoding="utf-8") as file:
    candidates = json.load(file)


app = Flask(__name__)


@app.route('/')
def get_candidates():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<candidate_id>')
def get_single(candidate_id):
    candidate = get_candidate(candidate_id, candidates)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def candidate_search(candidate_name):
    number_of_candidates = len(get_candidates_by_name(candidate_name, candidates))
    list_of_candidates = get_candidates_by_name(candidate_name, candidates)
    return render_template(
        'search.html',
        number_of_candidates=number_of_candidates,
        list_of_candidates=list_of_candidates,
        candidate_name=candidate_name
    )


@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    list_of_candidates = get_candidates_by_skill(skill_name, candidates)
    candidates_with_skill = len(get_candidates_by_skill(skill_name, candidates))
    return render_template(
        'skill.html',
        skill_name=skill_name,
        candidates_with_skill=candidates_with_skill,
        list_of_candidates=list_of_candidates
    )


if __name__ == '__main__':
    app.run()
