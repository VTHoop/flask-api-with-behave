__author__ = 'hooper-p'

from behave import given, then
from src.app import bikes


@given('The flask application is running')
def flask_running(context):
    assert context.client
    print('Flask is up and running!!!')


@then('I should receive a 200 response')
def success_response(context):
    assert(context.client.get('/').status == '200 OK')


@then('The user should see Hello, World')
def hello_world(context):
    assert(context.client.get('/').data.decode("utf-8") == 'Hello, World')


@given('a service pings bike service GET URI without an ID')
def get_bikes(context):
    assert(context.client.get('/bikeapp/api/v1/bikes'))


@given('a service pings the bike service GET URI for a bad bike ID')
def get_a_bike(context, bike_id=1):

    found = False

    for bike in bikes:
        if bike['_id'] == bike_id:
            found = True

    assert(not found)


@then('I should receive a 404 response')
def success_response(context):
    assert(context.client.get('/bikeapp/api/v1/bikes/1').status == '404 NOT FOUND')
