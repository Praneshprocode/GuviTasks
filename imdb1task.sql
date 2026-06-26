CREATE DATABASE IMDB;
USE IMDB;

CREATE TABLE Movie (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    release_year YEAR
);

CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    media_type VARCHAR(20),
    media_file VARCHAR(355),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50)
);

CREATE TABLE Movie_Genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating INT,
    review_text VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(100)
);

CREATE TABLE Skill (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(50)
);

CREATE TABLE Artist_Skill (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skill(skill_id)
);

CREATE TABLE Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50)
);

CREATE TABLE Movie_Artist_Role (
    movie_id INT,
    artist_id INT,
    role_id INT,
    PRIMARY KEY (movie_id, artist_id, role_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (role_id) REFERENCES Role(role_id)
);

INSERT INTO Movie (title, release_year)
VALUES
('Inception', 2010),
('Interstellar', 2014),
('The Dark Knight', 2008),
('Avatar', 2009),
('Titanic', 1997),
('Avengers: Endgame', 2019);

INSERT INTO Media (movie_id, media_type, media_file)
VALUES
(1, 'Image', 'inception.jpg'),
(1, 'Video', 'inception.mp4'),
(2, 'Image', 'interstellar.jpg'),
(3, 'Image', 'dark_knight.jpg'),
(3, 'Video', 'dark_knight.mp4'),
(4, 'Image', 'avatar.jpg'),
(5, 'Image', 'titanic.jpg'),
(6, 'Video', 'endgame.mp4');

INSERT INTO Genre (genre_name)
VALUES
('Action'),
('Sci-Fi'),
('Drama'),
('Thriller'),
('Adventure'),
('Romance'),
('Fantasy'),
('Superhero');

INSERT INTO Movie_Genre
VALUES
(1,1),(1,2),
(2,2),(2,3),
(3,1),(3,4),
(4,2),(4,7),
(5,3),(5,6),
(6,1),(6,8);

INSERT INTO User (user_name, email)
VALUES
('Pranesh', 'prana@gmail.com'),
('Santosh', 'santosh@gmail.com'),
('Goku', 'goku@gmail.com'),
('Priya', 'priya@gmail.com'),
('Rahul', 'rahul@gmail.com'),
('Jeeva', 'jeeva@gmail.com');

INSERT INTO Review (movie_id, user_id, rating, review_text)
VALUES
(1,1,5,'Nice movie'),
(1,2,4,'Good'),
(2,1,5,'Amazing visuals'),
(3,3,5,'Masterpiece film'),
(3,4,5,'Perfect storytelling'),
(4,5,4,'Stunning'),
(5,6,5,'Emotional love story'),
(6,2,5,'Best movie ever');

INSERT INTO Artist (artist_name)
VALUES
('Leonardo DiCaprio'),
('Christopher Nolan'),
('Christian Bale'),
('Kate Winslet'),
('Sam Worthington'),
('Robert Downey Jr.'),
('Zoe Saldana');

INSERT INTO Skill (skill_name)
VALUES
('Acting'),
('Directing'),
('Writing'),
('Cinematography'),
('Editing'),
('Production');

INSERT INTO Artist_Skill
VALUES
(1,1),
(2,2),
(2,3),
(3,1),
(4,1),
(5,1),
(6,1),
(6,5);

INSERT INTO Role (role_name)
VALUES
('Actor'),
('Director'),
('Writer'),
('Producer'),
('Cinematographer');

INSERT INTO Movie_Artist_Role
VALUES
(1,1,1),
(1,2,2),
(1,2,3),
(3,3,1),
(5,4,1),
(4,5,1),
(6,6,1),
(3,2,5);

