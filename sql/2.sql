INSERT INTO user (ip)
SELECT "error"
WHERE NOT EXISTS(
        SELECT 1
        FROM user
        WHERE ip = "error"
    );