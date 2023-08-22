from flask import Flask, render_template, jsonify, session, request
from build import Build
from backgrounds import backgrounds
from attributes import attributes
from skills import skills
import json

app = Flask(__name__)
app.secret_key = "Tajni ključ"

def load_build_from_session():
    build = json.loads(session['build'], object_hook=Build)
    return build

def save_build_to_session(build):
    session['build'] = json.dumps(build.__dict__, ensure_ascii=False)        


@app.route("/", methods=['GET'])
def index():
    if session.get('build') is None:
        build = Build()
        save_build_to_session(build)
    else:
        build = load_build_from_session()
    return render_template('index.html', build=build, backgrounds=backgrounds, attributes=attributes, skills=skills)

@app.route('/build', methods=['POST'])
def update_build():
    if session.get('build') is None:
        build = Build()
        save_build_to_session(build)
    else:
        build = load_build_from_session()
    print(request.form)
    attribute_values = []
    for attribute in attributes:
        attribute_values.append(int(request.form[attribute]))
    build.set_attribute_values(attribute_values)
    skill_values = []
    for skill in skills:
        skill_values.append(int(request.form[skill]))
    build.set_skill_values(skill_values)
    build.name = request.form["name"]
    build.level = int(request.form["level"])
    build.gender = int(request.form["gender"])
    build.father = int(request.form["father"])
    build.early_life = int(request.form["early_life"])
    build.occupation = int(request.form["occupation"])
    build.reason = int(request.form["reason"])
    save_build_to_session(build)
    return render_template('index.html', build=build, backgrounds=backgrounds, attributes=attributes, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
