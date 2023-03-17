import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor() #выполнять операции/транзакции

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, name TEXT, age TEXT, description TEXT)")
    
    db.commit()

async def create_profile(user_id):
    user = cur.execute("SELECT 1 from profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET photo = '{}', name = '{}', age = '{}', description = '{}' WHERE user_id == '{}'".format(data['photo'], data['name'], data['age'], data['description'], user_id))
        db.commit()

async def show_profile(user_id):
    cur.execute("SELECT * FROM profile WHERE user_id == '{}'".format(user_id))
    all_info = cur.fetchone()
    return all_info