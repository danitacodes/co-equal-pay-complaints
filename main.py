from bottle import Bottle, run, get, post, request, template

app = Bottle()


@app.get('/')
def home():
    return template('form')

@app.post('/generate_pdf')
def generate_pdf():
    employer = request.forms.get('employer_name')
    return f"<p>Your complaint against {employer} was received.</p>"



@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    return True

def check_inputs(company, details):
    return company != "" and details != ""

run(app, host='localhost', port=8080)
