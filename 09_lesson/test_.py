from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:9013@localhost:5432/QA"
db = create_engine(db_connection_string)

inspector = inspect(db)
print(inspector.get_table_names())


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'users' in names


def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql1 = text("INSERT INTO users(\"user_email\") VALUES (:new_name)")
    connection.execute(sql1, {"new_name": "Skypro@comm"})

    transaction.commit()
    # connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql2 = text("""UPDATE users
        SET "subject_id" = :subject_id
        WHERE "user_email" = :user_email""")
    connection.execute(sql2, {"subject_id": 1000, "user_email": "Skypro@comm"})
    transaction.commit()
    # connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql3 = text("""DELETE FROM users
        WHERE "user_email" = :user_email or "subject_id" = :subject_id""")
    connection.execute(sql3, {"user_email": "Skypro@comm", "subject_id": 1000})

    transaction.commit()
    connection.close()
