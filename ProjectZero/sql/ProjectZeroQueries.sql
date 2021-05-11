
--DQL(select)
select * from clients;
select * from accounts;

select * from accounts where id=10;
update accounts set amount = amount+-10 where id=10 and account_client_id = 5 returning *;


--testing select statement-- 
--select * FROM accounts WHERE account_client_id = 5 AND ( amount < 2000 AND amount > 400 );


create table scores (score_id serial, initial varchar(10), scores int)
drop table scores; 
select * from scores 