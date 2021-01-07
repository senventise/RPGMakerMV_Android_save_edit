import os
import shutil
import sqlite3
import sys

if not len(sys.argv) > 1:
    print("Invalid Argument.")
    sys.exit(0)

db_path = sys.argv[1]
if not os.path.isfile(db_path):
    print("No such file.")
    sys.exit(0)

try:
    os.mkdir("data/")
except FileExistsError:
    shutil.rmtree("data/")
    os.mkdir("data/")
shutil.copy(db_path, "data/")
os.chdir("data")

db = sqlite3.connect(db_path)
_keys = db.execute(f"SELECT key FROM ItemTable;").fetchall()
keys = []
for x in _keys:
    keys.append(x[0])

print("Exporting .rpgsave files.")
for x in keys:
    value = db.execute(f"SELECT value FROM ItemTable WHERE key IS \"{x}\";").fetchone()[0]
    value = value.decode("utf-16")
    with open(f"{x}.rpgsave", "w+") as f:
        f.write(value)
    print(f"{x}.rpgsave exported.")

db.close()
