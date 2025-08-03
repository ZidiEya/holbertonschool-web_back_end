-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userId INT)
BEGIN
    DECLARE avg_weighted_score FLOAT;

    -- Compute the average weighted score for the given user
    SELECT 
        SUM(c.score * p.weight) / SUM(p.weight)
    INTO avg_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = userId;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = userId;
END;
//

DELIMITER ;
