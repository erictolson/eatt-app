from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import routes

"""
CITATIONS:
The general structure of this program is based on the CS340 provided sample Flask App.
Our references to it have been ongoing through the term
https://github.com/osu-cs340-ecampus/flask-starter-app
"""


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
        if request.form.get("search"):
            search = request.form["search"].lower()
            query = '%' + search + '%'
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM Customers WHERE name LIKE %s", (query,))
            data = cur.fetchall()

            return render_template("customers.j2", data=data)

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
            id = request.form["customerID"]
            name = request.form["cname"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            query = "UPDATE Customers SET name = %s, email = %s, phone_num = %s, address = %s WHERE customerID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, email, phone, address, id))
            mysql.connection.commit()

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

            query = "INSERT INTO Drivers (name) VALUES (%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name,))
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


@app.route("/edit_items/<int:id>", methods=["POST", "GET"])
def edit_items(id):
    if request.method == "GET":
        query = "SELECT * FROM Items WHERE itemID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_items.j2", data=data)

    if request.method == "POST":
        if request.form.get("Edit_Item"):
            id = request.form["itemID"]
            name = request.form["iname"]
            price = request.form["price"]

            
            query = "UPDATE Items SET Items.name = %s, Items.price = %s WHERE Items.itemID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, price, id))
            mysql.connection.commit()

            return redirect("/items")


@app.route('/orders', methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        query = "SELECT * FROM Orders;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customer_data = cur.fetchall()

        query3 = "SELECT * FROM Drivers"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        driver_data = cur.fetchall()

        query4 = "SELECT * FROM Discounts"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        discount_data = cur.fetchall()

        return render_template("orders.j2", data=data, customers=customer_data, drivers=driver_data, discounts=discount_data)
    
    if request.method == "POST":
        if request.form.get("Add_Orders"):
            order_total = request.form["ordertotal"]
            is_delivery = request.form["isdelivery"]
            customerID = request.form["customerid"]
            driverID = request.form["driverid"]
            discountID = request.form["discountid"]
            credit_card = request.form["creditcard"]

            if driverID == "None" and discountID == "None":
                query = "INSERT INTO Orders (order_total, is_delivery, customerID, credit_card) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (order_total, is_delivery, customerID, credit_card))
                mysql.connection.commit()

            elif driverID == "None":
                query = "INSERT INTO Orders (order_total, is_delivery, customerID, discountID, credit_card) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (order_total, is_delivery, customerID, discountID, credit_card))
                mysql.connection.commit()

            elif discountID == "None":
                query = "INSERT INTO Orders (order_total, is_delivery, customerID, driverID, credit_card) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (order_total, is_delivery, customerID, driverID, credit_card))
                mysql.connection.commit()

            else:
                query = "INSERT INTO Orders (order_total, is_delivery, customerID, driverID, discountID, credit_card) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (order_total, is_delivery, customerID, driverID, discountID, credit_card))
                mysql.connection.commit()

            return redirect("/orders")


@app.route("/delete_orders/<int:id>")
def delete_orders(id):
    query = "DELETE FROM Orders WHERE orderID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/orders")


@app.route('/order_items', methods=["GET", "POST"])
def order_items():
    if request.method == "GET":
        query = "SELECT orderitemID, orderID, Order_Items.itemID, Items.name, unit_price, quantity, line_price FROM Order_Items LEFT JOIN Items ON Order_Items.itemID = Items.itemID;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        order_data = cur.fetchall()

        query3 = "SELECT * FROM Items"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        item_data = cur.fetchall()

        return render_template("order_items.j2", data=data, order_data=order_data, item_data=item_data)

    if request.method == "POST":
        if request.form.get("Add_Order_Items"):
            orderID = request.form["order"]
            itemID = request.form["item"]
            unit_price = request.form["unitprice"]
            quantity = request.form["quantity"]
            line_price = request.form["linetotal"]

            query = "INSERT INTO Order_Items (orderID, itemID, unit_price, quantity, line_price) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (orderID, itemID, unit_price, quantity, line_price))
            mysql.connection.commit()

            return redirect("/order_items")


@app.route("/edit_order_items/<int:id>", methods=["GET", "POST"])
def edit_order_items(id):
    if request.method == "GET":
        query = "SELECT orderitemID, orderID, Order_Items.itemID, Items.name, unit_price, quantity, line_price FROM Order_Items LEFT JOIN Items ON Order_Items.itemID = Items.itemID WHERE orderitemID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        order_data = cur.fetchall()

        query3 = "SELECT * FROM Items"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        item_data = cur.fetchall()

        return render_template("edit_order_items.j2", data=data, order_data=order_data, item_data=item_data)
    
    if request.method == "POST":
        if request.form.get("Edit_Order_Items"):
            orderitemID = request.form["orderitemID"]
            orderID = request.form["order"]
            itemID = request.form["item"]
            unit_price = request.form["unitprice"]
            quantity = request.form["quantity"]
            line_price = request.form["linetotal"]

            query = "UPDATE Order_Items SET orderID = %s, itemID = %s, unit_price = %s, quantity = %s, line_price = %s WHERE orderitemID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (orderID, itemID, unit_price, quantity, line_price, orderitemID))
            mysql.connection.commit()

            return redirect("/order_items")


@app.route("/delete_order_items/<int:id>")
def delete_order_items(id):
    query = "DELETE FROM Order_Items WHERE orderitemID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/order_items")


if __name__ == "__main__":
    app.run(port=8659, debug=True)
