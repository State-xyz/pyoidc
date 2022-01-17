import sqlite3
from werkzeug.security import generate_password_hash


def get_studentinfo_by_username(username):
    conn = sqlite3.connect("data/manageUser")
    sql = '''
    select u.userid, u.username, s.student_id, s.sub, s.given_name,
        s.family_name, s.email, s.address, s.phone_number, s.class_id 
    from dbuser u inner join student s on u.userid = s.userid 
    where u.username = ? and u.delete_flg = 'false'
    '''
    data = conn.execute(sql, (username,)).fetchone()
    conn.close()

    return data


def update_user_by_id(user_id, password, given_name, family_name, email, address,
                      phone_number, class_id):
    conn = sqlite3.connect("data/manageUser")
    sql_dbuser = '''
    update dbuser set password = ? where userid = ?
    '''
    if password:
        password_insert = generate_password_hash(password)
        conn.execute(sql_dbuser, (password_insert, user_id,))
    conn.commit()
    sql_userinfo = '''
    update student set given_name = ?, family_name = ?, email = ?, address = ?, 
    phone_number = ?, class_id= ? where userid = ?
    '''
    conn.execute(sql_userinfo, (given_name, family_name, email, address,
                                phone_number, class_id, user_id))
    conn.commit()
    conn.close()

    return True
