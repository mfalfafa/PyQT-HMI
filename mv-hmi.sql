-- Adminer 4.6.3 PostgreSQL dump

DROP TABLE IF EXISTS "data_downtime";
DROP SEQUENCE IF EXISTS data_downtime_id_seq;
CREATE SEQUENCE data_downtime_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."data_downtime" (
    "id" integer DEFAULT nextval('data_downtime_id_seq') NOT NULL,
    "data_dt" text NOT NULL,
    "update_dt" text NOT NULL,
    "update_flag" integer DEFAULT '0' NOT NULL,
    CONSTRAINT "data_downtime_id" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "data_downtime" ("id", "data_dt", "update_dt", "update_flag") VALUES
(6,	'downtime 04',	'',	0),
(7,	'downtime 05',	'',	0),
(8,	'downtime 06',	'',	0),
(9,	'downtime 07',	'',	0),
(10,	'downtime 08',	'',	0),
(11,	'downtime 09',	'',	0),
(12,	'downtime 10',	'',	0),
(13,	'downtime 11',	'',	0),
(14,	'Downtime 12',	'',	0),
(5,	'downtime 03',	'Mesin Mati {00:15:00}
1-Jun-2018 | 9:00:05',	0),
(15,	'Downtime 13',	'Mesin Mati {00:15:00}
1-Jun-2018 | 9:00:05',	1),
(4,	'downtime 02',	'Gear Patah {00:15:00}
1-Jun-2018 | 9:00:05',	1),
(1,	'downtime 01',	'Gear Patah {00:15:00}
1-Jun-2018 | 9:00:05',	1);

DROP TABLE IF EXISTS "login_data";
DROP SEQUENCE IF EXISTS table1_id_seq;
CREATE SEQUENCE table1_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."login_data" (
    "id" integer DEFAULT nextval('table1_id_seq') NOT NULL,
    "rfid" text,
    CONSTRAINT "table1_id" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "login_data" ("id", "rfid") VALUES
(1,	'11111'),
(2,	'22222');

DROP TABLE IF EXISTS "status_machine";
DROP SEQUENCE IF EXISTS "status-machine_id_seq";
CREATE SEQUENCE "status-machine_id_seq" INCREMENT  MINVALUE  MAXVALUE  START 1 CACHE ;

CREATE TABLE "public"."status_machine" (
    "id" integer DEFAULT nextval('"status-machine_id_seq"') NOT NULL,
    "status" text NOT NULL,
    CONSTRAINT "status-machine_id" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "status_machine" ("id", "status") VALUES
(4,	'0'),
(3,	'0'),
(1,	'1'),
(2,	'1');

DROP TABLE IF EXISTS "status_machine_dt";
DROP SEQUENCE IF EXISTS status_machine_dt_id_seq;
CREATE SEQUENCE status_machine_dt_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."status_machine_dt" (
    "id" integer DEFAULT nextval('status_machine_dt_id_seq') NOT NULL,
    "dt_status" text NOT NULL,
    CONSTRAINT "status_machine_dt_id" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "status_machine_dt" ("id", "dt_status") VALUES
(1,	'0'),
(2,	'0');

-- 2018-08-19 11:18:11.999994+07
