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


class AvailablePrebuiltEntityModel(Model):
    """Available Prebuilt entity model for using in an application.

    :param name: The entity name.
    :type name: str
    :param description: The entity description and usage information.
    :type description: str
    :param examples: Usage examples.
    :type examples: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'examples': {'key': 'examples', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AvailablePrebuiltEntityModel, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.examples = kwargs.get('examples', None)
