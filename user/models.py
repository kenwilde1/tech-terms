from flask import Flask, json, jsonify, request, session, redirect, render_template
from passlib.hash import pbkdf2_sha256
from db import user_collection, term_collection
import uuid
from bson.json_util import dumps, loads


class User:
    def initialize_session(self, user):
        """
        Creates a session for a given user. Returns that user session.
        """
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def register(self):
        """
        Register a new User with MongoDB. Returns JSON response. 
        """
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
        """
        Checks User credentials with MongoDB. Allows / Denies access.
        Returns a User session or a JSON errored response.
        """
        user = user_collection.find_one({"email": request.form.get('email')})
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.initialize_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401

    def logout(self):
        """
        Logs User out of system and clears the session.
        """
        session.clear()
        return redirect('/')

    def get_my_terms(self):
        """
        Returns User's created terms.
        """
        response = term_collection.find(
            {"created_by": {"$eq": session['user']['email']}}, {"_id": 0, "created_by": 0})
        return loads(dumps(response))


class Term:
    def get(self, term):
        """
        Returns a requested term and definition.
        """
        response = term_collection.find_one({"term": term})
        if response:
            return jsonify([response['definition'], term]), 200
        else:
            return jsonify({"error": "Could not find that term, please try again"}), 404

    def create(self):
        """
        Create a term record in MongoDB. Returns JSON response.
        """
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
        """
        Finds and edits the definition of a requested term.
        """
        term_edit = term_collection.find_one({"term": term})
        term_edit['definition'] = request.form.get('term-definition')
        term_collection.save(term_edit)
        return jsonify('saved term'), 200

    def delete(self, term):
        """
        Finds and deletes a requested term. User must be term owner.
        """
        term_to_delete = term_collection.find_one({"term": term})
        if term_to_delete['created_by'] == session['user']['email']:
            term_collection.delete_one({"term": term})
            return jsonify("Term deleted succesfully"), 200
        else:
            return jsonify({"error": "Request made not from term owner"}), 403

    def get_all(self):
        """
        Finds and returns all term definitions.
        """
        response = term_collection.find({}, {"_id": 0})
        return loads(dumps(response))
