from flask import Flask, render_template, request
from placement import Placement

app = Flask(__name__)

placement = Placement()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/placement")
def show_placement():

    regno = request.args.get("regno")
    name = request.args.get("name")
    cgpa = float(request.args.get("cgpa"))
    skills = request.args.get("skills")
    backlogs = int(request.args.get("backlogs"))

    data = placement.check_placement(
        regno,
        name,
        cgpa,
        skills,
        backlogs
    )

    return render_template("result.html", data=data)

app.run(debug=True)
