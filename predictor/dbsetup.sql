SHOW DATABASES;
CREATE DATABASE predictor;
USE predictor;

CREATE TABLE results (
	season SMALLINT,
    week TINYINT,
    home_team VARCHAR(30),
    home_score TINYINT,
    away_score TINYINT,
    away_team VARCHAR(30),
    winner VARCHAR(30),
    allan VARCHAR(30),
    primary key (season, week, home_team, away_team)
)