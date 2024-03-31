-- creates the database htbn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY_KEY NOT NULL UNIQUE;
	name VARCHAR(256)
);

