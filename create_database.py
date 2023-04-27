import sqlite3

connection = sqlite3.connect("hotel_bookings.db")

print("Database connected.")

create_table_query = "CREATE TABLE hotel (guest_name TEXT, checkin_date DATE, checkout_date DATE, room_type TEXT)"

connection.execute(create_table_query)

print("Table created successfully")

connection.close()
