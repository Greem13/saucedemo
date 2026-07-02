class AuthPageParser:
    @staticmethod
    def parse_password(text: str) -> str:
        return text.split(':')[1].strip()

    @staticmethod
    def parse_available_usernames(text: str, locked_out_username=None) -> list[str]:
        accepted_usernames = text.split(':')[1].split()
        if locked_out_username:
            if locked_out_username in accepted_usernames:
                accepted_usernames.remove(locked_out_username)
        return accepted_usernames