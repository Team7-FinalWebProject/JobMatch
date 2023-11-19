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

--
-- Name: check_user_id_admin_not_in_professionals_or_companies(); Type: FUNCTION; Schema: jobmatch; Owner: postgres
--

CREATE FUNCTION jobmatch.check_user_id_admin_not_in_professionals_or_companies() RETURNS trigger
    LANGUAGE plpgsql
    AS $$

BEGIN

  IF NEW.admin AND (

    EXISTS (SELECT 1 FROM jobmatch.professionals WHERE jobmatch.professionals.user_id = NEW.id) OR

    EXISTS (SELECT 1 FROM jobmatch.companies WHERE jobmatch.companies.user_id = NEW.id)

  ) THEN

    RAISE EXCEPTION 'id for admin cannot be the same as user_id in jobmatch.companies or jobmatch.professionals';

  END IF;

  RETURN NEW;

END;

$$;


ALTER FUNCTION jobmatch.check_user_id_admin_not_in_professionals_or_companies() OWNER TO postgres;

--
-- Name: check_user_id_companies_not_in_professionals(); Type: FUNCTION; Schema: jobmatch; Owner: postgres
--

CREATE FUNCTION jobmatch.check_user_id_companies_not_in_professionals() RETURNS trigger
    LANGUAGE plpgsql
    AS $$

BEGIN

  IF EXISTS (SELECT 1 FROM jobmatch.professionals WHERE jobmatch.professionals.user_id = NEW.user_id) THEN

    RAISE EXCEPTION 'user_id in jobmatch.companies cannot be the same as jobmatch.professionals';

  END IF;

  RETURN NEW;

END;

$$;


ALTER FUNCTION jobmatch.check_user_id_companies_not_in_professionals() OWNER TO postgres;

--
-- Name: check_user_id_professionals_not_in_companies(); Type: FUNCTION; Schema: jobmatch; Owner: postgres
--

CREATE FUNCTION jobmatch.check_user_id_professionals_not_in_companies() RETURNS trigger
    LANGUAGE plpgsql
    AS $$

BEGIN

  IF EXISTS (SELECT 1 FROM jobmatch.companies WHERE jobmatch.companies.user_id = NEW.user_id) THEN

    RAISE EXCEPTION 'user_id in jobmatch.professionals cannot be the same as jobmatch.companies';

  END IF;

  RETURN NEW;

END;

$$;


ALTER FUNCTION jobmatch.check_user_id_professionals_not_in_companies() OWNER TO postgres;

--
-- Name: insert_into_companies_and_users(text, bytea, text, text, text); Type: PROCEDURE; Schema: jobmatch; Owner: postgres
--

CREATE PROCEDURE jobmatch.insert_into_companies_and_users(IN new_username text, IN new_password bytea, IN new_name text, IN new_description text, IN new_address text)
    LANGUAGE plpgsql
    AS $_$
BEGIN
  WITH new_user_id AS (INSERT INTO jobmatch.users (username,password) VALUES ($1,$2) RETURNING id)
  INSERT INTO jobmatch.companies (user_id,name,description,address) VALUES (new_user_id,$3,$4,$5) RETURNING id;
END;
$_$;


ALTER PROCEDURE jobmatch.insert_into_companies_and_users(IN new_username text, IN new_password bytea, IN new_name text, IN new_description text, IN new_address text) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: company_requests; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_requests (
    id integer NOT NULL,
    company_offer_id integer NOT NULL,
    professional_id integer NOT NULL,
    professional_offer_id integer
);


ALTER TABLE jobmatch.company_requests OWNER TO postgres;

--
-- Name: comcompany_requests_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.comcompany_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.comcompany_requests_id_seq OWNER TO postgres;

--
-- Name: comcompany_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.comcompany_requests_id_seq OWNED BY jobmatch.company_requests.id;


--
-- Name: companies; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.companies (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text DEFAULT ''::text NOT NULL,
    address character varying(100) NOT NULL,
    picture bytea,
    approved boolean DEFAULT false NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE jobmatch.companies OWNER TO postgres;

--
-- Name: companies_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.companies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.companies_id_seq OWNER TO postgres;

--
-- Name: companies_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.companies_id_seq OWNED BY jobmatch.companies.id;


--
-- Name: users; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.users (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    admin boolean DEFAULT false NOT NULL,
    password bytea NOT NULL
);


ALTER TABLE jobmatch.users OWNER TO postgres;

--
-- Name: companies_view; Type: VIEW; Schema: jobmatch; Owner: postgres
--

CREATE VIEW jobmatch.companies_view AS
 SELECT c.id AS company_id,
    c.user_id AS company_user_id,
    c.name AS company_name,
    c.description AS company_description,
    c.address AS company_address,
    c.picture AS company_picture,
    c.approved AS company_approved,
    u.username AS company_username,
    u.password AS company_password
   FROM (jobmatch.companies c
     LEFT JOIN jobmatch.users u ON ((u.id = c.user_id)));


ALTER VIEW jobmatch.companies_view OWNER TO postgres;

--
-- Name: company_offers; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_offers (
    id integer NOT NULL,
    company_id integer NOT NULL,
    status character varying DEFAULT 'active'::character varying NOT NULL,
    chosen_professional_id integer,
    requirements jsonb DEFAULT '{}'::jsonb,
    min_salary integer DEFAULT 0 NOT NULL,
    max_salary integer DEFAULT 2147483647 NOT NULL,
    CONSTRAINT cns_company_offers_status_is_valid CHECK (((status)::text = ANY (ARRAY[('active'::character varying)::text, ('archived'::character varying)::text])))
);


ALTER TABLE jobmatch.company_offers OWNER TO postgres;

--
-- Name: company_offers_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_offers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.company_offers_id_seq OWNER TO postgres;

--
-- Name: company_offers_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.company_offers_id_seq OWNED BY jobmatch.company_offers.id;


--
-- Name: config; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.config (
    lock character(1) DEFAULT 'X'::bpchar NOT NULL,
    static_skills boolean DEFAULT false NOT NULL,
    min_level integer DEFAULT 0 NOT NULL,
    max_level integer DEFAULT 10 NOT NULL,
    baseline_skills text[] DEFAULT ARRAY['English'::text, 'French'::text, 'Computers'::text] NOT NULL,
    pending_approval_skills text[] DEFAULT ARRAY[]::text[] NOT NULL,
    approved_skills text[] DEFAULT ARRAY[]::text[],
    CONSTRAINT cns_config CHECK ((lock = 'X'::bpchar))
);


ALTER TABLE jobmatch.config OWNER TO postgres;

--
-- Name: messages; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.messages (
    id integer NOT NULL,
    sender_username character varying(100) NOT NULL,
    receiver_username character varying(100) NOT NULL,
    content text DEFAULT ''::text NOT NULL
);


ALTER TABLE jobmatch.messages OWNER TO postgres;

--
-- Name: messages_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.messages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.messages_id_seq OWNER TO postgres;

--
-- Name: messages_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.messages_id_seq OWNED BY jobmatch.messages.id;


--
-- Name: professional_offers; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professional_offers (
    id integer NOT NULL,
    professional_id integer NOT NULL,
    description text DEFAULT ''::text NOT NULL,
    chosen_company_offer_id integer,
    status character varying(100) DEFAULT 'active'::character varying NOT NULL,
    skills jsonb DEFAULT '{}'::jsonb,
    min_salary integer DEFAULT 0 NOT NULL,
    max_salary integer DEFAULT 2147483647 NOT NULL,
    CONSTRAINT cns_professional_offers_status_is_valid CHECK (((status)::text = ANY (ARRAY[('active'::character varying)::text, ('private'::character varying)::text, ('hidden'::character varying)::text, ('matched'::character varying)::text])))
);


ALTER TABLE jobmatch.professional_offers OWNER TO postgres;

--
-- Name: professional_offers_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professional_offers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professional_offers_id_seq OWNER TO postgres;

--
-- Name: professional_offers_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professional_offers_id_seq OWNED BY jobmatch.professional_offers.id;


--
-- Name: professional_requests; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professional_requests (
    id integer NOT NULL,
    professional_offer_id integer NOT NULL,
    company_offer_id integer NOT NULL
);


ALTER TABLE jobmatch.professional_requests OWNER TO postgres;

--
-- Name: professional_requests_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professional_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professional_requests_id_seq OWNER TO postgres;

--
-- Name: professional_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professional_requests_id_seq OWNED BY jobmatch.professional_requests.id;


--
-- Name: professionals; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.professionals (
    id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    address character varying NOT NULL,
    user_id integer NOT NULL,
    summary text DEFAULT ''::text NOT NULL,
    default_offer_id integer,
    picture bytea,
    approved boolean DEFAULT false NOT NULL
);


ALTER TABLE jobmatch.professionals OWNER TO postgres;

--
-- Name: professionals_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professionals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professionals_id_seq OWNER TO postgres;

--
-- Name: professionals_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professionals_id_seq OWNED BY jobmatch.professionals.id;


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.users_id_seq OWNED BY jobmatch.users.id;


--
-- Name: web_filters; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.web_filters (
    id integer NOT NULL,
    filter jsonb DEFAULT '{}'::jsonb NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE jobmatch.web_filters OWNER TO postgres;

--
-- Name: web_filters_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.web_filters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.web_filters_id_seq OWNER TO postgres;

--
-- Name: web_filters_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.web_filters_id_seq OWNED BY jobmatch.web_filters.id;


--
-- Name: companies id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies ALTER COLUMN id SET DEFAULT nextval('jobmatch.companies_id_seq'::regclass);


--
-- Name: company_offers id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers ALTER COLUMN id SET DEFAULT nextval('jobmatch.company_offers_id_seq'::regclass);


--
-- Name: company_requests id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests ALTER COLUMN id SET DEFAULT nextval('jobmatch.comcompany_requests_id_seq'::regclass);


--
-- Name: messages id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages ALTER COLUMN id SET DEFAULT nextval('jobmatch.messages_id_seq'::regclass);


--
-- Name: professional_offers id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers ALTER COLUMN id SET DEFAULT nextval('jobmatch.professional_offers_id_seq'::regclass);


--
-- Name: professional_requests id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests ALTER COLUMN id SET DEFAULT nextval('jobmatch.professional_requests_id_seq'::regclass);


--
-- Name: professionals id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals ALTER COLUMN id SET DEFAULT nextval('jobmatch.professionals_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.users ALTER COLUMN id SET DEFAULT nextval('jobmatch.users_id_seq'::regclass);


--
-- Name: web_filters id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.web_filters ALTER COLUMN id SET DEFAULT nextval('jobmatch.web_filters_id_seq'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.companies (id, name, description, address, picture, approved, user_id) FROM stdin;
1	Pepsi	We make the fizzy drink	Los Angeles, California	\N	t	5
2	Steam	We provide video games	Los Angeles, California	\N	t	6
3	Avid	We provide high tech gear	New York, USA	\N	t	7
\.


--
-- Data for Name: company_offers; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_offers (id, company_id, status, chosen_professional_id, requirements, min_salary, max_salary) FROM stdin;
1	1	active	\N	{"English": [7, "Native"], "Computers": [10, "Master"]}	3000	8000
2	2	active	\N	{"English": [5, "Advanced"], "Computers": [5, "Advanced"]}	2500	5500
3	3	active	\N	{"English": [4, "Advanced"], "Computers": [3, "Entry"]}	1500	2500
\.


--
-- Data for Name: company_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_requests (id, company_offer_id, professional_id, professional_offer_id) FROM stdin;
\.


--
-- Data for Name: config; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.config (lock, static_skills, min_level, max_level, baseline_skills, pending_approval_skills, approved_skills) FROM stdin;
X	f	0	10	{English,Computers,French}	{}	{}
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.messages (id, sender_username, receiver_username, content) FROM stdin;
\.


--
-- Data for Name: professional_offers; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professional_offers (id, professional_id, description, chosen_company_offer_id, status, skills, min_salary, max_salary) FROM stdin;
1	1	I can create a AAA title video game	1	active	{"English": [7, "Native"], "Computers": [10, "Master"]}	3000	10000
2	2	You need a data scientist? I am the man for the job.	2	active	{"English": [10, "Native"], "Computers": [3, "Entry"]}	2000	4000
3	3	I can build simple servers	3	active	{"English": [10, "Native"], "Computers": [3, "Entry"]}	1300	2300
\.


--
-- Data for Name: professional_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professional_requests (id, professional_offer_id, company_offer_id) FROM stdin;
1	1	1
2	2	2
3	3	3
\.


--
-- Data for Name: professionals; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals (id, first_name, last_name, address, user_id, summary, default_offer_id, picture, approved) FROM stdin;
1	John	Ivanov	bul.Skobelev, 24, Sofia, BG	2	10 years of experience in C# ASP.NET development	1	\N	t
2	Michael	Livingston	Ubbo-Emmunslaan str., Amsterdam, NE	3	Experienced Python developer	2	\N	t
3	William	Pique	Buterpark str., London, GBT	4	Junior Java developer	3	\N	f
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.users (id, username, admin, password) FROM stdin;
1	adminuser	t	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
2	testuser1	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
3	testuser2	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
4	testuser3	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
5	testuser4	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
6	testuser5	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
7	testuser6	f	\\x74657374
\.


--
-- Data for Name: web_filters; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.web_filters (id, filter, user_id) FROM stdin;
\.


--
-- Name: comcompany_requests_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.comcompany_requests_id_seq', 1, false);


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.companies_id_seq', 4, false);


--
-- Name: company_offers_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_offers_id_seq', 4, false);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.messages_id_seq', 1, false);


--
-- Name: professional_offers_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professional_offers_id_seq', 4, false);


--
-- Name: professional_requests_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professional_requests_id_seq', 1, false);


--
-- Name: professionals_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professionals_id_seq', 4, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.users_id_seq', 8, false);


--
-- Name: web_filters_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.web_filters_id_seq', 1, false);


--
-- Name: companies pk_company; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies
    ADD CONSTRAINT pk_company PRIMARY KEY (id);


--
-- Name: company_offers pk_company_offers; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT pk_company_offers PRIMARY KEY (id);


--
-- Name: company_requests pk_company_requests; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT pk_company_requests PRIMARY KEY (id);


--
-- Name: config pk_config; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.config
    ADD CONSTRAINT pk_config PRIMARY KEY (lock);


--
-- Name: messages pk_messages; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT pk_messages PRIMARY KEY (id);


--
-- Name: professional_offers pk_professional_offers; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT pk_professional_offers PRIMARY KEY (id);


--
-- Name: professional_requests pk_professional_requests; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT pk_professional_requests PRIMARY KEY (id);


--
-- Name: professionals pk_professionals; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT pk_professionals PRIMARY KEY (id);


--
-- Name: users pk_users; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.users
    ADD CONSTRAINT pk_users PRIMARY KEY (id);


--
-- Name: web_filters pk_web_filters; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.web_filters
    ADD CONSTRAINT pk_web_filters PRIMARY KEY (id);


--
-- Name: companies unq_companies; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies
    ADD CONSTRAINT unq_companies UNIQUE (user_id);


--
-- Name: company_requests unq_company_requests_professional_id; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT unq_company_requests_professional_id UNIQUE (professional_id);


--
-- Name: professional_requests unq_professional_requests_company_offer_id; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT unq_professional_requests_company_offer_id UNIQUE (company_offer_id);


--
-- Name: professionals unq_professionals; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT unq_professionals UNIQUE (user_id);


--
-- Name: users unq_users_username; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.users
    ADD CONSTRAINT unq_users_username UNIQUE (username);


--
-- Name: users check_user_id_admin_not_in_professionals_or_companies; Type: TRIGGER; Schema: jobmatch; Owner: postgres
--

CREATE TRIGGER check_user_id_admin_not_in_professionals_or_companies BEFORE INSERT OR UPDATE ON jobmatch.users FOR EACH ROW EXECUTE FUNCTION jobmatch.check_user_id_admin_not_in_professionals_or_companies();


--
-- Name: companies check_user_id_companies_not_in_professionals; Type: TRIGGER; Schema: jobmatch; Owner: postgres
--

CREATE TRIGGER check_user_id_companies_not_in_professionals BEFORE INSERT OR UPDATE ON jobmatch.companies FOR EACH ROW EXECUTE FUNCTION jobmatch.check_user_id_companies_not_in_professionals();


--
-- Name: professionals check_user_id_professionals_not_in_companies; Type: TRIGGER; Schema: jobmatch; Owner: postgres
--

CREATE TRIGGER check_user_id_professionals_not_in_companies BEFORE INSERT OR UPDATE ON jobmatch.professionals FOR EACH ROW EXECUTE FUNCTION jobmatch.check_user_id_professionals_not_in_companies();


--
-- Name: companies fk_companies_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies
    ADD CONSTRAINT fk_companies_users FOREIGN KEY (user_id) REFERENCES jobmatch.users(id);


--
-- Name: company_offers fk_company_offers_companies; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT fk_company_offers_companies FOREIGN KEY (company_id) REFERENCES jobmatch.companies(id);


--
-- Name: company_offers fk_company_offers_company_requests; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT fk_company_offers_company_requests FOREIGN KEY (chosen_professional_id) REFERENCES jobmatch.company_requests(professional_id);


--
-- Name: company_requests fk_company_requests_company_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT fk_company_requests_company_offers FOREIGN KEY (company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: company_requests fk_company_requests_professional_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT fk_company_requests_professional_offers FOREIGN KEY (professional_offer_id) REFERENCES jobmatch.professional_offers(id);


--
-- Name: company_requests fk_company_requests_professionals; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT fk_company_requests_professionals FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- Name: messages fk_messages_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT fk_messages_users FOREIGN KEY (sender_username) REFERENCES jobmatch.users(username);


--
-- Name: messages fk_messages_users_0; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT fk_messages_users_0 FOREIGN KEY (receiver_username) REFERENCES jobmatch.users(username);


--
-- Name: professional_offers fk_professional_offers_professional_requests; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_offers_professional_requests FOREIGN KEY (chosen_company_offer_id) REFERENCES jobmatch.professional_requests(company_offer_id);


--
-- Name: professional_offers fk_professional_offers_professionals; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_offers_professionals FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- Name: professional_requests fk_professional_requests_company_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT fk_professional_requests_company_offers FOREIGN KEY (company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: professional_requests fk_professional_requests_professional_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT fk_professional_requests_professional_offers FOREIGN KEY (professional_offer_id) REFERENCES jobmatch.professional_offers(id);


--
-- Name: professionals fk_professionals_professional_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT fk_professionals_professional_offers FOREIGN KEY (default_offer_id) REFERENCES jobmatch.professional_offers(id);


--
-- Name: professionals fk_professionals_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT fk_professionals_users FOREIGN KEY (user_id) REFERENCES jobmatch.users(id);


--
-- Name: web_filters fk_web_filters_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.web_filters
    ADD CONSTRAINT fk_web_filters_users FOREIGN KEY (user_id) REFERENCES jobmatch.users(id);


--
-- PostgreSQL database dump complete
--

