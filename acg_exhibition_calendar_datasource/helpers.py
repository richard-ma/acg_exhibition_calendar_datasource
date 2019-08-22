from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scrapy.utils.project import get_project_settings


class DBHelper():
    def __init__(self):
        self.engine = create_engine(SettingsHelper().get_setting('CONNECTION_STRING'))
        self.DBSession = sessionmaker(bind=self.engine)

    def get_session(self):
        session = DBSession()
        return session


class SettingsHelper():
    def __init__(self):
        self.settings = get_project_settings()

    def get_setting(self, name, default=None):
        return settings.get(name, default)
