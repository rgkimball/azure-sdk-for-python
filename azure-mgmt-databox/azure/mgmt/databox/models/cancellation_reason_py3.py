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


class CancellationReason(Model):
    """Reason for cancellation.

    All required parameters must be populated in order to send to Azure.

    :param reason: Required. Reason for cancellation.
    :type reason: str
    """

    _validation = {
        'reason': {'required': True},
    }

    _attribute_map = {
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str, **kwargs) -> None:
        super(CancellationReason, self).__init__(**kwargs)
        self.reason = reason
