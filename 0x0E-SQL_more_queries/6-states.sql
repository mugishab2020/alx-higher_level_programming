-- Creating DB if nkt exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- using the hbtn_0d_usa DB
USE hbtn_0d_usa;
-- Creating the table in Db
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id))
