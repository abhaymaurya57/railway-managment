create table railways.railway(
id INT auto_increment primary key,
name varchar(100) not null,
phone_number varchar(15) not null,
age int not null,
gender varchar(10)not null,
from_station varchar(50) not null,
to_station varchar(50) not null,
travel_date date not null
);

INSERT into railway(name ,phone_number,age,gender,from_station,to_station,travel_date) VALUE('UTKARSH SRIVASTAVA',
'9343463467',30,'M','AGRA FORT','LUCKNOW JUNCTION','2024-12-23');
INSERT into railway(name ,phone_number,age,gender,from_station,to_station,travel_date) VALUE('PRATYUSH KUMAR NISHAD','9834247252',
26,'M','AGRA FORT','BANARAS JUNTION','2024-12-24');

select * from railways.user_account;

create table railways.user_account(
id int auto_increment primary key,
user_name varchar(100) not null unique,
password varchar(100) not null,
first_name varchar(100),
last_name varchar(100),
phone_number varchar(10),
gender ENUM('M','F','N') default 'n',
dob date,
age int,
phone varchar(10)
);
create table railways.tickets(
id int auto_increment primary key,
name varchar(100) not null,
phone varchar(10) not null,
age int not null,
gender ENUM('M','F','N') default 'n' not null,
from_destination varchar(100) not null,
to_destination varchar(100) not null,
travel_date date not null
)
show database railways;
select * from railways.user_account;
select * from railways.tickets;
truncate table railways.user_account;
truncate table railways.tickets;
