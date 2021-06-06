from postgresql_context_manager.cm import OpenPostgre

# Data to access the database
with open('.\\access_data.txt', mode='r') as file:
    line = file.readline()
    access_data = {
        'dbname': None,
        'user': None,
        'password': None,
        'host': None
    }
    line = line.split(',')
    counter = 0
    for key in access_data.keys():
        access_data[key] = line[counter]
        counter += 1

# Testing
with OpenPostgre(**access_data) as cursor:
    # SQL Query
    query = """
    select * from empresas;
    """
    # Executing the query
    cursor.execute(query)
    # Fetching the data
    queried_data = cursor.fetchall()
    # Printing the data
    for row in queried_data:
        print(row)
