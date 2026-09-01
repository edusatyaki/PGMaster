CREATE TABLE departments (dept_id int PRIMARY KEY, dept_name text);
INSERT INTO departments VALUES (101,'IT'),(102,'Sales'),(103,'HR');
CREATE TABLE employees (
  id int PRIMARY KEY, name text, dept_id int REFERENCES departments,
  salary numeric, hire_date date, email text);
INSERT INTO employees VALUES
 (1,'Alice',101,70000,'2019-03-15','alice@corp.io'),
 (2,'Bob',102,85000,'2020-07-01','bob@corp.io'),
 (3,'Charlie',101,60000,'2021-11-23','charlie@corp.io'),
 (4,'Diana',102,92000,'2018-01-09','diana@corp.io'),
 (5,'Evan',NULL,55000,'2022-05-30',NULL);
CREATE TYPE mood AS ENUM ('sad','ok','happy');
CREATE SEQUENCE emp_seq START 100;
CREATE VIEW high_earners AS SELECT name, salary FROM employees WHERE salary > 80000;
CREATE INDEX idx_emp_name ON employees(name);
