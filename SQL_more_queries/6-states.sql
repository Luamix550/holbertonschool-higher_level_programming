-- creates the database htbn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL;
	name VARCHAR(256)
	PRIMARY KEY (id)
);

