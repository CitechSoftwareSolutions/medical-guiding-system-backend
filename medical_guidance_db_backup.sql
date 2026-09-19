--
-- PostgreSQL database dump
--

\restrict aO7zepQLlDclDRyao6GbT3b4F73xAYhlFbSPm5skbKCvLI8w5g6SrljYKRDJJje

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.user_roles DROP CONSTRAINT IF EXISTS user_roles_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.user_roles DROP CONSTRAINT IF EXISTS user_roles_role_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_subscriptions DROP CONSTRAINT IF EXISTS student_subscriptions_student_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_subscriptions DROP CONSTRAINT IF EXISTS student_subscriptions_plan_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_subscriptions DROP CONSTRAINT IF EXISTS student_subscriptions_payment_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_profiles DROP CONSTRAINT IF EXISTS student_profiles_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_documents DROP CONSTRAINT IF EXISTS student_documents_student_id_fkey;
ALTER TABLE IF EXISTS ONLY public.student_documents DROP CONSTRAINT IF EXISTS student_documents_document_id_fkey;
ALTER TABLE IF EXISTS ONLY public.role_permissions DROP CONSTRAINT IF EXISTS role_permissions_role_id_fkey;
ALTER TABLE IF EXISTS ONLY public.role_permissions DROP CONSTRAINT IF EXISTS role_permissions_permission_id_fkey;
ALTER TABLE IF EXISTS ONLY public.plans DROP CONSTRAINT IF EXISTS plans_doctor_id_fkey;
ALTER TABLE IF EXISTS ONLY public.payments DROP CONSTRAINT IF EXISTS payments_student_id_fkey;
ALTER TABLE IF EXISTS ONLY public.payments DROP CONSTRAINT IF EXISTS payments_plan_id_fkey;
ALTER TABLE IF EXISTS ONLY public.notifications DROP CONSTRAINT IF EXISTS notifications_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.documents DROP CONSTRAINT IF EXISTS documents_doctor_id_fkey;
ALTER TABLE IF EXISTS ONLY public.documents DROP CONSTRAINT IF EXISTS documents_category_id_fkey;
ALTER TABLE IF EXISTS ONLY public.doctor_profiles DROP CONSTRAINT IF EXISTS doctor_profiles_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.chat_sessions DROP CONSTRAINT IF EXISTS chat_sessions_student_id_fkey;
ALTER TABLE IF EXISTS ONLY public.chat_messages DROP CONSTRAINT IF EXISTS chat_messages_session_id_fkey;
ALTER TABLE IF EXISTS ONLY public.audit_logs DROP CONSTRAINT IF EXISTS audit_logs_user_id_fkey;
DROP INDEX IF EXISTS public.ix_users_email;
DROP INDEX IF EXISTS public.ix_student_subscriptions_student_id;
DROP INDEX IF EXISTS public.ix_student_subscriptions_plan_id;
DROP INDEX IF EXISTS public.ix_student_subscriptions_payment_id;
DROP INDEX IF EXISTS public.ix_student_profiles_user_id;
DROP INDEX IF EXISTS public.ix_student_documents_student_id;
DROP INDEX IF EXISTS public.ix_student_documents_document_id;
DROP INDEX IF EXISTS public.ix_roles_name;
DROP INDEX IF EXISTS public.ix_plans_name;
DROP INDEX IF EXISTS public.ix_plans_doctor_id;
DROP INDEX IF EXISTS public.ix_permissions_name;
DROP INDEX IF EXISTS public.ix_payments_transaction_id;
DROP INDEX IF EXISTS public.ix_payments_student_id;
DROP INDEX IF EXISTS public.ix_payments_plan_id;
DROP INDEX IF EXISTS public.ix_notifications_user_id;
DROP INDEX IF EXISTS public.ix_navigation_items_target_role;
DROP INDEX IF EXISTS public.ix_navigation_items_menu_type;
DROP INDEX IF EXISTS public.ix_documents_title;
DROP INDEX IF EXISTS public.ix_documents_doctor_id;
DROP INDEX IF EXISTS public.ix_documents_category_id;
DROP INDEX IF EXISTS public.ix_doctor_profiles_user_id;
DROP INDEX IF EXISTS public.ix_chat_sessions_student_id;
DROP INDEX IF EXISTS public.ix_chat_messages_session_id;
DROP INDEX IF EXISTS public.ix_categories_name;
DROP INDEX IF EXISTS public.ix_audit_logs_user_id;
DROP INDEX IF EXISTS public.ix_audit_logs_entity;
DROP INDEX IF EXISTS public.ix_audit_logs_action;
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS users_pkey;
ALTER TABLE IF EXISTS ONLY public.user_roles DROP CONSTRAINT IF EXISTS user_roles_pkey;
ALTER TABLE IF EXISTS ONLY public.user_roles DROP CONSTRAINT IF EXISTS uq_user_roles_user_role;
ALTER TABLE IF EXISTS ONLY public.student_documents DROP CONSTRAINT IF EXISTS uq_student_documents_student_doc;
ALTER TABLE IF EXISTS ONLY public.role_permissions DROP CONSTRAINT IF EXISTS uq_role_permissions_role_perm;
ALTER TABLE IF EXISTS ONLY public.student_subscriptions DROP CONSTRAINT IF EXISTS student_subscriptions_pkey;
ALTER TABLE IF EXISTS ONLY public.student_profiles DROP CONSTRAINT IF EXISTS student_profiles_pkey;
ALTER TABLE IF EXISTS ONLY public.student_documents DROP CONSTRAINT IF EXISTS student_documents_pkey;
ALTER TABLE IF EXISTS ONLY public.roles DROP CONSTRAINT IF EXISTS roles_pkey;
ALTER TABLE IF EXISTS ONLY public.role_permissions DROP CONSTRAINT IF EXISTS role_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.plans DROP CONSTRAINT IF EXISTS plans_pkey;
ALTER TABLE IF EXISTS ONLY public.permissions DROP CONSTRAINT IF EXISTS permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.payments DROP CONSTRAINT IF EXISTS payments_pkey;
ALTER TABLE IF EXISTS ONLY public.notifications DROP CONSTRAINT IF EXISTS notifications_pkey;
ALTER TABLE IF EXISTS ONLY public.navigation_items DROP CONSTRAINT IF EXISTS navigation_items_pkey;
ALTER TABLE IF EXISTS ONLY public.documents DROP CONSTRAINT IF EXISTS documents_pkey;
ALTER TABLE IF EXISTS ONLY public.doctor_profiles DROP CONSTRAINT IF EXISTS doctor_profiles_pkey;
ALTER TABLE IF EXISTS ONLY public.chat_sessions DROP CONSTRAINT IF EXISTS chat_sessions_pkey;
ALTER TABLE IF EXISTS ONLY public.chat_messages DROP CONSTRAINT IF EXISTS chat_messages_pkey;
ALTER TABLE IF EXISTS ONLY public.categories DROP CONSTRAINT IF EXISTS categories_pkey;
ALTER TABLE IF EXISTS ONLY public.audit_logs DROP CONSTRAINT IF EXISTS audit_logs_pkey;
ALTER TABLE IF EXISTS ONLY public.alembic_version DROP CONSTRAINT IF EXISTS alembic_version_pkc;
ALTER TABLE IF EXISTS public.users ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.user_roles ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.student_subscriptions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.student_profiles ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.student_documents ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.roles ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.role_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.plans ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.payments ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.notifications ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.navigation_items ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.documents ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.doctor_profiles ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.chat_sessions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.chat_messages ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.categories ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.audit_logs ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.users_id_seq;
DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.user_roles_id_seq;
DROP TABLE IF EXISTS public.user_roles;
DROP SEQUENCE IF EXISTS public.student_subscriptions_id_seq;
DROP TABLE IF EXISTS public.student_subscriptions;
DROP SEQUENCE IF EXISTS public.student_profiles_id_seq;
DROP TABLE IF EXISTS public.student_profiles;
DROP SEQUENCE IF EXISTS public.student_documents_id_seq;
DROP TABLE IF EXISTS public.student_documents;
DROP SEQUENCE IF EXISTS public.roles_id_seq;
DROP TABLE IF EXISTS public.roles;
DROP SEQUENCE IF EXISTS public.role_permissions_id_seq;
DROP TABLE IF EXISTS public.role_permissions;
DROP SEQUENCE IF EXISTS public.plans_id_seq;
DROP TABLE IF EXISTS public.plans;
DROP SEQUENCE IF EXISTS public.permissions_id_seq;
DROP TABLE IF EXISTS public.permissions;
DROP SEQUENCE IF EXISTS public.payments_id_seq;
DROP TABLE IF EXISTS public.payments;
DROP SEQUENCE IF EXISTS public.notifications_id_seq;
DROP TABLE IF EXISTS public.notifications;
DROP SEQUENCE IF EXISTS public.navigation_items_id_seq;
DROP TABLE IF EXISTS public.navigation_items;
DROP SEQUENCE IF EXISTS public.documents_id_seq;
DROP TABLE IF EXISTS public.documents;
DROP SEQUENCE IF EXISTS public.doctor_profiles_id_seq;
DROP TABLE IF EXISTS public.doctor_profiles;
DROP SEQUENCE IF EXISTS public.chat_sessions_id_seq;
DROP TABLE IF EXISTS public.chat_sessions;
DROP SEQUENCE IF EXISTS public.chat_messages_id_seq;
DROP TABLE IF EXISTS public.chat_messages;
DROP SEQUENCE IF EXISTS public.categories_id_seq;
DROP TABLE IF EXISTS public.categories;
DROP SEQUENCE IF EXISTS public.audit_logs_id_seq;
DROP TABLE IF EXISTS public.audit_logs;
DROP TABLE IF EXISTS public.alembic_version;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: audit_logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.audit_logs (
    id integer NOT NULL,
    user_id integer,
    action character varying(100) NOT NULL,
    entity character varying(100) NOT NULL,
    entity_id character varying(100),
    ip_address character varying(50),
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.audit_logs OWNER TO postgres;

--
-- Name: audit_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.audit_logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.audit_logs_id_seq OWNER TO postgres;

--
-- Name: audit_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.audit_logs_id_seq OWNED BY public.audit_logs.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(255),
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: chat_messages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chat_messages (
    id integer NOT NULL,
    session_id integer NOT NULL,
    role character varying(20) NOT NULL,
    message text NOT NULL,
    tokens integer DEFAULT 0 NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.chat_messages OWNER TO postgres;

--
-- Name: chat_messages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chat_messages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.chat_messages_id_seq OWNER TO postgres;

--
-- Name: chat_messages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chat_messages_id_seq OWNED BY public.chat_messages.id;


--
-- Name: chat_sessions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chat_sessions (
    id integer NOT NULL,
    student_id integer NOT NULL,
    started_at timestamp with time zone DEFAULT now() NOT NULL,
    ended_at timestamp with time zone
);


ALTER TABLE public.chat_sessions OWNER TO postgres;

--
-- Name: chat_sessions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chat_sessions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.chat_sessions_id_seq OWNER TO postgres;

--
-- Name: chat_sessions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chat_sessions_id_seq OWNED BY public.chat_sessions.id;


--
-- Name: doctor_profiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.doctor_profiles (
    id integer NOT NULL,
    user_id integer NOT NULL,
    license_number character varying(100),
    specialization character varying(150),
    qualification character varying(200),
    experience_years integer DEFAULT 0 NOT NULL,
    bio text,
    status character varying(20) DEFAULT 'active'::character varying NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.doctor_profiles OWNER TO postgres;

--
-- Name: doctor_profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.doctor_profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.doctor_profiles_id_seq OWNER TO postgres;

--
-- Name: doctor_profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.doctor_profiles_id_seq OWNED BY public.doctor_profiles.id;


--
-- Name: documents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.documents (
    id integer NOT NULL,
    doctor_id integer NOT NULL,
    category_id integer,
    title character varying(255) NOT NULL,
    description text,
    file_url character varying(500) NOT NULL,
    visibility character varying(20) DEFAULT 'free'::character varying NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.documents OWNER TO postgres;

--
-- Name: documents_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.documents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.documents_id_seq OWNER TO postgres;

--
-- Name: documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.documents_id_seq OWNED BY public.documents.id;


--
-- Name: navigation_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.navigation_items (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    path character varying(255) NOT NULL,
    icon character varying(50),
    menu_type character varying(50) DEFAULT 'top_navbar'::character varying NOT NULL,
    target_role character varying(50) DEFAULT 'all'::character varying NOT NULL,
    display_order integer DEFAULT 0 NOT NULL,
    is_active boolean DEFAULT true NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.navigation_items OWNER TO postgres;

--
-- Name: navigation_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.navigation_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.navigation_items_id_seq OWNER TO postgres;

--
-- Name: navigation_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.navigation_items_id_seq OWNED BY public.navigation_items.id;


--
-- Name: notifications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notifications (
    id integer NOT NULL,
    user_id integer NOT NULL,
    title character varying(200) NOT NULL,
    body text NOT NULL,
    is_read boolean DEFAULT false NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.notifications OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notifications_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.notifications_id_seq OWNER TO postgres;

--
-- Name: notifications_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notifications_id_seq OWNED BY public.notifications.id;


--
-- Name: payments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payments (
    id integer NOT NULL,
    student_id integer NOT NULL,
    plan_id integer,
    amount numeric(10,2) NOT NULL,
    currency character varying(10) DEFAULT 'USD'::character varying NOT NULL,
    gateway character varying(50) DEFAULT 'manual'::character varying NOT NULL,
    transaction_id character varying(100),
    status character varying(20) DEFAULT 'pending'::character varying NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.payments OWNER TO postgres;

--
-- Name: payments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.payments_id_seq OWNER TO postgres;

--
-- Name: payments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.payments_id_seq OWNED BY public.payments.id;


--
-- Name: permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permissions (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(255)
);


ALTER TABLE public.permissions OWNER TO postgres;

--
-- Name: permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.permissions_id_seq OWNER TO postgres;

--
-- Name: permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.permissions_id_seq OWNED BY public.permissions.id;


--
-- Name: plans; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plans (
    id integer NOT NULL,
    doctor_id integer,
    name character varying(100) NOT NULL,
    price numeric(10,2) DEFAULT 0.00 NOT NULL,
    duration_days integer DEFAULT 30 NOT NULL,
    description text,
    status character varying(20) DEFAULT 'active'::character varying NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    features json
);


ALTER TABLE public.plans OWNER TO postgres;

--
-- Name: plans_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.plans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.plans_id_seq OWNER TO postgres;

--
-- Name: plans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.plans_id_seq OWNED BY public.plans.id;


--
-- Name: role_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role_permissions (
    id integer NOT NULL,
    role_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.role_permissions OWNER TO postgres;

--
-- Name: role_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.role_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.role_permissions_id_seq OWNER TO postgres;

--
-- Name: role_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.role_permissions_id_seq OWNED BY public.role_permissions.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(255)
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roles_id_seq OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: student_documents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_documents (
    id integer NOT NULL,
    student_id integer NOT NULL,
    document_id integer NOT NULL,
    access_type character varying(20) DEFAULT 'granted'::character varying NOT NULL,
    granted_at timestamp with time zone DEFAULT now() NOT NULL,
    expires_at timestamp with time zone
);


ALTER TABLE public.student_documents OWNER TO postgres;

--
-- Name: student_documents_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_documents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_documents_id_seq OWNER TO postgres;

--
-- Name: student_documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_documents_id_seq OWNED BY public.student_documents.id;


--
-- Name: student_profiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_profiles (
    id integer NOT NULL,
    user_id integer NOT NULL,
    university character varying(200),
    batch character varying(50),
    year character varying(20),
    country character varying(100),
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.student_profiles OWNER TO postgres;

--
-- Name: student_profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_profiles_id_seq OWNER TO postgres;

--
-- Name: student_profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_profiles_id_seq OWNED BY public.student_profiles.id;


--
-- Name: student_subscriptions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_subscriptions (
    id integer NOT NULL,
    student_id integer NOT NULL,
    plan_id integer NOT NULL,
    payment_id integer,
    status character varying(20) DEFAULT 'active'::character varying NOT NULL,
    start_date timestamp with time zone DEFAULT now() NOT NULL,
    end_date timestamp with time zone NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.student_subscriptions OWNER TO postgres;

--
-- Name: student_subscriptions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_subscriptions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_subscriptions_id_seq OWNER TO postgres;

--
-- Name: student_subscriptions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_subscriptions_id_seq OWNED BY public.student_subscriptions.id;


--
-- Name: user_roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_roles (
    id integer NOT NULL,
    user_id integer NOT NULL,
    role_id integer NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.user_roles OWNER TO postgres;

--
-- Name: user_roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_roles_id_seq OWNER TO postgres;

--
-- Name: user_roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_roles_id_seq OWNED BY public.user_roles.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password_hash character varying(255) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone character varying(20),
    status character varying(20) DEFAULT 'active'::character varying NOT NULL,
    email_verified boolean DEFAULT false NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    avatar_url character varying(500)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: audit_logs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.audit_logs ALTER COLUMN id SET DEFAULT nextval('public.audit_logs_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: chat_messages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_messages ALTER COLUMN id SET DEFAULT nextval('public.chat_messages_id_seq'::regclass);


--
-- Name: chat_sessions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_sessions ALTER COLUMN id SET DEFAULT nextval('public.chat_sessions_id_seq'::regclass);


--
-- Name: doctor_profiles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor_profiles ALTER COLUMN id SET DEFAULT nextval('public.doctor_profiles_id_seq'::regclass);


--
-- Name: documents id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documents ALTER COLUMN id SET DEFAULT nextval('public.documents_id_seq'::regclass);


--
-- Name: navigation_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.navigation_items ALTER COLUMN id SET DEFAULT nextval('public.navigation_items_id_seq'::regclass);


--
-- Name: notifications id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications ALTER COLUMN id SET DEFAULT nextval('public.notifications_id_seq'::regclass);


--
-- Name: payments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments ALTER COLUMN id SET DEFAULT nextval('public.payments_id_seq'::regclass);


--
-- Name: permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions ALTER COLUMN id SET DEFAULT nextval('public.permissions_id_seq'::regclass);


--
-- Name: plans id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plans ALTER COLUMN id SET DEFAULT nextval('public.plans_id_seq'::regclass);


--
-- Name: role_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions ALTER COLUMN id SET DEFAULT nextval('public.role_permissions_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: student_documents id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_documents ALTER COLUMN id SET DEFAULT nextval('public.student_documents_id_seq'::regclass);


--
-- Name: student_profiles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_profiles ALTER COLUMN id SET DEFAULT nextval('public.student_profiles_id_seq'::regclass);


--
-- Name: student_subscriptions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subscriptions ALTER COLUMN id SET DEFAULT nextval('public.student_subscriptions_id_seq'::regclass);


--
-- Name: user_roles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roles ALTER COLUMN id SET DEFAULT nextval('public.user_roles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
de9e9ee26559
\.


--
-- Data for Name: audit_logs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.audit_logs (id, user_id, action, entity, entity_id, ip_address, created_at) FROM stdin;
1	1	REGISTER	User	1	testclient	2026-08-22 17:58:38.470093+05:30
2	2	REGISTER	User	2	testclient	2026-08-22 17:58:38.935262+05:30
3	1	LOGIN	User	1	testclient	2026-08-22 17:58:38.96855+05:30
4	2	LOGIN	User	2	testclient	2026-08-22 17:58:39.384489+05:30
5	1	UPLOAD_DOCUMENT	Document	1	\N	2026-08-22 17:58:39.932245+05:30
6	2	SUBSCRIBE_PLAN	StudentSubscription	1	\N	2026-08-22 17:58:40.068403+05:30
7	2	PROCESS_PAYMENT	Payment	1	\N	2026-08-22 17:58:40.185815+05:30
8	3	REGISTER	User	3	127.0.0.1	2026-08-22 18:41:54.648446+05:30
9	3	LOGIN	User	3	127.0.0.1	2026-08-22 18:42:43.417084+05:30
10	1	LOGIN	User	1	testclient	2026-08-22 23:04:53.804628+05:30
11	2	LOGIN	User	2	testclient	2026-08-22 23:04:54.237163+05:30
12	1	UPLOAD_DOCUMENT	Document	2	\N	2026-08-22 23:04:54.809312+05:30
13	2	SUBSCRIBE_PLAN	StudentSubscription	3	\N	2026-08-22 23:04:54.923717+05:30
14	2	PROCESS_PAYMENT	Payment	2	\N	2026-08-22 23:04:55.047404+05:30
15	4	REGISTER	User	4	testclient	2026-08-22 23:10:20.910857+05:30
16	5	REGISTER	User	5	testclient	2026-08-22 23:10:21.359457+05:30
17	6	REGISTER	User	6	testclient	2026-08-22 23:10:21.762813+05:30
18	4	LOGIN	User	4	testclient	2026-08-22 23:10:22.238282+05:30
19	5	LOGIN	User	5	testclient	2026-08-22 23:10:22.636684+05:30
20	6	LOGIN	User	6	testclient	2026-08-22 23:10:23.029178+05:30
21	4	CHANGE_PASSWORD	User	4	\N	2026-08-22 23:10:24.208531+05:30
22	4	LOGIN	User	4	testclient	2026-08-22 23:10:24.246454+05:30
23	4	UPLOAD_DOCUMENT	Document	3	\N	2026-08-22 23:10:24.986463+05:30
24	4	UPLOAD_DOCUMENT	Document	4	\N	2026-08-22 23:10:25.051124+05:30
25	4	CREATE_PLAN	Plan	4	\N	2026-08-22 23:10:25.28425+05:30
26	5	SUBSCRIBE_PLAN	StudentSubscription	5	\N	2026-08-22 23:10:25.347587+05:30
27	5	PROCESS_PAYMENT	Payment	3	\N	2026-08-22 23:10:25.439202+05:30
28	7	REGISTER	User	7	127.0.0.1	2026-09-03 10:04:42.226653+05:30
29	7	LOGIN	User	7	127.0.0.1	2026-09-03 10:04:42.28858+05:30
30	7	PROCESS_PAYMENT	Payment	4	\N	2026-09-03 10:10:23.61446+05:30
31	7	SUBSCRIBE_PLAN	StudentSubscription	8	\N	2026-09-03 10:10:44.774463+05:30
32	8	REGISTER	User	8	127.0.0.1	2026-09-18 14:30:24.202527+05:30
33	8	LOGIN	User	8	127.0.0.1	2026-09-18 14:30:24.248427+05:30
34	8	LOGIN	User	8	127.0.0.1	2026-09-18 19:32:09.320118+05:30
35	8	LOGIN	User	8	127.0.0.1	2026-09-18 20:10:05.325638+05:30
36	8	LOGIN	User	8	127.0.0.1	2026-09-18 20:50:16.095445+05:30
37	8	UPDATE_PROFILE	User	8	\N	2026-09-18 23:52:30.408891+05:30
38	8	LOGIN	User	8	127.0.0.1	2026-09-18 23:54:19.31124+05:30
39	8	UPDATE_AVATAR	User	8	\N	2026-09-19 01:22:43.870885+05:30
40	8	UPDATE_AVATAR	User	8	\N	2026-09-19 01:23:13.549652+05:30
41	8	LOGIN	User	8	127.0.0.1	2026-09-19 01:52:57.779935+05:30
42	9	REGISTER	User	9	127.0.0.1	2026-09-19 02:50:58.716392+05:30
43	9	LOGIN	User	9	127.0.0.1	2026-09-19 02:50:58.759751+05:30
44	9	UPDATE_AVATAR	User	9	\N	2026-09-19 02:54:13.053552+05:30
45	9	LOGIN	User	9	127.0.0.1	2026-09-19 05:04:10.345474+05:30
46	8	LOGIN	User	8	127.0.0.1	2026-09-19 05:19:45.450029+05:30
47	8	LOGIN	User	8	127.0.0.1	2026-09-19 11:15:11.834883+05:30
48	8	LOGIN	User	8	127.0.0.1	2026-09-19 11:40:37.02389+05:30
49	8	LOGIN	User	8	127.0.0.1	2026-09-19 11:51:40.992411+05:30
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, name, description, created_at) FROM stdin;
1	Anatomy	Human gross and microscopic anatomy, histology, and embryology	2026-08-22 17:52:22.754376+05:30
2	Physiology	Human organ systems and physiological mechanisms	2026-08-22 17:52:22.754376+05:30
3	Pathology	General and systemic disease pathology and diagnostic markers	2026-08-22 17:52:22.754376+05:30
4	Pharmacology	Drug classes, mechanisms of action, pharmacokinetics, and toxicities	2026-08-22 17:52:22.754376+05:30
5	Internal Medicine	Clinical cases, diagnostic algorithms, and therapeutic guidelines	2026-08-22 17:52:22.754376+05:30
6	Surgery	Surgical techniques, operative notes, and perioperative care	2026-08-22 17:52:22.754376+05:30
7	Clinical Cardiology	Heart murmur auscultation, ECG cases, and emergency protocols	2026-08-22 18:54:22.680226+05:30
8	Neurology Cases 1f6678	Clinical neurology examination and stroke triage	2026-08-22 23:10:24.890621+05:30
\.


--
-- Data for Name: chat_messages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.chat_messages (id, session_id, role, message, tokens, created_at) FROM stdin;
1	1	user	Can you explain the difference between systolic and diastolic murmurs in cardiology?	12	2026-08-22 17:58:40.101557+05:30
2	1	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'Can you explain the difference between systolic and diastolic murmurs in cardiology?'.	39	2026-08-22 17:58:40.101557+05:30
3	2	user	Can you explain the difference between systolic and diastolic murmurs in cardiology?	12	2026-08-22 23:04:54.953646+05:30
4	2	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'Can you explain the difference between systolic and diastolic murmurs in cardiology?'.	39	2026-08-22 23:04:54.953646+05:30
5	3	user	What is the clinical triad of normal pressure hydrocephalus?	9	2026-08-22 23:10:25.498705+05:30
6	3	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'What is the clinical triad of normal pressure hydrocephalus?'.	36	2026-08-22 23:10:25.498705+05:30
7	3	user	Can you elaborate on gait disturbance in NPH?	8	2026-08-22 23:10:25.546968+05:30
8	3	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'Can you elaborate on gait disturbance in NPH?'.	35	2026-08-22 23:10:25.546968+05:30
9	4	user	hello	1	2026-09-03 10:12:45.071717+05:30
10	4	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'hello'.	28	2026-09-03 10:12:45.071717+05:30
11	4	user	i need u to assist me	6	2026-09-03 10:12:55.551346+05:30
12	4	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'i need u to assist me'.	33	2026-09-03 10:12:55.551346+05:30
13	5	user	kk	1	2026-09-03 10:13:06.894143+05:30
14	5	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'kk'.	28	2026-09-03 10:13:06.894143+05:30
15	6	user	jjj	1	2026-09-19 01:06:18.873936+05:30
16	6	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'jjj'.	28	2026-09-19 01:06:18.873936+05:30
17	7	user	hdhd	1	2026-09-19 11:57:18.663523+05:30
18	7	assistant	Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: 'hdhd'.	28	2026-09-19 11:57:18.663523+05:30
\.


--
-- Data for Name: chat_sessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.chat_sessions (id, student_id, started_at, ended_at) FROM stdin;
1	1	2026-08-22 17:58:40.101557+05:30	\N
2	1	2026-08-22 23:04:54.953646+05:30	\N
3	2	2026-08-22 23:10:25.498705+05:30	\N
4	4	2026-09-03 10:12:45.071717+05:30	\N
5	4	2026-09-03 10:13:06.894143+05:30	\N
6	5	2026-09-19 01:06:18.873936+05:30	\N
7	5	2026-09-19 11:57:18.663523+05:30	\N
\.


--
-- Data for Name: doctor_profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.doctor_profiles (id, user_id, license_number, specialization, qualification, experience_years, bio, status, created_at, updated_at) FROM stdin;
1	1	MED-99482	Diagnostic Medicine	\N	15	Specialist in nephrology and complex diagnostics.	active	2026-08-22 17:58:38.048648+05:30	2026-08-22 17:58:39.828303+05:30
2	3	\N	\N	\N	0	\N	active	2026-08-22 18:41:54.240554+05:30	2026-08-22 18:41:54.240554+05:30
3	4	LIC-1f6678	Pediatric Surgery	MD, MS (Surgery), FACS	16	Specialist in minimally invasive pediatric surgery.	active	2026-08-22 23:10:20.483762+05:30	2026-08-22 23:10:24.716642+05:30
4	9	\N	\N	\N	0	\N	active	2026-09-19 02:50:58.3496+05:30	2026-09-19 02:50:58.3496+05:30
\.


--
-- Data for Name: documents; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.documents (id, doctor_id, category_id, title, description, file_url, visibility, created_at, updated_at) FROM stdin;
1	1	1	Cardiovascular Examination Guide	Comprehensive murmur evaluation and clinical bedside guide.	/uploads/cardio_guide.pdf	free	2026-08-22 17:58:39.900958+05:30	2026-08-22 17:58:39.900958+05:30
2	1	1	Cardiovascular Examination Guide	Comprehensive murmur evaluation and clinical bedside guide.	/uploads/cardio_guide.pdf	free	2026-08-22 23:04:54.777536+05:30	2026-08-22 23:04:54.777536+05:30
3	3	8	Cranial Nerve Examination 1f6678	Step-by-step examination of CN I to XII	/uploads/4_neuro_handbook.pdf	free	2026-08-22 23:10:24.958324+05:30	2026-08-22 23:10:24.958324+05:30
4	3	8	Acute Stroke Neuroimaging Atlas 1f6678	CT perfusion and MRI DWI high-yield review	/uploads/4_neuro_handbook.pdf	premium	2026-08-22 23:10:25.021485+05:30	2026-08-22 23:10:25.021485+05:30
\.


--
-- Data for Name: navigation_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.navigation_items (id, title, path, icon, menu_type, target_role, display_order, is_active, created_at) FROM stdin;
1	Home	/	Home	top_navbar	all	1	t	2026-09-18 15:14:25.20158+05:30
2	About	/about	Info	top_navbar	all	2	t	2026-09-18 15:14:25.20158+05:30
3	Services	/services	Activity	top_navbar	all	3	t	2026-09-18 15:14:25.20158+05:30
4	Contact	/contact	Phone	top_navbar	all	4	t	2026-09-18 15:14:25.20158+05:30
5	Dashboard	/dashboard	LayoutDashboard	sidebar_student	student	1	t	2026-09-18 15:14:25.20158+05:30
6	Resources	/documents	BookOpen	sidebar_student	student	2	t	2026-09-18 15:14:25.20158+05:30
7	Clinical Guidance	/chat	MessageSquare	sidebar_student	student	3	t	2026-09-18 15:14:25.20158+05:30
8	Plans	/plans	CreditCard	sidebar_student	student	4	t	2026-09-18 15:14:25.20158+05:30
9	Dashboard	/doctor/dashboard	LayoutDashboard	sidebar_doctor	doctor	1	t	2026-09-18 15:14:25.20158+05:30
10	Documents	/doctor/documents	FileText	sidebar_doctor	doctor	2	t	2026-09-18 15:14:25.20158+05:30
11	Student Access	/doctor/grant-access	UserCheck	sidebar_doctor	doctor	3	t	2026-09-18 15:14:25.20158+05:30
12	Plans	/plans	CreditCard	sidebar_doctor	doctor	4	t	2026-09-18 15:14:25.20158+05:30
13	Dashboard	/admin/users	LayoutDashboard	sidebar_admin	admin	1	t	2026-09-18 15:14:25.20158+05:30
14	Audit Logs	/admin/audit-logs	FileText	sidebar_admin	admin	2	t	2026-09-18 15:14:25.20158+05:30
15	Documents	/doctor/documents	BookOpen	sidebar_admin	admin	3	t	2026-09-18 15:14:25.20158+05:30
16	Student Access	/doctor/grant-access	UserCheck	sidebar_admin	admin	4	t	2026-09-18 15:14:25.20158+05:30
\.


--
-- Data for Name: notifications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notifications (id, user_id, title, body, is_read, created_at) FROM stdin;
\.


--
-- Data for Name: payments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payments (id, student_id, plan_id, amount, currency, gateway, transaction_id, status, created_at) FROM stdin;
1	1	2	29.00	USD	manual	TXN-F9AFA9374F3B	successful	2026-08-22 17:58:40.147087+05:30
2	1	2	29.00	USD	manual	TXN-124BCB17CDDD	successful	2026-08-22 23:04:54.999222+05:30
3	2	4	45.00	USD	stripe	TXN-328A2DB0485D	successful	2026-08-22 23:10:25.405703+05:30
4	4	2	29.00	USD	stripe_mock	TXN-2AE5570C58F7	successful	2026-09-03 10:10:23.51117+05:30
\.


--
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permissions (id, name, description) FROM stdin;
1	ViewDocument	View document metadata and preview
2	UploadDocument	Upload new medical/educational documents
3	DeleteDocument	Delete uploaded documents
4	DownloadDocument	Download full document contents
5	ManageStudents	View and manage student profiles and access
6	ManageDoctors	Manage doctor accounts and profiles
7	CreatePlan	Create and update subscription plans
8	ManageSubscription	Purchase, renew, or cancel subscriptions
9	UseChatbot	Interact with AI medical guidance chatbot
10	UsePremiumChatbot	Extended AI usage quota and specialized guidance
\.


--
-- Data for Name: plans; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plans (id, doctor_id, name, price, duration_days, description, status, created_at, updated_at, features) FROM stdin;
4	3	Neurology Masterclass 1f6678	45.00	45	Comprehensive neurology clinical preparation	active	2026-08-22 23:10:25.256013+05:30	2026-08-22 23:10:25.256013+05:30	\N
1	\N	Free Starter	0.00	365	Access to all free documents and basic clinical guidance.	active	2026-08-22 17:52:22.754376+05:30	2026-09-18 15:14:25.20158+05:30	["Access to all Free core documents", "Basic clinical guidance consultation", "Standard community forum access", "View public clinical categories"]
2	\N	Pro Monthly	29.00	30	Full access to all premium documents and extended diagnostic consultation.	active	2026-08-22 17:52:22.754376+05:30	2026-09-18 15:14:25.20158+05:30	["Full access to 300+ Pro clinical documents", "Unlimited Clinical Guidance consultation", "Detailed examination notes & auscultation guides", "Direct doctor access request entitlement", "Priority student support"]
3	\N	Premium Annual	199.00	365	Complete 1-year unlimited access to all platform materials and priority support.	active	2026-08-22 17:52:22.754376+05:30	2026-09-18 15:14:25.20158+05:30	["Everything in Pro Monthly plan", "Full 365 days unlimited VIP access", "Exclusive high-yield exam preparation packages", "Direct clinical mentor messaging & webinars", "Official certificate of completion"]
\.


--
-- Data for Name: role_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.role_permissions (id, role_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	2	1
12	2	2
13	2	3
14	2	4
15	2	5
16	2	6
17	2	7
18	2	8
19	2	9
20	2	10
21	3	1
22	3	2
23	3	3
24	3	4
25	3	5
26	3	7
27	4	1
28	4	4
29	4	8
30	4	9
31	4	10
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id, name, description) FROM stdin;
1	Admin	System administrator with full access
2	Owner	Platform/Organization owner doctor
3	Doctor	Medical educator/doctor uploading resources and managing plans
4	Student	Medical student studying and accessing educational material
\.


--
-- Data for Name: student_documents; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_documents (id, student_id, document_id, access_type, granted_at, expires_at) FROM stdin;
1	2	4	granted	2026-08-22 23:10:25.177435+05:30	\N
\.


--
-- Data for Name: student_profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_profiles (id, user_id, university, batch, year, country, created_at, updated_at) FROM stdin;
1	2	\N	\N	\N	\N	2026-08-22 17:58:38.531604+05:30	2026-08-22 17:58:38.531604+05:30
3	6	\N	\N	\N	\N	2026-08-22 23:10:21.3883+05:30	2026-08-22 23:10:21.3883+05:30
2	5	Cambridge School of Clinical Medicine	2026 Batch	Clinical Year 2	United Kingdom	2026-08-22 23:10:20.966446+05:30	2026-08-22 23:10:24.843703+05:30
4	7	\N	\N	\N	\N	2026-09-03 10:04:41.761779+05:30	2026-09-03 10:04:41.761779+05:30
5	8	University of Moratuwa				2026-09-18 14:30:23.80943+05:30	2026-09-18 23:52:30.588835+05:30
\.


--
-- Data for Name: student_subscriptions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_subscriptions (id, student_id, plan_id, payment_id, status, start_date, end_date, created_at, updated_at) FROM stdin;
1	1	2	\N	expired	2026-08-22 17:58:40.052608+05:30	2026-09-21 17:58:40.052608+05:30	2026-08-22 17:58:40.027768+05:30	2026-08-22 17:58:40.176435+05:30
2	1	2	1	expired	2026-08-22 17:58:40.178772+05:30	2026-09-21 17:58:40.178772+05:30	2026-08-22 17:58:40.176435+05:30	2026-08-22 23:04:54.884207+05:30
3	1	2	\N	expired	2026-08-22 23:04:54.904833+05:30	2026-09-21 23:04:54.904833+05:30	2026-08-22 23:04:54.884207+05:30	2026-08-22 23:04:55.035594+05:30
4	1	2	2	active	2026-08-22 23:04:55.041445+05:30	2026-09-21 23:04:55.041445+05:30	2026-08-22 23:04:55.035594+05:30	2026-08-22 23:04:55.035594+05:30
5	2	4	\N	expired	2026-08-22 23:10:25.338951+05:30	2026-10-06 23:10:25.338951+05:30	2026-08-22 23:10:25.322442+05:30	2026-08-22 23:10:25.427044+05:30
6	2	4	3	active	2026-08-22 23:10:25.432161+05:30	2026-10-06 23:10:25.432161+05:30	2026-08-22 23:10:25.427044+05:30	2026-08-22 23:10:25.427044+05:30
7	4	2	4	expired	2026-09-03 10:10:23.568265+05:30	2026-10-03 10:10:23.568265+05:30	2026-09-03 10:10:23.560623+05:30	2026-09-03 10:10:44.671215+05:30
8	4	1	\N	active	2026-09-03 10:10:44.711596+05:30	2027-09-03 10:10:44.711596+05:30	2026-09-03 10:10:44.671215+05:30	2026-09-03 10:10:44.671215+05:30
\.


--
-- Data for Name: user_roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_roles (id, user_id, role_id, created_at) FROM stdin;
1	1	3	2026-08-22 17:58:38.048648+05:30
2	2	4	2026-08-22 17:58:38.531604+05:30
3	3	3	2026-08-22 18:41:54.240554+05:30
4	4	3	2026-08-22 23:10:20.483762+05:30
5	5	4	2026-08-22 23:10:20.966446+05:30
6	6	1	2026-08-22 23:10:21.3883+05:30
7	7	4	2026-09-03 10:04:41.761779+05:30
8	8	4	2026-09-18 14:30:23.80943+05:30
9	9	3	2026-09-19 02:50:58.3496+05:30
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, password_hash, first_name, last_name, phone, status, email_verified, created_at, updated_at, avatar_url) FROM stdin;
1	dr.house_200@hospital.org	$2b$12$spxeO7E6Nf74NLbPJmhWquY.kTM9dNIm4AIydh2ReNG1XMdpi.o/.	Gregory	House	+1234567890	active	f	2026-08-22 17:58:38.048648+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=400
2	student.john_200@medschool.edu	$2b$12$MUa.Grvc/MCYpTdsAFX3TOpJJO.ZwvEHo/2DWi3p5ODzo/XPa6RLa	John	Watson	+1987654321	active	f	2026-08-22 17:58:38.531604+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400
3	doctor.smith@hospital.org	$2b$12$MnABwQjrHLKmXhyHKhznFetJ3PpwKsL8ebnoxBec1sffoyQsq7Tiy	John	Smith	+1234567890	active	f	2026-08-22 18:41:54.240554+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=400
4	doctor_1f6678@clinic.org	$2b$12$EMrYg9HMHOb/TOT9Y69xx.xcwq0PtgyL4ycXmnKUErRH3mUwmJ94a	Marcus	Welby	+1555123456	active	f	2026-08-22 23:10:20.483762+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=400
5	student_1f6678@uni.edu	$2b$12$PthnqFUaPd4lNv8XD1Q.K.BBalPDfEQxXEwBFWOZCqgPOK/KLbJQm	Claire	Bennet	+1555987654	active	f	2026-08-22 23:10:20.966446+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400
6	admin_1f6678@platform.org	$2b$12$5ADJ5tROA3z6uiTr.bZaJeHXgEoGDccVBlbM0QLlp1Kaq2EqfWGt2	Super	Admin	+1555000111	active	f	2026-08-22 23:10:21.3883+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400
7	tharusharayan15@gmail.com	$2b$12$ZUyGGBtF3/fc33y1S6g9SOdgw5qzVfP5LFBtCtNDoRgS9ZeOTTjAa	Tharusha	Rayan	123456789	active	f	2026-09-03 10:04:41.761779+05:30	2026-09-18 22:06:15.673766+05:30	https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400
8	student1@medguidance.com	$2b$12$uTRDf3IdPqmuzTKKZNJ1y.aJTZfRtoq9eVmQ6KcPAEneuHZcGolX6	john	Mccathy	123456789	active	f	2026-09-18 14:30:23.80943+05:30	2026-09-19 01:23:13.522344+05:30	http://127.0.0.1:8000/uploads/avatar_8_1789761193.png
9	john@medguidance.com	$2b$12$IKZEzNg4gdkfcacR7tHfhuuN4XpTi6de3wUlgwvspoYquU3OvDwTe	john	watson	123456789	active	f	2026-09-19 02:50:58.3496+05:30	2026-09-19 02:54:13.031085+05:30	http://127.0.0.1:8000/uploads/avatar_9_1789766653.png
\.


--
-- Name: audit_logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.audit_logs_id_seq', 49, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 8, true);


--
-- Name: chat_messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.chat_messages_id_seq', 18, true);


--
-- Name: chat_sessions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.chat_sessions_id_seq', 7, true);


--
-- Name: doctor_profiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.doctor_profiles_id_seq', 4, true);


--
-- Name: documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.documents_id_seq', 4, true);


--
-- Name: navigation_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.navigation_items_id_seq', 16, true);


--
-- Name: notifications_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notifications_id_seq', 1, true);


--
-- Name: payments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payments_id_seq', 4, true);


--
-- Name: permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.permissions_id_seq', 10, true);


--
-- Name: plans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.plans_id_seq', 4, true);


--
-- Name: role_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.role_permissions_id_seq', 31, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 4, true);


--
-- Name: student_documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_documents_id_seq', 1, true);


--
-- Name: student_profiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_profiles_id_seq', 5, true);


--
-- Name: student_subscriptions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_subscriptions_id_seq', 8, true);


--
-- Name: user_roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_roles_id_seq', 9, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 9, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: audit_logs audit_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.audit_logs
    ADD CONSTRAINT audit_logs_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: chat_messages chat_messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_messages
    ADD CONSTRAINT chat_messages_pkey PRIMARY KEY (id);


--
-- Name: chat_sessions chat_sessions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_sessions
    ADD CONSTRAINT chat_sessions_pkey PRIMARY KEY (id);


--
-- Name: doctor_profiles doctor_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor_profiles
    ADD CONSTRAINT doctor_profiles_pkey PRIMARY KEY (id);


--
-- Name: documents documents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documents
    ADD CONSTRAINT documents_pkey PRIMARY KEY (id);


--
-- Name: navigation_items navigation_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.navigation_items
    ADD CONSTRAINT navigation_items_pkey PRIMARY KEY (id);


--
-- Name: notifications notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_pkey PRIMARY KEY (id);


--
-- Name: payments payments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_pkey PRIMARY KEY (id);


--
-- Name: permissions permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);


--
-- Name: plans plans_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plans
    ADD CONSTRAINT plans_pkey PRIMARY KEY (id);


--
-- Name: role_permissions role_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_pkey PRIMARY KEY (id);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: student_documents student_documents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_documents
    ADD CONSTRAINT student_documents_pkey PRIMARY KEY (id);


--
-- Name: student_profiles student_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_profiles
    ADD CONSTRAINT student_profiles_pkey PRIMARY KEY (id);


--
-- Name: student_subscriptions student_subscriptions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subscriptions
    ADD CONSTRAINT student_subscriptions_pkey PRIMARY KEY (id);


--
-- Name: role_permissions uq_role_permissions_role_perm; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT uq_role_permissions_role_perm UNIQUE (role_id, permission_id);


--
-- Name: student_documents uq_student_documents_student_doc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_documents
    ADD CONSTRAINT uq_student_documents_student_doc UNIQUE (student_id, document_id);


--
-- Name: user_roles uq_user_roles_user_role; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT uq_user_roles_user_role UNIQUE (user_id, role_id);


--
-- Name: user_roles user_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_audit_logs_action; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_audit_logs_action ON public.audit_logs USING btree (action);


--
-- Name: ix_audit_logs_entity; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_audit_logs_entity ON public.audit_logs USING btree (entity);


--
-- Name: ix_audit_logs_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_audit_logs_user_id ON public.audit_logs USING btree (user_id);


--
-- Name: ix_categories_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_categories_name ON public.categories USING btree (name);


--
-- Name: ix_chat_messages_session_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_chat_messages_session_id ON public.chat_messages USING btree (session_id);


--
-- Name: ix_chat_sessions_student_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_chat_sessions_student_id ON public.chat_sessions USING btree (student_id);


--
-- Name: ix_doctor_profiles_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_doctor_profiles_user_id ON public.doctor_profiles USING btree (user_id);


--
-- Name: ix_documents_category_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_documents_category_id ON public.documents USING btree (category_id);


--
-- Name: ix_documents_doctor_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_documents_doctor_id ON public.documents USING btree (doctor_id);


--
-- Name: ix_documents_title; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_documents_title ON public.documents USING btree (title);


--
-- Name: ix_navigation_items_menu_type; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_navigation_items_menu_type ON public.navigation_items USING btree (menu_type);


--
-- Name: ix_navigation_items_target_role; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_navigation_items_target_role ON public.navigation_items USING btree (target_role);


--
-- Name: ix_notifications_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_notifications_user_id ON public.notifications USING btree (user_id);


--
-- Name: ix_payments_plan_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_payments_plan_id ON public.payments USING btree (plan_id);


--
-- Name: ix_payments_student_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_payments_student_id ON public.payments USING btree (student_id);


--
-- Name: ix_payments_transaction_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_payments_transaction_id ON public.payments USING btree (transaction_id);


--
-- Name: ix_permissions_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_permissions_name ON public.permissions USING btree (name);


--
-- Name: ix_plans_doctor_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_plans_doctor_id ON public.plans USING btree (doctor_id);


--
-- Name: ix_plans_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_plans_name ON public.plans USING btree (name);


--
-- Name: ix_roles_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_roles_name ON public.roles USING btree (name);


--
-- Name: ix_student_documents_document_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_student_documents_document_id ON public.student_documents USING btree (document_id);


--
-- Name: ix_student_documents_student_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_student_documents_student_id ON public.student_documents USING btree (student_id);


--
-- Name: ix_student_profiles_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_student_profiles_user_id ON public.student_profiles USING btree (user_id);


--
-- Name: ix_student_subscriptions_payment_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_student_subscriptions_payment_id ON public.student_subscriptions USING btree (payment_id);


--
-- Name: ix_student_subscriptions_plan_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_student_subscriptions_plan_id ON public.student_subscriptions USING btree (plan_id);


--
-- Name: ix_student_subscriptions_student_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_student_subscriptions_student_id ON public.student_subscriptions USING btree (student_id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: audit_logs audit_logs_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.audit_logs
    ADD CONSTRAINT audit_logs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE SET NULL;


--
-- Name: chat_messages chat_messages_session_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_messages
    ADD CONSTRAINT chat_messages_session_id_fkey FOREIGN KEY (session_id) REFERENCES public.chat_sessions(id) ON DELETE CASCADE;


--
-- Name: chat_sessions chat_sessions_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_sessions
    ADD CONSTRAINT chat_sessions_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student_profiles(id) ON DELETE CASCADE;


--
-- Name: doctor_profiles doctor_profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor_profiles
    ADD CONSTRAINT doctor_profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: documents documents_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documents
    ADD CONSTRAINT documents_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id) ON DELETE SET NULL;


--
-- Name: documents documents_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.documents
    ADD CONSTRAINT documents_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctor_profiles(id) ON DELETE CASCADE;


--
-- Name: notifications notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notifications
    ADD CONSTRAINT notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: payments payments_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_plan_id_fkey FOREIGN KEY (plan_id) REFERENCES public.plans(id) ON DELETE SET NULL;


--
-- Name: payments payments_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student_profiles(id) ON DELETE CASCADE;


--
-- Name: plans plans_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plans
    ADD CONSTRAINT plans_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctor_profiles(id) ON DELETE SET NULL;


--
-- Name: role_permissions role_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.permissions(id) ON DELETE CASCADE;


--
-- Name: role_permissions role_permissions_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;


--
-- Name: student_documents student_documents_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_documents
    ADD CONSTRAINT student_documents_document_id_fkey FOREIGN KEY (document_id) REFERENCES public.documents(id) ON DELETE CASCADE;


--
-- Name: student_documents student_documents_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_documents
    ADD CONSTRAINT student_documents_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student_profiles(id) ON DELETE CASCADE;


--
-- Name: student_profiles student_profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_profiles
    ADD CONSTRAINT student_profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: student_subscriptions student_subscriptions_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subscriptions
    ADD CONSTRAINT student_subscriptions_payment_id_fkey FOREIGN KEY (payment_id) REFERENCES public.payments(id) ON DELETE SET NULL;


--
-- Name: student_subscriptions student_subscriptions_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subscriptions
    ADD CONSTRAINT student_subscriptions_plan_id_fkey FOREIGN KEY (plan_id) REFERENCES public.plans(id) ON DELETE RESTRICT;


--
-- Name: student_subscriptions student_subscriptions_student_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subscriptions
    ADD CONSTRAINT student_subscriptions_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student_profiles(id) ON DELETE CASCADE;


--
-- Name: user_roles user_roles_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;


--
-- Name: user_roles user_roles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict aO7zepQLlDclDRyao6GbT3b4F73xAYhlFbSPm5skbKCvLI8w5g6SrljYKRDJJje

