--TABLE
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE user(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    pass TEXT,
    email TEXT
);