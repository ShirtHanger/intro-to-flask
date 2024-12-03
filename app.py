from flask import Flask # Import the flask package with capital letter
from flask import request # Imported for query parameters to work
app = Flask(__name__)

""" STATIC ROUTES """

@app.route('/') # http://127.0.0.1:5000/
# A method "Index() below"
def index():
    return 'Hello Flask!' # Renders on basic route

""" 
decorators (@) are wrapper functions used to modify and extend the behavior of a normal function.

In Flask, we can use route() decorators like @app.route("/") to assign functions to specific URL paths. 
When a user accesses a specific route, Flask is able to determine which function needs to run. 

To add a second route to our Flask app, simply define another function beneath a new @app.route() decorator, like so:
"""

@app.route('/information') # http://127.0.0.1:5000/information
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

""" DYNAMITC ROUTE

We define route parameters using this syntax: <variable> 
- where variable is the name of the parameter that will be defined in the function where we want to access it.
Similar to /:variable in JS
"""

@app.route('/profile/<name>')
def profile(name):
    return f"This is the profile information for {name.upper()}"

@app.route('/personnel/<name>')
def personnel(name):
    
    personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}
    if name.lower() in personnel:
        return f"{name.upper()} is {personnel[f'{name.lower()}']} at The ICA"
    else:
        return f"404, {name.upper()} is not in this company"

@app.route('/ica/<name>')
def ica_personnel(name):
    
    ica_personnel = {
    "Diana Burnwood": "A Handler and Senior ICA Operative",
    "Agent 47": "An Elite Field Operative",
    "Erich Soders": "Former ICA Board Member and Senior Controller",
    "Lucas Grey": "Field Operative and Rebel Leader",
    "Arthur Edwards": "The Constant and Chief Administrator"
}
    
    if name.lower() in ica_personnel:
        return f"{name.upper()} is {ica_personnel[f'{name.lower()}']} at The ICA"
    else:
        return f"404, {name.upper()} is not in this company"
    
@app.route('/g-corp/<name>')
def tekken_personnel(name):
    
    tekken_personnel = {
    "kazuya mishima": "The CEO",
    "jane": "The Lead Scientist",
    "nina williams": "The Head Of Operations",
    "anna williams": "A Special Operative",
    "fahkumram": "An Enforcer"
}
    
    if name.lower() in tekken_personnel:
        return f"{name.upper()} is {tekken_personnel[f'{name.lower()}']} at G-Corp"
    else:
        return f"404, {name.upper()} is not in this company"


""" 
Query Parameters

Another effective way to pass additional information in a URL to a server is though query parameters. 
Query parameters are added to the end of a URL after a ? and are formatted as key=value pairs. 
In Express, these parameters are conveniently accessible through the req.query object.

For example, consider the following URL localhost:5000/employee-search?name=Christy&age=32.

This URL contains two query parameters:

name with a value of “Christy”
age with a value of “32”.
These parameters follow the ? symbol in the URL and are separated by &.

When a request is made to this URL, the server can retrieve these values from the request object.
"""

@app.route('/employee-search') # http://127.0.0.1:5000/employee-search?name=Christy&age=32&company=JPMorgan
def employee_search():
    name = request.args.get('name')
    age = request.args.get('age')
    company = request.args.get('company')
    return f"I searched for {company} employees named {name} who are {age} years old"
    # I searched for JPMorgan employees named Christy who are 32 years old
    
""" 
The name and age keys in the request object correspond to the query parameters in the URL. 
The server can then use this data, commonly for filtering results from a database.
"""


if __name__ == '__main__':
    app.run()
    
# Run the file to see your server at http://127.0.0.1:5000/

""" 
More on Flask Routing
https://flask.palletsprojects.com/en/stable/api/?highlight=route#flask.Flask.route
"""
