-- this strategy using raw MySQL script also does not work, somehow the data is not deleted
DELETE FROM tasks; -- not speed-optimal method, but OK
ALTER TABLE tasks AUTO_INCREMENT = 1;
TRUNCATE TABLE dones;