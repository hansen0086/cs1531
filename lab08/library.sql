PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE BOOK
(ID INT PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
AUTHOR TEXT NOT NULL,
YEAR TEXT,
GENRE TEXT);
INSERT INTO "BOOK" VALUES(1,'Agile Design Principles','Martin','1996','Engineering Textbook');
INSERT INTO "BOOK" VALUES(2,'The Lord of the Rings','Tolkien','1954','Fantasy');
INSERT INTO "BOOK" VALUES(3,'Pride and Prejudice','Jane','1813','Romance');
INSERT INTO "BOOK" VALUES(4,'The Great Gatsby','Scott','2004','Literary Fiction');
INSERT INTO "BOOK" VALUES(5,'Introduction to Cooking','Tom','2016','Cook Book');
INSERT INTO "BOOK" VALUES(6,'SOLID in OO','Martin','2004','Design Guidebook');
COMMIT;
