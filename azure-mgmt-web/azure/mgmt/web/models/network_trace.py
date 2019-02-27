# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NetworkTrace(Model):
    """Network trace.

    :param path: Local file path for the captured network trace file.
    :type path: str
    :param status: Current status of the network trace operation, same as
     Operation.Status (InProgress/Succeeded/Failed).
    :type status: str
    :param message: Detailed message of a network trace operation, e.g. error
     message in case of failure.
    :type message: str
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NetworkTrace, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)
