#!/data/data/com.termux/files/usr/bin/python
import sqlite3
import os
import sys

db_path = sys.argv[1]
if not os.path.isfile(db_path):
    print("No such file.")
    sys.exit(0)

os.system("mkdir ./data/ && rm ./data/*") # 用于存储数据
os.system(f"cp {db_path} ./data/")
os.chdir("data")

db = sqlite3.connect(db_path)
_keys = db.execute(f"SELECT key FROM ItemTable;").fetchall()
keys = []
for x in _keys:
    keys.append(x[0])

print("Exporting .rpgsave files.")
for x in keys:
    value = db.execute(f"SELECT value FROM ItemTable WHERE key IS \"{x}\";").fetchone()[0]
    value = str(value).replace("\'","").replace("\\","").replace("x00","")[1:] # 写得比较丑，但是能用
    if type(value) is str:
        with open(f"{x}.rpgsave","w+") as f:
            f.write(value)
    elif type(value) is bytes:
        with open(f"{x}.rpgsave","wb+") as f:
            f.write((value))

db.close()
