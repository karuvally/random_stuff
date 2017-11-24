create or replace function product_count
return int is
    total_count int;
    
BEGIN
    select count(pid)
    into total_count
    from products;
    
    return total_count;

END;
/