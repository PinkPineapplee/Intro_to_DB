CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT FOREIGN KEY REFERENCES Authors(author_id),
    price DOUBLE NOT NULL,
    published_date DATE NOT NULL
);

CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215)
    address TEXT
);

CREATE TABLE Orders (
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_id INT PRIMARY KEY,
    order_date DATE
    order_id INT FOREIGN KEY REFERENCES Orders(order_id), 
);


CREATE TABLE Order_Details (
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id), 
    orderdetailid INT PRIMARY KEY,
    quantity DOUBLE
);