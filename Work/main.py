import flask

import utils

data = utils.file_("candidates.json")

app = flask.Flask(__name__)


@app.route("/")
def main_page():
    return flask.render_template("index.html", candidate=data)


@app.route("/candidate/<int:uid>")
def profile_page(uid):
    candidate = utils.get_candidate(uid)
    return flask.render_template("profile.html", candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = utils.get_candidates_by_name(name)
    return flask.render_template("search.html", candidates=candidates, candidate_len=len(candidates) )


@app.route("/search_skills/<skills>")
def search_skills(skills):
    candidates = utils.get_candidates_by_skill(skills)
    return flask.render_template("skills.html", candidates=candidates, candidate_len=len(candidates), skill=skills)


app.run(debug=True)
