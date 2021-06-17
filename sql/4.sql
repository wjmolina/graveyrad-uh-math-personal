CREATE TRIGGER IF NOT EXISTS comment_updated
AFTER
UPDATE ON comment BEGIN
UPDATE comment
SET updated_at = CURRENT_TIMESTAMP
WHERE _id = OLD._id;
END;