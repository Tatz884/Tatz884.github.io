DELETE FROM tasks; -- not speed-optimal method, but OK
ALTER TABLE tasks AUTO_INCREMENT = 1;
TRUNCATE TABLE dones;