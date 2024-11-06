DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';


CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid VARCHAR(255),
    name VARCHAR(255) UNIQUE NOT NULL,
    abstract VARCHAR(255),
    FOREIGN KEY (uid) REFERENCES users(uid)
);
