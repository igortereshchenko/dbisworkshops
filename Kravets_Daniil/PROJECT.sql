------------TRIGGERS---------------

CREATE SEQUENCE sq_order_song
START WITH 1
INCREMENT BY 1
NOMAXVALUE;

CREATE OR REPLACE TRIGGER tr_ai_order_song before INSERT ON "OrderSong" FOR each row
BEGIN
    SELECT sq_order_song.NEXTVAL
    INTO :new.song_id
    FROM dual;
END;
/
-----------------------------------

CREATE SEQUENCE sq_order_announcement
START WITH 1
INCREMENT BY 1
NOMAXVALUE;

CREATE OR REPLACE TRIGGER tr_ai_order_announcement before INSERT ON "Announcement" FOR each row
BEGIN
    SELECT sq_order_announcement.NEXTVAL
    INTO :new.announcement_id
    FROM dual;
END;
/
-----------------------------------

CREATE SEQUENCE sq_broadcast
START WITH 1
INCREMENT BY 1
NOMAXVALUE;

CREATE OR REPLACE TRIGGER tr_ai_broadcast before INSERT ON "Broadcast" FOR each row
BEGIN
    SELECT sq_broadcast.NEXTVAL
    INTO :new.broadcast_id
    FROM dual;
END;
/
------------------------------------
CREATE SEQUENCE sq_feedback
START WITH 1
INCREMENT BY 1
NOMAXVALUE;

CREATE OR REPLACE TRIGGER tr_ai_feedback before INSERT ON "Feedback" FOR each row
BEGIN
    SELECT sq_feedback.NEXTVAL
    INTO :new.feedback_id
    FROM dual;
END;
/

