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

from .resource_py3 import Resource


class ConsumerGroup(Resource):
    """Single item in List or Get Consumer group operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar created_at: Exact time the message was created.
    :vartype created_at: datetime
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    :param user_metadata: User Metadata is a placeholder to store user-defined
     string data with maximum length 1024. e.g. it can be used to store
     descriptive data, such as list of teams and their contact information also
     user-defined configuration settings can be stored.
    :type user_metadata: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'user_metadata': {'key': 'properties.userMetadata', 'type': 'str'},
    }

    def __init__(self, *, user_metadata: str=None, **kwargs) -> None:
        super(ConsumerGroup, self).__init__(**kwargs)
        self.created_at = None
        self.updated_at = None
        self.user_metadata = user_metadata
