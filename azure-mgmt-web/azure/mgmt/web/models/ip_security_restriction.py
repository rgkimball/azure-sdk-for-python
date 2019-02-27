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


class IpSecurityRestriction(Model):
    """IP security restriction on an app.

    :param ip_address: IP address the security restriction is valid for.
     It can be in form of pure ipv4 address (required SubnetMask property) or
     CIDR notation such as ipv4/mask (leading bit match). For CIDR,
     SubnetMask property must not be specified.
    :type ip_address: str
    :param subnet_mask: Subnet mask for the range of IP addresses the
     restriction is valid for.
    :type subnet_mask: str
    :param vnet_subnet_resource_id: Virtual network resource id
    :type vnet_subnet_resource_id: str
    :param vnet_traffic_tag: (internal) Vnet traffic tag
    :type vnet_traffic_tag: int
    :param subnet_traffic_tag: (internal) Subnet traffic tag
    :type subnet_traffic_tag: int
    :param action: Allow or Deny access for this IP range.
    :type action: str
    :param tag: Defines what this IP filter will be used for. This is to
     support IP filtering on proxies. Possible values include: 'Default',
     'XffProxy'
    :type tag: str or ~azure.mgmt.web.models.IpFilterTag
    :param priority: Priority of IP restriction rule.
    :type priority: int
    :param name: IP restriction rule name.
    :type name: str
    :param description: IP restriction rule description.
    :type description: str
    """

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'subnet_mask': {'key': 'subnetMask', 'type': 'str'},
        'vnet_subnet_resource_id': {'key': 'vnetSubnetResourceId', 'type': 'str'},
        'vnet_traffic_tag': {'key': 'vnetTrafficTag', 'type': 'int'},
        'subnet_traffic_tag': {'key': 'subnetTrafficTag', 'type': 'int'},
        'action': {'key': 'action', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'IpFilterTag'},
        'priority': {'key': 'priority', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IpSecurityRestriction, self).__init__(**kwargs)
        self.ip_address = kwargs.get('ip_address', None)
        self.subnet_mask = kwargs.get('subnet_mask', None)
        self.vnet_subnet_resource_id = kwargs.get('vnet_subnet_resource_id', None)
        self.vnet_traffic_tag = kwargs.get('vnet_traffic_tag', None)
        self.subnet_traffic_tag = kwargs.get('subnet_traffic_tag', None)
        self.action = kwargs.get('action', None)
        self.tag = kwargs.get('tag', None)
        self.priority = kwargs.get('priority', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
