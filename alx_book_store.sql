CREATE DATABASE alx_book_store;
USE alx_book_store;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT FOREIGN KEY REFERENCES authors(author_id),
    price DOUBLE NOT NULL,
    published_date DATE NOT NULL
);

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215)
    address TEXT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
    order_date DATE
    order_id INT FOREIGN KEY REFERENCES orders(order_id), 
);


CREATE TABLE orders_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES orders(order_id), 
    book_id INT FOREIGN KEY REFERENCES books(book_id),
    quantity DOUBLE
);