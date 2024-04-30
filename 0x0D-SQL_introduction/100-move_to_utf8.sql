-- Step 1: Convert the database charset and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Convert the table charset and collation
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 3: Alter the `id` column to match the desired structure
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN id int(11) DEFAULT NULL;

-- Step 4: Convert the field charset and collation
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(256) DEFAULT NULL;
