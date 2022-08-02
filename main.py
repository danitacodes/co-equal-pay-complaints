from bottle import Bottle, run, get, post, request, template

app = Bottle()

# will be deprecated when new FE is built
@app.get('/')
def home():
    return template('form')

# get pdf returns the list of pdfs created by the user previously
@app.get("/pdf")
def get_pdfs():
    pass

# create new pdf for user
@app.post('/pdf')
def generate_pdf():
    employer = request.forms.get('employer_name')
    return f"<p>Your complaint against {employer} was received.</p>"

# submit pdf sends the generated pdf
# to the Colorado Department of Labor and Employment
def submit_pdf():
    pass

run(app, host='localhost', port=8080)
