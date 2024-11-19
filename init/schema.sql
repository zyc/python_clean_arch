CREATE DATABASE IF NOT EXISTS clean_database;

CREATE TABLE IF NOT EXISTS 'clean_database. 'users' (
  id BIGINT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR (255) NOT NULL,
  last name VARCHAR(255) NOT NULL,
  age BIGINT NOT NULL,
  primaryikey (id)
) ;
