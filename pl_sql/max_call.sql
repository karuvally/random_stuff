set serveroutput on size 30000;

DECLARE
    price int;

BEGIN
    price := max_price();
    dbms_output.put_line(price);

END;
/