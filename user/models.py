from flask import Flask, json, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from db import user_collection, term_collection
import uuid
from bson.json_util import dumps, loads


class User:
    def initialize_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def register(self):
        print(request.form)
        user = {
            '_id': uuid.uuid4().hex,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if user_collection.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400

        if user_collection.insert_one(user):
            return self.initialize_session(user)

        return jsonify({"error": "Register failed"}), 400

    def login(self):
        user = user_collection.find_one({"email": request.form.get('email')})
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.initialize_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401

    def logout(self):
        session.clear()
        return redirect('/')


class Term:
    def get_term(self, term):
        response = term_collection.find_one({"term": term})
        if response:
            return jsonify(response['definition']), 200
        else:
            return jsonify({"error": "Could not find that term, please try again"}), 404

    def create_term(self):
        payload = {
            "created_by": session['user']['email'],
            "term": request.form.get('term-name'),
            "definition": request.form.get('term-definition')
        }
        if term_collection.find_one({"term": request.form.get('term-name')}):
            return jsonify({"error": "term already has a definition"}), 400
        else:
            term_collection.insert_one(payload)
            return jsonify('Term created'), 200
