-- Draft of Data Manipulation Queries for CS 340 Project

---------------------------------------------------------------------------------------------------------
-- Customers Table
-- We can do CRUD, CRU, or CR. Leaning towards CRU. 
-- : Used to denote variables that will be populated by the website backend.
---------------------------------------------------------------------------------------------------------

-- Display Customers
SELECT customerID, name, email, phone_num, address
FROM Customers;

SELECT * FROM Customers;

-- Create new Customers
INSERT INTO Customers (name, email, phone_num, address)
VALUES (:nameInput, :emailInput, :phone_numInput, :addressInput);

-- Delete Customers
DELETE FROM Customers WHERE CustomerID = :CustomerID;

-- Update Customers
SELECT name, email, phone_num, address 
FROM Customers 
WHERE customerID = :CustomerID;

UPDATE Customers
SET name = :nameInput,
    email = emailInput,
    phone_num = :phone_numInput,
    address = :addressInput
WHERE customerID = :CustomerID;

---------------------------------------------------------------------------------------------------------
-- Drivers Table
-- We can do CR for this table to simplify things.
-- : Used to denote variables that will be populated by the website backend.
---------------------------------------------------------------------------------------------------------

-- Display Drivers
SELECT driverID, name
FROM Drivers;

SELECT * FROM Drivers;

-- Create new Drivers
INSERT INTO Drivers (name)
VALUES (:nameInput);

---------------------------------------------------------------------------------------------------------
-- Items Table
-- We can do CRUD, CRU, or CR. Leaning towards CRU.
-- : Used to denote variables that will be populated by the website backend.
---------------------------------------------------------------------------------------------------------

-- Display Items
SELECT itemID, name, price
FROM Items;

SELECT * FROM Items;

-- Create new Items
INSERT INTO Items (name, price)
VALUES (:nameInput, :priceInput);

-- Delete Items
DELETE FROM Items WHERE itemID = :ItemID;

-- Update Items
SELECT name, price 
FROM Items 
WHERE itemID = :ItemID;

UPDATE Items
SET name = :nameInput,
    price = :priceInput
WHERE itemID = :ItemID;

---------------------------------------------------------------------------------------------------------
-- Discounts Table
-- We can do CRUD, CRU, CRD, or CR. Leaning towards CR if we add an expiration date attribute.
-- : Used to denote variables that will be populated by the website backend.
---------------------------------------------------------------------------------------------------------

-- Display Discounts
SELECT discountID, code, percent_off
FROM Discounts;

SELECT * FROM Discounts;

-- Create new Discounts
INSERT INTO Discounts (code, percent_off)
VALUES (:codeInput, :percent_offInput);

-- Delete Discounts
DELETE FROM Discounts WHERE discountID = :DiscountID;

-- Update Discounts
SELECT code, percent_off 
FROM Discounts 
WHERE discountID = :DiscountID;

UPDATE Discounts
SET code = :codeInput,
    percent_off = :percent_offInput
WHERE discountID = :DiscountID;

---------------------------------------------------------------------------------------------------------
-- Orders Table
-- Full CRUD implementation
-- : Used to denote variables that will be populated by the website backend.
---------------------------------------------------------------------------------------------------------

-- Display Orders
SELECT Orders.orderID, Customer.name, Orders.is_delivery, Drivers.name, Orders.credit_card, Discounts.code, Orders.order_total
FROM Orders INNER JOIN Customers ON Orders.customerID = Customers.customerID
INNER JOIN Drivers ON Orders.driverID = Drivers,driverID
INNER JOIN Discounts ON Orders.discountID = Discounts.discountID;

-- Create new Orders
-- Drop down for Customer, Driver, and Discount.
SELECT customerID, name FROM Customers;
SELECT driverID, name FROM Drivers;
SELECT discountID, code FROM Discounts;

INSERT INTO Orders (customer_name, is_delivery, driver_name, credit_card, discount_code, order_total)
VALUES (:customer_dropInput, :is_delivery, :driver_dropInput, credit_card, discount_dropInput, order_total);

-- Delete Orders
DELETE FROM Orders WHERE orderID = :OrderID;

-- Update Orders
SELECT Orders.orderID, Customer.name, Orders.is_delivery, Drivers.name, Orders.credit_card, Discounts.code, Orders.order_total
FROM Orders INNER JOIN Customers ON Orders.customerID = Customers.customerID
INNER JOIN Drivers ON Orders.driverID = Drivers,driverID
INNER JOIN Discounts ON Orders.discountID = Discounts.discountID
WHERE orderID = :OrderID;

UPDATE Orders
SET customer_name = :customer_dropInput,
    is_delivery = :is_deliveryInput
    driver_name = :driver_dropInput
    credit_card = :credit_cardInput
    discount_code = :discount_dropInput
    order_total = :order_totalInput
WHERE orderID = :OrderID;
