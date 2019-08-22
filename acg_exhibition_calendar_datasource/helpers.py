from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from scrapy.utils.project import get_project_settings
from acg_exhibition_calendar_datasource.models import Base


class DBHelper():
    def __init__(self):
        self.engine = create_engine(SettingsHelper().get_setting('CONNECTION_STRING'), encoding="utf-8", echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.DBSession()


class SettingsHelper():
    def __init__(self):
        self.settings = get_project_settings()

    def get_setting(self, name, default=None):
        return self.settings.get(name, default)
