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


class ReferenceVmFragment(Model):
    """Details of a Reference Vm.

    :param user_name: The username of the virtual machine
    :type user_name: str
    :param password: The password of the virtual machine. This will be set to
     null in GET resource API
    :type password: str
    """

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, *, user_name: str=None, password: str=None, **kwargs) -> None:
        super(ReferenceVmFragment, self).__init__(**kwargs)
        self.user_name = user_name
        self.password = password
