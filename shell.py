import sqlite3

def run_sql_shell(db_name="test.db"):
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    print(f"Connected to database: {db_name}")
    print("Type your SQL commands below. Type 'exit' to quit.\n")

    while True:
        try:
            # Take input from user
            command = input("sqlite> ").strip()
            
            # Exit condition
            if command.lower() in ["exit", "quit"]:
                print("Closing connection. Goodbye!")
                break
            
            # Skip empty input
            if not command:
                continue

            # Execute SQL command
            cursor.execute(command)

            # If it's a SELECT, fetch results
            if command.lower().startswith("select"):
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                # Commit changes for INSERT/UPDATE/DELETE
                conn.commit()
                print("Query executed successfully.")

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # Close connection
    conn.close()

if __name__ == "__main__":
    run_sql_shell("test.db")
