from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Vehicle(BaseModel):
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    created: datetime
    crew: str
    edited: datetime
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    pilots: List[HttpUrl]
    films: List[HttpUrl]
    url: HttpUrl
    vehicle_class: str


class Vehicles(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Vehicle]
