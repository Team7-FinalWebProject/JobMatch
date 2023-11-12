from os import getcwd, environ, path
from time import sleep
import psycopg2
from data.db_password import password
from db_data import config
from subprocess import PIPE, run

_USER, _DBNAME, _SCHEMA = config._USER, config._DBNAME, config._SCHEMA
_BIN_PATH, _PSQL, _PG_DUMP = config._BIN_PATH, config._PSQL, config._PG_DUMP
_REL_IMPORT_DUMP_PATH, _REL_EXPORT_DUMP_PATH = config._REL_IMPORT_DUMP_PATH, config._REL_EXPORT_DUMP_PATH

current_directory = getcwd()


def _get_connection():
    return psycopg2.connect(
        host='localhost',
        user=_USER,
        dbname=_DBNAME,
        # Schemas
        options=f'-c search_path={_SCHEMA}',
        password=password,
        port=5432
    )


def delete_db():
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"DROP SCHEMA IF EXISTS {_SCHEMA} CASCADE")
        conn.commit()
        cursor.close()
    print('DB dropped successfully if exists')
    return


def mysql_io(io, binary, dump):
    environ['PGPASSWORD'] = password
    if io == 'import':
        process = run(args=[binary, f'--username={_USER}', f'--dbname={_DBNAME}', f'--file={current_directory + dump}'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print('DB imported successfully' if not process.stderr or not process.stderr.strip(
        ) else process.stderr)
    elif io == 'dump':
        process = run(args=[binary, f'--username={_USER}', f'--dbname={_DBNAME}', f'--schema={_SCHEMA}'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if process.stderr and process.stderr.strip():
            print(f"Error: {process.stderr}")
        else:
            with open(current_directory + dump, "w") as dump_file:
                dump_file.write(process.stdout)
            print(f'DB dumped (check file {current_directory + dump})')
    return


def get_bkp_dump_extension(extensions):
    # Choses .bkp file to use. Choses non-existing or oldest files to delay overwriting the newest file.
    for extension in extensions:
        if not path.isfile(current_directory + _REL_EXPORT_DUMP_PATH + extension):
            return extension
    return_extension, modify_time = None, None
    for extension in extensions:
        new_time = path.getmtime(
            current_directory + _REL_EXPORT_DUMP_PATH + extension)
        if not modify_time or new_time < modify_time:
            modify_time = new_time
            return_extension = extension
    return return_extension


def make_copy():
    bkp_extension = get_bkp_dump_extension([".1.bkp", ".2.bkp", ".3.bkp"])
    mysql_io('dump', _BIN_PATH + _PG_DUMP,
             _REL_EXPORT_DUMP_PATH + bkp_extension)


def main(silent_export=False, silent_import=False):
    def dump():
        mysql_io('dump', _BIN_PATH + _PG_DUMP, _REL_EXPORT_DUMP_PATH)

    def drop():
        make_copy()
        sleep(2)
        try:
            delete_db()
        except:
            print(f'DB schema {_SCHEMA} does not exist or other error, skipping drop')

    def imp(copy=True):
        if copy:
            make_copy()
            sleep(2)
        mysql_io('import', _BIN_PATH + _PSQL, _REL_IMPORT_DUMP_PATH)

    def user_query(question):
        answer = None
        while not answer or answer.upper() not in ['Y', 'N']:
            answer = input(question)
        return answer.upper()
    if silent_import and not silent_export:
        drop()
        imp(copy=False)
    elif silent_export and not silent_import:
        dump()
    else:
        copy = True
        if user_query(f'Would you like to export the {_SCHEMA} schema (Y/N)?') == 'Y':
            dump()
        if user_query(f'Would you like to drop and import the {_SCHEMA} schema (Y/N)?') == 'Y':
            drop()
            imp(copy=False)
        if user_query(f'Would you like additional commands (Y/N)?') == 'Y':
            if user_query(f'Would you like to drop the {_SCHEMA} schema (Y/N)?') == 'Y':
                drop()
                copy = False
            if user_query(f'Would you like to import the {_SCHEMA} schema (Y/N)?') == 'Y':
                imp(copy=copy)
