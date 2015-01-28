# -*- coding: utf-8 -*-

from routes import Mapper

import pprint

#: @type routes: routes.Mapper
routes = None


class RoutingNotInitialized(Exception):
    pass


class RouteNotFound(Exception):
    pass


def init():
    """
    Creates and initializes all current routes
    """
    global routes

    routes = Mapper()
    routes.connect(None, "/ec2/instances/{id}/get_status", method='modules.ec2')


def match(route):
    if routes is None:
        raise RoutingNotInitialized

    context = routes.match(route)

    if context is None:
        raise RouteNotFound

    return context


def match_call(route):
    context = match(route)
    my_import(context['method'])


def my_import(name):
    mod = __import__(name)
    pprint.pprint(mod)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, 'EC2')

    pprint(mod)
    return mod
