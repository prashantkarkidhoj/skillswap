from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "SkillSwap is running!"

def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

if __name__ == "__main__":
    app.run(debug=True)