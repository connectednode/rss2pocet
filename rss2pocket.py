import feedparser
import sqlite3

con = sqlite3.connect("test.db")

temp = con.execute("SELECT uri, f.id FROM user u LEFT JOIN feed f ON f.owner IS u.id WHERE u.name IS ?", ("cat",)).fetchall()

print(temp)
d = feedparser.parse(temp[0][0])

new_entries = []
for entrie in d.entries:
    new_entries.append((temp[0][1],entrie.link,entrie.id))


con.executemany("INSERT INTO entrie (feed, uri, guid) VALUES (?,?,?)", new_entries)
con.commit()

#for entry in d.entries:
#    print(entry.link)
#    print(entry.id)


