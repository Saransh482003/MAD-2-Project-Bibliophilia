import sqlite3

# Path to your SQLite database
db_path = './instance/library.sqlite3'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Create a cursor object
cursor = conn.cursor()

# Execute the VACUUM command
cursor.execute('VACUUM')

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Database vacuumed successfully.")
