from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, HttpUrl, validator

from tests.API.custom_validators import validate_swapi_urls


class People(BaseModel):
    name: str
    birth_year: str
    eye_color: str
    gender: str
    hair_color: str
    height: str
    mass: str
    skin_color: str
    homeworld: str
    films: List[HttpUrl]
    species: List[HttpUrl]
    starships: List[HttpUrl]
    vehicles: List[HttpUrl]
    url: HttpUrl
    created: datetime
    edited: datetime

    @validator("films", "species", "starships", "vehicles", 'url')
    def validate_url(cls, v):
        return validate_swapi_urls(v)


class Peoples(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[People]
