from flask import Flask # Import the flask package with capital letter
from flask import request # Imported for query parameters to work
app = Flask(__name__)

""" STATIC ROUTES """

@app.route('/') # http://127.0.0.1:5000/
# A method "Index() below"
def index():
    return 'Hello Flask!' # Renders on basic route

@app.route('/<company>/<name>')
def personnel_info(company, name):
    company_data = {
        "jpmorgan": {
            "rachel": "Executive Vice President of Managerial Functions",
            "wallace": "Senior Vice President of Managerial Functions",
            "rosie": "Staff Vice President of Managerial Functions",
            "james": "Vice Vice President of Managerial Functions",
            "henri": "Junior Vice President of Managerial Functions"
        },
        "ica": {
            "diana burnwood": "A Handler and Senior ICA Operative",
            "agent 47": "An Elite Field Operative",
            "erich soders": "Former ICA Board Member and Senior Controller",
            "lucas grey": "Field Operative and Rebel Leader",
            "arthur edwards": "The Constant and Chief Administrator"
        },
        "g-corp": {
            "kazuya mishima": "The CEO",
            "jane": "The Lead Scientist",
            "nina williams": "The Head Of Operations",
            "anna williams": "A Special Operative",
            "fahkumram": "An Enforcer"
        }
    }
    
    if company.lower() in company_data:
        personnel = company_data[company.lower()]
        if name.lower() in personnel:
            return f"{name.upper()} is {personnel[name.lower()]} at {company.upper()}"
        else:
            return f"404, {name.upper()} is not in {company.upper()}"
    else:
        return f"404, {company.upper()} is not a recognized company"
