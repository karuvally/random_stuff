create or replace function max_price
return int is
    retrieved_price int;

BEGIN
    select max(price)
    into retrieved_price
    from products;
    
    return retrieved_price;

END;
/