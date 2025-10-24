SELECT 
    book_id,
    title,
    author_id
    price,
    published_date
FROM alx_book_store.Books
WHERE TABLE_SCHEMA = DATABASE('alx_book_store')
  AND TABLE_NAME = 'Books';