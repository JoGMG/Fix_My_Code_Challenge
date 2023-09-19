#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
from status_server.api.v1.views.index import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
