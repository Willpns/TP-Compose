CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO utilisateurs (nom, email) VALUES 
('Alice Dupont', 'alice@example.com'),
('Bob Martin', 'bob@example.com');