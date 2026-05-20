import sqlite3


def init_db():

    conn = sqlite3.connect("database/logs.db")

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            module TEXT,

            action TEXT,

            target TEXT,

            result TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()



def add_log(module, action, target, result):

    conn = sqlite3.connect("database/logs.db")

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO logs
        (module, action, target, result)

        VALUES (?, ?, ?, ?)

    """, (module, action, target, result))

    conn.commit()

    conn.close()



def get_logs():

    conn = sqlite3.connect("database/logs.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *
        FROM logs
        ORDER BY id DESC

    """)

    logs = cursor.fetchall()

    conn.close()

    return logs
