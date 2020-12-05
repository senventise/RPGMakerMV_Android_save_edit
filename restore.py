#!/data/data/com.termux/files/usr/bin/python
import os
import sqlite3

os.chdir("data")

db_name = "file__0.localstorage"
db = sqlite3.connect(db_name)
db.execute("DELETE FROM ItemTable;")
db.commit()


# 在每个字节后面加上\x00
def wtf(f):
    o = ""
    for x in f:
        o = o + x
        o = o + "\x00"
    return bytes(o, encoding="ASCII")


files = []  # 所有 .rpgsave 文件
for x in os.listdir("."):
    if x.split(".")[-1] == "rpgsave":
        content = open(x, "rb").read()
        files.append((x.split(".")[0], content.decode("utf-8").encode("utf-16").decode("utf-16")))

for x in files:
    db.execute("""INSERT INTO ItemTable VALUES (?,?);""", x)
    db.commit()

db.close()
