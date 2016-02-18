Flask-restful URL generator
===========================

Generates list of API endpoints for flask-restful.

Outputs JSON for endpoint paths, methods and docstrings for both classes and methods (if available).


Installation:

::

  pip install flask_restful_url_generator

or clone `the repository <https://github.com/ojarva/flask-restful-url-generator>`_ and run

::

  python setup.py install

Usage:

::

  from flask_restful_url_generator import UrlList
  from flask import Flask
  from flask_restful import Resource, Api

  app = Flask(__name__)
  api = Api(app)

  # define your resources here
  # api.add_resource(YourClass, "/yourpath/...")
  api.add_resource(UrlList, "/", resource_class_kwargs={"api": api})

