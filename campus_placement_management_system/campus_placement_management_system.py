from flask import Flask, request

app = Flask(__name__)

class Placement:

    def check_placement(self, regno, name, cgpa, skills, backlogs):

        if cgpa >= 7.0 and backlogs == 0:
            status = "Eligible"
        else:
            status = "Not Eligible"

        if cgpa >= 9:
            company = "Google / Microsoft"
        elif cgpa >= 8:
            company = "Amazon / Infosys"
        elif cgpa >= 7:
            company = "TCS / Wipro"
        else:
            company = "No Company Recommendation"

        return f"""
        <h1>Campus Placement Management System</h1>

        <h3>Student Details</h3>

        Register Number : {regno}<br>
        Name : {name}<br>
        Skills : {skills}<br><br>

        <h3>Placement Summary</h3>

        CGPA : {cgpa}<br>
        Backlogs : {backlogs}<br>
        Eligibility Status : {status}<br>
        Recommended Companies : {company}<br>
        """

placement = Placement()

@app.route("/")
def home():

    return """
    <h1>Campus Placement Management System</h1>

    <form action="/placement">

        Register Number:
        <input type="text" name="regno"><br><br>

        Student Name:
        <input type="text" name="name"><br><br>

        CGPA:
        <input type="number" step="0.01" name="cgpa"><br><br>

        Skills:
        <input type="text" name="skills"><br><br>

        Number of Backlogs:
        <input type="number" name="backlogs"><br><br>

        <input type="submit" value="Check Placement Eligibility">

    </form>
    """

@app.route("/placement")
def show_placement():

    regno = request.args.get("regno")
    name = request.args.get("name")
    cgpa = float(request.args.get("cgpa"))
    skills = request.args.get("skills")
    backlogs = int(request.args.get("backlogs"))

    return placement.check_placement(
        regno,
        name,
        cgpa,
        skills,
        backlogs
    )

app.run(debug=True)
