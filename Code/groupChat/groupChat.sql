create table room
(
    id int auto_increment primary key,
    roomName varchar(20)
);

create table roomMember
(
    id int auto_increment primary key,
    roomID int,
    userID int,
    
    constraint FK_user foreign key userID references account(id),
    constraint FK_room foreign key roomID references room(id)
);