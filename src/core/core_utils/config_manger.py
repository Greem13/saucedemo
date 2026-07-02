from src.core.core_utils.json_reader import JsonReader
from src.core.core_utils.path_manager import PathManager
from src.core.core_models.config_model import Config
from src.core.logger.logger import Logger

class ConfigManager:
    _config_path = PathManager.root_path() / 'src' / 'data' / 'config.json'
    _config = None

    @classmethod
    def config(cls) -> Config:
        if cls._config is None:
            try:
                Logger.debug(f"Загрузка конфигурации из: {cls._config_path}")
                cls._config = JsonReader.get_model(Config, cls._config_path)
                Logger.debug("Конфигурация успешно загружена")
            except Exception as e:
                Logger.error(f"Ошибка загрузки конфигурации: {e}")
                raise
        return cls._config