from postgres_cm import OpenPostgres


login_data = {
    'host': "Your host",
    'dbname': "Your database name",
    'user': "Your username",
    'password': "Your password"
}

with OpenPostgres(**login_data) as cursor:
    cursor.execute("Your SQL query here | Select, Insert, Update, Delete")
    for row in cursor:
        print(row)  # Printing each line from a query
