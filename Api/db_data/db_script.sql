-- DROP SCHEMA jobmatch;

CREATE SCHEMA jobmatch AUTHORIZATION postgres;

-- DROP SEQUENCE jobmatch.companies_id_seq;

CREATE SEQUENCE jobmatch.companies_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.company_ads_id_seq;

CREATE SEQUENCE jobmatch.company_ads_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.job_ads_id_seq;

CREATE SEQUENCE jobmatch.job_ads_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.job_ads_location_seq;

CREATE SEQUENCE jobmatch.job_ads_location_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.job_ads_requirements_seq;

CREATE SEQUENCE jobmatch.job_ads_requirements_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.job_ads_salary_range_seq;

CREATE SEQUENCE jobmatch.job_ads_salary_range_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.job_ads_status_seq;

CREATE SEQUENCE jobmatch.job_ads_status_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE jobmatch.professionals_id_seq;

CREATE SEQUENCE jobmatch.professionals_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- jobmatch.companies definition

-- Drop table

-- DROP TABLE jobmatch.companies;

CREATE TABLE jobmatch.companies (
	id serial4 NOT NULL,
	description varchar(255) NULL,
	"location" varchar(255) NULL,
	picture path NULL,
	CONSTRAINT companies_pkey PRIMARY KEY (id)
);


-- jobmatch.professionals definition

-- Drop table

-- DROP TABLE jobmatch.professionals;

CREATE TABLE jobmatch.professionals (
	id serial4 NOT NULL,
	summary varchar(255) NULL,
	"location" varchar(255) NULL,
	status varchar(128) NOT NULL DEFAULT 'active'::character varying,
	picture path NULL,
	CONSTRAINT professionals_pkey PRIMARY KEY (id)
);


-- jobmatch.company_ads definition

-- Drop table

-- DROP TABLE jobmatch.company_ads;

CREATE TABLE jobmatch.company_ads (
	id serial4 NOT NULL,
	salary_range int4 NOT NULL,
	description varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	skill_set varchar(255) NOT NULL,
	"skill level" int4 NOT NULL DEFAULT 1,
	professional int4 NULL,
	CONSTRAINT company_ads_pkey PRIMARY KEY (id),
	CONSTRAINT prof_id FOREIGN KEY (professional) REFERENCES jobmatch.professionals(id)
);


-- jobmatch.job_ads definition

-- Drop table

-- DROP TABLE jobmatch.job_ads;

CREATE TABLE jobmatch.job_ads (
	id serial4 NOT NULL,
	salary_range int4 NOT NULL,
	"location" varchar(255) NOT NULL,
	status varchar(128) NOT NULL DEFAULT 'active'::character varying,
	requirements text NOT NULL,
	company int4 NULL,
	CONSTRAINT job_ads_pkey PRIMARY KEY (id),
	CONSTRAINT comp_id FOREIGN KEY (company) REFERENCES jobmatch.companies(id)
);


-- jobmatch.professionals_requests definition

-- Drop table

-- DROP TABLE jobmatch.professionals_requests;

CREATE TABLE jobmatch.professionals_requests (
	p_id int4 NOT NULL,
	comp_add_id int4 NOT NULL,
	CONSTRAINT professionals_requests_pkey PRIMARY KEY (p_id, comp_add_id),
	CONSTRAINT company_ad FOREIGN KEY (comp_add_id) REFERENCES jobmatch.company_ads(id),
	CONSTRAINT professional FOREIGN KEY (p_id) REFERENCES jobmatch.professionals(id)
);


-- jobmatch.company_requests definition

-- Drop table

-- DROP TABLE jobmatch.company_requests;

CREATE TABLE jobmatch.company_requests (
	c_id int4 NOT NULL,
	job_add_id int4 NOT NULL,
	CONSTRAINT company_requests_pkey PRIMARY KEY (c_id, job_add_id),
	CONSTRAINT comp_id FOREIGN KEY (c_id) REFERENCES jobmatch.companies(id),
	CONSTRAINT jadd_id FOREIGN KEY (job_add_id) REFERENCES jobmatch.job_ads(id)
);