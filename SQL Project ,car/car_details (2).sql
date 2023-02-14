create database project;
use project;

select*from car_details;

select *from car_details where name like 'mar%';

select *from car_details where name like 'Hon%';

select *from car_details where name like 'TATA%';

select *from car_details where year like '__07%';

select *from car_details where year between 1990 and 2010;

select *from car_details where year between 2011 and 2015;

select *from car_details where year between 2016 and 2020;

select *from car_details where selling_price between 10000 and 100000;

select *from car_details where selling_price between 100001 and 400000 order by selling_price;

select *from car_details where selling_price between 400001  and 800000 order by selling_price desc ;

select *from car_details where selling_price between 800001 and 1200000 order by selling_price limit 20;

select *from car_details where selling_price between 1200001 and 1600000;

select *from car_details where selling_price between 1600001 and 2000000 order by selling_price limit 10;

select *from car_details where seller_type="Individual";

select *from car_details where seller_type="Dealer";

select *from car_details order by km_driven;

select * from car_details where selling_price = (select max(selling_price) from car_details);

select *from  car_details where selling_price=(select min(selling_price)from car_details);

select *from car_details where selling_price <=500000 order by selling_price;

select avg(selling_price) from car_details;

select count(name),selling_price from car_details group by selling_price;

select name,count(*) from car_details group by name;

select name, year, selling_price from car_details group by name having selling_price>=2000000;

select *from car_details where selling_price = 1000000;

select *from car_details where selling_price <>50000 order by selling_price desc limit 20;

select name, year, owner, selling_price from car_details having owner like 'First%';

select name, year, owner, selling_price from car_details having owner like 'Second%' limit 25;

select name, year, owner, selling_price from car_details having owner like 'Third%';

select *from car_details where (name like 'Audi%' or name like 'BMW%' or name like 'Juguar%'  or name like 'Land%'
or name like 'Mercedes%'  or name like 'Volvo%') order by name; 

select count(*) from car_details; 

select *from car_details where (name like 'Audi%' or name like 'BMW%' or name like 'Juguar%'  or name like 'Land%'
or name like 'Mercedes%'  or name like 'Volvo%') having fuel like 'Petrol%' order by name; 

select name, year, selling_price, km_driven, fuel, seller_type, transmission, owner, count(name) as total_model_sell 
from car_details group by name order by total_model_sell; 

select fuel,count(fuel) as fuel_count from car_details group by fuel; 

select transmission,count(transmission) as transmission_count from car_details group by transmission; 

update car_details set year =2022;

drop table car_details;

drop database project;
 
 