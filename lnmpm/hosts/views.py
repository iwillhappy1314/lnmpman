# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('hosts', __name__, url_prefix='/hosts', static_folder='../static')

