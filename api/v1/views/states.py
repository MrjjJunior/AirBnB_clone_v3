#!/usr/bin/python3
''' RESTful API for class State '''
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/api/v1/states', methods=['GET'], strict_slashes=False)
def get_state():
    ''' return state in json form '''
    state_list = [s.to_dict() for s in storage.all('State').values()]
    return jsonify(state_list)


@app_views.route('/state/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    ''' Return state '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route(
    '/states/<state_id>',
    methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    ''' deletes states obj '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/api/v1/states/<state_id>', methods=['POST'], strict_slashes=False)
def create_state():
    ''' creates new state object '''
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in request.get_json():
        return jsonify({"error": "Misssing name"}), 400
    else:
        obj_data = request.get_json()
        obj = State(**obj_data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/api/v1/states/<states_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    ''' updates state '''
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    obj = storage.get(State, states_id)
    if obj is None:
        abort(404)
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
