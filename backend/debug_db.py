import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST', '127.0.0.1')
port = int(os.getenv('DB_PORT', 3306))
dbname = os.getenv('DB_NAME', 'homely')

candidates = [
    ('root', os.getenv('DB_PASSWORD', '')),
    ('root', ''),
    ('root', 'root'),
    ('root', 'password'),
    ('root', 'admin'),
]

print(f"Testing connection to {host}:{port} for DB '{dbname}'")

success = False
for user, password in candidates:
    print(f"Testing user='{user}' password='{password}' ... ", end='')
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=dbname,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("SUCCESS!")
        print(f"Working credentials found: USER={user}, PASSWORD={password}")
        success = True
        connection.close()
        break
    except pymysql.err.OperationalError as e:
        print(f"FAILED: {e}")
    except pymysql.err.InternalError as e:
         # Unknown database 'homely'
        if e.args[0] == 1049:
             print(f"FAILED (Database '{dbname}' does not exist, but auth worked): {e}")
             # valid auth, just need to create DB
             print(f"Working credentials found for Server: USER={user}, PASSWORD={password}")
             success = True
             break
        else:
             print(f"FAILED: {e}")

if not success:
    print("All common credentials failed.")
