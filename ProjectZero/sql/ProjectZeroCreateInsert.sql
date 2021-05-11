--DML(create,alter,drop,truncate))

drop table clients;
drop table if exists accounts;

create table clients ( 
	id SERIAL primary key,
	name VARCHAR(50)
);
create table accounts (
	id SERIAL primary key,
	name VARCHAR(50),
	amount NUMERIC(20,2),
	account_client_id bigint references clients(id) on delete set null
);
alter table accounts add constraint positive_amount
	check (amount >=0);

--DDL(insert, update, delete)
insert into clients values (default, 'name');
insert into clients values (default, 'charles');
insert into clients values (default, 'david');
insert into clients values (default, 'helpme');
insert into clients values (default, 'lost');
insert into clients values (default, 'leftover');
insert into clients values (default, 'aunty');
insert into clients values (default, 'lost');
insert into clients values (default, 'devil');
insert into clients values (default, 'table');
insert into clients values (default, 'here');
insert into clients values (default, 'red');

insert into accounts values (default, 'zoo_account', 20, 1);
insert into accounts values (default, 'yeah_account', 9999, 2);
insert into accounts values (default, 'vice_account', 20, 3);
insert into accounts values (default, 'uniform_account', 9999, 4);
insert into accounts values (default, 'trek_account', 20, 5);
insert into accounts values (default, 'stick_account', 9999, 5);
insert into accounts values (default, 'run_account', 20, 6);
insert into accounts values (default, 'question_account', 9999, 7);
insert into accounts values (default, 'pop_account', 20, 8);
insert into accounts values (default, 'open_account', 9999, 9);
insert into accounts values (default, 'never_account', 20, 10);
insert into accounts values (default, 'metal_account', 9999, 11);

update accounts set amount=-5556 where id=12 or id=11;
update accounts set amount= 1000, account_client_id = 5 where id = 5 returning *;


--after testing postman 
insert into clients values (2, 'second');
insert into accounts values (13, 'tidal',7525,5);
delete from accounts where id=2 returning *;
delete from clients where id=8 returning *;