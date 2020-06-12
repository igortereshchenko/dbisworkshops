CREATE OR REPLACE TRIGGER trig_users
BEFORE INSERT ON "USERS"
FOR EACH ROW
BEGIN
    IF :new."name" IS NULL
    THEN
        raise_application_error(-20110,'Name of user must be specified');
    END IF;

    IF LENGTH(:new."name") > 40
    THEN
        raise_application_error(-20111,'Name is to long (must be not more than 40 characters)');
    END IF;

    IF LOWER(:new."name") LIKE '%[!a-z]%'
    THEN
        raise_application_error(-20112,'Name must contain only latin characters');
    END IF;



    IF :new."last_name" IS NOT NULL
    THEN
        IF LENGTH(:new."last_name") > 55
        THEN
            raise_application_error(-20121,'Last name is to long (must be not more than 50 characters)');
        END IF;

        IF LOWER(:new."last_name") LIKE '%[!a-z]%'
        THEN
            raise_application_error(-20122,'Last name must contain only latin characters');
        END IF;
    END IF;



    IF :new."lang_code" IS NULL
    THEN
        raise_application_error(-20130,'Language code must be specified');
    END IF;
    IF :new."lang_code" NOT IN ('az', 'sq', 'am', 'en', 'ar', 'af', 'eu', 'bn', 'be', 'my', 'bg',
                                'bs', 'vi', 'cy', 'hy', 'haw', 'ht', 'hi', 'el', 'ka', 'gl', 'gu',
                                'da', 'eo', 'et', 'zu', 'iw', 'ig', 'yi', 'id', 'ga', 'is', 'es',
                                'it', 'yo', 'kk', 'km', 'kn', 'ca', 'ky', 'zh', 'zh-CN', 'zh-TW',
                                'ko', 'co', 'ku', 'xh', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg',
                                'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nl', 'de', 'no', 'or',
                                'pa', 'fa', 'pl', 'pt', 'ps', 'ru', 'rw', 'ro', 'sm', 'ceb', 'sr',
                                'st', 'si', 'sd', 'sk', 'sl', 'so', 'sw', 'su', 'tg', 'th', 'ta',
                                'tt', 'te', 'tr', 'tk', 'hu', 'uz', 'ug', 'uk', 'ur', 'tl', 'fi',
                                'fr', 'fy', 'ha', 'hmn', 'hr', 'cs', 'ny', 'sv', 'sn', 'gd', 'jw',
                                'ja')
    THEN
        raise_application_error(-20131,'Not maintained or incorrect language code given');
    END IF;



    IF :new."username" IS NULL
    THEN
        raise_application_error(-20140,'Username must be specified');
    END IF;

    IF :new."username" < 5 OR :new."username" > 45
    THEN
        raise_application_error(-20141,'username field must contain between 5 and 45 characters');
    END IF;

    IF :new."username" LIKE '%[!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_]%'
    THEN
        raise_application_error(-20142,'username allowed to contain only characters of latin script, numbers and underscore symbol');
    END IF;

    IF :new."password" IS NULL
    THEN
        raise_application_error(-20150,'password must be specified');
    END IF;
    /*
    Other characteristics (length and format) do not checked due to probable encrypting of passwords
    */



    IF :new."reg_date" IS NULL
    THEN
        raise_application_error(-20160,'Registration date must be specified');
    END IF;

    IF :new."reg_date" < '2020-06-12 03:00:00'
    THEN
        raise_application_error(-20161,'Registration date incorrect (can not be earlier than DB created)');
    END IF;
END;
/



CREATE OR REPLACE TRIGGER trig_dialogs
BEFORE INSERT ON "DIALOGS"
FOR EACH ROW
BEGIN
    IF :new."initiator_id" IS NULL
    THEN
        raise_application_error(-20210,'ID of user-initiator must be specified');
    END IF;



    IF :new."target_id" IS NULL
    THEN
        raise_application_error(-20220,'ID of user with whom dialog started must be specified');
    END IF;
END;
/



CREATE OR REPLACE TRIGGER trig_messages
BEFORE INSERT ON "MESSAGES"
FOR EACH ROW
BEGIN
    IF :new."date" IS NULL
    THEN
        raise_application_error(-20310,'Date of sent message must be specified');
    END IF;
    IF :new."date" < '2020-06-12 03:00:00'
    THEN
        raise_application_error(-20311,'Date of sent message incorrect (can not be earlier than DB created)');
    END IF;



    IF :new."dialog_id" IS NULL
    THEN
        raise_application_error(-20320,'Dialog ID in message must be specified');
    END IF;



	IF :new."sender_id" IS NULL
    THEN
        raise_application_error(-20330,'ID of sender must be specified');
    END IF;
    IF :new."receiver_id" IS NULL
    THEN
        raise_application_error(-20340,'ID of receiver must be specified');
    END IF;

	IF :new."sender_id" NOT IN SELECT initiator_id FROM "DIALOGS" WHERE "DIALOGS"."initiator_id" = :new."dialog_id"
    THEN
        IF :new."sender_id" NOT IN SELECT target_id FROM "DIALOGS" WHERE "DIALOGS"."initiator_id" = :new."dialog_id"
        THEN
            raise_application_error(-20331,'ID of sender incorrect: sender is not initiator nor target user of dialog');
        ELSE
            IF :new."receiver_id" NOT IN SELECT initiator_id FROM "DIALOGS" WHERE "DIALOGS"."initiator_id" = :new."dialog_id"
            THEN
                raise_application_error(-20341,'ID of receiver incorrect: receiver is not initiator while sender is target. Probably incorrect dialog ID');
            END IF;
        END IF;
    ELSE
        IF :new."receiver_id" NOT IN SELECT target_id FROM "DIALOGS" WHERE "DIALOGS"."initiator_id" = :new."dialog_id"
        THEN
            raise_application_error(-20342,'ID of receiver incorrect: receiver is not target while sender is initiator. Probably incorrect dialog ID');
        END IF;
    END IF;



    IF :new."s_l" IS NULL
    THEN
        raise_application_error(-20350,'Source language code must be specified');
    END IF;
    IF :new."s_l"   NOT IN      ('az', 'sq', 'am', 'en', 'ar', 'af', 'eu', 'bn', 'be', 'my', 'bg',
                                'bs', 'vi', 'cy', 'hy', 'haw', 'ht', 'hi', 'el', 'ka', 'gl', 'gu',
                                'da', 'eo', 'et', 'zu', 'iw', 'ig', 'yi', 'id', 'ga', 'is', 'es',
                                'it', 'yo', 'kk', 'km', 'kn', 'ca', 'ky', 'zh', 'zh-CN', 'zh-TW',
                                'ko', 'co', 'ku', 'xh', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg',
                                'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nl', 'de', 'no', 'or',
                                'pa', 'fa', 'pl', 'pt', 'ps', 'ru', 'rw', 'ro', 'sm', 'ceb', 'sr',
                                'st', 'si', 'sd', 'sk', 'sl', 'so', 'sw', 'su', 'tg', 'th', 'ta',
                                'tt', 'te', 'tr', 'tk', 'hu', 'uz', 'ug', 'uk', 'ur', 'tl', 'fi',
                                'fr', 'fy', 'ha', 'hmn', 'hr', 'cs', 'ny', 'sv', 'sn', 'gd', 'jw',
                                'ja')
    THEN
        raise_application_error(-20351,'Not maintained or incorrect source language code given');
    END IF;



    IF :new."t_l" IS NULL
    THEN
        raise_application_error(-20160,'Translation language code must be specified');
    END IF;
    IF :new."t_l"   NOT IN      ('az', 'sq', 'am', 'en', 'ar', 'af', 'eu', 'bn', 'be', 'my', 'bg',
                                'bs', 'vi', 'cy', 'hy', 'haw', 'ht', 'hi', 'el', 'ka', 'gl', 'gu',
                                'da', 'eo', 'et', 'zu', 'iw', 'ig', 'yi', 'id', 'ga', 'is', 'es',
                                'it', 'yo', 'kk', 'km', 'kn', 'ca', 'ky', 'zh', 'zh-CN', 'zh-TW',
                                'ko', 'co', 'ku', 'xh', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg',
                                'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nl', 'de', 'no', 'or',
                                'pa', 'fa', 'pl', 'pt', 'ps', 'ru', 'rw', 'ro', 'sm', 'ceb', 'sr',
                                'st', 'si', 'sd', 'sk', 'sl', 'so', 'sw', 'su', 'tg', 'th', 'ta',
                                'tt', 'te', 'tr', 'tk', 'hu', 'uz', 'ug', 'uk', 'ur', 'tl', 'fi',
                                'fr', 'fy', 'ha', 'hmn', 'hr', 'cs', 'ny', 'sv', 'sn', 'gd', 'jw',
                                'ja')
    THEN
        raise_application_error(-20361,'Not maintained or incorrect translation language code given');
    END IF;



    IF :new."text" IS NULL
    THEN
        raise_application_error(-20170, 'Message must contain text');
    END IF;
    IF LENGTH(:new."text") > 65536
    THEN
        raise_application_error(-20171, 'Message text is to long ');
    END IF;


    IF :new."translation" IS NOT NULL
    THEN
        IF :new."s_l" = :new."t_l"
        THEN
            raise_application_error(-20181, 'Text must not be translated when source and translation languages are equal');
        END IF;
    END IF;
END;
