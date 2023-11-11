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
    picture path
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
    professional integer
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
-- Name: company_requests; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_requests (
    c_id integer NOT NULL,
    job_add_id integer NOT NULL
);


ALTER TABLE jobmatch.company_requests OWNER TO postgres;

--
-- Name: job_ads; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.job_ads (
    id integer NOT NULL,
    salary_range integer NOT NULL,
    location character varying(255) NOT NULL,
    status character varying(128) DEFAULT 'active'::character varying NOT NULL,
    requirements text NOT NULL,
    company integer
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
-- Name: professionals; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professionals (
    id integer NOT NULL,
    summary character varying(255),
    location character varying(255),
    status character varying(128) DEFAULT 'active'::character varying NOT NULL,
    picture path
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
-- Name: professionals_requests; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professionals_requests (
    p_id integer NOT NULL,
    comp_add_id integer NOT NULL
);


ALTER TABLE jobmatch.professionals_requests OWNER TO postgres;

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

COPY jobmatch.companies (id, description, location, picture) FROM stdin;
\.


--
-- Data for Name: company_ads; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_ads (id, salary_range, description, status, skill_set, "skill level", professional) FROM stdin;
\.


--
-- Data for Name: company_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_requests (c_id, job_add_id) FROM stdin;
\.


--
-- Data for Name: job_ads; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.job_ads (id, salary_range, location, status, requirements, company) FROM stdin;
\.


--
-- Data for Name: professionals; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals (id, summary, location, status, picture) FROM stdin;
\.


--
-- Data for Name: professionals_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals_requests (p_id, comp_add_id) FROM stdin;
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
-- Name: company_requests company_requests_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT company_requests_pkey PRIMARY KEY (c_id, job_add_id);


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
-- Name: professionals_requests professionals_requests_pkey; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals_requests
    ADD CONSTRAINT professionals_requests_pkey PRIMARY KEY (p_id, comp_add_id);


--
-- Name: job_ads comp_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.job_ads
    ADD CONSTRAINT comp_id FOREIGN KEY (company) REFERENCES jobmatch.companies(id);


--
-- Name: company_requests comp_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT comp_id FOREIGN KEY (c_id) REFERENCES jobmatch.companies(id);


--
-- Name: professionals_requests company_ad; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals_requests
    ADD CONSTRAINT company_ad FOREIGN KEY (comp_add_id) REFERENCES jobmatch.company_ads(id);


--
-- Name: company_requests jadd_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT jadd_id FOREIGN KEY (job_add_id) REFERENCES jobmatch.job_ads(id);


--
-- Name: company_ads prof_id; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_ads
    ADD CONSTRAINT prof_id FOREIGN KEY (professional) REFERENCES jobmatch.professionals(id);


--
-- Name: professionals_requests professional; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals_requests
    ADD CONSTRAINT professional FOREIGN KEY (p_id) REFERENCES jobmatch.professionals(id);


--
-- PostgreSQL database dump complete
--

