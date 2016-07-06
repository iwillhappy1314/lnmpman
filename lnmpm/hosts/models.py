# -*- coding: utf-8 -*-
"""User models."""

from lnmpm.database import Column, Model, SurrogatePK, db


class Hosts(SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'hosts'
    site = Column(db.String(80), unique=True, nullable=False)
    client = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, site, client, **kwargs):
        """Create instance."""
        db.Model.__init__(self, site=site, client=client, **kwargs)
        if site:
            self.site = site
        else:
            self.site = None