import psycopg2

connection = psycopg2.connect(user="fadzlkknyafmvn",
                              password="034fac3d7851c96bdaecbf721be3565ec9fcdc77f7e09a9ae6889e85c3c38546",
                              host="ec2-54-217-213-79.eu-west-1.compute.amazonaws.com",
                              port="5432",
                              database="dae21bhcp9fiao")


class DivisionDB:
    def __enter__(self):
        self.conn = connection
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        return self.conn.commit()


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
        return A/B, fetched_id[0]
