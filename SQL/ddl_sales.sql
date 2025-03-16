-- public.sales определение

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	id serial4 NOT NULL,
	dt date NULL,
	store varchar(20) NULL,
	cash varchar(20) NULL,
	doc_id varchar(20) NULL,
	item varchar(100) NULL,
	category varchar(30) NULL,
	amount numeric NULL,
	price numeric NULL,
	discount numeric NULL,
	CONSTRAINT sales_pkey PRIMARY KEY (id)
);