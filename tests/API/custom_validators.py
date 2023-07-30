def validate_swapi_urls(v):
    if not v:
        return v
    if not isinstance(v, list):
        v = [v]
    for url in v:
        if not url.startswith("https://swapi.dev"):
            raise ValueError("URL must start with 'https://swapi.dev'")
    return v
