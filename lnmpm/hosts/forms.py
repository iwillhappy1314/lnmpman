# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from lnmpm.hosts.models import Hosts


class HostsForm(Form):
    """Register form."""

    site = StringField('域名',
                       validators=[DataRequired(), Length(min=3, max=25)])
    client = StringField('客户',
                         validators=[DataRequired(), Length(min=6, max=40)])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(HostsForm, self).__init__(*args, **kwargs)
        self.site = None