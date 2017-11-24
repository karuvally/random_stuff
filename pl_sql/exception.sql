set serveroutput on size 30000;

DECLARE
    retrieved_price int;
    input_pid int;

BEGIN
    input_pid := &PID;
    
    select price
    into retrieved_price
    from products
    where pid = input_pid;
    
    dbms_output.put_line('the product costs ' || retrieved_price);
    
    exception
        when no_data_found then
            dbms_output.put_line('No data found');
        when others then
            dbms_output.put_line('Some random error!');

END;
/