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
    admin boolean NOT NULL DEFAULT FALSE

);
INSERT INTO users (id, name, email_address, password, phone_number, admin) VALUES (1, '高倉 文太','futaba@futaba.com', 'a06a2b6f3b1a099522c2a9a2578a4337cffae2ea874838407ebf22d1028df841', '0799647061', 1);
INSERT INTO users (id, name, email_address, password, phone_number, admin) VALUES (2, '野原 みさえ','misae@kureyonn.com','e19f7ef7976fb75fe5d83b374f3f3696073f69236370778c177a684b226e5588', '0799222222', 0);



CREATE TABLE children (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name varchar(255) NOT NULL,
    sex varchar(10) NOT NULL,
    allergies boolean NOT NULL,
    birthday DATE NOT NULL,
    allergies_PDF varchar(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO children (id, user_id, name, sex, allergies, birthday) VALUES (1,2, '野原 しんのすけ',0, 1, '2022-05-05');


CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL
);
INSERT INTO classes (id, name) VALUES (1, 'ひまわり');


CREATE TABLE channels (
    id VARCHAR(255) PRIMARY KEY,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    update_at DATETIME NOT NULL,
    is_open boolean DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO channels (id, name, update_at, is_open) VALUES("9ED83D6C-8522-4869-BF13-ACD481FC9F0B", "お知らせチャンネル", '2020-01-01 10:10:10-08:00', 1);


CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    channel_id varchar(255) NOT NULL,
    message varchar(255) NOT NULL,
    datetime DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (channel_id) REFERENCES channels(id)
);
INSERT INTO messages (id, user_id, channel_id, message, datetime) VALUES(1, 1, "9ED83D6C-8522-4869-BF13-ACD481FC9F0B", 'お知らせテストですよ。', '2020-01-01 10:10:10-10:00');
INSERT INTO messages (id, user_id, channel_id, message, datetime) VALUES(2, 1, '9ED83D6C-8522-4869-BF13-ACD481FC9F0B', '園長の文太です。よろしくお願いします。', '2020-01-01 12:10:10-10:00');

CREATE TABLE allergens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    allergen_items varchar(255) NOT NULL
);
INSERT INTO allergens (allergen_items) VALUES ('えび');
INSERT INTO allergens (allergen_items) VALUES ('かに');
INSERT INTO allergens (allergen_items) VALUES ('くるみ');
INSERT INTO allergens (allergen_items) VALUES ('小麦');
INSERT INTO allergens (allergen_items) VALUES ('そば');
INSERT INTO allergens (allergen_items) VALUES ('卵');
INSERT INTO allergens (allergen_items) VALUES ('乳');
INSERT INTO allergens (allergen_items) VALUES ('落花生（ピーナッツ）');
INSERT INTO allergens (allergen_items) VALUES ('アーモンド');
INSERT INTO allergens (allergen_items) VALUES ('あわび');
INSERT INTO allergens (allergen_items) VALUES ('いか');
INSERT INTO allergens (allergen_items) VALUES ('いくら');
INSERT INTO allergens (allergen_items) VALUES ('オレンジ');
INSERT INTO allergens (allergen_items) VALUES ('カシューナッツ');
INSERT INTO allergens (allergen_items) VALUES ('キウイフルーツ');
INSERT INTO allergens (allergen_items) VALUES ('牛肉');
INSERT INTO allergens (allergen_items) VALUES ('ごま');
INSERT INTO allergens (allergen_items) VALUES ('さけ');
INSERT INTO allergens (allergen_items) VALUES ('さば');
INSERT INTO allergens (allergen_items) VALUES ('大豆');
INSERT INTO allergens (allergen_items) VALUES ('鶏肉');
INSERT INTO allergens (allergen_items) VALUES ('バナナ');
INSERT INTO allergens (allergen_items) VALUES ('豚肉');
INSERT INTO allergens (allergen_items) VALUES ('マカダミアナッツ');
INSERT INTO allergens (allergen_items) VALUES ('もも');
INSERT INTO allergens (allergen_items) VALUES ('やまいも');
INSERT INTO allergens (allergen_items) VALUES ('りんご');
INSERT INTO allergens (allergen_items) VALUES ('ゼラチン');



CREATE TABLE childrenallergens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    children_id INT NOT NULL,
    allergen_id INT NOT NULL,
    FOREIGN KEY (children_id) REFERENCES children(id),
    FOREIGN KEY (allergen_id) REFERENCES allergens(id)
);
INSERT INTO childrenallergens (id, children_id, allergen_id) VALUES (1, 1, 6);


CREATE TABLE meals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL
);
INSERT INTO meals (name) VALUES ('ご飯');
INSERT INTO meals (name) VALUES ('ハンバーグ');
INSERT INTO meals (name) VALUES ('ポテトサラダ');
INSERT INTO meals (name) VALUES ('コーンスープ');
INSERT INTO meals (name) VALUES ('白身魚のゆかり揚げ');
INSERT INTO meals (name) VALUES ('ほうれん草の磯和え');
INSERT INTO meals (name) VALUES ('豚汁');
INSERT INTO meals (name) VALUES ('ロールパン');
INSERT INTO meals (name) VALUES ('トマトグラタン');
INSERT INTO meals (name) VALUES ('コールスローサラダ');
INSERT INTO meals (name) VALUES ('きのことベーコンのスープ');
INSERT INTO meals (name) VALUES ('酢豚');
INSERT INTO meals (name) VALUES ('春雨サラダ');
INSERT INTO meals (name) VALUES ('青梗菜の中華スープ');
INSERT INTO meals (name) VALUES ('ビーフカレーライス');
INSERT INTO meals (name) VALUES ('ミモザサラダ');
INSERT INTO meals (name) VALUES ('鮭のゴマ味噌焼き');
INSERT INTO meals (name) VALUES ('きんぴらごぼう');
INSERT INTO meals (name) VALUES ('麩のすまし汁');
INSERT INTO meals (name) VALUES ('チキンカツ');
INSERT INTO meals (name) VALUES ('きゅうりとかにかまの酢の物');
INSERT INTO meals (name) VALUES ('豆腐の味噌汁');
INSERT INTO meals (name) VALUES ('八宝菜');
INSERT INTO meals (name) VALUES ('春雨スープ');
INSERT INTO meals (name) VALUES ('鯖の塩焼き');
INSERT INTO meals (name) VALUES ('切干大根の煮物');
INSERT INTO meals (name) VALUES ('なめこ味噌汁');
INSERT INTO meals (name) VALUES ('麻婆豆腐');
INSERT INTO meals (name) VALUES ('ブロッコリーのじゃこナムル');
INSERT INTO meals (name) VALUES ('中華スープ');
INSERT INTO meals (name) VALUES ('オムライス');
INSERT INTO meals (name) VALUES ('ポトフ');
INSERT INTO meals (name) VALUES ('ミートスパゲティー');
INSERT INTO meals (name) VALUES ('キャベツとちくわの和え物');
INSERT INTO meals (name) VALUES ('りんご');


CREATE TABLE mealallergens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    allergen_id INT NOT NULL,
    meal_id INT NOT NULL,
    FOREIGN KEY (allergen_id) REFERENCES allergens(id),
    FOREIGN KEY (meal_id) REFERENCES meals(id)
);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (4, 2);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (6, 2);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (7, 2);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (16, 2);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (6, 3);
INSERT INTO mealallergens (allergen_id, meal_id) VALUES (7, 4);


CREATE TABLE menus (
    id INT AUTO_INCREMENT PRIMARY KEY,
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
INSERT INTO menus (date, meal_id1, meal_id2, meal_id3, meal_id4) VALUES('2024-11-18', 1, 2, 3, 4);




