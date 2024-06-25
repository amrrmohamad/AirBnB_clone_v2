#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
import sqlalchemy
from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class DBStorage:
    """interaacts with the MySQL database"""
    __session = None
    __engine = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on database"""
        new_dictionary = {}
        for clss in classes:
            if cls is classes[clss] or cls is clss or cls is None:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dictionary[key] = obj
        return (new_dictionary)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        fact_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(fact_sess)
        self.__session = Session

    def new(self, obj):
        """add the object to database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes in database """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
