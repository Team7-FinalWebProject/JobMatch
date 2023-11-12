--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: jobmatch; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA jobmatch;


ALTER SCHEMA jobmatch OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: companies; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.companies (
    id integer NOT NULL,
    description character varying(255),
    location character varying(255),
    picture path,
    username character varying(100),
    company_name character varying(100),
    password text
);


ALTER TABLE jobmatch.companies OWNER TO postgres;

--
-- Name: companies_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.companies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.companies_id_seq OWNER TO postgres;

--
-- Name: companies_id_seq1; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.companies_id_seq1
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.companies_id_seq1 OWNER TO postgres;

--
-- Name: companies_id_seq1; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.companies_id_seq1 OWNED BY jobmatch.companies.id;


--
-- Name: company_ads; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_ads (
    id integer NOT NULL,
    salary_range integer NOT NULL,
    description character varying(255) NOT NULL,
    status character varying(255) NOT NULL,
    skill_set character varying(255) NOT NULL,
    "skill level" integer DEFAULT 1 NOT NULL,
    professional_id integer,
    company_id integer,
    match_request_job_ad_id integer
);


ALTER TABLE jobmatch.company_ads OWNER TO postgres;

--
-- Name: company_ads_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_ads_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.company_ads_id_seq OWNER TO postgres;

--
-- Name: company_ads_id_seq1; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_ads_id_seq1
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.company_ads_id_seq1 OWNER TO postgres;

--
-- Name: company_ads_id_seq1; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.company_ads_id_seq1 OWNED BY jobmatch.company_ads.id;


--
-- Name: job_ads; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.job_ads (
    id integer NOT NULL,
    salary_range integer NOT NULL,
    location character varying(255) NOT NULL,
    status character varying(128) DEFAULT 'active'::character varying NOT NULL,
    requirements text NOT NULL,
    company_id integer,
    professional_id integer
);


ALTER TABLE jobmatch.job_ads OWNER TO postgres;

--
-- Name: job_ads_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_id_seq OWNER TO postgres;

--
-- Name: job_ads_id_seq1; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_id_seq1
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_id_seq1 OWNER TO postgres;

--
-- Name: job_ads_id_seq1; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.job_ads_id_seq1 OWNED BY jobmatch.job_ads.id;


--
-- Name: job_ads_location_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_location_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_location_seq OWNER TO postgres;

--
-- Name: job_ads_requirements_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_requirements_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_requirements_seq OWNER TO postgres;

--
-- Name: job_ads_salary_range_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_salary_range_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_salary_range_seq OWNER TO postgres;

--
-- Name: job_ads_status_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.job_ads_status_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.job_ads_status_seq OWNER TO postgres;

--
-- Name: messages; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.messages (
    job_ad_id integer,
    company_ad_id integer,
    content integer
);


ALTER TABLE jobmatch.messages OWNER TO postgres;

--
-- Name: professionals; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professionals (
    id integer NOT NULL,
    summary character varying(255),
    location character varying(255),
    status character varying(128) DEFAULT 'active'::character varying NOT NULL,
    picture path,
    username character varying(100),
    first_name character varying(100),
    last_name character varying(100),
    password text
);


ALTER TABLE jobmatch.professionals OWNER TO postgres;

--
-- Name: professionals_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professionals_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;


ALTER SEQUENCE jobmatch.professionals_id_seq OWNER TO postgres;

--
-- Name: professionals_id_seq1; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professionals_id_seq1
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professionals_id_seq1 OWNER TO postgres;

--
-- Name: professionals_id_seq1; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professionals_id_seq1 OWNED BY jobmatch.professionals.id;


--
-- Name: companies id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies ALTER COLUMN id SET DEFAULT nextval('jobmatch.companies_id_seq1'::regclass);


--
-- Name: company_ads id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads ALTER COLUMN id SET DEFAULT nextval('jobmatch.company_ads_id_seq1'::regclass);


--
-- Name: job_ads id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.job_ads ALTER COLUMN id SET DEFAULT nextval('jobmatch.job_ads_id_seq1'::regclass);


--
-- Name: professionals id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals ALTER COLUMN id SET DEFAULT nextval('jobmatch.professionals_id_seq1'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.companies (id, description, location, picture, username, company_name, password) FROM stdin;
\.


--
-- Data for Name: company_ads; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_ads (id, salary_range, description, status, skill_set, "skill level", professional_id, company_id, match_request_job_ad_id) FROM stdin;
\.


--
-- Data for Name: job_ads; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.job_ads (id, salary_range, location, status, requirements, company_id, professional_id) FROM stdin;
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.messages (job_ad_id, company_ad_id, content) FROM stdin;
\.


--
-- Data for Name: professionals; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals (id, summary, location, status, picture, username, first_name, last_name, password) FROM stdin;
\.


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.companies_id_seq', 1, false);


--
-- Name: companies_id_seq1; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.companies_id_seq1', 1, false);


--
-- Name: company_ads_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_ads_id_seq', 1, false);


--
-- Name: company_ads_id_seq1; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_ads_id_seq1', 1, false);


--
-- Name: job_ads_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_id_seq', 1, false);


--
-- Name: job_ads_id_seq1; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_id_seq1', 1, false);


--
-- Name: job_ads_location_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_location_seq', 1, false);


--
-- Name: job_ads_requirements_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_requirements_seq', 1, false);


--
-- Name: job_ads_salary_range_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_salary_range_seq', 1, false);


--
-- Name: job_ads_status_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.job_ads_status_seq', 1, false);


--
-- Name: professionals_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professionals_id_seq', 1, false);


--
-- Name: professionals_id_seq1; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professionals_id_seq1', 1, false);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);


--
-- Name: company_ads company_ads_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads
    ADD CONSTRAINT company_ads_pkey PRIMARY KEY (id);


--
-- Name: job_ads job_ads_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.job_ads
    ADD CONSTRAINT job_ads_pkey PRIMARY KEY (id);


--
-- Name: professionals professionals_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT professionals_pkey PRIMARY KEY (id);


--
-- Name: job_ads comp_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.job_ads
    ADD CONSTRAINT comp_id FOREIGN KEY (company_id) REFERENCES jobmatch.companies(id);


--
-- Name: company_ads fk_company_ads_companies; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads
    ADD CONSTRAINT fk_company_ads_companies FOREIGN KEY (company_id) REFERENCES jobmatch.companies(id);


--
-- Name: company_ads fk_company_ads_job_ads; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads
    ADD CONSTRAINT fk_company_ads_job_ads FOREIGN KEY (match_request_job_ad_id) REFERENCES jobmatch.job_ads(id);


--
-- Name: job_ads fk_job_ads_professionals; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.job_ads
    ADD CONSTRAINT fk_job_ads_professionals FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- Name: messages fk_messages_company_ads; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT fk_messages_company_ads FOREIGN KEY (company_ad_id) REFERENCES jobmatch.company_ads(id);


--
-- Name: messages fk_messages_job_ads; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT fk_messages_job_ads FOREIGN KEY (job_ad_id) REFERENCES jobmatch.job_ads(id);


--
-- Name: company_ads prof_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads
    ADD CONSTRAINT prof_id FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- PostgreSQL database dump complete
--

