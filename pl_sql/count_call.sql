set serveroutput on size 30000;

DECLARE
    item_count int;

BEGIN
    item_count := product_count();
    dbms_output.put_line(item_count);

END;
/