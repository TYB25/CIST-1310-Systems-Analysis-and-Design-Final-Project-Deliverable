from flask import Flask, render_template, request
import sqlite3 as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/bookaroom')
def bookaroom():
    return render_template('booking.html')

@app.route("/addbookingrecord", methods = ["POST", "GET"])
def addbookingrecord():
    if request.method == "POST":
        guest_name = request.form["name"]
        checkin_date = request.form["checkin"]
        checkout_date = request.form["checkout"]
        room_type = request.form["roomtype"]

        insert_query = "INSERT INTO hotel (guest_name, checkin_date, checkout_date, room_type) VALUES (?, ?, ?, ?)"

        with sql.connect("hotel_bookings.db") as conn:
            cursor = conn.cursor()
            cursor.execute(insert_query, (guest_name, checkin_date, checkout_date, room_type))
            conn.commit()
            return render_template("confirmation.html", name=guest_name, checkin=checkin_date, checkout=checkout_date, roomtype=room_type)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Flask' and password == 'Panther$':
            conn = sql.connect("hotel_bookings.db")
            conn.row_factory = sql.Row

            select_query = "SELECT * FROM hotel"
            cursor = conn.cursor()
            cursor.execute(select_query)
            rows = cursor.fetchall()
            conn.close()
            return render_template("reservation_list.html", rows=rows)
        else:
            return render_template('login_error.html', name=username)
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run()