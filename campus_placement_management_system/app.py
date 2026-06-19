from flask import Flask, render_template, request

app = Flask(__name__)

# Step 1 - Show search form
@app.route("/")
def home():
    return render_template("search.html")


# Step 2 - Check placement eligibility
@app.route("/search", methods=["POST"])
def search():

    regno = request.form["regno"]
    name = request.form["name"]
    department = request.form["department"]
    cgpa = float(request.form["cgpa"])

    if cgpa >= 8.5:
        company = "TCS"
        package = "6 LPA"
    elif cgpa >= 7.5:
        company = "Infosys"
        package = "5 LPA"
    elif cgpa >= 6.5:
        company = "Wipro"
        package = "4 LPA"
    else:
        company = "Not Eligible"
        package = "0 LPA"

    return render_template(
        "placement.html",
        regno=regno,
        name=name,
        department=department,
        cgpa=cgpa,
        company=company,
        package=package
    )


# Step 3 - Confirm placement
@app.route("/apply", methods=["POST"])
def apply():

    regno = request.form["regno"]
    name = request.form["name"]
    department = request.form["department"]
    cgpa = request.form["cgpa"]
    company = request.form["company"]
    package = request.form["package"]

    return render_template(
        "success.html",
        regno=regno,
        name=name,
        department=department,
        cgpa=cgpa,
        company=company,
        package=package
    )


if __name__ == "__main__":
    app.run(debug=True)
