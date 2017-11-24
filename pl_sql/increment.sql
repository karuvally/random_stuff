set serveroutput on size 30000;

DECLARE
    input_pid int;
    retrieved_price int;

BEGIN
    input_pid := &pid;
    
    select price
    into retrieved_price
    from products
    where pid = input_pid;
    
    dbms_output.put_line(retrieved_price);

END;
/