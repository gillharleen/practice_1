Create table if not exists Exp(
    ID BIGINT primary key,
    name varchar(35) Not Null,
    amount numeric(10,2) not null CHECK (amount >0),
    category varchar(20) not null
);