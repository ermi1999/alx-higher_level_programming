-- creates the table unique_id on your MySQL server.
-- the table values contain id INT default 1 UNIQUE and name VARCHAR(256).
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
)
