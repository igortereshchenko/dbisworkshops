CREATE TABLE "Vendors"
(
"id" NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
"vendor_name" NVARCHAR2(20) UNIQUE NOT NULL,
"vendor_email" NVARCHAR2(100) NOT NULL,
"ticket_number" NUMBER NOT NULL,
);

CREATE TABLE "Ivents"
(
"id" number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
"event_name" NVARCHAR2(100) NOT NULL,
"event_category" NVARCHAR2(250) NOT NULL,
"event_date" TIMESTAMP NOT NULL,
"vendor_id" NUMBER NOT NULL,
"ticket_number" NUMBER NOT NULL
);

ALTER TABLE "Vendors"
ADD CONSTRAINT pk_Vendors PRIMARY KEY("id");

ALTER TABLE "Ivents"
ADD CONSTRAINT pk_Ivents PRIMARY KEY("id");

ALTER TABLE "Ivents"
ADD CONSTRAINT fk_Vendors_id FOREIGN KEY("vendor_id") REFERENCES "Vendors"("id");

ALTER TABLE "Ivents"
ADD CONSTRAINT fk_Vendors_ticket_number FOREIGN KEY("ticket_number") REFERENCES "Vendors"("ticket_number");