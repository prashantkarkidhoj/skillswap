from flask import Flask, jsonify, request

app = Flask(__name__)

skills = [
    {"id": 1, "name": "Python", "category": "Programming"},
    {"id": 2, "name": "Design", "category": "Creative"},
    {"id": 3, "name": "Project Management", "category": "Management"},
]

@app.route("/")
def home():
    return "SkillSwap is running!"

@app.route("/skills")
def get_skills():
    return jsonify(skills)

@app.route("/skills/<int:skill_id>")
def get_skill(skill_id):
    for skill in skills:
        if skill["id"] == skill_id:
            return jsonify(skill)
    return jsonify({"error": "Skill not found"}), 404

@app.route("/skills/search")
def search_skills():
    category = request.args.get("category")
    matches = []
    if category is None:
        return jsonify(skills)
    for skill in skills:
        if skill["category"].lower() == category.lower():
            matches.append(skill)
    return jsonify(matches)
@app.route("/skills/by-name")
def get_skill_by_name():
    name = request.args.get("name")
    for skill in skills:
        if skill["name"].lower() == name.lower():
            return jsonify(skill)
    return jsonify({"error": "Skill not found"}), 404

@app.route("/skills", methods=["POST"])
def add_skill():
    new_skill_data = request.get_json()
    ids = []
    for skill in skills:
        ids.append (skill["id"])
    new_id = max(ids) + 1
    new_skill = {"id": new_id , "name": new_skill_data["name"] , "category":new_skill_data["category"]}
    skills.append(new_skill)
    return jsonify(new_skill), 201

if __name__ == "__main__":
    app.run(debug=True)
