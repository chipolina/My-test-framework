from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl, validator


class Planet(BaseModel):
    climate: str
    created: datetime
    diameter: int
    edited: datetime
    films: List[HttpUrl]
    gravity: str
    name: str
    orbital_period: int
    population: str
    residents: List[HttpUrl]
    rotation_period: str
    surface_water: str
    terrain: str
    url: HttpUrl

    @validator("gravity")
    def validate_gravity(cls, v):
        if v == 'N/A':
            return v
        try:
            return float(v.split()[0])
        except:
            raise ValueError("Gravity should starts with integer")

    @validator("population")
    def validate_population(cls, v):
        if v == 'unknown':
            return v
        try:
            return int(v.split()[0])
        except:
            raise ValueError("Population should be integer")


class Planets(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Planet]
