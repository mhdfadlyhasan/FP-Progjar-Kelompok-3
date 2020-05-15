create table account(
	id int auto_increment primary key,
	name varchar(50),
	email varchar(50)
);
create table chatxaccount(
	account_id int,
	chat_id int
);
create table chat(
	id int auto_increment primary key,
	chat_name varchar(50)
);
create table message(
	chat_id int,
	msg varchar (500),
	get_time datetime 
);

insert into account(name,email)values('dummy','dummy@email.com');