


class Response:
    """
    Класс для валидации и проверки ответа
    """

    def __init__(self, response, schema=None):
        self.response = response
        self.response_json = self.response.json()
        self.response_status = self.response.status_code
        self.schema = schema

    def check_status_code(self, status_code):
        """
        Проверяем код ответа
        """

        assert self.response_status == status_code, f"Responce status code {self.response_status} " \
                                                    f"is not equal expected code {status_code}"
        return self

    def validate(self):
        """
        Валидируем схему
        Если json приходит в виде списка, то проходим по каждому
        элементу и валидируем его
        """
        if isinstance(self.response_json, list):
            for item in self.response_json:
                self.schema.parse_obj(item)
        else:
            self.schema.parse_obj(self.response_json)

    def check_length(self, path: str, length: int):
        assert len(self.response_json[path]) <= length
