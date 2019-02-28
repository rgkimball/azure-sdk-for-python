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


class Permissions(Model):
    """Permissions.

    :param odatatype: Microsoft.DirectoryServices.OAuth2PermissionGrant
    :type odatatype: str
    :param client_id: The objectId of the Service Principal associated with
     the app
    :type client_id: str
    :param object_id: The objectId of the permission grant
    :type object_id: str
    :param consent_type: Typically set to AllPrincipals
    :type consent_type: str
    :param principal_id: Set to null if AllPrincipals is set
    :type principal_id: object
    :param resource_id: Service Principal Id of the resource you want to grant
    :type resource_id: str
    :param scope: Typically set to user_impersonation
    :type scope: str
    :param start_time: Start time for TTL
    :type start_time: str
    :param expiry_time: Expiry time for TTL
    :type expiry_time: str
    """

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'consent_type': {'key': 'consentType', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'object'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'expiry_time': {'key': 'expiryTime', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Permissions, self).__init__(**kwargs)
        self.odatatype = kwargs.get('odatatype', None)
        self.client_id = kwargs.get('client_id', None)
        self.object_id = kwargs.get('object_id', None)
        self.consent_type = kwargs.get('consent_type', None)
        self.principal_id = kwargs.get('principal_id', None)
        self.resource_id = kwargs.get('resource_id', None)
        self.scope = kwargs.get('scope', None)
        self.start_time = kwargs.get('start_time', None)
        self.expiry_time = kwargs.get('expiry_time', None)
