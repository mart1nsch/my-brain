import sqlite3
from sqlite3 import Connection


def _create_connection() -> Connection:
    return sqlite3.connect('my-brain.db')


def create_tables() -> None:
    con = _create_connection()
    con.execute('CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY, text TEXT, user_or_agent TEXT)')
    con.execute('CREATE TABLE IF NOT EXISTS user_directory (directory TEXT)')
    con.commit()
    con.close()


def _return_len_chat() -> int:
    con = _create_connection()
    res = con.execute('SELECT COUNT(1) FROM chat')
    value = res.fetchone()[0]
    con.close()
    return value


def clean_chat(starting:bool) -> None:
    con = _create_connection()
    if starting:
        con.execute('DELETE FROM chat')
    elif _return_len_chat() == 5:
        res = con.execute('SELECT MIN(id) FROM chat')
        id = res.fetchone()[0]
        con.execute(f"DELETE FROM chat WHERE id = {id}")
    con.commit()
    con.close()


def include_chat_data(text:str, user_or_agent:str) -> None:
    con = _create_connection()
    clean_chat(False)
    con.execute('INSERT INTO chat (text, user_or_agent) VALUES (?, ?)', (text, user_or_agent))
    con.commit()
    con.close()


def return_chat_data() -> list[tuple]:
    con = _create_connection()
    res = con.execute('SELECT text, user_or_agent FROM chat ORDER BY ID')
    values = res.fetchall()
    con.close()
    return values