-------------------------------------------------------------------------------
-- 用户主表
CREATE TABLE dk_user (
    user_id VARCHAR(20) NOT NULL PRIMARY KEY,	-- 用户名
    user_roles TEXT,				-- ROLE_ADMIN, ROLE_USER, ROLE_...
    user_privileges TEXT,			-- cache

    master_email VARCHAR(128) NOT NULL UNIQUE,	-- 用户主email
    email2 VARCHAR(128),			-- email
    email_more BOOL,				-- 还有别的email?

    phone_mobile VARCHAR(20),			--
    phone_office VARCHAR(20),			--
    phone_home VARCHAR(20),			--
    phone_more BOOL,				--

    private_key TEXT,				--

    real_name TEXT,				-- 真实姓名
    title TEXT,					-- 职务
    org TEXT,					-- 单位
    addr TEXT					-- 地址
);

CREATE INDEX dk_user_master_email ON dk_user(master_email);

-- 更多用户信息
CREATE TABLE dk_user_info (
    user_id TEXT,
    info_type INTEGER, -- { email, phone, }
    info TEXT,
    FOREIGN KEY(user_id) REFERENCES dk_user(user_id)
);

CREATE INDEX dk_user_info_user_id ON dk_user_info(user_id);

-------------------------------------------------------------------------------
-- 记录用户操作的log
CREATE TABLE dk_history (
    log_id  INTERGER PRIMARY KEY,
    datetime TEXT,
    user_id TEXT,
    operation TEXT, --   OP_REGISTER, OP_MODIFY_INFO, 
		    --   OP_LOGIN, OP_LOGOUT
		    --   OP_SYSTEM_INIT,
		    --   OP_KEY_REQUEST, OP_KEY_GEN, OP_KEY_DOWNLOAD,
		    --   OP_KEY_EXPIRE
    detail TEXT	    --	 ?
);

-------------------------------------------------------------------------------
-- privilege lookup table
CREATE TABLE dk_priv_name (
    priv_name TEXT,
    priv_display_name TEXT
);

-- role lookup table
CREATE TABLE dk_role_name (
    role_name TEXT,
    role_display_name TEXT
);

CREATE TABLE dk_role (
    role_name TEXT,
    role_priv TEXT,
    FOREIGN KEY(role_priv) REFERENCES dk_priv_name(priv_name),
    FOREIGN KEY(role_name) REFERENCES dk_role_name(role_name)
);

-------------------------------------------------------------------------------

