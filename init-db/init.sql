CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,        -- ���������� ������������� ��� ������ ������
    surname VARCHAR(255) NOT NULL, -- �������
    name VARCHAR(255) NOT NULL,    -- ���
    patronymic VARCHAR(255),       -- �������� (�������������� ����)
    group_name VARCHAR(50)         -- ������ (�������������� ����)
);