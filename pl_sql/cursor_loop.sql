set serveroutput on size 30000;

DECLARE
    cursor product_names is
        select name
        from products;
    
    retrieved_name;

BEGIN
    for record in product_names
    loop
        dbms_output.put_line(record.name);
    end loop;

END;
/