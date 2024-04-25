import streamlit as st
import sqlite3

# Function to create tables
def create_tables():
    # Connect to the SQLite database
    conn = sqlite3.connect('hotel_database.db')
    c = conn.cursor()

    # Create Hotel table
    c.execute('''CREATE TABLE IF NOT EXISTS Hotel (
                    Hotel_Branch_Id INT PRIMARY KEY,
                    Location VARCHAR(255),
                    Name VARCHAR(255)
                )''')

    # Create Department table
    c.execute('''CREATE TABLE IF NOT EXISTS Department (
                    Dept_Id INT PRIMARY KEY,
                    Dept_Name VARCHAR(255),
                    Descrpt VARCHAR(255),
                    Manager_Id INT,
                    Hotel_Branch_Id INT,
                    FOREIGN KEY (Hotel_Branch_Id) REFERENCES Hotel(Hotel_Branch_Id)
                )''')

    # Create Service table
    c.execute('''CREATE TABLE IF NOT EXISTS Service (
                    Service_id INT PRIMARY KEY,
                    Service_category VARCHAR(255),
                    Availability VARCHAR(255),
                    Cost DECIMAL(10, 2),
                    Duration VARCHAR(255),
                    Restriction VARCHAR(255),
                    Hotel_Branch_Id INT,
                    FOREIGN KEY (Hotel_Branch_Id) REFERENCES Hotel(Hotel_Branch_Id)
                )''')

    # Create Service-Service_name table
    c.execute('''CREATE TABLE IF NOT EXISTS Service_Service_name (
                    Service_id INT,
                    Service_name VARCHAR(255),
                    FOREIGN KEY (Service_id) REFERENCES Service(Service_id)
                )''')

    # Create Room table
    c.execute('''CREATE TABLE IF NOT EXISTS Room (
                    Room_id INT PRIMARY KEY,
                    Room_Types VARCHAR(255),
                    Description VARCHAR(255),
                    Rate DECIMAL(10, 2),
                    Availability VARCHAR(255),
                    Max_Occupancy INT,
                    Amenities VARCHAR(255),
                    Hotel_branch_id INT,
                    FOREIGN KEY (Hotel_branch_id) REFERENCES Hotel(Hotel_Branch_Id)
                )''')

    # Create Room-Floor_number table
    c.execute('''CREATE TABLE IF NOT EXISTS Room_Floor_number (
                    Room_id INT,
                    Floor_number INT,
                    FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
                )''')

    # Create Employee table
    c.execute('''CREATE TABLE IF NOT EXISTS Employee (
                    Emp_id INT PRIMARY KEY,
                    Emp_email_id VARCHAR(255),
                    Emp_Name VARCHAR(255),
                    DOB VARCHAR(255),
                    Address VARCHAR(255),
                    Date_of_joining VARCHAR(255),
                    Position VARCHAR(255),
                    Hotel_branch_id INT,
                    Dept_Id INT,
                    FOREIGN KEY (Hotel_branch_id) REFERENCES Hotel(Hotel_Branch_Id),
                    FOREIGN KEY (Dept_Id) REFERENCES Department(Dept_Id)
                )''')

    # Create Inventory table
    c.execute('''CREATE TABLE IF NOT EXISTS Inventory (
                    Item_Id INT PRIMARY KEY,
                    Supplier_Id INT,
                    Location VARCHAR(255),
                    Item_Name VARCHAR(255),
                    Unit_price DECIMAL(10, 2),
                    Quantity_on_hand INT,
                    Reorder_level INT,
                    Reorder_quantity INT,
                    Last_Order_Date VARCHAR(255),
                    Last_delivery_date VARCHAR(255),
                    Hotel_branch_Id INT,
                    FOREIGN KEY (Supplier_Id) REFERENCES Supplier(Supplier_Id),
                    FOREIGN KEY (Hotel_branch_Id) REFERENCES Hotel(Hotel_Branch_Id)
                )''')

    # Create Supplier table
    c.execute('''CREATE TABLE IF NOT EXISTS Supplier (
                    Supplier_Id INT PRIMARY KEY,
                    Supplier_email_Id VARCHAR(255),
                    Supplier_name VARCHAR(255),
                    Supplier_phone_no VARCHAR(20),
                    Address VARCHAR(255),
                    Contact_person VARCHAR(255),
                    Contract_details VARCHAR(255),
                    Product_category VARCHAR(255),
                    Payment_terms VARCHAR(255),
                    Transaction_history VARCHAR(255),
                    Hotel_branch_id INT,
                    FOREIGN KEY (Hotel_branch_id) REFERENCES Hotel(Hotel_Branch_Id)
                )''')

    # Create Guest table
    c.execute('''CREATE TABLE IF NOT EXISTS Guests (
                    Primary_Guest_Id INT PRIMARY KEY,
                    Primary_Guest_Name VARCHAR(255),
                    Room_id INT,
                    Membership_Details VARCHAR(255),
                    Guest_Address VARCHAR(255),
                    Guest_Email_Id VARCHAR(255),
                    Card_Details VARCHAR(255),
                    PG_Legal_Docs VARCHAR(255)
                )''')

    # Create Make_Reservation table
    c.execute('''CREATE TABLE IF NOT EXISTS Make_Reservation (
                    Primary_Guest_Id INT,
                    Reservation_Id VARCHAR(50) PRIMARY KEY,
                    Reservation_Date VARCHAR(50),
                    Check_In VARCHAR(50),
                    Check_Out VARCHAR(50),
                    Off_Season_Discount VARCHAR(50),
                    Festive_Discount VARCHAR(50),
                    Membership_Discount VARCHAR(50),
                    Payment VARCHAR(50),
                    FOREIGN KEY (Primary_Guest_Id) REFERENCES Guests(Primary_Guest_Id)
                )''')

    # Create Shares_Feedback table
    c.execute('''CREATE TABLE IF NOT EXISTS Shares_Feedback (
                    Primary_Guest_id INT,
                    Feedback_id VARCHAR(255) PRIMARY KEY,
                    Date_of_feedback DATE,
                    Comments VARCHAR(255),
                    Ratings VARCHAR(255),
                    FOREIGN KEY (Primary_Guest_id) REFERENCES Guests(Primary_Guest_Id)
                )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to insert values into tables
def insert_values():
    # Connect to the SQLite database
    conn = sqlite3.connect('hotel_database.db')
    c = conn.cursor()

    # Insert values into Hotel table
    c.execute('''INSERT INTO Hotel (Hotel_Branch_Id, Location, Name)
                VALUES (1, 'New York', 'Grand Hotel'),
                       (2, 'Paris', 'Eiffel Palace'),
                       (3, 'Tokyo', 'Sakura Inn')''')

    # Insert values into Department table
    c.execute('''INSERT INTO Department (Dept_Id, Dept_Name, Descrpt, Manager_Id, Hotel_Branch_Id)
                VALUES (101, 'Front Desk', 'Manages guest check-in and check-out', 201, 1),
                       (102, 'Housekeeping', 'Responsible for room cleaning and maintenance', 202, 2),
                       (103, 'Restaurant', 'Manages food and beverage services', 203, 3)''')

    # Insert values into Service table
    c.execute('''INSERT INTO Service (Service_id, Service_category, Availability, Cost, Duration, Restriction, Hotel_Branch_Id)
                VALUES (301, 'Room Service', '24/7', 15.00, '1 hour', 'None', 1),
                       (302, 'Laundry', '8:00 AM - 8:00 PM', 20.00, 'Same day', 'Dry cleaning only', 2),
                       (303, 'Concierge', '24/7', 0.00, 'N/A', 'None', 3)''')

    # Insert values into Room table
    c.execute('''INSERT INTO Room (Room_id, Room_Types, Description, Rate, Availability, Max_Occupancy, Amenities, Hotel_branch_id)
                VALUES (401, 'Standard', 'Cozy room with a queen-size bed', 100.00, 'Available', 2, 'Wi-Fi, TV, Mini-bar', 1),
                       (402, 'Deluxe', 'Spacious room with a king-size bed and city view', 150.00, 'Available', 2, 'Wi-Fi, TV, Mini-bar, Balcony', 2),
                       (403, 'Suite', 'Luxurious suite with separate living and bedroom areas', 250.00, 'Available', 4, 'Wi-Fi, TV, Mini-bar, Jacuzzi', 3)''')

    # Insert values into Employee table
    c.execute('''INSERT INTO Employee (Emp_id, Emp_email_id, Emp_Name, DOB, Address, Date_of_joining, Position, Hotel_branch_id, Dept_Id)
                VALUES (501, 'john@example.com', 'John Doe', '1985-05-10', '123 Main St, New York', '2020-01-15', 'Manager', 1, 101),
                       (502, 'jane@example.com', 'Jane Smith', '1990-08-20', '456 Elm St, Paris', '2019-11-20', 'Supervisor', 2, 102),
                       (503, 'alice@example.com', 'Alice Johnson', '1988-03-15', '789 Oak Ave, Tokyo', '2021-03-05', 'Waiter', 3, 103)''')

    # Insert values into Inventory table
    c.execute('''INSERT INTO Inventory (Item_Id, Supplier_Id, Location, Item_Name, Unit_price, Quantity_on_hand, Reorder_level, Reorder_quantity, Last_Order_Date, Last_delivery_date, Hotel_branch_Id)
                VALUES (601, 301, 'Storage Room 1', 'Towels', 5.00, 100, 20, 50, '2023-12-10', '2024-01-05', 1),
                       (602, 302, 'Laundry Room', 'Detergent', 10.00, 50, 10, 30, '2024-01-15', '2024-02-05', 2),
                       (603, 303, 'Concierge Desk', 'City Maps', 2.00, 200, 50, 100, '2024-02-10', '2024-03-05', 3)''')

    # Insert values into Supplier table
    c.execute('''INSERT INTO Supplier (Supplier_Id, Supplier_email_Id, Supplier_name, Supplier_phone_no, Address, Contact_person, Contract_details, Product_category, Payment_terms, Transaction_history, Hotel_branch_id)
                VALUES (701, 'supplier1@example.com', 'ABC Suppliers', '123-456-7890', '123 Main St, City', 'John Smith', 'Supplier contract details', 'Textiles', 'Net 30 days', 'Transaction history details', 1),
                       (702, 'supplier2@example.com', 'XYZ Inc.', '987-654-3210', '456 Elm St, Town', 'Jane Doe', 'Supplier contract details', 'Cleaning supplies', 'Net 45 days', 'Transaction history details', 2),
                       (703, 'supplier3@example.com', 'PQR Enterprises', '111-222-3333', '789 Oak Ave, Village', 'Alice Johnson', 'Supplier contract details', 'Furniture', 'Net 60 days', 'Transaction history details', 1)''')

    # Insert values into Guests table
    c.execute('''INSERT INTO Guests (Primary_Guest_Id, Primary_Guest_Name, Room_id, Membership_Details, Guest_Address, Guest_Email_Id, Card_Details, PG_Legal_Docs)
                VALUES (801, 'Rahul', 401, 'Gold Member', 'Delhi', 'rahul@example.com', '1234-5678-9012-3456', 'Aadhar Card-6589 3286 5876'),
                       (802, 'Neha', 402, 'Platinum Member', 'Mumbai', 'neha@example.com', '2345-6789-0123-4567', 'Aadhar Card-7896 7412 9632'),
                       (803, 'Amit', 403, 'Platinum Member', 'Jaipur', 'amit@example.com', '3456-7890-1234-5678', 'Aadhar Card-8974 7412 9658'),
                       (804, 'Priya', 401, 'Gold Member', 'Kolkata', 'priya@example.com', '4567-8901-2345-6789', 'Aadhar Card-8529 7418 9632'),
                       (805, 'Mohan', 402, 'Silver Member', 'Udaipur', 'mohan@example.com', '5678-9012-3456-7890', 'Aadhar Card-7412 8523 9874')''')

    # Insert values into Make_Reservation table
    c.execute('''INSERT INTO Make_Reservation (Primary_Guest_Id, Reservation_Id, Reservation_Date, Check_In, Check_Out, Off_Season_Discount, Festive_Discount, Membership_Discount, Payment)
                VALUES ('801', 'RE_1001', '2024-04-25', NULL, '2024-05-10', '10%', '5%', '0%', 'Paid'),
                       ('802', 'RE_1002', '2024-04-28', NULL, '2024-05-20', '15%', '0%', '10%', 'Pending'),
                       ('803', 'RE_1003', '2024-05-01', NULL, '2024-05-15', '20%', '10%', '5%', 'Paid'),
                       ('804', 'RE_1004', '2024-05-05', NULL, '2024-05-25', '25%', '15%', '0%', 'Pending'),
                       ('805', 'RE_1005', '2024-05-10', NULL, '2024-06-01', '10%', '0%', '20%', 'Paid')''')

    # Insert values into Shares_Feedback table
    c.execute('''INSERT INTO Shares_Feedback (Primary_Guest_id, Feedback_id, Date_of_feedback, Comments, Ratings)
                VALUES ('801', 'FE_2001', '2024-05-15', 'Had a wonderful stay, great service!', '5'),
                       ('802', 'FE_2002', '2024-05-25', 'Room was clean, staff was friendly.', '4'),
                       ('803', 'FE_2003', '2024-06-05', 'Excellent experience overall!', '5'),
                       ('804', 'FE_2004', '2024-06-10', 'Could improve room amenities.', '3'),
                       ('805', 'FE_2005', '2024-06-20', 'Average stay, nothing special.', '2')''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to delete a record from a table
def delete_record(table_name, condition):
    # Connect to the SQLite database
    conn = sqlite3.connect('hotel_database.db')
    c = conn.cursor()

    # Delete record from the table
    c.execute(f'DELETE FROM {table_name} WHERE {condition}')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to update a record in a table
def update_record(table_name, set_clause, condition):
    # Connect to the SQLite database
    conn = sqlite3.connect('hotel_database.db')
    c = conn.cursor()

    # Update record in the table
    c.execute(f'UPDATE {table_name} SET {set_clause} WHERE {condition}')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Streamlit UI
st.title('Hotel Management System')

# Button to create tables
if st.button('Create Tables'):
    create_tables()
    st.success('Tables created successfully!')

# Button to insert values
if st.button('Insert Values'):
    insert_values()
    st.success('Values inserted successfully!')

# Button to delete a record
if st.button('Delete Record'):
    table_name = st.text_input('Enter table name:')
    condition = st.text_input('Enter condition:')
    if table_name and condition:
        delete_record(table_name, condition)
        st.success('Record deleted successfully!')

# Button to update a record
if st.button('Update Record'):
    table_name = st.text_input('Enter table name:')
    set_clause = st.text_input('Enter set clause:')
    condition = st.text_input('Enter condition:')
    if table_name and set_clause and condition:
        update_record(table_name, set_clause, condition)
        st.success('Record updated successfully!')
