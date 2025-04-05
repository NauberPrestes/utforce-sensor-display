from db_connect import cursor, db
from psycopg import sql


def db_write_data(table, column, value):
    cursor.execute(
        "INSERT INTO {tab} ({col}) VALUES ({val})"
        .format(tab=table,
                col=column,
                val=value
                ))

    db.commit()
