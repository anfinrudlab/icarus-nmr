#!/usr/bin/env python3
"""
DATAQ 4108 Device Level code
author: Valentyn Stadnytskyi
Date: November 2017 - August 2021

This is an example script that starts "mock" device channel access server.

The variable SERVER_NAME needs to be changed to launch the server with a unique name that corresponds to the desired server.


"""
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
import caproto
from textwrap import dedent
from pdb import pm

from numpy import random, array, zeros, ndarray, nan, isnan
from time import time,sleep

SERVER_NAME = 'mock'


if __name__ == '__main__':
    from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
    import caproto
    from textwrap import dedent
    from pdb import pm

    from numpy import random, array, zeros, ndarray, nan, isnan
    from time import time, sleep

    from pdb import pm

    from icarus_nmr.event_handler import Handler
    from icarus_nmr.event_daq import DAQ
    from icarus_nmr.event_client import Client
    from icarus_nmr.event_server import Server

    client = Client()
    daq = DAQ(client)
    daq.init()
    #daq.start()

    handler = Handler(daq, client)
    handler.init()
    handler.fault_detection_init()
    handler.start()

    ioc_options, run_options = ioc_arg_parser(
        default_prefix=f'event_handler_{SERVER_NAME}:',
        desc=dedent(Server.__doc__))

    ioc = Server(**ioc_options)
    ioc.device = handler
    run(ioc.pvdb, **run_options)
