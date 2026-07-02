import inspect
import logging
from src.core.core_utils.path_manager import PathManager

class Logger:
    _initialized = False
    _PROJECT_ROOT = PathManager.root_path()
    _LOG_PATH = _PROJECT_ROOT / 'log' / 'log.log'
    _logger_name = "framework"
    _MODULE_NAME_FIELD = "module_name"
    _LINENO_FIELD = "caller_lineno"

    @classmethod
    def _initialize(cls):
        if cls._initialized:
            return

        log_dir = cls._LOG_PATH.parent
        if not log_dir.exists():
            log_dir.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger(cls._logger_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            f"%(asctime)s - %(levelname)s - %({cls._MODULE_NAME_FIELD})s:%({cls._LINENO_FIELD})d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(cls._LOG_PATH, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        cls._initialized = True

    @classmethod
    def _log(cls, level: str, message: str):
        cls._initialize()
        caller_module, lineno = cls._get_caller_info()
        logger = logging.getLogger(cls._logger_name)

        log_method = getattr(logger, level.lower())
        log_method(message, extra={cls._MODULE_NAME_FIELD: caller_module, cls._LINENO_FIELD: lineno})

    @classmethod
    def info(cls, message: str):
        cls._log("INFO", message)

    @classmethod
    def debug(cls, message: str):
        cls._log("DEBUG", message)

    @classmethod
    def warning(cls, message: str):
        cls._log("WARNING", message)

    @classmethod
    def error(cls, message: str):
        cls._log("ERROR", message)

    @classmethod
    def _get_caller_info(cls):
        stack = inspect.stack()
        for frame_info in stack[2:]:
            frame = frame_info.frame
            module = inspect.getmodule(frame)
            if module and module.__name__ != __name__:
                return module.__name__, frame_info.lineno
        return "unknown", 0