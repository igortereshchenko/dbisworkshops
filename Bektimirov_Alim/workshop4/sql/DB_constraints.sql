/*
    This block contains constraint creation,
    such as FOREIGN KEYs, CHECKs etc.
*/
ALTER TABLE expected_film_list
ADD CONSTRAINT check_film_rating
CHECK (rating >= 0 and rating<=10);


