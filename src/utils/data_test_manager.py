from src.core.core_utils.path_manager import PathManager
from src.core.core_utils.json_reader import JsonReader
from src.models.data_test.data_test_model import DataTest
from src.core.logger.logger import Logger

class DataTestManager:
    _data_test_path = PathManager.root_path() / 'src' / 'data' / 'data_test.json'
    _data_test = None

    @classmethod
    def data(cls) -> DataTest:
        if cls._data_test is None:
            try:
                Logger.debug(f"Загрузка тестовых данных из: {cls._data_test_path}")
                cls._data_test = JsonReader.get_model(DataTest, cls._data_test_path)
                Logger.debug("Тестовые данные успешно загружены")
            except Exception as e:
                Logger.error(f"Ошибка загрузки тестовых данных: {e}")
                raise
        return cls._data_test