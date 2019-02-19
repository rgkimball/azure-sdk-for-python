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

from .proxy_resource_py3 import ProxyResource


class ServerEndpoint(ProxyResource):
    """Server Endpoint object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param server_local_path: Server Local path.
    :type server_local_path: str
    :param cloud_tiering: Cloud Tiering. Possible values include: 'on', 'off'
    :type cloud_tiering: str or ~azure.mgmt.storagesync.models.enum
    :param volume_free_space_percent: Level of free space to be maintained by
     Cloud Tiering if it is enabled.
    :type volume_free_space_percent: int
    :param tier_files_older_than_days: Tier files older than days.
    :type tier_files_older_than_days: int
    :param friendly_name: Friendly Name
    :type friendly_name: str
    :param server_resource_id: Server Resource Id.
    :type server_resource_id: str
    :param provisioning_state: ServerEndpoint Provisioning State
    :type provisioning_state: str
    :param last_workflow_id: ServerEndpoint lastWorkflowId
    :type last_workflow_id: str
    :param last_operation_name: Resource Last Operation Name
    :type last_operation_name: str
    :ivar sync_status: Server Endpoint sync status
    :vartype sync_status:
     ~azure.mgmt.storagesync.models.ServerEndpointSyncStatus
    :param offline_data_transfer: Offline data transfer. Possible values
     include: 'on', 'off'
    :type offline_data_transfer: str or ~azure.mgmt.storagesync.models.enum
    :ivar offline_data_transfer_storage_account_resource_id: Offline data
     transfer storage account resource ID
    :vartype offline_data_transfer_storage_account_resource_id: str
    :ivar offline_data_transfer_storage_account_tenant_id: Offline data
     transfer storage account tenant ID
    :vartype offline_data_transfer_storage_account_tenant_id: str
    :param offline_data_transfer_share_name: Offline data transfer share name
    :type offline_data_transfer_share_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'volume_free_space_percent': {'maximum': 100, 'minimum': 0},
        'tier_files_older_than_days': {'maximum': 2147483647, 'minimum': 0},
        'sync_status': {'readonly': True},
        'offline_data_transfer_storage_account_resource_id': {'readonly': True},
        'offline_data_transfer_storage_account_tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_local_path': {'key': 'properties.serverLocalPath', 'type': 'str'},
        'cloud_tiering': {'key': 'properties.cloudTiering', 'type': 'str'},
        'volume_free_space_percent': {'key': 'properties.volumeFreeSpacePercent', 'type': 'int'},
        'tier_files_older_than_days': {'key': 'properties.tierFilesOlderThanDays', 'type': 'int'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'server_resource_id': {'key': 'properties.serverResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'last_workflow_id': {'key': 'properties.lastWorkflowId', 'type': 'str'},
        'last_operation_name': {'key': 'properties.lastOperationName', 'type': 'str'},
        'sync_status': {'key': 'properties.syncStatus', 'type': 'ServerEndpointSyncStatus'},
        'offline_data_transfer': {'key': 'properties.offlineDataTransfer', 'type': 'str'},
        'offline_data_transfer_storage_account_resource_id': {'key': 'properties.offlineDataTransferStorageAccountResourceId', 'type': 'str'},
        'offline_data_transfer_storage_account_tenant_id': {'key': 'properties.offlineDataTransferStorageAccountTenantId', 'type': 'str'},
        'offline_data_transfer_share_name': {'key': 'properties.offlineDataTransferShareName', 'type': 'str'},
    }

    def __init__(self, *, server_local_path: str=None, cloud_tiering=None, volume_free_space_percent: int=None, tier_files_older_than_days: int=None, friendly_name: str=None, server_resource_id: str=None, provisioning_state: str=None, last_workflow_id: str=None, last_operation_name: str=None, offline_data_transfer=None, offline_data_transfer_share_name: str=None, **kwargs) -> None:
        super(ServerEndpoint, self).__init__(**kwargs)
        self.server_local_path = server_local_path
        self.cloud_tiering = cloud_tiering
        self.volume_free_space_percent = volume_free_space_percent
        self.tier_files_older_than_days = tier_files_older_than_days
        self.friendly_name = friendly_name
        self.server_resource_id = server_resource_id
        self.provisioning_state = provisioning_state
        self.last_workflow_id = last_workflow_id
        self.last_operation_name = last_operation_name
        self.sync_status = None
        self.offline_data_transfer = offline_data_transfer
        self.offline_data_transfer_storage_account_resource_id = None
        self.offline_data_transfer_storage_account_tenant_id = None
        self.offline_data_transfer_share_name = offline_data_transfer_share_name
