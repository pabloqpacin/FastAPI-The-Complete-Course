DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

-- ===== CREATE TABLES =====

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL,
  email varchar(200) DEFAULT NULL,
  username varchar(45) DEFAULT NULL,
  first_name varchar(45) DEFAULT NULL,
  last_name varchar(45) DEFAULT NULL,
  hashed_password varchar(200) DEFAULT NULL,
  is_active boolean DEFAULT NULL,
  role varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
  id SERIAL,
  title varchar(200) DEFAULT NULL,
  description varchar(200) DEFAULT NULL,
  priority integer DEFAULT NULL,
  complete boolean DEFAULT NULL,
  owner_id integer DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- ===== POPULATE TABLES =====

-- SELECT * FROM pg_extension;
-- CREATE EXTENSION IF NOT EXISTS pgcrypto;

/* Credenciales: foo==123abc; bar==123xyz */
INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active, role) VALUES
-- ( 'foo@example.com', 'foo', 'foo', 'example', crypt('123abc', gen_salt('bf')), TRUE, 'admin'),
  ( 'foo@example.com', 'foo', 'foo', 'example', '$2b$12$hevQQk73MbsOt5AG7Ofe7OZ6FWsp9Xwz8gh048fkK06ZuwS1lJ1DW', TRUE, 'admin'),
  ( 'bar@example.com', 'bar', 'bar', 'example', '$2b$12$TFlZ99l/WK/hIhJHJPajk.GuloOgrntRwQ2SDmnu2shD4bPy7qXVq', TRUE, '')
;

INSERT INTO todos (title, description, priority, complete, owner_id) VALUES
  ('Go to store','supdawg',4,false,1),
  ('Haircut','supdawg',3,true,2),
  ('Feed dog','supdawg',5,false,1),
  ('Water plant','supdawg',4,false,2),
  ('Learn something new','supdawg',5,true,1)
;

