set serveroutput on size 30000;

DECLARE
    input_value int;

BEGIN
    input_value := &input;
    input_value := input_value * 10;
    dbms_output.put_line(input_value);

END;
/