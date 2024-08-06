#!/usr/bin/python3
'''
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
'''
from flask import jsonify, abort
from  models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    ''' gets the list pf all state objects '''
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    ''' gets state id '''
    state = storage.get(State, state_id)

    if state:
        return jsonsify(State, state_id)
    else:
        return abort(404)
    

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    ''' deletes a state '''
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    ''' creates new state '''
    if request.content_type != 'application/json':
        return abort(404, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    kwargs = request.get_json()

    if 'name' not in kwargs:
        abort(400, 'Missing name')

    state = State(**kwargs)
    state.save()
    return jsonify(state.to_dict()), 200
