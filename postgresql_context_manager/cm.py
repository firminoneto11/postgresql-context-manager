import psycopg2


class OpenPostgre:

    def __init__(self, dbname, user, password, host):
        # Data to access the database
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

        # Making a connection
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )

        # Creating the cursor
        self.cursor = self.connection.cursor()

    def __enter__(self):
        # Returning the cursor to the context manager
        return self.cursor

    def __iter__(self):
        for item in self.cursor:
            yield item

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closing the cursor
        self.cursor.close()
        if isinstance(exc_val, Exception):
            # Rollback if any errors occur
            self.connection.rollback()
        else:
            # Committing the changes if doesn't occur any errors
            self.connection.commit()
        # Closing the connection
        self.connection.close()
