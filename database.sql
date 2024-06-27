CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(25) NOT NULL,
  password VARCHAR(64) NOT NULL 
);

INSERT INTO users (username, password) VALUES ('admin', 'fc07c43afc51cd1c3ba246cb14a5ba919bea4de6308e3f32822a33a0bf3ca864');
INSERT INTO users (username, password) VALUES ('user1', '7c6a180b36896a0a8c02787eeafb0e4c90e678a2eddb5d42464d4eb213d0b515');
INSERT INTO users (username, password) VALUES ('user2', '66a045b4525c02145cb492c06ca0e6c4f8b30a4efad34638ec1d6a62ec6f0bcd');
INSERT INTO users (username, password) VALUES ('user3', 'e47f95e9b362eaca6ef0a1cd3607d43cf96f191f47bcd8cd19f8373e56fdde3e');
INSERT INTO users (username, password) VALUES ('user4', '0d107d09f5bbe40cade3de5c71e9e9b7');
