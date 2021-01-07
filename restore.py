import os
import sqlite3

os.chdir("data")

db_name = "file__0.localstorage"
db = sqlite3.connect(db_name)
db.execute("DELETE FROM ItemTable;")
db.commit()


files = []  # 所有 .rpgsave 文件
for x in os.listdir("."):
    if x.split(".")[-1] == "rpgsave":
        content = open(x, "rb").read()
        files.append((x.split(".")[0], content.decode("utf-8").encode("utf-16")))

for x in files:
    db.execute("""INSERT INTO ItemTable VALUES (?,?);""", x)
    print(f"{x[0]} restored.")
    db.commit()

db.close()
print("done.")
