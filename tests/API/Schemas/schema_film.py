from typing import List, Optional
from datetime import date

from pydantic import BaseModel, validator, HttpUrl

from tests.API.custom_validators import validate_swapi_urls


class Film(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: date
    characters: List[HttpUrl]
    planets: List[HttpUrl]
    starships: List[HttpUrl]
    vehicles: List[HttpUrl]
    species: List[HttpUrl]
    created: str
    edited: str
    url: HttpUrl

    @validator("characters", "planets", "starships", "vehicles", "species",'url')
    def validate_url(cls, v):
        return validate_swapi_urls(v)


class Films(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Film]
