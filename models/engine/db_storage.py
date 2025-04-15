import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


classes = {
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objs = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls is None:
                return objs
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objs[key] = obj
        else:
            for model in classes.values():
                for obj in self.__session.query(model).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
