from django.apps import AppConfig
from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
