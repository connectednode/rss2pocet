import Parser from 'rss-parser';
import { Database } from 'sqlite3';


(async () => {
  const parser = new Parser();
  const feed = await parser.parseURL("https://blog.ironsm4sh.nl/feed.xml");
  console.log(feed.title);

  feed.items.forEach(item => {
    console.log(item) 
  });
})();
const db = new Database(':memory:');

db.serialize(() => {
    db.run("CREATE TABLE lorem (info TEXT)");

    const stmt = db.prepare("INSERT INTO lorem VALUES (?)");
    for (let i = 0; i < 10; i++) {
        stmt.run("Ipsum " + i);
    }
    stmt.finalize();

    db.each("SELECT rowid AS id, info FROM lorem", (_, row: any) => {
        console.log(row.id + ": " + row.info);
    });
});

db.close();


