--Вік клієнта не менше 18 років.
ALTER TABLE clients
ADD CONSTRAINT clients_age CHECK (client_age >= 18);
--Пароль не менше 8 символів.
ALTER TABLE clients
ADD CONSTRAINT clients_pass CHECK (LENGTH(client_pass) >= 8);
--Телефон має бути в форматі +3800000000000
ALTER TABLE clients
ADD CONSTRAINT clients_phone CHECK (client_phone like '+380%');
--Телефон має бути в форматі +3800000000000
ALTER TABLE clients
ADD CONSTRAINT clients_phone_l CHECK (LENGTH(client_phone) = 13);
--Не можна зареєструватися на дві події в один і той час.
ALTER TABLE guests
ADD CONSTRAINT unique_event_time UNIQUE(client_phone, event_time);