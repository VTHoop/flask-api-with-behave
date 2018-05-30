__author__ = 'hooper-p'

from src.app import app


def before_feature(context, feature):
    context.client = app.test_client()

