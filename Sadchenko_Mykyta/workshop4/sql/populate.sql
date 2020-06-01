INSERT INTO USER (user_id, username, email, password)
    VALUES (1, 'Bob', 'ex@gmail.com', 'securestsecure');
INSERT INTO USER (user_id, username, password)
    VALUES (2, 'Bob1', 'secures123tsecure');
INSERT INTO USER (user_id, username, password)
    VALUES (3, 'Bob21', 's312312urestsecure');
INSERT INTO USER (user_id, username, password)
    VALUES (4, '43Bob', 'dsfadasdsaurestsecure');

INSERT INTO NOTE (note_id, url_id, title, text, created)
    VALUES (1, 'asddaf12F', 'Titlest', 'Lorem impum ...sadmk', '13-NOV-18');
INSERT INTO NOTE (note_id, url_id, title, created)
    VALUES (2, '3123Df12F', 'T441itlest', '13-MAR-20');
INSERT INTO NOTE (note_id, url_id, created)
    VALUES (3, 'ffASDf12F', '11-NOV-20');
INSERT INTO NOTE (note_id, url_id, title, created)
    VALUES (4, 'SdASD4321', 'tggitlest', '30-NOV-20');

INSERT INTO USER_NOTE_PARAMS (params_id, change_possibility, private_access, encryption, user_id, note_id)
    VALUES (1, 'T', 'F', 'T', 1, 2);
INSERT INTO USER_NOTE_PARAMS (params_id, change_possibility, private_access, encryption, user_id, note_id)
    VALUES (2, 'T', 'T', 'F', 4, 3);
INSERT INTO USER_NOTE_PARAMS (params_id, user_id, note_id)
    VALUES (3, 4, 3);
INSERT INTO USER_NOTE_PARAMS (params_id, user_id, note_id)
    VALUES (4, 4, 4);
    
INSERT INTO PRIVATE_ACCESS (access_id, user_id, note_id) VALUES (1, 1, 2);
INSERT INTO PRIVATE_ACCESS (access_id, user_id, note_id) VALUES (2, 2, 2);
INSERT INTO PRIVATE_ACCESS (access_id, user_id, note_id) VALUES (3, 3, 3);
INSERT INTO PRIVATE_ACCESS (access_id, user_id, note_id) VALUES (4, 4, 2);

