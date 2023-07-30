from pydantic import BaseModel, validator
from pydantic.networks import HttpUrl

from tests.API.custom_validators import validate_swapi_urls


class Root(BaseModel):
    people: HttpUrl
    planets: HttpUrl
    films: HttpUrl
    species: HttpUrl
    vehicles: HttpUrl
    starships: HttpUrl

    @validator("*")
    def validate_url(cls, v):
        return validate_swapi_urls(v)
