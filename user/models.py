from flask import Flask, json, jsonify, request, session, redirect, render_template
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

    def get_my_terms(self):
        response = term_collection.find(
            {"created_by": {"$eq": session['user']['email']}}, {"_id": 0, "created_by": 0})
        # print(loads(dumps(response)))
        return loads(dumps(response))


class Term:
    def get(self, term):
        response = term_collection.find_one({"term": term})
        if response:
            return jsonify(response['definition']), 200
        else:
            return jsonify({"error": "Could not find that term, please try again"}), 404

    def create(self):
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

    def edit(self, term):
        print(term)
        term_edit = term_collection.find_one({"term": term})
        print(term_edit)
        term_edit['definition'] = request.form.get('term-definition')
        print(request.form.get('term-definition'))
        term_collection.save(term_edit)
        return jsonify('saved term'), 200
