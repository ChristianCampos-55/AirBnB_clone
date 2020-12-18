#!/usr/bin/python3
"""database engine modified using sqlalchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.base_model import Base
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DBstorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for session and connection"""
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        running_environment = os.environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if running_environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects"""
        classes = [User, Place, State, City, Amenity, Review]
        all_obj = []
        if cls:
            all_obj = self.__session.query(cls).all()
        else:
            for class_name in classes:
                query = self.__session.query(class_name).all()
                for element in query:
                    all_obj.append(element)
        new_dict = {}
        for element in all_obj:
            new_dict[element.__class__.
                           __name__ + "." + element.id] = element
        return(new_dict)

    def new(self, obj):
        """add  a new object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changesin open session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from current session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads table"""
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = session()

    def close(self):
        """closes session"""
        self.__session.close()
