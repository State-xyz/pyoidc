import sqlite3


def get_user_by_username(username):
    conn = sqlite3.connect("data/manage_RP")
    sql = '''
    select password from dbuser where username = ? and delete_flg = 'false'
    '''
    data = conn.execute(sql, (username,)).fetchone()[0]
    conn.close()

    return data


