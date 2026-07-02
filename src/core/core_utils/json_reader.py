import json
from pydantic import BaseModel
from typing import Type, TypeVar
from src.core.logger.logger import Logger

M = TypeVar('M', bound=BaseModel)

class JsonReader:
    @classmethod
    def get_model(cls, model: Type[M], path: str) -> M:
        Logger.debug(f"Открытие файла: {path}")
        with open(path, 'r', encoding='utf-8') as file:
            Logger.debug("Файл открыт, чтение JSON")
            data = json.load(file)
        Logger.debug("JSON прочитан, валидация через Pydantic")
        result = model(**data)
        Logger.debug("Данные успешно валидированы")
        return result