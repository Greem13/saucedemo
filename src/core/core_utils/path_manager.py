from pathlib import Path

class PathManager:
    @staticmethod
    def root_path():
        root = Path(__file__).parent.parent.parent.parent
        return root