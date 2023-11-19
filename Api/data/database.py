import psycopg2 
from data.db_password import password


def _get_connection():
    return psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        dbname = 'postgres',
        options='-c search_path=jobmatch',
        password = password,
        port = 5432
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
        # last_row_id = cursor.fetchone()
        # return last_row_id[0] if last_row_id else None
        last_row_id = cursor.lastrowid
        return last_row_id


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
        except psycopg2.Error as error:
            print(f"Database update failed: {error}")
            conn.rollback()
            return False


def insert_queries_trasnaction(sql_queries: tuple[str], sql_params: tuple[tuple]) -> int:
    with _get_connection() as conn:
        try:
            cursor = conn.cursor()
            for i in range(len(sql_queries)):
                cursor.execute(sql_queries[i], sql_params[i])

            conn.commit()
            last_row_id = cursor.fetchone()
            return last_row_id[0] if last_row_id else None
        except psycopg2.Error as error:
            print(f"Database update failed: {error}")
            conn.rollback()
            return False
        
#TODO check for implementations
def multi_read_query_trasnaction(sql_queries: tuple[str], sql_params: tuple[tuple]) -> list:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany(sql_queries, sql_params)
        
        return list(cursor)