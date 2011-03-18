CREATE TABLE dk_user (
    user_id TEXT NOT NULL PRIMARY KEY,  -- 用户名
    master_email TEXT NOT NULL UNIQUE,  -- 用户主email
    real_name TEXT,			-- 真实姓名
    title TEXT,  -- 职务
    org TEXT,    -- 单位
    addr TEXT,   -- 地址
    FOREIGN KEY(master_email) REFERENCES dk_user_email(email)
);

CREATE INDEX dk_user_master_email ON dk_user(master_email);

CREATE TABLE dk_user_email (
    email TEXT NOT NULL, -- 用户可以有多个email
    user_id TEXT,
    FOREIGN KEY(user_id) REFERENCES dk_user(user_id)
);

CREATE TABLE dk_user_phone (
    phone TEXT NOT NULL, -- 用户可以有多个电话
    user_id TEXT,
    FOREIGN KEY(user_id) REFERENCES dk_user(user_id)
);

