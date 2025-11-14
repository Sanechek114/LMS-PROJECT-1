create_db_query = '''CREATE TABLE animals (
    id    INTEGER PRIMARY KEY AUTOINCREMENT
                  NOT NULL,
    name  TEXT    NOT NULL,
    type  TEXT    NOT NULL,
    day   INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year  INTEGER NOT NULL,
    breed TEXT    NOT NULL,
    code  TEXT
);'''


def search_query(s):
    return f'''SELECT * FROM animals
    WHERE id = '{s}' OR name LIKE '%{s}%' OR type LIKE '%{s}%' OR
        code LIKE "%{s}%" OR breed LIKE "%{s}%"
    ORDER BY name'''


def delete_query(s):
    return f'DELETE FROM animals WHERE id = {s}'


def create_row_query(name, type, day, month, year, breed, code):
    return f"INSERT INTO animals(name, type, day, month, year, breed, code) \
        VALUES('{name}', '{type}', {day}, \
            {month}, {year}, '{breed}', '{code}')"


'%{self.search}%'
