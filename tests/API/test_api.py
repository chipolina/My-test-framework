import pytest
import requests

from tests.API.Schemas.schema_character import People, Peoples
from tests.API.Schemas.schema_film import Film, Films
from tests.API.Schemas.schema_planets import Planet, Planets
from tests.API.Schemas.schema_root import Root
from tests.API.Schemas.schema_vehicles import Vehicles, Vehicle
from tests.API.helper import Response
import allure

base_url = "https://swapi.dev/api/"


@pytest.mark.api
@allure.title('Check server status')
def test_api_status():
    r = requests.get(base_url)
    resp = Response(r, Root)
    resp.check_status_code(200).validate()


@pytest.mark.api
@allure.title('Get all films')
def test_get_all_film():
    r = requests.get(f"{base_url}/films")
    resp = Response(r, Films)
    resp.check_status_code(200).validate()
    resp.check_length('results', 6)


@pytest.mark.api
@allure.title('Get existing film info')
def test_get_existing_film_info():
    film_id = 1
    r = requests.get(f"{base_url}/films/{film_id}")
    resp = Response(r, Film)
    resp.check_status_code(200).validate()

    assert resp.response_json['title'] == "A New Hope"


@pytest.mark.api
@allure.title('Get not existing film')
def test_get_not_existing_film():
    film_id = 10
    r = requests.get(f"{base_url}/films/{film_id}")
    resp = Response(r)
    resp.check_status_code(404)


@pytest.mark.api
@allure.title('Get existing character info')
def test_get_existing_character_info():
    character_id = 1
    r = requests.get(f"{base_url}/people/{character_id}")
    resp = Response(r, People)
    resp.check_status_code(200).validate()

    assert resp.response_json['name'] == "Luke Skywalker"


@pytest.mark.api
@allure.title('Get not existing character')
def test_get_not_existing_character():
    character_id = 200
    r = requests.get(f"{base_url}/people/{character_id}")
    resp = Response(r)
    resp.check_status_code(404)


@pytest.mark.api
@pytest.mark.parametrize('name, count, result', [
    pytest.param("LUKE", 1, "Luke Skywalker", id='uppercase'),
    pytest.param("luke", 1, "Luke Skywalker", id='lowercase'),
    pytest.param("Lu", 2, "Luke Skywalker", id='short name'),
    pytest.param("r2", 1, "R2-D2", id='name with number')])
def test_search_character_by_name(name, count, result):
    allure.dynamic.title("test_search_character_by_name")
    allure.dynamic.description(name)
    r = requests.get(f"{base_url}/people/?search={name}")
    resp = Response(r, Peoples)
    resp.check_status_code(200).validate()
    resp.check_length('results', count)

    assert resp.response_json['results'][0]['name'] == result


@pytest.mark.api
@allure.title('Get all vehicles')
def test_get_all_vehicles():
    r = requests.get(f"{base_url}/vehicles/")
    resp = Response(r, Vehicles)
    resp.check_status_code(200).validate()


@pytest.mark.api
@allure.title('Search vehicle by id')
def test_vehicle_by_id():
    vehicle_id = 4
    r = requests.get(f"{base_url}/vehicles/{vehicle_id}")
    resp = Response(r, Vehicle)
    resp.check_status_code(200).validate()

    assert resp.response_json['name'] == "Sand Crawler"


@pytest.mark.api
@allure.title('Get non existing vehicle')
def test_get_non_existing_vehicle():
    vehicle_id = 40
    r = requests.get(f"{base_url}/vehicles/{vehicle_id}")
    resp = Response(r)
    resp.check_status_code(404)


@pytest.mark.api
@allure.title('Search vehicle by name')
@pytest.mark.parametrize('name, count, result', [pytest.param("skiff", 1, "Bantha-II cargo skiff", id="lowercase"),
                                                 pytest.param("SKIFF", 1, "Bantha-II cargo skiff", id="uppercase"),
                                                 pytest.param("sk", 2, "T-16 skyhopper", id="short name")])
def test_search_vehicle_by_name(name, count, result):
    r = requests.get(f"{base_url}/vehicles/?search={name}")
    resp = Response(r, Vehicles)
    resp.check_status_code(200).validate()
    resp.check_length('results', count)

    assert resp.response_json['results'][0]['name'] == result


@pytest.mark.api
@allure.title('Search vehicle by model')
@pytest.mark.parametrize('model_name, count, result', [pytest.param("Digger", 1, "Digger Crawler", id="capitalize"),
                                                       pytest.param("DIGGER", 1, "Digger Crawler", id="uppercase"),
                                                       pytest.param("digger", 1, "Digger Crawler", id="lowercase"),
                                                       pytest.param("dIgGeR", 1, "Digger Crawler", id="mixed")])
def test_search_vehicle_by_model(model_name, count, result):
    r = requests.get(f"{base_url}/vehicles/?search={model_name}")
    resp = Response(r, Vehicles)
    resp.check_status_code(200).validate()
    resp.check_length('results', count)

    assert resp.response_json['results'][0]['model'] == result


@pytest.mark.api
@allure.title('Search planet by id')
def test_get_planet_by_id():
    planet_id = 2
    r = requests.get(f"{base_url}/planets/{planet_id}")
    resp = Response(r, Planet)
    resp.check_status_code(200).validate()


@pytest.mark.api
@allure.title('Search not existing planet')
def test_get_non_existing_planet():
    planet_id = 400
    r = requests.get(f"{base_url}/planets/{planet_id}")
    resp = Response(r)
    resp.check_status_code(404)


@pytest.mark.api
@allure.title('Search planet by name')
@pytest.mark.parametrize('planet_name, count, result', [pytest.param("Polis", 1, "Polis Massa", id="capitalize"),
                                                        pytest.param("POLIS", 1, "Polis Massa", id="uppercase"),
                                                        pytest.param("polis", 1, "Polis Massa", id="lowercase"),
                                                        pytest.param("PoLis", 1, "Polis Massa", id="mixed")])
def test_search_planet_by_name(planet_name, count, result):
    r = requests.get(f"{base_url}/planets/?search={planet_name}")
    resp = Response(r, Planets)
    resp.check_status_code(200).validate()
    resp.check_length('results', count)

    assert resp.response_json['results'][0]['name'] == result


@pytest.mark.api
@allure.title('Get all planets')
def test_get_all_planets():
    r = requests.get(f"{base_url}/planets")
    resp = Response(r, Planets)
    resp.check_status_code(200).validate()
