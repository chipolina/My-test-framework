import pytest
import requests

from tests.API.Schemas.schema_character import People, Peoples
from tests.API.Schemas.schema_film import Film, Films
from tests.API.Schemas.schema_root import Root
from tests.API.helper import Response

base_url = "https://swapi.dev/api/"


def test_api_status():
    r = requests.get(base_url)
    resp = Response(r, Root)
    resp.check_status_code(200).validate()


# def test_get_all_film():
#     r = requests.get(f"{base_url}/films")
#     resp = Response(r, Films)
#     resp.check_status_code(200).validate()
#     resp.check_length('results', 6)


def test_get_existing_film_info():
    film_id = 1
    r = requests.get(f"{base_url}/films/{film_id}")
    resp = Response(r, Film)
    resp.check_status_code(200).validate()

    assert resp.response_json['title'] == "A New Hope"


def test_get_not_existing_film():
    film_id = 10
    r = requests.get(f"{base_url}/films/{film_id}")
    resp = Response(r)
    resp.check_status_code(404)


def test_get_existing_character_info():
    character_id = 1
    r = requests.get(f"{base_url}/people/{character_id}")
    resp = Response(r, People)
    resp.check_status_code(200).validate()

    assert resp.response_json['name'] == "Luke Skywalker"


def test_get_not_existing_character():
    character_id = 200
    r = requests.get(f"{base_url}/people/{character_id}")
    resp = Response(r)
    resp.check_status_code(404)


@pytest.mark.parametrize('search_text, count, result', [("LUKE", 1, "Luke Skywalker"),
                                                        ("luke", 1, "Luke Skywalker"),
                                                        ("Lu", 2, "Luke Skywalker"),
                                                        ("r2", 1, "R2-D2")])
def test_search_character_by_name(search_text, count, result):
    r = requests.get(f"{base_url}/people/?search={search_text}")
    resp = Response(r, Peoples)
    resp.check_status_code(200).validate()
    resp.check_length('results', count)

    assert resp.response_json['results'][0]['name'] == result
