CREATE DATABASE worldbank_db;
USE worldbank_db;


CREATE TABLE worldbank (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Country Name` TEXT,
  `Country Code` TEXT,
  Year FLOAT,
  `Central government debt, total (% of GDP)` FLOAT,
  `Poverty headcount ratio at $1.90 a day (% of pop)` FLOAT,
  `Revenue, excluding grants (% of GDP)` FLOAT
);



select * from worldbank;