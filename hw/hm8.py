import sqlite3

connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        movie_id INTEGER,
        rating INTEGER
    )
""")

cursor.execute("DELETE FROM reviews")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM movies")

cursor.execute("""
    INSERT INTO users (name)
    VALUES
        ('Алиса'),
        ('Бектур'),
        ('Дана'),
        ('Тимур'),
        ('Мария')
""")

cursor.execute("""
    INSERT INTO movies (title, genre)
    VALUES
        ('Начало', 'Sci-Fi'),
        ('Интерстеллар', 'Sci-Fi'),
        ('Тёмный рыцарь', 'Action'),
        ('Паразиты', 'Thriller'),
        ('Побег из Шоушенка', 'Drama'),
        ('Дюна', 'Sci-Fi')
""")

cursor.execute("""
    INSERT INTO reviews (user_id, movie_id, rating)
    VALUES
        (1, 1, 9),
        (1, 2, 10),
        (1, 5, 10),
        (2, 1, 8),
        (2, 3, 9),
        (2, 4, 7),
        (3, 2, 9),
        (3, 4, 10),
        (4, 3, 10),
        (4, 5, 9),
        (5, 1, 7),
        (5, 2, 8)
""")

connect.commit()

print("1. Пользователь, фильм и оценка:")
cursor.execute("""
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
""")
for row in cursor.fetchall():
    print(row)

print("2. Все фильмы:")
cursor.execute("""
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
""")
for row in cursor.fetchall():
    print(row)

print("3. Оценки:")
cursor.execute("""
    SELECT AVG(rating), MAX(rating), MIN(rating)
    FROM reviews
""")
res = cursor.fetchone()

print("Средняя:", round(res[0], 2))
print("Максимальная:", res[1])
print("Минимальная:", res[2])

connect.close()
