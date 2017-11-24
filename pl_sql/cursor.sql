set serveroutput on size 30000;

DECLARE
    cursor product_name is
        select name
        from products;
    
    retrieved_name varchar(15);

BEGIN
    open product_name;
        fetch product_name
        into retrieved_name;
    close product_name;
    
    dbms_output.put_line(retrieved_name);

END;
/