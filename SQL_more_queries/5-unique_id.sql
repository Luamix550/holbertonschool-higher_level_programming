-- creates the table unique_id 
CREATE TABLE IF NOT EXISTS unique_id (
	id int DEFAULT '1',
	name varchar(256)
	UNIQUE (id)
);

