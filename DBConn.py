import psycopg2, os, sys
from psycopg2 import OperationalError, errorcodes, errors
import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='DBConn.log', encoding='utf-8', level=logging.DEBUG)

## this is a class I'm re-using from another project to more easily communicate with the database.
class DBConn:
    database_override=None
    def __init__(self):
        """
        A simple class to interact with Postgres using the psycopg2 driver. Creating an object 
        """
        print('connection opened ...')
        if self.database_override is not None:
            db = self.database_override
        else:
            db = os.getenv('DB_NAME', 'postgres')
        
        self._conn = psycopg2.connect(
            database=db,
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASS', None),
            host=os.getenv('DB_HOST', '127.0.0.1'),
            port=os.getenv('DB_PORT', '5432'),
            )
        self._conn.autocommit = True
        self.cursor = None
    
    @classmethod
    def set_database(cls, database):
        cls.database_override = database
    
    @classmethod
    def get_database(cls):
        return cls.database_override

    def copy_from(self, path, table:str, columns=None, sep=",", *args):
        """
        Copies .csv file at <path> to <table>.
        """
        if self.cursor is None:
            self.get_cursor()

        with open(path, 'r') as file:
            return self.cursor.copy_from(file, table=table, sep=sep, columns=columns, *args)

    def exec(self, sql_statement, *args):
        """
        Executes sql via self.cursor.execute(sql_statement, *args)
        """
        if self.cursor is None:
            self.get_cursor()
        return self.cursor.execute(sql_statement, *args)     
        
    
    def get_cursor(self):
        """
        Returns cursor and creates cursor if none exists.
        """
        if self.cursor is None:     
            self.cursor = self._conn.cursor()
        return self.cursor

    def close(self):
        """
        Destroys self and closes connection
        """
        print('... connection closed.')
        self._conn.close()
        del self
    