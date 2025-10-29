from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

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
    flash("Thanks! Your invoice has been submitted.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
