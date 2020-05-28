-- balance check
CREATE OR REPLACE TRIGGER validate_user_balance
BEFORE UPDATE ON user_config
FOR EACH ROW
BEGIN
    -- check for withdraw more than 5
    IF(:old.balance > :new.balance) AND ((:old.balance - :new.balance) < 5)  THEN
      RAISE_APPLICATION_ERROR(-20000,'Withdraw should be more than 5$.');
    END IF;

    -- check for residual balance more then 2
    IF(:old.balance > :new.balance) AND :new.balance < 2  THEN
      RAISE_APPLICATION_ERROR(-20000,'Residual balance should be more than 2$.');
    END IF;
END validate_user_balance;


-- check filter timings
CREATE OR REPLACE TRIGGER validate_user_filters_change
BEFORE INSERT ON user_actions
FOR EACH ROW
DECLARE
    filters_changed int;
BEGIN
    -- check filters editing(2 per day for users)
    SELECT  count(*) INTO filters_changed FROM user_actions WHERE user_id_fk = :new.user_id_fk
                AND action_date = :new.action_date AND action_type = 'filter_change';
    IF (filters_changed > 1) THEN
        RAISE_APPLICATION_ERROR(-20003,'More than 2 filters editing per day.');
    END IF;
END validate_user_filters_change;

-- check for profit percent more or queal 10
CREATE OR REPLACE TRIGGER validate_user_profit
BEFORE UPDATE OR INSERT ON user_config
FOR EACH ROW
BEGIN
    If(:new.profit_percent < 10) THEN
        RAISE_APPLICATION_ERROR(-20004,'Profit percent should be more or equal 10%.');
    END IF;
END validate_user_profit;

-- check for user prices
CREATE OR REPLACE TRIGGER validate_user_prices
BEFORE UPDATE OR INSERT ON user_config
FOR EACH ROW
BEGIN
    If(:new.min_price > :new.max_price) THEN
        RAISE_APPLICATION_ERROR(-20004,'Max price should be higher then min price');
    END IF;
END validate_user_profit;