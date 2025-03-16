import psycopg2


class PGDatabase:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self._connect()

    def _connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                client_encoding='utf8'
            )
            self.connection.set_client_encoding('UTF8')
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True
            return True
        except Exception:
            return False

    def post(self, query, args=()):
        try:
            self.cursor.execute(query, args)
            return True
        except Exception:
            try:
                self._connect()
                self.cursor.execute(query, args)
                return True
            except Exception:
                return False

    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def __del__(self):
        self.close()