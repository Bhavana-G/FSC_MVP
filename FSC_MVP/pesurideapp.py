from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ride.db'
db = SQLAlchemy(app)

class Rides(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    source = db.Column(db.String(255), nullable=False)
    dest = db.Column(db.String(255), nullable=False)
    ride_type = db.Column(db.String(255), nullable=False)
    free_seats = db.Column(db.Integer(), nullable=False)
    departure = db.Column(db.DateTime(), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    ph_no = db.Column(db.Integer(), nullable=False)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/addRide', methods=['POST', 'GET'])
def addRide():
    if request.method == 'POST':
        new_ride = Rides(source=request.form['source'],
                        dest=request.form['dest'],
                        ride_type=request.form['type'],
                        free_seats=request.form['seats'],
                        departure=datetime.strptime(request.form['dept'], r'%Y-%m-%dT%H:%M'),
                        name=request.form['name'],
                        ph_no=request.form['number'])
        try:
            db.session.add(new_ride)
            db.session.commit()
            return '<div style="display:block;"><a href="/"><img alt="PES University" src="/static/images/PESlogo.jpeg"/></a>' + '<span style="padding: 60px; display: inline-block; vertical-align: top; text-align: center; background: #1abc9c; color: white; font-size: 50px; font-family: Arial;">Ride ID ' + str(new_ride.id) +' added successfully</span></div>'
        except Exception as e:
            return 'There was an error adding the Ride, please try again'
    else:
        return render_template('addRide.html')

@app.route('/findRide')
def findRide():
    rides = Rides.query.order_by(Rides.departure).all()
    return render_template('findRide.html', rides=rides)

@app.route('/deleteRide/<int:id>')
def delRide(id):
    ride = Rides.query.get_or_404(id)

    try:
        db.session.delete(ride)
        db.session.commit()
        return redirect('/findRide')
    except:
        return 'There was problem deleting that ride'

@app.route('/updateRide/<int:id>', methods= ['GET', 'POST'])
def updateRide(id):
    ride = Rides.query.get_or_404(id)
    
    if request.method == 'POST':
        ride.ride_type = request.form['type']
        ride.free_seats= request.form['seats']
        ride.departure = datetime.strptime(request.form['dept'], r'%Y-%m-%dT%H:%M')

        try:
            db.session.commit()
            return redirect('/findRide')
        except:
            return 'There was problem updating that ride'
    else:
        return render_template('updateRide.html', ride=ride)

if __name__ == "__main__":
    app.run('0.0.0.0')
