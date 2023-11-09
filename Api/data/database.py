import mariadb # CHANGE TO WORK WITH POSTGRESQL
from mariadb import connect # SEE PROPER CONNECTOR FOR POSTGRESQL
from data.db_password import password
from mariadb.connections import Connection


def _get_connection() -> Connection:
    return connect(
        user='root',
        password=f'{password}',
        host='localhost',
        port=3306,
        database='forum'
    )


def read_query(sql: str, sql_params=()):
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)

        return list(cursor)


def insert_query(sql: str, sql_params=()) -> int:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)
        conn.commit()

        return cursor.lastrowid


def update_query(sql: str, sql_params=()) -> bool:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)
        conn.commit()

        return cursor.rowcount
    

def update_queries_transaction(sql_queries: tuple[str], sql_params: tuple[tuple]) -> bool:
    with _get_connection() as conn:
        try:
            cursor = conn.cursor()
            for i in range(len(sql_queries)):
                cursor.execute(sql_queries[i], sql_params[i])

            conn.commit()
            return True
        except mariadb.Error as error:
            print(f"Database update failed: {error}")
            conn.rollback()
            return False
