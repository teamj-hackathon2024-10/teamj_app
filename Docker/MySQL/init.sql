DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';


CREATE TABLE Users (
    id INT PRIMARY KEY,
    name varchar(255) NOT NULL,
    mail_address varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    phon_number varchar(11) NOT NULL,
    admin boolean NOT NULL,
);

CREATE TABLE Children (
    id INT PRIMARY KEY,
    user_id vachar(100) NOT NULL,
    name varchar(255) NOT NULL,
    sex varchar(10) NOT NULL,
    allergies boolean NOT NULL,
    class_id varchar(255) NOT NULL,
    birthday date NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(uid)
    FOREIGN KEY (cid) REFERENCES users(cid)
);


CREATE TABLE Messages (
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    message varchar(255) NOT NULL,
    datetime DATETIME NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(uid)
    FOREIGN KEY (chid) REFERENCES users(chid)
);

CREATE TABLE classes (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL,

);

CREATE TABLE channels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid VARCHAR(255),
    name VARCHAR(255) UNIQUE NOT NULL,
    abstract VARCHAR(255),
    FOREIGN KEY (uid) REFERENCES users(uid)
);
