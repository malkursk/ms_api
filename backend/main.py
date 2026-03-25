from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .database import engine
from . import models
from .routers import router

# Создаем таблицы
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🏛️ Музей-выставка",
    description="""
    REST API для управления музейными экспонатами и выставками
    
    Основные возможности:
    - 📊 Управление владельцами экспонатов
    - 🖼️ Управление экспонатами и их типами  
    - 🏛️ Управление местами выставок
    - 🚚 Управление перемещениями экспонатов
    - 📊 Аналитика и статистика
    
    Для удобства:
    - Endpoint'ы сгруппированы по категориям
    - Каждый endpoint имеет описание
    - Ответы содержат поле `sql` с выполненными запросами к БД
    """,
    version="1.0.1",
    license_info={
        "name": "@malsoft",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Подключаем все роутеры
app.include_router(router, prefix="/api/v1", tags=["api"])

@app.get("/", tags=["🏠 Главная"])
def read_root():
    return {
        "message": "Добро пожаловать в API Музея-выставки России", 
        "docs": "/docs",
        "description": "Используйте /docs для просмотра документации API"
    }

@app.get("/health", tags=["🔧 Система"])
def health_check():
    """Проверка работоспособности API"""
    return {"status": "ok", "message": "API работает корректно"}