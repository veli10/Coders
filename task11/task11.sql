-- CREATE TABLE PRODUCTS(
--     ID INT,
-- 	PRODUCT_COUNT INT,
--     PRODUCT_PRICE INT
-- )
-- INSERT INTO PRODUCTS (ID, PRODUCT_COUNT, PRODUCT_PRICE) VALUES (1, 5, 5);
-- INSERT INTO PRODUCTS (ID, PRODUCT_COUNT, PRODUCT_PRICE) VALUES (2, 10, 2);
-- INSERT INTO PRODUCTS (ID, PRODUCT_COUNT, PRODUCT_PRICE) VALUES(3, 3, 20);
-- INSERT INTO PRODUCTS (ID, PRODUCT_COUNT, PRODUCT_PRICE) VALUES(4, 7, 10);

-- ALTER TABLE PRODUCTS ADD TOTAL_VALUE NUMBER;

-- UPDATE PRODUCTS 
-- SET TOTAL_VALUE = PRODUCT_COUNT * PRODUCT_PRICE;

-- SELECT * FROM PRODUCTS ORDER BY TOTAL_VALUE

----------------------------------------------------------------------------------------

-- CREATE TABLE MY_EMPLOYEES(
--     NAME NVARCHAR2(50),
-- 	SALARY INT,
--     DEPARTAMENT NVARCHAR2(50)
-- )
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES ('Mansur', 1000, 'satis');
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES ('Eli', 1200, 'IT');
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES('Murad', 900, 'satis');
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES('Azer', 550, 'satis');
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES('Ayaz', 700, 'satis');
-- INSERT INTO MY_EMPLOYEES (NAME, SALARY, DEPARTAMENT) VALUES('Elcin', 1400, 'IT');

-- SELECT * FROM MY_EMPLOYEES WHERE DEPARTAMENT='satis' AND SALARY>600 ORDER BY SALARY DESC;

------------------------------------------------------------------------------------------------------

-- CREATE TABLE MY_LIBRARY (
--     NAME NVARCHAR2(100),
--     GENRE NVARCHAR2(50),
--     PUBLICATION_DATE DATE
-- );

-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Girl on the Train', 'Thriller', TO_DATE('2013-01-13', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Nightingale', 'Historical Fiction', TO_DATE('2012-02-03', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('All the Light We Cannot See', 'Historical Fiction', TO_DATE('2014-04-07', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Martian', 'Science Fiction', TO_DATE('2014-10-28', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Underground Railroad', 'Historical Fiction', TO_DATE('2016-08-02', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Handmaids Tale', 'Dystopian', TO_DATE('2017-03-26', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('Educated', 'Memoir', TO_DATE('2018-02-18', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('Where the Crawdads Sing', 'Mystery', TO_DATE('2018-08-14', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('Becoming', 'Biography', TO_DATE('2018-11-13', 'YYYY-MM-DD'));
-- INSERT INTO MY_LIBRARY (NAME, GENRE, PUBLICATION_DATE) VALUES ('The Silent Patient', 'Thriller', TO_DATE('2019-02-05', 'YYYY-MM-DD'));


-- SELECT * FROM MY_LIBRARY WHERE PUBLICATION_DATE > TO_DATE('2015-12-31', 'YYYY-MM-DD') ORDER BY GENRE;

---------------------------------------------------------------------------------------------------------------------------------------------

-- CREATE TABLE MOVIES (
--     MOVIE_NAME NVARCHAR2(100),
--     DATE_OF_RELEASE DATE,
--     RATING NUMBER(3, 1)
-- );

-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('Inception', TO_DATE('2010-07-16', 'YYYY-MM-DD'), 8.8);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('The Dark Knight', TO_DATE('2008-07-18', 'YYYY-MM-DD'), 9.0);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('Interstellar', TO_DATE('2014-11-07', 'YYYY-MM-DD'), 8.6);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('The Matrix', TO_DATE('1999-03-31', 'YYYY-MM-DD'), 8.7);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('Gladiator', TO_DATE('2000-05-05', 'YYYY-MM-DD'), 8.5);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('Avatar', TO_DATE('2009-12-18', 'YYYY-MM-DD'), 7.8);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('Titanic', TO_DATE('1997-12-19', 'YYYY-MM-DD'), 7.8);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('The Lord of the Rings: The Return of the King', TO_DATE('2003-12-17', 'YYYY-MM-DD'), 8.9);
-- INSERT INTO MOVIES (MOVIE_NAME, DATE_OF_RELEASE, RATING) VALUES ('The Shawshank Redemption', TO_DATE('1994-09-23', 'YYYY-MM-DD'), 9.3);

-- SELECT MOVIE_NAME, DATE_OF_RELEASE, RATING FROM MOVIES WHERE DATE_OF_RELEASE > TO_DATE('2000-01-01', 'YYYY-MM-DD') AND RATING >= 7.0 ORDER BY RATING DESC;