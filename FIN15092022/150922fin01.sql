create table finance.symbols (
	symbol varchar(4) primary key,
	name text,
	country text
);

insert into finance.symbols values ('MSFT', 'Microsoft', 'United States');

select * from finance.symbols;

delete from finance.symbols;

select count(1) from finance.symbols 
where symbol = 'MSFT';


	
create table finance.earnings_quarter (
	symbol varchar(4),
	quarter char(6),
	revenue bigint,
	earnings bigint,
	primary key (symbol, quarter)
);

ALTER TABLE finance.earnings_quarter ADD CONSTRAINT earnings_quarter_fk 
	FOREIGN KEY (symbol) REFERENCES finance.symbols(symbol);

select * from finance.earnings_quarter eq;



