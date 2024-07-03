CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

INSERT INTO users (username) VALUES 
('user1'),
('user2'),
('user3'),
('user4'),
('user5');
