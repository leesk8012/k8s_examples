CREATE DATABASE db1;
use db1;

CREATE TABLE contacts(
id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL, address VARCHAR(40) NOT NULL, PRIMARY KEY(id)
);

CREATE USER 'user1'@'%' IDENTIFIED BY 'pass1';
GRANT ALL ON db1.* TO 'user1'@'%';
FLUSH PRIVILEGES;
INSERT INTO contacts (name,address) VALUES('Lee', 'Incheon');
INSERT INTO contacts (name,address) VALUES('Kim', 'Seoul');
