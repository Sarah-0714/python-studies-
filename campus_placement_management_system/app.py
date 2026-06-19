from flask import Flask, render_template, request

app = Flask(__name__)

students = {
    "23MSC001": {"name": "Sarah", "department": "AI & DS", "cgpa": 8.5, "company": "TCS", "package": 4.5},
    "23MSC002": {"name": "Assu",  "department": "CSE",     "cgpa": 9.0, "company": "Infosys", "package": 5.0},
    "23MSC003": {"name": "Priya",  "department": "IT",      "cgpa": 8.2, "company": "Wipro", "package": 4.0},
    "23MSC004": {"name": "Kavin",  "department": "ECE",     "cgpa": 7.8, "company": "HCL", "package": 3.8}
}


# Step 1 - Show search form
@app.route("/")
def home():
    return render_template("search.html")


# Step 2 - Search student eligibility
@app.route("/search", methods=["POST"])
def search():

    regno = request.form["regno"]

    if regno in students:

        student = students[regno]

        return render_template(
            "placement.html",
            regno=regno,
            name=student["name"],
            department=student["department"],
            cgpa=student["cgpa"],
            company=student["company"],
            package=student["package"]
        )

    return render_template(
        "search.html",
        error="Student record not found."
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
