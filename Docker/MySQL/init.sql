DROP DATABASE chatapp;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser';


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    email_address varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    phone_number varchar(11) NOT NULL,
    admin boolean NOT NULL
);

CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE children (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name varchar(255) NOT NULL,
    sex varchar(10) NOT NULL,
    allergies boolean NOT NULL,
    class_id INT NOT NULL,
    birthday DATE NOT NULL,
    allergies_PDF varchar(255),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (class_id) REFERENCES classes(id)
);

CREATE TABLE channels (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    update_at DATETIME NOT NULL
);

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id varchar(255) NOT NULL,
    message varchar(255) NOT NULL,
    datetime DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);

CREATE TABLE userchannels (
    id INT NOT NULL PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id varchar(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);

CREATE TABLE allergens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    allergen_items varchar(255) NOT NULL
);

CREATE TABLE childrenallergens (
    id INT PRIMARY KEY,
    children_id INT NOT NULL,
    allergen_id INT NOT NULL,
    FOREIGN KEY (children_id) REFERENCES children(id),
    FOREIGN KEY (allergen_id) REFERENCES allergens(id)
);

CREATE TABLE meals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE mealallergens (
    id INT PRIMARY KEY,
    allergen_id INT NOT NULL,
    meal_id INT NOT NULL,
    FOREIGN KEY (allergen_id) REFERENCES allergens(id),
    FOREIGN KEY (meal_id) REFERENCES meals(id)
);

CREATE TABLE menus (
    id INT PRIMARY KEY,
    date DATE NOT NULL,
    meal_id1 INT NOT NULL,
    meal_id2 INT,
    meal_id3 INT,
    meal_id4 INT,
    FOREIGN KEY (meal_id1) REFERENCES meals(id),
    FOREIGN KEY (meal_id2) REFERENCES meals(id),
    FOREIGN KEY (meal_id3) REFERENCES meals(id),
    FOREIGN KEY (meal_id4) REFERENCES meals(id)
);