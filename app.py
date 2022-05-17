from flask import Flask, render_template, json, redirect, jsonify
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_trinhaa'
app.config['MYSQL_PASSWORD'] = '5478' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_trinhaa'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes
@app.route('/')
def home():
    return render_template("main.j2")

@app.route('/customers', methods=["GET", "POST"])
def customers():
    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("customers.j2", data=data)

    if request.method == "POST":
        if request.form.get("Add_Customers"):
            name = request.form["cname"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            query = "INSERT INTO Customers (name, email, phone_num, address) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, email, phone, address))
            mysql.connection.commit()

            return redirect("/customers")

@app.route("/delete_customers/<int:id>")
def delete_customers(id):
    query = "DELETE FROM Customers WHERE customerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/customers")

# Listener
if __name__ == "__main__":
    app.run(port=1995, debug=True)

