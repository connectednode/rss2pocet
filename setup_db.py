import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("PRAGMA journal_mode=WAL;")

cur.execute("""CREATE TABLE "user" (
	"id"    INTEGER NOT NULL UNIQUE,
    "name"  TEXT,
    "token" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE "feed" (
	"id"    INTEGER NOT NULL UNIQUE,
    "uri"   TEXT NOT NULL,
    "name"  TEXT,
    "owner" INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY (owner) REFERENCES user(id)
);""")
cur.execute("""CREATE TABLE "entrie" (
	"id"    INTEGER NOT NULL UNIQUE,
    "feed"  INTEGER,
    "uri"	TEXT NOT NULL,
    "guid"  TEXT
	PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY (feed) REFERENCES feed(id)
);""")
