import sqlite3

# CLI directly: sqlite3 bot/database/mirror-bot.db
DB_PATH = "bot/database/mirror-bot.db"

# function from the sqlite3 module to create a new SQLite database
def get_connection():
    try:
        connection = sqlite3.connect(DB_PATH)
        print("Connection is good")
        return connection
    except sqlite3.Error as error:
        print("Failed to connect with sqlite3 database", error)

# creating first basic table
def init_db():
    with get_connection() as connection:
        connection.execute("""
                           CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           user_id INTEGER NOT NULL,
                           username TEXT,
                           joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                           )
                          """)
        
if __name__ == "__main__":
    init_db()
    print("Database created")