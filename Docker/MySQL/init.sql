DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';


CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_name varchar(255) NOT NULL,
    email_adress varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    phone_number varchar(11) NOT NULL,
    admin boolean NOT NULL,
);


CREATE TABLE Children (
    children_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    children_name varchar(255) NOT NULL,
    sex varchar(10) NOT NULL,
    allergies boolean NOT NULL,
    class_id varchar(255) NOT NULL,
    birthday DATE NOT NULL,
    allergies PDF varchar(255),
);

CREATE TABLE Channels (
    channel_id vachar(255) PRIMARY KEY,
    channel_name vachar(255) NOT NULL,
    update_at DATETIME NOT NULL,
);

CREATE TABLE Messages (
    message_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id varchar(255) NOT NULL,
    message varchar(255) NOT NULL,
    datetime DATETIME NOT NULL,
);

CREATE TABLE Classes (
    class_id INT PRIMARY KEY,
    class_name varchar(255) NOT NULL,
);

CREATE TABLE UserChannels (
    user_id INT PRIMARY KEY,
    channel_id varchar(255) NOT NULL,
);

CREATE TABLE ChildrenAllergens (
    childrenallergens_id INT PRIMARY KEY,
    children_id INT NOT NULL,
    allergen_id INT NOT NULL,
);

CREATE TABLE Allergens (
    allergen_id INT PRIMARY KEY,
    allergen_items varchar(255) NOT NULL,
);

CREATE TABLE MealAllergens (
    mealallergens_id INT PRIMARY KEY,
    allergen_id INT NOT NULL,
    meal_id INT NOT NULL,
);

CREATE TABLE Meals (
    meal_id INT PRIMARY KEY,
    meal_name varchar(255) NOT NULL,
);

CREATE TABLE Menus (
    menu_id INT PRIMARY KEY,
    date DATE NOT NULL,
    meal_id1 INT NOT NULL,
    meal_id2 INT,
    meal_id3 INT,
    meal_id4 INT,
);