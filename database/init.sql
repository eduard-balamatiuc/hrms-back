--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2024-09-16 16:09:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 24763)
-- Name: appointments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appointments (
    id uuid NOT NULL,
    patient_user_id uuid NOT NULL,
    doctor_user_id uuid NOT NULL,
    start_datetime date NOT NULL,
    end_datetime date,
    comments character varying
);


ALTER TABLE public.appointments OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 24744)
-- Name: doctor_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.doctor_user (
    id uuid NOT NULL,
    "IDNP" character varying(50) NOT NULL,
    name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    mail character varying(50) NOT NULL,
    password character varying(255) NOT NULL,
    location character varying(255) NOT NULL,
    phone integer,
    image_uri character varying
);


ALTER TABLE public.doctor_user OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24751)
-- Name: general_information; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.general_information (
    id uuid NOT NULL,
    patient_user_id uuid NOT NULL,
    height double precision,
    weight double precision,
    blood_type character varying,
    gender character varying,
    date_of_birth date
);


ALTER TABLE public.general_information OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 24737)
-- Name: patient_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient_user (
    id uuid NOT NULL,
    "IDNP" character varying(50) NOT NULL,
    mail character varying(50) NOT NULL,
    password character varying(255) NOT NULL,
    name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    location character varying(255) NOT NULL,
    phone integer,
    image_uri character varying
);


ALTER TABLE public.patient_user OWNER TO postgres;

--
-- TOC entry 4802 (class 0 OID 24763)
-- Dependencies: 218
-- Data for Name: appointments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appointments (id, patient_user_id, doctor_user_id, start_datetime, end_datetime, comments) FROM stdin;
\.


--
-- TOC entry 4800 (class 0 OID 24744)
-- Dependencies: 216
-- Data for Name: doctor_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.doctor_user (id, "IDNP", name, surname, mail, password, location, phone, image_uri) FROM stdin;
\.


--
-- TOC entry 4801 (class 0 OID 24751)
-- Dependencies: 217
-- Data for Name: general_information; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.general_information (id, patient_user_id, height, weight, blood_type, gender, date_of_birth) FROM stdin;
\.


--
-- TOC entry 4799 (class 0 OID 24737)
-- Dependencies: 215
-- Data for Name: patient_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient_user (id, "IDNP", mail, password, name, surname, location, phone, image_uri) FROM stdin;
\.


--
-- TOC entry 4652 (class 2606 OID 24769)
-- Name: appointments appointments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_pkey PRIMARY KEY (id);


--
-- TOC entry 4648 (class 2606 OID 24750)
-- Name: doctor_user doctor_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor_user
    ADD CONSTRAINT doctor_user_pkey PRIMARY KEY (id);


--
-- TOC entry 4650 (class 2606 OID 24757)
-- Name: general_information general_information_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.general_information
    ADD CONSTRAINT general_information_pkey PRIMARY KEY (id);


--
-- TOC entry 4646 (class 2606 OID 24743)
-- Name: patient_user patient_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_user
    ADD CONSTRAINT patient_user_pkey PRIMARY KEY (id);


--
-- TOC entry 4654 (class 2606 OID 24775)
-- Name: appointments doctor_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT doctor_user_id FOREIGN KEY (doctor_user_id) REFERENCES public.doctor_user(id);


--
-- TOC entry 4653 (class 2606 OID 24758)
-- Name: general_information patient_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.general_information
    ADD CONSTRAINT patient_user_id FOREIGN KEY (patient_user_id) REFERENCES public.patient_user(id);


--
-- TOC entry 4655 (class 2606 OID 24770)
-- Name: appointments patient_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT patient_user_id FOREIGN KEY (patient_user_id) REFERENCES public.patient_user(id);

ALTER TABLE public.doctor_user
ALTER COLUMN phone TYPE bigint;

ALTER TABLE public.patient_user
ALTER COLUMN phone TYPE bigint;


-- Completed on 2024-09-16 16:09:21

--
-- PostgreSQL database dump complete
--

