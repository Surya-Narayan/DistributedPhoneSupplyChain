# This it the code to create a database in postgreSQL
import psycopg2

# This is my username
MY_USERNAME='postgres'
# This is my personal password
PASSWORD='0000'

# SQL statements to create tables
create_tables_sql = [
    """
    CREATE TABLE Supplier (
        SupplierID SERIAL PRIMARY KEY,
        SupplierName VARCHAR(255),
        ContactInfo TEXT,
        Address TEXT
    )
    """,
    """
    CREATE TABLE Manufacturer (
        ManufacturerID SERIAL PRIMARY KEY,
        ManufacturerName VARCHAR(255),
        Country VARCHAR(255),
        ContactInfo TEXT
    )
    """,
    """
    CREATE TABLE MobilePhone (
        MobilePhoneID SERIAL PRIMARY KEY,
        ManufacturerID INT,
        ModelName VARCHAR(255),
        Price DECIMAL(10, 2),
        ReleaseDate DATE,
        FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID)
    )
    """,
    """
    CREATE TABLE Warehouse (
        WarehouseID SERIAL PRIMARY KEY,
        Location VARCHAR(255),
        Capacity INT
    )
    """,
    """
    CREATE TABLE Inventory (
        InventoryID SERIAL PRIMARY KEY,
        MobilePhoneID INT,
        WarehouseID INT,
        Quantity INT,
        PurchaseDate DATE,
        FOREIGN KEY (MobilePhoneID) REFERENCES MobilePhone(MobilePhoneID),
        FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
    )
    """,
    """
    CREATE TABLE Order (
        OrderID SERIAL PRIMARY KEY,
        CustomerName VARCHAR(255),
        OrderDate DATE,
        DeliveryDate DATE,
        Status VARCHAR(50)
    )
    """,
    """
    CREATE TABLE OrderDetails (
        OrderDetailID SERIAL PRIMARY KEY,
        OrderID INT,
        MobilePhoneID INT,
        Quantity INT,
        Subtotal DECIMAL(10, 2),
        FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
        FOREIGN KEY (MobilePhoneID) REFERENCES MobilePhone(MobilePhoneID)
    )
    """
]

def create_database_tables():
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(database='postgres', user=MY_USERNAME, password=PASSWORD, host='localhost', port='5432')
        cursor = conn.cursor()

        # Create tables
        for create_table_sql in create_tables_sql:
            cursor.execute(create_table_sql)

        # Commit the changes
        conn.commit()
        print("Tables created successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()



if __name__ == "__main__":
    create_database_tables()
