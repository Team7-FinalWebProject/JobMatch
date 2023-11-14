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
    name character varying(100) NOT NULL,
    description text DEFAULT ''::text NOT NULL,
    address character varying(100) NOT NULL,
    picture bytea,
    approved boolean DEFAULT false NOT NULL
);


ALTER TABLE jobmatch.companies OWNER TO postgres;

--
-- Name: company_offers; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_offers (
    id integer NOT NULL,
    company_id integer NOT NULL,
    status character varying DEFAULT 'active'::character varying NOT NULL,
    chosen_professional_id integer,
    requirements jsonb,
    min_salary integer DEFAULT 0 NOT NULL,
    max_salary integer DEFAULT 2147483647 NOT NULL
);


ALTER TABLE jobmatch.company_offers OWNER TO postgres;

--
-- Name: company_avatar_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_avatar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.company_avatar_id_seq OWNER TO postgres;

--
-- Name: company_avatar_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.company_avatar_id_seq OWNED BY jobmatch.company_offers.id;


--
-- Name: company_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.company_id_seq OWNER TO postgres;

--
-- Name: company_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.company_id_seq OWNED BY jobmatch.companies.id;


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
-- Name: company_interactions_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.company_interactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.company_interactions_id_seq OWNER TO postgres;

--
-- Name: company_interactions_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.company_interactions_id_seq OWNED BY jobmatch.company_requests.id;


--
-- Name: company_users; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.company_users (
    company_id integer NOT NULL,
    user_id integer NOT NULL,
    admin boolean DEFAULT false NOT NULL,
    approved boolean DEFAULT false NOT NULL
);


ALTER TABLE jobmatch.company_users OWNER TO postgres;

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
    skills jsonb,
    min_salary integer DEFAULT 0 NOT NULL,
    max_salary integer DEFAULT 2147483647 NOT NULL
);


ALTER TABLE jobmatch.professional_offers OWNER TO postgres;

--
-- Name: professional_avatars_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professional_avatars_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professional_avatars_id_seq OWNER TO postgres;

--
-- Name: professional_avatars_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professional_avatars_id_seq OWNED BY jobmatch.professional_offers.id;


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
-- Name: professional_interactions_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.professional_interactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.professional_interactions_id_seq OWNER TO postgres;

--
-- Name: professional_interactions_id_seq; Type: SEQUENCE OWNED BY; Schema: jobmatch; Owner: postgres
--

ALTER SEQUENCE jobmatch.professional_interactions_id_seq OWNED BY jobmatch.professional_requests.id;


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
-- Name: users; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.users (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    admin boolean DEFAULT false NOT NULL,
    approved boolean DEFAULT false NOT NULL,
    password bytea NOT NULL
);


ALTER TABLE jobmatch.users OWNER TO postgres;

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
-- Name: companies id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies ALTER COLUMN id SET DEFAULT nextval('jobmatch.company_id_seq'::regclass);


--
-- Name: company_offers id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers ALTER COLUMN id SET DEFAULT nextval('jobmatch.company_avatar_id_seq'::regclass);


--
-- Name: company_requests id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests ALTER COLUMN id SET DEFAULT nextval('jobmatch.company_interactions_id_seq'::regclass);


--
-- Name: messages id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages ALTER COLUMN id SET DEFAULT nextval('jobmatch.messages_id_seq'::regclass);


--
-- Name: professional_offers id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers ALTER COLUMN id SET DEFAULT nextval('jobmatch.professional_avatars_id_seq'::regclass);


--
-- Name: professional_requests id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests ALTER COLUMN id SET DEFAULT nextval('jobmatch.professional_interactions_id_seq'::regclass);


--
-- Name: professionals id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals ALTER COLUMN id SET DEFAULT nextval('jobmatch.professionals_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.users ALTER COLUMN id SET DEFAULT nextval('jobmatch.users_id_seq'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.companies (id, name, description, address, picture, approved) FROM stdin;
\.


--
-- Data for Name: company_offers; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_offers (id, company_id, status, chosen_professional_id, requirements, min_salary, max_salary) FROM stdin;
\.


--
-- Data for Name: company_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_requests (id, company_offer_id, professional_id, professional_offer_id) FROM stdin;
\.


--
-- Data for Name: company_users; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_users (company_id, user_id, admin, approved) FROM stdin;
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
\.


--
-- Data for Name: professional_requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professional_requests (id, professional_offer_id, company_offer_id) FROM stdin;
\.


--
-- Data for Name: professionals; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals (id, first_name, last_name, address, user_id, summary, default_offer_id, picture, approved) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.users (id, username, admin, approved, password) FROM stdin;
\.


--
-- Name: company_avatar_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_avatar_id_seq', 1, false);


--
-- Name: company_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_id_seq', 1, false);


--
-- Name: company_interactions_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_interactions_id_seq', 1, false);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.messages_id_seq', 1, false);


--
-- Name: professional_avatars_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professional_avatars_id_seq', 1, false);


--
-- Name: professional_interactions_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professional_interactions_id_seq', 1, false);


--
-- Name: professionals_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professionals_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.users_id_seq', 1, false);


--
-- Name: companies pk_company; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.companies
    ADD CONSTRAINT pk_company PRIMARY KEY (id);


--
-- Name: company_offers pk_company_avatar; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT pk_company_avatar PRIMARY KEY (id);


--
-- Name: company_requests pk_company_interactions; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT pk_company_interactions PRIMARY KEY (id);


--
-- Name: messages pk_messages; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages
    ADD CONSTRAINT pk_messages PRIMARY KEY (id);


--
-- Name: professional_offers pk_professional_avatars; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT pk_professional_avatars PRIMARY KEY (id);


--
-- Name: professional_requests pk_professional_interactions; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT pk_professional_interactions PRIMARY KEY (id);


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
-- Name: company_requests unq_company_requests_professional_id; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT unq_company_requests_professional_id UNIQUE (professional_id);


--
-- Name: company_users unq_company_users_user_id; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_users
    ADD CONSTRAINT unq_company_users_user_id UNIQUE (user_id);


--
-- Name: professional_requests unq_professional_requests_company_offer_id; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT unq_professional_requests_company_offer_id UNIQUE (company_offer_id);


--
-- Name: users unq_users_username; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.users
    ADD CONSTRAINT unq_users_username UNIQUE (username);


--
-- Name: company_users fk_company_admins_companies; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_users
    ADD CONSTRAINT fk_company_admins_companies FOREIGN KEY (company_id) REFERENCES jobmatch.companies(id);


--
-- Name: company_users fk_company_admins_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_users
    ADD CONSTRAINT fk_company_admins_users FOREIGN KEY (user_id) REFERENCES jobmatch.users(id);


--
-- Name: company_offers fk_company_avatars_companies; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT fk_company_avatars_companies FOREIGN KEY (company_id) REFERENCES jobmatch.companies(id);


--
-- Name: company_offers fk_company_avatars_company_requests; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT fk_company_avatars_company_requests FOREIGN KEY (chosen_professional_id) REFERENCES jobmatch.company_requests(professional_id);


--
-- Name: company_requests fk_company_interactions_company_avatars; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT fk_company_interactions_company_avatars FOREIGN KEY (company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: company_requests fk_company_requests_professional_avatars; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_requests
    ADD CONSTRAINT fk_company_requests_professional_avatars FOREIGN KEY (professional_offer_id) REFERENCES jobmatch.professional_offers(id);


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
-- Name: professional_offers fk_professional_avatars_professionals; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_avatars_professionals FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- Name: professional_requests fk_professional_interactions_professional_avatars; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT fk_professional_interactions_professional_avatars FOREIGN KEY (professional_offer_id) REFERENCES jobmatch.professional_offers(id);


--
-- Name: professional_offers fk_professional_offers_professional_requests; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_offers_professional_requests FOREIGN KEY (chosen_company_offer_id) REFERENCES jobmatch.professional_requests(company_offer_id);


--
-- Name: professional_requests fk_professional_requests_company_avatars; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_requests
    ADD CONSTRAINT fk_professional_requests_company_avatars FOREIGN KEY (company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: professionals fk_professionals_professional_avatars; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT fk_professionals_professional_avatars FOREIGN KEY (default_offer_id) REFERENCES jobmatch.professional_offers(id);


--
-- Name: professionals fk_professionals_users; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professionals
    ADD CONSTRAINT fk_professionals_users FOREIGN KEY (user_id) REFERENCES jobmatch.users(id);


--
-- PostgreSQL database dump complete
--

