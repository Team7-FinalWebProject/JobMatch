##pg_dumb binary has to be used for dumping the db unless we use the C API libq
##It would take a long project to reimplement the functionality of pg_dump otherwise
##As such to use export (dump) feature a postgre client (or otherwise obtaining pg_dump) is currently required
##Everything else should be possible to migrate to psycopg2 although the binaries offer some advantages
##createdb and dropdb are implemented with psycopg2 to make it easier for tests to runs

from os import getcwd, environ, path, getenv
from time import sleep
import psycopg2
# from data.db_password import password
from db_data import config
from subprocess import PIPE, run
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql

_USER, _DBNAME, _SCHEMA = config._USER, config._DBNAME, config._SCHEMA
_BIN_PATH = config._BIN_PATH
_REL_IMPORT_DUMP_PATH, _REL_EXPORT_DUMP_PATH = config._REL_IMPORT_DUMP_PATH, config._REL_EXPORT_DUMP_PATH
_REMOTE_HOST =  config._REMOTE_HOST

_PSQL, _PG_DUMP = r'\psql.exe', r'\pg_dump.exe'
# _CREATEDB, _DROPDB = r'\createdb.exe', r'\dropdb.exe'

current_directory = getcwd()

def test_db_get_connection(remote=False):
    return psycopg2.connect(
        host = _REMOTE_HOST if remote else "localhost",
        user = 'postgres',
        dbname = 'postgres',
        options='-c search_path=test_schema',
        password = getenv('jobgrepass') if remote else getenv("password"),
        port = 5432,
    )

def dropdb(remote=False):
    #Since 2.9 with conn starts a transaction https://stackoverflow.com/questions/77160257/postgresql-create-database-cannot-run-inside-a-transaction-block
    try:
        conn = test_db_get_connection(remote=remote)
        conn.autocommit = True
        with conn.cursor() as cur:
            result = cur.execute("DROP DATABASE test_db WITH (FORCE)")
    finally:
        conn.close()
    return list(result) if result else None

def createdb(remote=False):
    #Since 2.9 with conn starts a transaction https://stackoverflow.com/questions/77160257/postgresql-create-database-cannot-run-inside-a-transaction-block
    try:
        conn = test_db_get_connection(remote=remote)
        conn.autocommit = True
        with conn.cursor() as cur:
            result = cur.execute("CREATE DATABASE test_db;")
    finally:
        conn.close()
    return list(result) if result else None
    
def get_bkp_dump_extension_helper(extensions):
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

##Core functionality:
def cmd_interface(action, remote=False, skipcopy=False, dump=None):

    success,fail = lambda proc:None,lambda proc:None
    dbname = _DBNAME

    def dump_success(process):
        try:
            with open(current_directory + dump, "w") as dump_file:
                dump_file.write(process.stdout)
            print(f'DB dumped to extra file (check file {current_directory + dump})')
        except(Exception) as e:
            print(e)
      
    match action:
        case 'import':
            if not skipcopy:
                cmd_interface('make_copy', remote=remote)
                sleep(2)
            binary, dump = (_BIN_PATH + _PSQL), _REL_IMPORT_DUMP_PATH
            success = lambda process:print('DB imported successfully')
            fail = lambda process:print(f'Impored failed error:{process.stderr}')
        case 'dump':
            binary, dump = (_BIN_PATH + _PG_DUMP), _REL_EXPORT_DUMP_PATH
            success = lambda process:dump_success(process)
            fail = lambda process:print(f"Error: {process.stderr}") 
        case 'drop':
            cmd_interface('make_copy', remote=remote)
            sleep(2)
            binary, dump = (_BIN_PATH + _PSQL), _REL_EXPORT_DUMP_PATH
            success = lambda process:print('DB dropped successfully if exists')
            fail = lambda process:print(f'DB schema {_SCHEMA} does not exist or error:{process.stderr}, skipping drop')
        case 'dropdb':
            # binary, dump, dbname = (_BIN_PATH + _DROPDB), None, 'test_db'
            success = lambda process:print(f"DB: {dbname} dropped successfully in remote:{remote}")
            fail = lambda process:print(f"Error: {process.stderr}") 
            return dropdb(remote=remote)
        case 'createdb':
            # binary, dump, dbname = (_BIN_PATH + _CREATEDB), None, 'test_db'
            success = lambda process:print(f"DB: {dbname} created successfully in remote:{remote}")
            fail = lambda process:print(f"Error: {process.stderr}") 
            return createdb(remote=remote)
        case 'drop_and_imp':
            cmd_interface('drop', remote=remote)
            return cmd_interface('import', remote=remote,skipcopy=True)
        case 'make_copy':
            extensions = [".1.bkp", ".2.bkp", ".3.bkp"] if not remote else [".remote.1.bkp", ".remote.2.bkp", ".remote.3.bkp"]
            bkp_extension = get_bkp_dump_extension_helper(extensions)
            binary, dump, action = (_BIN_PATH + _PG_DUMP),(_REL_EXPORT_DUMP_PATH + bkp_extension),'dump'
            success = lambda process:dump_success(process)
            fail = lambda process:print(f"Error, extra copy not created: {process.stderr}") 
        case _:
            return

    ###Second match kept for easier to reading of args
    # (also logic is windy due to different exes having different synthax)
    args=[
    binary,
    f'--username={_USER}']
    if action not in ['createdb','dropdb']:
        args.append(f'--dbname={dbname}')
    if remote:
        args.append(f'--host={_REMOTE_HOST}')
    match action:
        case 'import':
            args.append(f'--file={current_directory + dump}')
        case 'dump':
            args.append(f'--schema={_SCHEMA}')
        case 'drop':
            args.append(f'-c')
            args.append(f'DROP SCHEMA IF EXISTS {_SCHEMA} CASCADE')
        case 'createdb':
            args.append(dbname)
        case 'dropdb':
            args.append(f'-f')
            args.append(dbname)

    # print(args)
    environ['PGPASSWORD'] = getenv('jobgrepass') if remote else getenv('password')
    process = run(args=args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)

    err = process.stderr
    if not err or not process.stderr.strip() or process.stderr.strip().startswith("NOTICE"):
        success(process)
    else:
        fail(process)

##User interface:
def main(silent_action=None, silent_remote=False, silent_test_sql=False):
    if silent_test_sql:
        global _REL_IMPORT_DUMP_PATH
        global _DBNAME
        global _SCHEMA
        _REL_IMPORT_DUMP_PATH = r'\db_data\db_test.sql'
        _DBNAME = 'test_db'
        _SCHEMA = 'test_schema'

    def user_query(question, action, remote=False):
        answer = None
        while not answer or answer.upper() not in ['Y', 'N']:
            answer = input(question)
        if answer.upper() == 'Y':
            if action == 'nest':
                return True
            return cmd_interface(action=action, remote=remote)
        return False
    
    if silent_action:
        cmd_interface(silent_action, remote=silent_remote)
    else:
        user_query(f'Would you like to export the local {_SCHEMA} schema (Y/N)?', action='dump')
        user_query(f'Would you like to drop and import the local {_SCHEMA} schema (Y/N)?', action='drop_and_imp')
        if user_query(f'Would you like remote commands (Y/N)?', action='nest'):
            user_query(f'Would you like to export the remote {_SCHEMA} schema (Y/N)?', action='dump', remote=True)
            user_query(f'Would you like to drop and import the remote {_SCHEMA} schema (Y/N)?', action='drop_and_imp', remote=True)
        if user_query(f'Would you like additional commands (Y/N)?', action='nest'):
            user_query(f'Would you like to create a local test_db database (Y/N)?', action='createdb')
            user_query(f'Would you like to drop the local test_db database (Y/N)?', action='dropdb')
            user_query(f'Would you like to drop the local {_SCHEMA} schema (Y/N)?', action='drop')
            user_query(f'Would you like to import the local {_SCHEMA} schema (Y/N)?', action='import')
            user_query(f'Would you like to drop the remote {_SCHEMA} schema (Y/N)?', action='drop', remote=True)
            user_query(f'Would you like to import the remote {_SCHEMA} schema (Y/N)?', action='import', remote=True)
