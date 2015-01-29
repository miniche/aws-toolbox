# -*- coding: utf-8 -*-

import importlib

from routes import Mapper

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
    with routes.submapper(module='aws_toolbox.modules.ec2', module_class='EC2', path_prefix='/ec2') as m:
        m.connect(None, '/instances/{id}/get_status', method="get_status")
        m.connect(None, "/instances/{id}/wait_started", method="wait_started")


def match(route):
    if routes is None:
        raise RoutingNotInitialized

    context = routes.match(route)

    if context is None:
        raise RouteNotFound

    return context


def match_call(route):
    call_method(match(route))


def call_method(context):
    imported_module = importlib.import_module(context['module'])
    imported_object = getattr(imported_module, context['module_class'])()
    getattr(imported_object, context['method'])(context)

