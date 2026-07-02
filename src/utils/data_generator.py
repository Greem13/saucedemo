from faker import Faker

class DataGenerator:
    _faker = Faker()

    @classmethod
    def get_password(cls):
        return cls._faker.password()

    @classmethod
    def get_user_name(cls):
        return cls._faker.user_name()

    @classmethod
    def get_first_name(cls):
        return cls._faker.first_name()

    @classmethod
    def get_last_name(cls):
        return cls._faker.last_name()

    @classmethod
    def get_postcode(cls):
        return cls._faker.postcode()


