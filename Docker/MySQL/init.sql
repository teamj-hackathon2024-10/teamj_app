DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';


CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_name varchar(255) NOT NULL,
    mail_adress varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    phon_number varchar(11) NOT NULL,
    admin boolean NOT NULL,
);


CREATE TABLE Children (
    children_id INT PRIMARY KEY,
    user_id vachar(100) NOT NULL,
    children_name varchar(255) NOT NULL,
    sex varchar(10) NOT NULL,
    allergies boolean NOT NULL,
    class_id varchar(255) NOT NULL,
    birthday date NOT NULL,
);

CREATE TABLE Channels (
    channel_id serial PRIMARY KEY,
    channel_name vachar(255) NOT NULL,
    children_id INT NOT NULL,
    user_id INT NOT NULL,
);

CREATE TABLE Messages (
    message_id serial PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    message varchar(255) NOT NULL,
    datetime DATETIME NOT NULL,
);

CREATE TABLE classes (
    class_id serial PRIMARY KEY,
    class_name varchar(255) NOT NULL,
);
