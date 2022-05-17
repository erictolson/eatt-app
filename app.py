from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_tolsone'
app.config['MYSQL_PASSWORD'] = '3269' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_tolsone'
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

@app.route("/edit_customers/<int:id>", methods=["GET", "POST"])
def edit_customers(id):
    if request.method == "GET":
        query = "SELECT * FROM Customers WHERE customerID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_customers.j2", data=data)
    
    if request.method == "POST":
        if request.form.get("Edit_Customer"):
            customerID = request.form["customerID"]
            name = request.form["cname"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            query = "UPDATE Customers SET name = %s, email = %s, phone_num = %s, address = %s WHERE customerID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, email, phone, address))
            data = cur.fetchall()

            return redirect("/customers")

@app.route('/discounts', methods=["GET", "POST"])
def discounts():
    if request.method == "GET":
        query = "SELECT * FROM Discounts;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("discounts.j2", data=data)

    if request.method == "POST":
        if request.form.get("Add_Discounts"):
            code = request.form["code"]
            percent_off = request.form["percent_off"]

            query = "INSERT INTO Discounts (code, percent_off) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (code, percent_off))
            mysql.connection.commit()

            return redirect("/discounts")


@app.route('/drivers', methods=["GET", "POST"])
def drivers():
    if request.method == "GET":
        query = "SELECT * FROM Drivers;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("drivers.j2", data=data)

    if request.method == "POST":
        if request.form.get("Add_Drivers"):
            name = request.form["dname"]

            query = "INSERT INTO Drivers (name) VALUES (%s)" % name
            cur = mysql.connection.cursor()
            cur.execute(query, (name))
            mysql.connection.commit()

            return redirect("/drivers")


@app.route('/items', methods=["GET", "POST"])
def items():
    if request.method == "GET":
        query = "SELECT * FROM Items;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("items.j2", data=data)

    if request.method == "POST":
        if request.form.get("Add_Items"):
            name = request.form["iname"]
            price = request.form["price"]

            query = "INSERT INTO Items (name, price) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price))
            mysql.connection.commit()

            return redirect("/items")


@app.route("/delete_items/<int:id>")
def delete_items(id):
    query = "DELETE FROM Items WHERE itemID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/items")


# route for edit functionality, updating the attributes of a person in bsg_people
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/edit_items/<int:id>", methods=["POST", "GET"])
def edit_items(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Items WHERE itemID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_items.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Item' button
        if request.form.get("Edit_Item"):
            # grab user form inputs
            id = request.form["itemID"]
            name = request.form["iname"]
            price = request.form["price"]

            
            query = "UPDATE Items SET Items.name = %s, Items.price = %s WHERE Items.itemID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price, id))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/items")



# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=8659, debug=True)
