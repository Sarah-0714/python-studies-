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

        return {
            "regno": regno,
            "name": name,
            "cgpa": cgpa,
            "skills": skills,
            "backlogs": backlogs,
            "status": status,
            "company": company
        }
