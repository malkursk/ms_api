from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import List, Optional

class OwnerBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_date: date

class TypeBase(BaseModel):
    name: str

class WingBase(BaseModel):
    owner_id: int
    type_id: int
    profit: float
    name: str

class PlaceBase(BaseModel):
    location: str
    scale: float

class MoveBase(BaseModel):
    wing_id: int
    place_id: int
    price: float
    dt: datetime

class OwnerCreate(OwnerBase):
    pass

class TypeCreate(TypeBase):
    pass

class WingCreate(WingBase):
    pass

class PlaceCreate(PlaceBase):
    pass

class MoveCreate(MoveBase):
    pass

class Owner(OwnerBase):
    id: int
    
    class Config:
        from_attributes = True

class Type(TypeBase):
    id: int
    
    class Config:
        from_attributes = True

class Wing(WingBase):
    id: int
    
    class Config:
        from_attributes = True

class WingWithDetails(Wing):
    owner: Owner
    type: Type
    
    class Config:
        from_attributes = True

class Place(PlaceBase):
    id: int
    
    class Config:
        from_attributes = True

class Move(MoveBase):
    id: int
    
    class Config:
        from_attributes = True

# 📌 НОВЫЕ СХЕМЫ ДЛЯ ОПЕРАЦИЙ
class WingUpdate(WingBase):
    """Схема для обновления экспоната"""
    pass

class DeleteResponse(BaseModel):
    """Схема для ответа при удалении"""
    message: str
    deleted_id: int

class OwnerStats(BaseModel):
    owner_id: int
    email: str
    first_name: str
    last_name: str
    wings_count: int

class WingProfitability(BaseModel):
    wing_id: int
    wing_name: str
    total_profit: float
    total_moves: int
    avg_profit_per_move: float

class PlaceProfitability(BaseModel):
    place_id: int
    location: str
    total_revenue: float
    total_moves: int

class TraveledWingStats(BaseModel):
    wing_id: int
    wing_name: str
    moves_count: int
    total_logistics_cost: float