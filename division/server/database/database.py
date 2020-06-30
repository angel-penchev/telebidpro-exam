import psycopg2


class DivisionDB:
    def __enter__(self):
        self.conn = psycopg2.connect(user="tsb",
                                     password="verysecurenohack",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="division")
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        connection.putconn(self.conn)


def calculate_new_request(A: float, B: float, name: str):
    with DivisionDB() as database:
        database.execute('''
            CREATE TABLE IF NOT EXISTS numbers
            (id SERIAL PRIMARY KEY, A INTEGER, B INTEGER, name VARCHAR);
        ''')

        database.execute('''
            INSERT INTO numbers (A, B, name)
            VALUES (%s, %s, %s)
        ''', (A, B, name))

        database.execute('''
            SELECT id
            FROM numbers
            ORDER BY id DESC
        ''')

        fetched_id = database.fetchone()
        return A/B + fetched_id
