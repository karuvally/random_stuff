set serveroutput on size 30000;

DECLARE
    current_number int := 1;
    past_number int := 0;
    temp_val int;

BEGIN
    dbms_output.put_line(past_number);
    
    loop
        exit when current_number > 10;
        dbms_output.put_line(current_number);
        
        temp_val := current_number;
        current_number := past_number + current_number;
        past_number := temp_val;
    end loop;

END;
/