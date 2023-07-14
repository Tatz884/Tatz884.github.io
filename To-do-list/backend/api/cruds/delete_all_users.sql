DELETE FROM users; -- not speed-optimal method, but OK
ALTER TABLE users AUTO_INCREMENT = 1;