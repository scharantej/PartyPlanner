
# main.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///party_planner.db'
db = SQLAlchemy(app)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    special_requests = db.Column(db.String(255))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guest_list', methods=['GET'])
def guest_list():
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)

@app.route('/invitations', methods=['POST'])
def invitations():
    emails = request.form.getlist('emails')
    subject = request.form.get('subject')
    message = request.form.get('message')
    # Send invitations to the specified email addresses here
    flash('Invitations sent successfully!')
    return redirect(url_for('home'))

@app.route('/rsvp', methods=['POST'])
def rsvp():
    name = request.form.get('name')
    email = request.form.get('email')
    special_requests = request.form.get('special_requests')
    guest = Guest(name=name, email=email, special_requests=special_requests)
    db.session.add(guest)
    db.session.commit()
    # Send RSVP confirmation email to the guest here
    flash('Thank you for RSVPing!')
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
