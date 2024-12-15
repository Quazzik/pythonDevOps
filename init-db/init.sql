CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,        -- Уникальный идентификатор для каждой записи
    surname VARCHAR(255) NOT NULL, -- Фамилия
    name VARCHAR(255) NOT NULL,    -- Имя
    patronymic VARCHAR(255),       -- Отчество (необязательное поле)
    group_name VARCHAR(50)         -- Группа (необязательное поле)
);