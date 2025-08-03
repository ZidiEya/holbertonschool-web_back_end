-- function sql

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE uid INT;

    -- Declare a cursor for looping through all user ids
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO uid;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Compute and update the average weighted score for each user
        UPDATE users
        SET average_score = (
            SELECT SUM(score * weight) / SUM(weight)
            FROM corrections
            JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = uid
        )
        WHERE id = uid;

    END LOOP;

    CLOSE user_cursor;
END $$

DELIMITER ;
