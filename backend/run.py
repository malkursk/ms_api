#!/usr/bin/env python3
"""
Основной файл запуска приложения Музей-выставка в масштабе России
"""

import uvicorn
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
from .seed import seed_database

def check_existing_data():
    """Проверяет, есть ли уже данные в базе"""
    db = SessionLocal()
    try:
        # Считаем количество владельцев
        owners_count = db.query(models.Owner).count()
        print(f"📊 В базе данных найдено {owners_count} владельцев")
        return owners_count
    except Exception as e:
        print(f"⚠️ Ошибка при проверке базы данных: {e}")
        return 0
    finally:
        db.close()

def init_database():
    """Инициализация базы данных"""
    print("🔄 Создание таблиц в базе данных...")
    models.Base.metadata.create_all(bind=engine)
    
    # Проверяем, есть ли уже данные
    owners_count = check_existing_data()
    
    # Заполняем только если владельцев меньше 5
    if owners_count < 5:
        print("🌱 Заполнение базы данных тестовыми данными...")
        seed_database()
        print("✅ База данных заполнена!")
    else:
        print("✅ База данных уже содержит данные, заполнение не требуется")

def main():
    """Основная функция запуска"""
    print("🚀 Запуск приложения Музей-выставка в масштабе России")
    print("📊 Инициализация базы данных...")
    
    # Инициализируем БД
    init_database()
    
    print("🌐 Запуск сервера FastAPI...")
    print("📚 Документация API будет доступна по адресу: http://localhost:8000/docs")
    print("🛑 Для остановки сервера нажмите Ctrl+C")
    
    # Запускаем сервер
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()