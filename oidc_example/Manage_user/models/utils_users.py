import sqlite3


def get_users():
    conn = sqlite3.connect("data/manage_RP")
    sql = '''
    select * from dbuser where delete_flg = 'false' order by userid
    '''
    data = conn.execute(sql).fetchall()
    conn.close()
    return data


def get_user_by_id(user_id):
    conn = sqlite3.connect("data/manage_RP")
    sql = '''
    select * from dbuser where userid = ? and delete_flg = 'false'
    '''
    data = conn.execute(sql, (user_id,)).fetchone()
    conn.close()

    return data


def get_user_by_username(username):
    conn = sqlite3.connect("data/manage_RP")
    sql = '''
    select password from dbuser where username = ? and delete_flg = 'false'
    '''
    data = conn.execute(sql, (username,)).fetchone()[0]
    conn.close()

    return data


def delete_user_by_id(userid):
    conn = sqlite3.connect("data/manage_RP")
    sql1 = '''
    delete from dbuser where userid = ?
    '''
    conn.execute(sql1, (userid,))
    conn.commit()
    conn.close()
    return userid


def insert_user_by_id(username, password, email, admin_flg):
    conn = sqlite3.connect("data/manage_RP")
    sql_dbuser = '''
    insert into dbuser (username, password, email, admin_flg, delete_flg) VALUES (?, ?, ?, ?, 'false')
    '''
    conn.execute(sql_dbuser, (username, password, email, admin_flg,))
    conn.commit()
    conn.close()

    return True


def update_user_by_id(user_id, password, admin_flg):
    conn = sqlite3.connect("data/manage_RP")
    sql_dbuser = '''
    update dbuser set password = ?, admin_flg = ? where userid = ?
    '''
    conn.execute(sql_dbuser, (password, admin_flg, user_id,))
    conn.commit()
    conn.close()

    return True

