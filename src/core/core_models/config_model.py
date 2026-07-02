from typing import Dict, List

from pydantic import BaseModel

class Config(BaseModel):
    browser: str
    browser_options: Dict[str, List[str]]
    firefox_profile: Dict[str, bool]
    timeout: int
    base_url: str
    page_load_strategy: str

    def get_current_browser_options(self):
        return self.browser_options.get(self.browser)