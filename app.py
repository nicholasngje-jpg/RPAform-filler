from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    company = request.form['company']
    amount = request.form['amount']
    print(f"Received: {name}, {email}, {company}, {amount}")
    return f"Thanks! Your invoice has been submitted."

if __name__ == '__main__':
    app.run()
