create database gym_db;
use gym_db;
create table members(
    id int auto_increment primary key,
    name varchar(50) not null,
    age int not null
);
create table workout_sessions(
    id int auto_increment primary key,
    member_id int,
    date date not null,
    duration_minutes int not null,
    calories_burned int not null,
    foreign key (member_id) references members(id)
);