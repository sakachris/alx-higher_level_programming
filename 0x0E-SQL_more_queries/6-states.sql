-- creates the database hbtn_0d_usa and the table states
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null

CREATE TABLE IF NOT EXISTS unique_id (
    id AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);
