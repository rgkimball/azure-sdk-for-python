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

from .copy_sink import CopySink


class SqlDWSink(CopySink):
    """A copy activity SQL Data Warehouse sink.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param pre_copy_script: SQL pre-copy script. Type: string (or Expression
     with resultType string).
    :type pre_copy_script: object
    :param allow_poly_base: Indicates to use PolyBase to copy data into SQL
     Data Warehouse when applicable. Type: boolean (or Expression with
     resultType boolean).
    :type allow_poly_base: object
    :param poly_base_settings: Specifies PolyBase-related settings when
     allowPolyBase is true.
    :type poly_base_settings: ~azure.mgmt.datafactory.models.PolybaseSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'pre_copy_script': {'key': 'preCopyScript', 'type': 'object'},
        'allow_poly_base': {'key': 'allowPolyBase', 'type': 'object'},
        'poly_base_settings': {'key': 'polyBaseSettings', 'type': 'PolybaseSettings'},
    }

    def __init__(self, **kwargs):
        super(SqlDWSink, self).__init__(**kwargs)
        self.pre_copy_script = kwargs.get('pre_copy_script', None)
        self.allow_poly_base = kwargs.get('allow_poly_base', None)
        self.poly_base_settings = kwargs.get('poly_base_settings', None)
        self.type = 'SqlDWSink'
