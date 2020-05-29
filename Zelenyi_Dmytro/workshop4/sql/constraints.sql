ALTER TABLE contacts
    ADD CONSTRAINT contacts_fk FOREIGN KEY(email) REFERENCES photographers(email);

ALTER TABLE services
    ADD CONSTRAINT services_fk FOREIGN KEY(email) REFERENCES photographers(email);
    
ALTER TABLE comments
    ADD CONSTRAINT comments_customer_fk FOREIGN KEY(email_customer) REFERENCES customers(email);    
    
ALTER TABLE comments
    ADD CONSTRAINT comments_photographer_fk FOREIGN KEY(email_photographer) REFERENCES photographers(email);
    
ALTER TABLE portfolios
    ADD CONSTRAINT portfolios_fk FOREIGN KEY(author_email) REFERENCES photographers(email);

ALTER TABLE history
    ADD CONSTRAINT history_customer_fk FOREIGN KEY(customer) REFERENCES customers(email);
    
ALTER TABLE history
    ADD CONSTRAINT history_photographer_fk FOREIGN KEY(photographer) REFERENCES photographers(email);

ALTER TABLE photographers
    ADD CONSTRAINT check_experience CHECK (experience > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_object_shooting CHECK (object_shooting > 0);

ALTER TABLE services
    ADD CONSTRAINT check_portrait_shooting CHECK (portrait_shooting > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_wedding_photo_shoot CHECK (wedding_photo_shoot > 0);

ALTER TABLE services
    ADD CONSTRAINT check_family_photo_shot CHECK (family_photo_shot > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_event_photography CHECK (event_photography > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_reportage_shooting CHECK (reportage_shooting > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_childrens_photo_shoot CHECK (childrens_photo_shoot > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_interior_shooting CHECK (interior_shooting > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_photosession_love_story CHECK (photosession_love_story > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_pregnant_photoshoot CHECK (pregnant_photoshoot > 0);
    
ALTER TABLE services
    ADD CONSTRAINT check_neither CHECK (neither > 0);
