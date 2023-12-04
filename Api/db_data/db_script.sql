--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Ubuntu 15.1-1.pgdg20.04+1)
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
-- Name: companies; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.companies (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text DEFAULT ''::text NOT NULL,
    address character varying(100) NOT NULL,
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
    chosen_professional_offer_id integer,
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
    baseline_skills jsonb DEFAULT '{"French": null, "English": null, "Computers": null}'::jsonb NOT NULL,
    approved_skills jsonb DEFAULT '{}'::jsonb NOT NULL,
    pending_approval_skills jsonb DEFAULT '{}'::jsonb NOT NULL,
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
    approved boolean DEFAULT false NOT NULL,
    status character varying DEFAULT 'active'::character varying NOT NULL,
    CONSTRAINT cns_professionals CHECK (((status)::text = ANY (ARRAY[('active'::character varying)::text, ('busy'::character varying)::text])))
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
-- Name: requests_id_seq; Type: SEQUENCE; Schema: jobmatch; Owner: postgres
--

CREATE SEQUENCE jobmatch.requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE jobmatch.requests_id_seq OWNER TO postgres;

--
-- Name: requests; Type: TABLE; Schema: jobmatch; Owner: postgres
--

CREATE TABLE jobmatch.requests (
    id integer DEFAULT nextval('jobmatch.requests_id_seq'::regclass) NOT NULL,
    professional_offer_id integer NOT NULL,
    company_offer_id integer NOT NULL,
    request_from character varying NOT NULL,
    CONSTRAINT cns_requests CHECK (((request_from)::text = ANY (ARRAY[('company'::character varying)::text, ('professional'::character varying)::text])))
);


ALTER TABLE jobmatch.requests OWNER TO postgres;

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
-- Name: messages id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.messages ALTER COLUMN id SET DEFAULT nextval('jobmatch.messages_id_seq'::regclass);


--
-- Name: professional_offers id; Type: DEFAULT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers ALTER COLUMN id SET DEFAULT nextval('jobmatch.professional_offers_id_seq'::regclass);


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

COPY jobmatch.companies (id, name, description, address, approved, user_id) FROM stdin;
1	Pepsi	We make the fizzy drink	Los Angeles, California	t	5
2	Steam	We provide video games	Los Angeles, California	t	6
3	Avid	We provide audio grear	New York, USA	t	7
4	LinguaTech	Language solutions for global communication	Bucharest, Romania	f	8
5	LinguaTech	We specialize in language solutions and linguistic expertise.	Bucharest, Romania	f	9
6	LinguaExpert	Hello! I'm a helpful linguistic expert.	Bucharest, Romania	f	10
7	AceTech Solutions	Providing innovative tech solutions for businesses worldwide.	Lviv, Ukraine	t	11
8	Swift Globe	Empowering global logistics	Sofia, Bulgaria	t	12
9	AgroAlba	Empowering agricultural growth	Tirana, Albania	t	18
10	DatalakeUS	We are a leading data storage company, providing secure and scalable solutions for businesses of all sizes.	Miami, USA	t	19
11	GlobalTech Solutions	Providing innovative technology solutions for businesses worldwide.	Eastern Europe, address upon request	f	22
12	InnovativeStorm	Pioneering solutions for businesses worldwide.	Bucharest, Romania	f	27
13	GlobalTech Solutions	Innovative technology company providing cutting-edge solutions for businesses worldwide	Bucharest, Romania	f	28
14	Globit	We provide innovative solutions for global logistics.	Bucharest, Romania	f	31
15	Brightstar Solutions	Innovative IT solutions for businesses worldwide	Kyiv, Ukraine	f	32
16	TechDyno	Empowering digital transformations	Krakow, Poland	f	33
17	AgileGenius Consulting	Driving agility and innovation in organizations	Bucharest, Romania	f	34
18	TechGenix	Leading provider of innovative tech solutions	Bucharest, Romania	f	35
19	VitaSolutions	Revolutionizing health and wellness industry	Krakow, Poland	f	36
20	StyleMerge	Bringing fashion trends together	Kyiv, Ukraine	f	37
21	TradeGenius	Empowering global trade	Sofia, Bulgaria	f	38
22	YiSangCo	We blend modern architecture with traditional design principles, creating spaces that inspire and endure.	Seoul, South Korea	f	43
23	SangWorks	Innovative architectural solutions fueled by creativity and a passion for sustainable design.	Warsaw, Poland	f	44
24	YiSangDesign	Crafting spaces that harmonize with nature, embodying simplicity and elegance.	Bucharest, Romania	f	45
25	SangiTech	Pioneering the integration of technology and architecture to shape the cities of tomorrow.	Tbilisi, Georgia	f	46
26	YiSangConstruct	Building the future through precision engineering and timeless design.	Kyiv, Ukraine	f	47
27	SangArch	Elevating urban landscapes through avant-garde architectural concepts and practical solutions.	Moscow, Russia	f	48
28	YiSangInnovate	Where innovation meets aesthetics, redefining architectural excellence one project at a time.	Sofia, Bulgaria	f	49
29	SangDesignLab	A laboratory of creativity and functionality, shaping architectural marvels with a human touch.	Belgrade, Serbia	f	50
30	YiSangStudio	A fusion of artistry and engineering, producing architectural masterpieces that stand the test of time.	Minsk, Belarus	f	51
31	SangVision	Envisioning architectural wonders that celebrate culture, sustainability, and community.	Riga, Latvia	f	52
32	YiSangEnvision	Empowering communities through visionary architectural solutions that honor heritage and progress.	Vilnius, Lithuania	f	53
33	SangCraft	Crafting architectural excellence with a blend of tradition, innovation, and unwavering dedication.	Prague, Czech Republic	f	54
34	YiSangForge	Forging a new era of architectural design, where creativity and functionality intertwine seamlessly.	Budapest, Hungary	f	55
35	SangForm	Sculpting architectural forms that resonate with the soul and transform skylines into poetry.	Tallinn, Estonia	f	56
36	YiSangVista	Offering a panoramic view of architectural mastery, where every detail reflects elegance and purpose.	Bratislava, Slovakia	f	57
37	SangHarmony	Harmonizing architecture with the pulse of nature and the rhythm of urban life, creating balanced environments.	Ljubljana, Slovenia	f	58
38	YiSangFormulate	Formulating architectural visions that blend functionality, sustainability, and cultural inspiration.	Murmansk, Russia	f	59
39	SangCraftsmen	A guild of architectural craftsmen dedicated to preserving heritage while embracing modernity.	Lviv, Ukraine	f	60
40	YiSangSculpt	Sculpting architectural spaces that mold seamlessly with the environment, transcending mere structures.	Cluj-Napoca, Romania	f	61
41	SangCanvas	Painting architectural canvases that resonate with the spirit of the past and the promise of the future.	Bucharest, Romania	f	62
\.


--
-- Data for Name: company_offers; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.company_offers (id, company_id, status, chosen_professional_offer_id, requirements, min_salary, max_salary) FROM stdin;
1	1	active	\N	{"English": [7, "Native"], "Computers": [10, "Master"]}	3000	8000
2	2	active	\N	{"English": [5, "Advanced"], "Computers": [5, "Advanced"]}	2500	5500
3	3	active	\N	{"English": [4, "Advanced"], "Computers": [3, "Entry"]}	1500	2500
4	8	active	\N	{"SQL": [6, "Database management skill"], "Java": [7, "Experienced developer"], "Spring Framework": [5, "Intermediate level"], "Team Collaboration": [8, "Excellent team player"]}	3000	5000
5	7	active	\N	{"Java": [7, "Experienced developer"], "Communication": [8, "Effective communicator"], "Problem-solving": [9, "Analytical thinker"], "Spring Framework": [6, "Skilled user"]}	2500	3500
6	6	active	\N	{"Java": [7, "Intermediate developer"], "HTML/CSS": [5, "Experienced"], "JavaScript": [8, "Senior developer"], "Communication": [9, "Excellent communicator"]}	2500	3500
7	9	active	\N	{"Java": [7, "Experienced developer"], "Spring Framework": [6, "Intermediate level"], "Agile Methodology": [5, "Familiar with Agile practices"], "Communication Skills": [8, "Excellent verbal and written communication"]}	3000	4500
8	9	active	\N	{"AWS": [4, "Familiar with cloud services"], "React": [6, "Proficient in building UI components"], "Node.js": [5, "Ability to work on server-side applications"], "JavaScript": [7, "Experienced front-end developer"], "Agile Methodology": [6, "Experience working in Agile teams"]}	4000	6000
9	9	active	\N	{"Microsoft Excel": [4, "Proficiency in basic Excel functions"], "Time Management": [2, "Ability to prioritize tasks effectively"], "Customer Service": [3, "Basic customer interaction skills"]}	1800	2500
10	11	active	\N	{"SQL": [5, "Skilled in database management"], "Java": [7, "Experienced developer"], "Teamwork": [8, "Collaborative team player"], "Spring Boot": [6, "Proficient"]}	2500	3500
11	9	active	\N	{"CSS": [2, "Basic understanding of CSS"], "HTML": [3, "Proficient in HTML"], "English": [5, "Good communication skills in English"], "JavaScript": [4, "Experienced in JavaScript"]}	1800	2500
12	12	active	\N	{"SQL": [5, "Intermediate"], "Java": [7, "Experienced developer"], "HTML/CSS": [4, "Familiar"], "Team Player": [9, "Collaborative and communicative"], "Problem-Solving": [8, "Analytical and creative"], "Spring Framework": [6, "Proficient"]}	2500	3500
13	17	active	\N	{"React": [6, "Proficient in building user interfaces"], "Node.js": [5, "Familiar with backend development"], "JavaScript": [7, "Experienced frontend developer"]}	2500	3500
14	17	active	\N	{"Java": [8, "Senior software engineer"], "Spring Boot": [7, "Expert in building scalable applications"], "Microservices": [6, "Experience in developing microservices architecture"]}	3000	4500
15	17	active	\N	{"Python": [9, "Lead data scientist"], "TensorFlow": [7, "Proficient in building ML models"], "Machine Learning": [8, "Strong background in ML algorithms"]}	4000	6000
16	17	active	\N	{"AWS": [5, "Experience with cloud services"], "Java": [7, "Experienced in backend development"], "React": [6, "Proficient in building interactive user interfaces"], "Communication": [8, "Excellent verbal and written communication skills"]}	2500	3500
\.


--
-- Data for Name: config; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.config (lock, static_skills, min_level, max_level, baseline_skills, approved_skills, pending_approval_skills) FROM stdin;
X	f	0	10	{"R": null, "Go": null, "AWS": null, "Ada": null, "C++": null, "COq": null, "CSS": null, "IOT": null, "PHP": null, "SEO": null, "SQL": null, "HTML": null, "Java": null, "LISP": null, "Perl": null, "Ruby": null, "SaaS": null, "COBOL": null, "Julia": null, "Scala": null, "Scrum": null, "Swift": null, "DevOps": null, "Docker": null, "Elixir": null, "Erlang": null, "French": null, "Kotlin": null, "MATLAB": null, "Prolog": null, "Python": null, "Scheme": null, "Vue.js": null, "Angular": null, "Clojure": null, "English": null, "MongoDB": null, "Node.js": null, "Tax Law": null, "Robotics": null, "Teamwork": null, "Computers": null, "Hydrology": null, "UX Design": null, "Aquaponics": null, "Blockchain": null, "Creativity": null, "E-commerce": null, "JavaScript": null, "Kubernetes": null, "Leadership": null, "Resilience": null, "TypeScript": null, "UI Testing": null, "3D Printing": null, "A/B Testing": null, "Agritourism": null, "Aquaculture": null, "Bookkeeping": null, "Copywriting": null, "Data Mining": null, "Hydroponics": null, "Negotiation": null, "Objective-C": null, "Photography": null, "UX Research": null, "Adaptability": null, "Agroforestry": null, "Food Science": null, "React Native": null, "UI/UX Design": null, "UX/UI Design": null, "Web Security": null, "Agrochemicals": null, "Biostatistics": null, "Culinary Arts": null, "Cybersecurity": null, "Data Analysis": null, "Field Mapping": null, "Legal Writing": null, "Multi-tasking": null, "Python Django": null, "Ruby on Rails": null, "Soil Analysis": null, "User Research": null, "Video Editing": null, "Web Analytics": null, "Bioinformatics": null, "Cloud Security": null, "Event Planning": null, "Graphic Design": null, "Legal Research": null, "Medical Coding": null, "Plant Breeding": null, "RF Engineering": null, "Salesforce CRM": null, "Speech Therapy": null, "Clinical Trials": null, "Cloud Computing": null, "Content Writing": null, "Crop Management": null, "Decision Making": null, "Design Thinking": null, "Disaster Relief": null, "Drip Irrigation": null, "Ethical Hacking": null, "Event Marketing": null, "Fashion Styling": null, "Impact Analysis": null, "Interior Design": null, "Market Research": null, "Medical Billing": null, "Microsoft Azure": null, "Motion Graphics": null, "Organic Farming": null, "Pest Management": null, "Pharmacotherapy": null, "Problem Solving": null, "Public Speaking": null, "Risk Assessment": null, "Risk Management": null, "SEO Copywriting": null, "Shell Scripting": null, "Time Management": null, "Web Development": null, "Content Strategy": null, "Customer Service": null, "Drug Development": null, "Embedded Systems": null, "Fitness Training": null, "Game Development": null, "Humanitarian Aid": null, "Legal Compliance": null, "Machine Learning": null, "Mobile Marketing": null, "Music Production": null, "Network Security": null, "Pharmacogenomics": null, "Pharmacokinetics": null, "Project Planning": null, "Public Relations": null, "SEO Optimization": null, "Water Management": null, "AR/VR Development": null, "Agile Methodology": null, "Assembly Language": null, "Branding Strategy": null, "Change Management": null, "Chemical Analysis": null, "Civil Engineering": null, "Clinical Research": null, "Content Marketing": null, "Crisis Management": null, "Critical Thinking": null, "Database Security": null, "Digital Marketing": null, "Food Microbiology": null, "Foreign Languages": null, "Industrial Design": null, "Inventory Control": null, "Petroleum Geology": null, "Pharmacoeconomics": null, "Pharmacovigilance": null, "Quality Assurance": null, "Soil Conservation": null, "Talent Management": null, "Teaching/Tutoring": null, "Technical Writing": null, "Zoology Knowledge": null, "Big Data Analytics": null, "Biomedical Science": null, "Biopharmaceuticals": null, "Cloud Architecture": null, "Community Outreach": null, "Dance Choreography": null, "Data Visualization": null, "Event Coordination": null, "Financial Analysis": null, "Financial Modeling": null, "Financial Planning": null, "Industrial Hygiene": null, "Investment Banking": null, "Irrigation Systems": null, "Livestock Handling": null, "Marine Engineering": null, "Marketing Strategy": null, "Paralegal Services": null, "Petroleum Refining": null, "Product Management": null, "Project Management": null, "Regulatory Affairs": null, "Strategic Planning": null, "Analytical Thinking": null, "Attention to Detail": null, "Conflict Resolution": null, "Database Management": null, "E-commerce Strategy": null, "Genetic Engineering": null, "Livestock Husbandry": null, "Livestock Nutrition": null, "Maritime Navigation": null, "Musical Composition": null, "Network Engineering": null, "Nuclear Engineering": null, "Presentation Skills": null, "Architectural Design": null, "Business Development": null, "Chemical Engineering": null, "Communication Skills": null, "Computer Engineering": null, "Contract Negotiation": null, "Genetic Modification": null, "Hardware Development": null, "Information Security": null, "Interpersonal Skills": null, "Livestock Management": null, "Network Architecture": null, "Pesticide Management": null, "Pharmaceutical Sales": null, "Public Health Policy": null, "Remote Collaboration": null, "Retail Merchandising": null, "Robotics Engineering": null, "Social Work Advocacy": null, "Software Development": null, "Statistical Analysis": null, "Statistical Modeling": null, "Aerospace Engineering": null, "Blockchain Technology": null, "Business Intelligence": null, "Clinical Pharmacology": null, "Database Optimization": null, "E-commerce Management": null, "Facilities Management": null, "Fashion Merchandising": null, "Google Cloud Platform": null, "Greenhouse Management": null, "IT Project Management": null, "Industrial Automation": null, "Irrigation Technology": null, "Laboratory Techniques": null, "Market Trend Analysis": null, "Materials Engineering": null, "Medical Transcription": null, "Nonprofit Fundraising": null, "Operations Management": null, "Organic Certification": null, "Petroleum Engineering": null, "Precision Agriculture": null, "Regulatory Compliance": null, "Reservoir Engineering": null, "System Administration": null, "User Interface Design": null, "Agricultural Economics": null, "Automotive Engineering": null, "Biomedical Engineering": null, "Bioprocess Engineering": null, "Biotechnology Research": null, "Blockchain Development": null, "Cryptocurrency Trading": null, "Educational Psychology": null, "Electrical Engineering": null, "Emotional Intelligence": null, "Fertilizer Application": null, "Food Safety Management": null, "Geological Engineering": null, "Industrial Engineering": null, "Leadership Development": null, "Mechanical Engineering": null, "Mobile App Development": null, "Network Administration": null, "Public Policy Analysis": null, "Stakeholder Management": null, "Wireless Communication": null, "Artificial Intelligence": null, "Crowdfunding Management": null, "Data Privacy Compliance": null, "Database Administration": null, "Food Safety Regulations": null, "International Trade Law": null, "Social Media Management": null, "Supply Chain Management": null, "Sustainable Agriculture": null, "User Experience Testing": null, "Biomolecular Engineering": null, "Clinical Data Management": null, "Corporate Communications": null, "Corporate Sustainability": null, "Creative Problem Solving": null, "Cybersecurity Consulting": null, "Geotechnical Engineering": null, "Market Research Analysis": null, "Mental Health Counseling": null, "Mergers and Acquisitions": null, "Pharmaceutical Chemistry": null, "Pharmaceutical Marketing": null, "Pharmaceutical Packaging": null, "Pharmacokinetic Modeling": null, "Social Media Advertising": null, "Sustainability Reporting": null, "Sustainable Architecture": null, "Transportation Logistics": null, "Environmental Engineering": null, "Financial Risk Management": null, "Gaming Industry Knowledge": null, "Healthcare Administration": null, "Organizational Psychology": null, "Pharmacovigilance Systems": null, "Salesforce Administration": null, "Solar Energy Installation": null, "Supply Chain Optimization": null, "Farm Equipment Maintenance": null, "Pharmaceutical Formulation": null, "Public Relations Campaigns": null, "Control Systems Engineering": null, "Natural Language Processing": null, "Pharmaceutical Distribution": null, "Renewable Energy Technology": null, "Virtual Reality Development": null, "Business Continuity Planning": null, "Business Process Improvement": null, "Environmental Sustainability": null, "Foreign Language Proficiency": null, "IT Infrastructure Management": null, "Laboratory Technician Skills": null, "Pharmaceutical Manufacturing": null, "Renewable Energy Engineering": null, "Political Campaign Management": null, "Business Intelligence Analysis": null, "Clinical Research Coordination": null, "Telecommunications Engineering": null, "Real Estate Investment Analysis": null, "Diversity and Inclusion Training": null, "Pharmaceutical Quality Assurance": null, "Search Engine Optimization (SEO)": null, "Information Technology Management": null, "Pharmaceutical Law and Compliance": null, "International Business Negotiation": null, "Manufacturing Process Optimization": null, "Pharmaceutical Compliance Auditing": null, "Pharmaceutical Process Optimization": null, "Customer Relationship Management (CRM)": null, "Pharmaceutical Formulation Development": null, "Pharmaceutical Research and Development": null, "Human Resources Information Systems (HRIS)": null}	{}	{}
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
4	6	An experienced data scientist with a passion for machine learning and predictive modeling.	\N	active	{"R": [7, "Proficient"], "SQL": [7, "Proficient"], "Python": [9, "Expert"], "Statistics": [8, "Advanced"], "Data Analysis": [9, "Expert"], "Machine Learning": [8, "Advanced"], "Big Data Technologies": [7, "Proficient"]}	5000	7000
5	5	An experienced web developer with a passion for front-end development.	\N	active	{"CSS": [7, "Senior"], "HTML": [9, "Expert"], "React": [6, "Experienced"], "JavaScript": [8, "Advanced"], "UI/UX Design": [5, "Good knowledge"]}	3500	5000
6	4	A retired tennis champion with a wealth of experience and a passion for coaching and sports management.	\N	active	{"Tennis": [10, "Expert"], "English": [8, "Fluent"], "Spanish": [10, "Native"], "Coaching": [8, "Experienced"], "Leadership": [9, "Inspiring"], "Sports Management": [7, "Skilled"]}	4000	6000
7	6	A seasoned marketing strategist with a passion for creating compelling brand stories.	\N	active	{"Copywriting": [7, "Advanced"], "Market Research": [8, "Senior"], "Public Speaking": [6, "Intermediate"], "Content Creation": [8, "Senior"], "Digital Marketing": [9, "Expert"], "Social Media Management": [7, "Advanced"]}	4000	6000
8	6	A motivated marketing specialist with a passion for digital media and brand management.	\N	active	{"Copywriting": [4, "Skilled"], "Content Creation": [3, "Experienced"], "Google Analytics": [3, "Familiar"], "Social Media Marketing": [4, "Proficient"]}	2500	3500
9	9	A creative graphic designer with a passion for clean and modern design.	\N	active	{"Typography": [7, "Advanced"], "Illustration": [6, "Experienced"], "UI/UX Design": [8, "Senior"], "Adobe Creative Suite": [9, "Expert"]}	2500	4000
10	6	An experienced digital marketing specialist with a passion for content creation and social media management.	\N	active	{"SEO": [4, "Proficient"], "Content Writing": [3, "Intermediate"], "Google Analytics": [3, "Intermediate"], "Social Media Management": [4, "Proficient"]}	2500	3500
11	12	An experienced data scientist with a passion for machine learning and predictive analytics.	\N	active	{"R": [7, "Proficient"], "SQL": [7, "Proficient"], "Python": [9, "Expert"], "Communication": [9, "Excellent"], "Data Analysis": [9, "Expert"], "Machine Learning": [8, "Advanced"], "Statistical Modeling": [8, "Advanced"]}	5000	7000
12	17	A creative graphic designer with a strong eye for detail.	\N	active	{"Typography": [7, "Proficient"], "Illustrator": [8, "Advanced"], "Adobe Photoshop": [9, "Expert"]}	2500	3500
13	17	An experienced project manager with a proven track record of delivering successful results.	\N	active	{"Agile Methodology": [7, "Proficient"], "Project Management": [9, "Expert"], "Stakeholder Management": [8, "Advanced"]}	4000	6000
14	17	A skilled full-stack developer with expertise in building scalable web applications.	\N	active	{"Node.js": [7, "Proficient"], "React.js": [8, "Advanced"], "JavaScript": [9, "Expert"]}	3500	5000
15	17	Experienced software developer with a passion for creating innovative web applications.	\N	active	{"SQL": [6, "Advanced"], "React": [8, "Advanced"], "Node.js": [7, "Proficient"], "HTML/CSS": [7, "Proficient"], "JavaScript": [9, "Expert"]}	5000	7000
\.


--
-- Data for Name: professionals; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.professionals (id, first_name, last_name, address, user_id, summary, default_offer_id, approved, status) FROM stdin;
1	John	Ivanov	bul.Skobelev, 24, Sofia, BG	2	10 years of experience in C# ASP.NET development	1	t	active
2	Michael	Livingston	Ubbo-Emmunslaan str., Amsterdam, NE	3	Experienced Python developer	2	t	active
3	William	Pique	Buterpark str., London, GBT	4	Junior Java developer	3	f	active
4	Lena	Kovic	Bratislava, Slovakia	13	Experienced professional seeking new opportunities in the tech industry.	\N	t	active
5	Max	Olovsky	Krakow, Poland	14	Experienced professional with a background in software development and project management. Skilled in leading cross-functional teams and driving successful project outcomes. Seeking new opportunities in the IT industry.	\N	t	active
6	Erik	Mikhaylov	Sofia, Bulgaria	17	Experienced professional seeking new opportunities in the finance industry.	\N	t	active
7	Asda	Dad	Eastern Europe	20	Experienced professional seeking new opportunities in the job market.	\N	f	active
8	Lila	Petrov	Sofia, Bulgaria	21	Creative and passionate junior art graduate seeking opportunities in the art and design industry.	\N	f	active
9	Natalia	Dmitrov	Lviv, Ukraine	23	Experienced professional seeking new opportunities in project management.	\N	f	active
10	Lana	Mation	Warsaw, Poland	24	Just graduated in chemistry with a passion for 3D animation. Seeking opportunities to apply chemical knowledge in creative projects.	\N	f	active
11	Emil	Kozlov	Lviv, Ukraine	25	Experienced professional with expertise in project management and IT. Proven track record of delivering complex projects on time and within budget.	\N	f	active
12	Lena	Kov	Krakow, Poland	26	Experienced professional seeking new opportunities in the technology industry.	\N	f	active
13	Adam	Kovacs	Budapest, Hungary	30	Experienced marketing professional with a strong track record of driving successful campaigns and increasing brand visibility.	\N	f	active
14	Natalie	Kovalenko	Kyiv, Ukraine	39	Experienced software engineer with expertise in full-stack development and project management.	\N	f	active
15	Daniela	Stoica	Bucharest, Romania	40	Dedicated medical professional with specialization in neurology and research experience in pharmaceutical industry.	\N	f	active
16	Miroslav	Petrović	Belgrade, Serbia	41	Seasoned financial professional with extensive knowledge in investment banking and risk analysis.	\N	f	active
17	Jennica	Tsvetkova	Sofia, Bulgaria	42	Experienced professional with a background in finance and marketing. Skilled in data analysis and strategic planning. Seeking new opportunities in the Eastern European market.	\N	f	active
18	Aiko	Nakamura	Tokyo, Japan	63	Experienced architect specialized in sustainable design.	\N	f	active
19	Rina	Sato	Osaka, Japan	64	Passionate about creating innovative and functional architectural designs.	\N	f	active
20	Takumi	Yamamoto	Kyoto, Japan	65	Skilled in project management and construction supervision for large-scale developments.	\N	f	active
21	Sakura	Tanaka	Seoul, South Korea	66	Expertise in interior architecture and spatial design for commercial spaces.	\N	f	active
22	Kai	Chen	Shanghai, China	67	Specializing in urban planning and sustainable development strategies.	\N	f	active
\.


--
-- Data for Name: requests; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.requests (id, professional_offer_id, company_offer_id, request_from) FROM stdin;
1	1	1	company
2	2	2	company
3	3	3	professional
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
54	sangcraft	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
8	linguisticpro	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
9	linguisticexpert	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
10	linguisticexp	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
11	ace_solutions	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
12	swiftglobe	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
13	projobseeker	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
14	maxwell23	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
17	projobseeker87	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
18	agroalba	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
19	datalakeUSA	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
20	asdadadad	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
7	testuser6	f	\\x74657374
21	artgrad21	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
22	globalTechSol	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
23	projobhunter	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
24	chem3D	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
25	pro_jobhunt123	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
26	projobseeker83	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
27	innostorm	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
28	globaltech	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
30	adamsmith87	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
31	globoff	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
32	brightstar	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
33	techdyno	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
34	agilegenius	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
35	techsavy	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
36	healthinno	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
37	fashify	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
38	TradeGenius	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
39	techpro_87	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
40	medpro_dani	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
41	finpro_miro	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
42	jenny007	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
43	yisangco	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
44	sangworks	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
45	yisangdesign	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
46	sangitecture	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
47	yisangconstruct	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
48	sangarch	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
49	yisanginnovate	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
50	sangdesignlab	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
51	yisangstudio	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
52	sangvision	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
53	yisangenvision	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
55	yisangforge	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
56	sangform	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
57	yisangvista	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
58	sangharmony	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
59	yisangformulate	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
60	sangcraftsmen	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
61	yisangsculpt	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
62	sangcanvas	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
63	archasia1	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
64	designer123	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
65	buildingpro	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
66	interiorarch	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
67	urbanplanner	f	\\x34303161653462353130636139313635316364626334613731343039323261643235363130356438346565646233346334326635623137343633613865393863
\.


--
-- Data for Name: web_filters; Type: TABLE DATA; Schema: jobmatch; Owner: postgres
--

COPY jobmatch.web_filters (id, filter, user_id) FROM stdin;
\.


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.companies_id_seq', 41, true);


--
-- Name: company_offers_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.company_offers_id_seq', 16, true);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.messages_id_seq', 1, false);


--
-- Name: professional_offers_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professional_offers_id_seq', 15, true);


--
-- Name: professionals_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.professionals_id_seq', 22, true);


--
-- Name: requests_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.requests_id_seq', 4, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: jobmatch; Owner: postgres
--

SELECT pg_catalog.setval('jobmatch.users_id_seq', 67, true);


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
-- Name: requests pk_professional_requests; Type: CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.requests
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
-- Name: unq_requests; Type: INDEX; Schema: jobmatch; Owner: postgres
--

CREATE UNIQUE INDEX unq_requests ON jobmatch.requests USING btree (professional_offer_id, company_offer_id);


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
-- Name: company_offers fk_company_offers_professional_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.company_offers
    ADD CONSTRAINT fk_company_offers_professional_offers FOREIGN KEY (chosen_professional_offer_id) REFERENCES jobmatch.professional_offers(id);


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
-- Name: professional_offers fk_professional_offers_company_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_offers_company_offers FOREIGN KEY (chosen_company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: professional_offers fk_professional_offers_professionals; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.professional_offers
    ADD CONSTRAINT fk_professional_offers_professionals FOREIGN KEY (professional_id) REFERENCES jobmatch.professionals(id);


--
-- Name: requests fk_professional_requests_company_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.requests
    ADD CONSTRAINT fk_professional_requests_company_offers FOREIGN KEY (company_offer_id) REFERENCES jobmatch.company_offers(id);


--
-- Name: requests fk_professional_requests_professional_offers; Type: FK CONSTRAINT; Schema: jobmatch; Owner: postgres
--

ALTER TABLE ONLY jobmatch.requests
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

