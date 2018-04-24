import sqlite3

DB_FILE_NAME = 'database.sqlite3'
DB_SCRIPT_FILE = 'init_database_sqlite3.sql'


def main():
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()

    script = open(DB_SCRIPT_FILE).read()

    print(script)

    cursor.executescript(script)
    connection.commit()
    connection.close()

    print('Done ;_))')


if __name__ == '__main__':
    main()
