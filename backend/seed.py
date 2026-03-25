from sqlalchemy.orm import Session
from faker import Faker
import random
from datetime import datetime, timedelta, date
from .database import SessionLocal
from . import models

fake = Faker('ru_RU')

# 📌 СОГЛАСОВАННЫЕ ФИО ПО ПОЛУ
male_first_names = [
    'Александр', 'Алексей', 'Андрей', 'Антон', 'Артем', 'Борис', 'Вадим', 'Валентин', 
    'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', 'Владислав', 'Геннадий', 
    'Георгий', 'Григорий', 'Даниил', 'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Иван', 
    'Игорь', 'Илья', 'Кирилл', 'Константин', 'Лев', 'Леонид', 'Максим', 'Марк', 
    'Матвей', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Петр', 'Роман', 
    'Руслан', 'Сергей', 'Станислав', 'Степан', 'Тимофей', 'Федор', 'Юрий', 'Ярослав'
]

female_first_names = [
    'Александра', 'Алена', 'Алина', 'Алиса', 'Алла', 'Анастасия', 'Ангелина', 'Анна', 
    'Валентина', 'Валерия', 'Варвара', 'Вера', 'Вероника', 'Виктория', 'Галина', 
    'Дарья', 'Диана', 'Ева', 'Евгения', 'Екатерина', 'Елена', 'Елизавета', 'Жанна', 
    'Зоя', 'Ирина', 'Кира', 'Ксения', 'Лариса', 'Лидия', 'Любовь', 'Людмила', 
    'Маргарита', 'Марина', 'Мария', 'Надежда', 'Наталья', 'Нина', 'Оксана', 'Олеся', 
    'Ольга', 'Полина', 'Светлана', 'София', 'Тамара', 'Татьяна', 'Ульяна', 'Юлия', 'Яна'
]

male_last_names = [
    'Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Попов', 'Лебедев', 'Козлов', 
    'Новиков', 'Морозов', 'Волков', 'Соловьев', 'Васильев', 'Зайцев', 'Павлов', 
    'Семенов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьев', 'Федоров', 'Михайлов', 
    'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселев', 'Макаров', 'Андреев'
]

female_last_names = [
    'Иванова', 'Петрова', 'Сидорова', 'Смирнова', 'Кузнецова', 'Попова', 'Лебедева', 
    'Козлова', 'Новикова', 'Морозова', 'Волкова', 'Соловьева', 'Васильева', 'Зайцева', 
    'Павлова', 'Семенова', 'Голубева', 'Виноградова', 'Богданова', 'Воробьева', 
    'Федорова', 'Михайлова', 'Беляева', 'Тарасова', 'Белова', 'Комарова', 'Орлова', 
    'Киселева', 'Макарова', 'Андреева'
]

male_middle_names = [
    'Александрович', 'Алексеевич', 'Андреевич', 'Антонович', 'Артемович', 'Борисович',
    'Вадимович', 'Валентинович', 'Валерьевич', 'Васильевич', 'Викторович', 'Витальевич',
    'Владимирович', 'Владиславович', 'Геннадьевич', 'Георгиевич', 'Григорьевич',
    'Данилович', 'Денисович', 'Дмитриевич', 'Евгеньевич', 'Егорович', 'Иванович',
    'Игоревич', 'Ильич', 'Кириллович', 'Константинович', 'Львович', 'Леонидович',
    'Максимович', 'Маркович', 'Матвеевич', 'Михайлович', 'Никитич', 'Николаевич',
    'Олегович', 'Павлович', 'Петрович', 'Романович', 'Русланович', 'Сергеевич',
    'Станиславович', 'Степанович', 'Тимофеевич', 'Федорович', 'Юрьевич', 'Ярославович'
]

female_middle_names = [
    'Александровна', 'Алексеевна', 'Андреевна', 'Антоновна', 'Артемовна', 'Борисовна',
    'Вадимовна', 'Валентиновна', 'Валерьевна', 'Васильевна', 'Викторовна', 'Витальевна',
    'Владимировна', 'Владиславовна', 'Геннадьевна', 'Георгиевна', 'Григорьевна',
    'Даниловна', 'Денисовна', 'Дмитриевна', 'Евгеньевна', 'Егоровна', 'Ивановна',
    'Игоревна', 'Ильинична', 'Кирилловна', 'Константиновна', 'Львовна', 'Леонидовна',
    'Максимовна', 'Марковна', 'Матвеевна', 'Михайловна', 'Никитична', 'Николаевна',
    'Олеговна', 'Павловна', 'Петровна', 'Романовна', 'Руслановна', 'Сергеевна',
    'Станиславовна', 'Степановна', 'Тимофеевна', 'Федоровна', 'Юрьевна', 'Ярославовна'
]

def generate_birth_date():
    """Генерирует дату рождения с 1960 по 2010 год"""
    start_date = date(1960, 1, 1)
    end_date = date(2010, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

def generate_move_date():
    """Генерирует дату передвижения с 2020 года по текущую дату"""
    start_date = datetime(2020, 1, 1)
    end_date = datetime.now()
    return fake.date_time_between(start_date=start_date, end_date=end_date)

def generate_owner_data():
    """Генерирует согласованные ФИО по полу"""
    is_male = random.choice([True, False])
    
    if is_male:
        first_name = random.choice(male_first_names)
        last_name = random.choice(male_last_names)
        middle_name = random.choice(male_middle_names)
    else:
        first_name = random.choice(female_first_names)
        last_name = random.choice(female_last_names)
        middle_name = random.choice(female_middle_names)
    
    # 30% случаев без отчества
    if random.random() < 0.3:
        middle_name = None
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,
        'birth_date': generate_birth_date()
    }

def seed_database():
    db = SessionLocal()
    
    try:
        # Очистка существующих данных (только если нужно перезаполнить)
        print("🧹 Очистка старых данных...")
        db.query(models.Move).delete()
        db.query(models.Wing).delete()
        db.query(models.Place).delete()
        db.query(models.Type).delete()
        db.query(models.Owner).delete()
        db.commit()
    except Exception as e:
        print(f"⚠️ Ошибка при очистке: {e}")
        db.rollback()
    
    # Заполнение владельцев
    print("👥 Создание владельцев...")
    owners = []
    for i in range(150):
        owner_data = generate_owner_data()
        owner = models.Owner(
            email=fake.unique.email(),
            first_name=owner_data['first_name'],
            last_name=owner_data['last_name'],
            middle_name=owner_data['middle_name'],
            birth_date=owner_data['birth_date']
        )
        owners.append(owner)
        db.add(owner)
    db.commit()
    print("✅ Владельцы созданы")
    
    # Заполнение типов экспонатов
    print("🏷️ Создание типов экспонатов...")
    type_names = [
        "Картина", "Скульптура", "Артефакт", "Рукопись", "Фотография",
        "Источник вдохновения", "Оружие", "Мебель", "Ювелирное изделие", "Керамика",
        "Текстиль", "Монета", "Книга", "Прибор", "Инструмент"
    ]

    types = []
    for name in type_names:
        type_obj = models.Type(name=name)
        types.append(type_obj)
        db.add(type_obj)
    db.commit()
    print("✅ Типы экспонатов созданы")
    
    # Заполнение выставок
    print("🏛️ Создание мест выставок...")
    places = []
    russian_cities = [
        "Москва", "Курск", "Обоянь", "Калининград", "Ставрополь",
        "Нижний Новгород", "Анапа", "Владивосток", "Омск", "Ялта",
        "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград"
    ] * 3
    
    for city in russian_cities[:50]:
        place = models.Place(
            location=f"{city}, {fake.street_address()}",
            scale=round(random.uniform(0.5, 2.0), 2)
        )
        places.append(place)
        db.add(place)
    db.commit()
    print("✅ Места выставок созданы")
    
    # Заполнение экспонатов
    print("🖼️ Создание экспонатов (40-60 на владельца)...")
    wings = []
    total_wings = 0
    for owner in owners:
        wings_count = random.randint(40, 60)
        total_wings += wings_count
        for _ in range(wings_count):
            wing = models.Wing(
                owner_id=owner.id,
                type_id=random.choice(types).id,
                profit=round(random.uniform(0.1, 3.0), 2),
                name=fake.catch_phrase()
            )
            wings.append(wing)
            db.add(wing)
    db.commit()
    print(f"✅ Создано {total_wings} экспонатов")
    
    # Заполнение передвижений
    print("🚚 Создание передвижений (10-50 на экспонат)...")
    current_date = datetime.now()
    total_moves = 0
    
    for wing in wings:
        moves_count = random.randint(10, 50)
        total_moves += moves_count
        
        # Генерируем даты передвижений с 2020 года по текущую дату
        move_dates = sorted([generate_move_date() for _ in range(moves_count)])
        
        for move_date in move_dates:
            move = models.Move(
                wing_id=wing.id,
                place_id=random.choice(places).id,
                price=round(random.uniform(1000, 50000), 2),
                dt=move_date
            )
            db.add(move)
    
    db.commit()
    db.close()
    print(f"✅ Создано {total_moves} передвижений")
    print("🎉 База данных заполнена успешно!")
    
    
    
    
  