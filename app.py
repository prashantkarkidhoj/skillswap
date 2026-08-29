from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)
