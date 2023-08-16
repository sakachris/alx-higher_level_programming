-- creates the table id_not_null on your MySQL server.
-- force_name description:
-- id INT default 1
-- name VARCHAR(256) can’t be null

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
