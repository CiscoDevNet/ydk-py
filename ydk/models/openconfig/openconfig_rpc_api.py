""" openconfig_rpc_api 

This module documents a set of RPCs recommended for network
management systems (NMS) based on OpenConfig models and
conventions. The RPCs are intended to offer guidance for server
implementors as a reference for service endpoints which can meet
requirements for configuration and telemetry.

Actual implementations may provide slightly different variations
on parameters, naming, etc., or extensions which add additional
service endpoints.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CancelTelemetrySubscriptionRpc(object):
    """
    Terminates and removes an exisiting telemetry subscription
    
    .. attribute:: subscription_id
    
    	Subscription identifier as returned by the device when subscription was requested
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.subscription_id = None

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:cancelTelemetrySubscription'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.subscription_id is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['CancelTelemetrySubscriptionRpc']['meta_info']


class EditConfigCommands_Identity(object):
    """
    Base identity for subcommands for the edit\-config
    service.
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['EditConfigCommands_Identity']['meta_info']


class EditConfigRpc(object):
    """
    Modify configuration on the target device. The editConfig
    service accepts a combination of commands, each with an
    associated path specification to indicate which data should
    be modified.
    
    The commands in an editConfig request should be
    fully validated and accepted by the device before a response
    is returned.  The application of the configuration commands
    may or may not be complete when the command returns.  The NMS
    is expected to be able to track the application of the
    configuration using the operational state data in the telemetry
    stream, or by retrieving the state data using an RPC.
    
    .. attribute:: config_command
    
    	List of configuration data items, each consisting of the data model path, and corresponding data encoded based on the requested format
    	**type**\: list of :py:class:`ConfigCommand <ydk.models.openconfig.openconfig_rpc_api.EditConfigRpc.ConfigCommand>`
    
    .. attribute:: message
    
    	Error or information text associated with the return\-code value
    	**type**\: str
    
    .. attribute:: request_id
    
    	Identifier sent in request messages
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: request_id
    
    	The request id corresponding to the request
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: response_code
    
    	Numerical code corresponding to the returned message
    	**type**\: :py:class:`OpenconfigRpcResponseTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigRpcResponseTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.config_command = YList()
        self.config_command.parent = self
        self.config_command.name = 'config_command'
        self.message = None
        self.request_id = None
        self.request_id = None
        self.response_code = None


    class ConfigCommand(object):
        """
        List of configuration data items, each consisting of the
        data model path, and corresponding data encoded based on
        the requested format
        
        .. attribute:: path
        
        	Data model path corresponding to the data in the message
        	**type**\: str
        
        .. attribute:: command
        
        	The type of configuration modification requested for the corresponding path.  Note that some commands, such as 'delete' do not specify any associated data with the path
        	**type**\: :py:class:`EditConfigCommands_Identity <ydk.models.openconfig.openconfig_rpc_api.EditConfigCommands_Identity>`
        
        .. attribute:: values
        
        	Data encoded using the encoding specified in setDataEncoding, or the device's default encoding.  This data may be specified by the management system, e.g., when sending configuration data, or by the device when returning configuration or operational state / telemetry data
        	**type**\: str
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.path = None
            self.command = None
            self.values = None

        @property
        def _common_path(self):
            if self.path is None:
                raise YPYDataValidationError('Key property path is None')

            return '/openconfig-rpc-api:editConfig/openconfig-rpc-api:config-command[openconfig-rpc-api:path = ' + str(self.path) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                return True

            if self.command is not None:
                return True

            if self.values is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['EditConfigRpc.ConfigCommand']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:editConfig'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.config_command is not None:
            for child_ref in self.config_command:
                if child_ref._has_data():
                    return True

        if self.message is not None:
            return True

        if self.request_id is not None:
            return True

        if self.request_id is not None:
            return True

        if self.response_code is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['EditConfigRpc']['meta_info']


class GetConfigRpc(object):
    """
    Prompts the device to return configuration data at the path
    specified in the request.  All 'config\: true' data is
    returned.
    
    .. attribute:: data
    
    	List of configuration data items, each consisting of the data model path, and corresponding data encoded based on the requested format
    	**type**\: list of :py:class:`Data <ydk.models.openconfig.openconfig_rpc_api.GetConfigRpc.Data>`
    
    .. attribute:: message
    
    	Error or information text associated with the return\-code value
    	**type**\: str
    
    .. attribute:: path
    
    	List of data model paths to retrieve
    	**type**\: list of str
    
    .. attribute:: request_id
    
    	Identifier sent in request messages
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: request_id
    
    	The request id corresponding to the request
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: response_code
    
    	Numerical code corresponding to the returned message
    	**type**\: :py:class:`OpenconfigRpcResponseTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigRpcResponseTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.data = YList()
        self.data.parent = self
        self.data.name = 'data'
        self.message = None
        self.path = []
        self.request_id = None
        self.request_id = None
        self.response_code = None


    class Data(object):
        """
        List of configuration data items, each consisting of the
        data model path, and corresponding data encoded based on
        the requested format
        
        .. attribute:: path
        
        	Data model path corresponding to the data in the message
        	**type**\: str
        
        .. attribute:: values
        
        	Data encoded using the encoding specified in setDataEncoding, or the device's default encoding.  This data may be specified by the management system, e.g., when sending configuration data, or by the device when returning configuration or operational state / telemetry data
        	**type**\: str
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.path = None
            self.values = None

        @property
        def _common_path(self):
            if self.path is None:
                raise YPYDataValidationError('Key property path is None')

            return '/openconfig-rpc-api:getConfig/openconfig-rpc-api:data[openconfig-rpc-api:path = ' + str(self.path) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                return True

            if self.values is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['GetConfigRpc.Data']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:getConfig'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.data is not None:
            for child_ref in self.data:
                if child_ref._has_data():
                    return True

        if self.message is not None:
            return True

        if self.path is not None:
            for child in self.path:
                if child is not None:
                    return True

        if self.request_id is not None:
            return True

        if self.request_id is not None:
            return True

        if self.response_code is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['GetConfigRpc']['meta_info']


class GetDataEncodingsRpc(object):
    """
    Return the set of data encodings supported by the device for
    configuration and telemetry data modeled in YANG
    
    .. attribute:: encoding
    
    	List of identifiers indicating the supported encoding schemes
    	**type**\: list of :py:class:`OpenconfigDataEncodingTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigDataEncodingTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.encoding = YList()
        self.encoding.parent = self
        self.encoding.name = 'encoding'

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:getDataEncodings'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.encoding is not None:
            for child_ref in self.encoding:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['GetDataEncodingsRpc']['meta_info']


class GetModelsRpc(object):
    """
    Returns a repeated structure of supported data models
    
    .. attribute:: request_mode
    
    	Mode for delivering the schema data
    	**type**\: :py:class:`OpenconfigSchemaModeTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigSchemaModeTypes_Identity>`
    
    .. attribute:: schema
    
    	list of supported schemas
    	**type**\: list of :py:class:`Schema <ydk.models.openconfig.openconfig_rpc_api.GetModelsRpc.Schema>`
    
    .. attribute:: schema_format
    
    	Schema format requested, e.g., JSON\-Schema, XSD, Proto, YANG
    	**type**\: :py:class:`OpenconfigSchemaFormatTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigSchemaFormatTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.request_mode = None
        self.schema = YList()
        self.schema.parent = self
        self.schema.name = 'schema'
        self.schema_format = None


    class Schema(object):
        """
        list of supported schemas
        
        .. attribute:: model_name
        
        	Name of the corresponding YANG module
        	**type**\: str
        
        .. attribute:: model_data
        
        	Model data, formatted according to the requested format (e.g., JSON\-Schema, YANG, etc.) and using the requested mode (URI, file, etc.)
        	**type**\: str
        
        .. attribute:: model_namespace
        
        	Namespace the model belongs to, whether standard or ad\-hoc
        	**type**\: str
        
        .. attribute:: model_version
        
        	Model version \-\- for YANG models this should be at least the 'revision' but could also include a more conventional version number
        	**type**\: str
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.model_name = None
            self.model_data = None
            self.model_namespace = None
            self.model_version = None

        @property
        def _common_path(self):
            if self.model_name is None:
                raise YPYDataValidationError('Key property model_name is None')

            return '/openconfig-rpc-api:getModels/openconfig-rpc-api:schema[openconfig-rpc-api:model-name = ' + str(self.model_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.model_name is not None:
                return True

            if self.model_data is not None:
                return True

            if self.model_namespace is not None:
                return True

            if self.model_version is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['GetModelsRpc.Schema']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:getModels'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.request_mode is not None:
            return True

        if self.schema is not None:
            for child_ref in self.schema:
                if child_ref._has_data():
                    return True

        if self.schema_format is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['GetModelsRpc']['meta_info']


class GetOperationalRpc(object):
    """
    Prompts the device to return operational state data at the
    path specified in the request.  The caller may specify that
    only data marked 'operational\: true' in the schema are
    returned, otherwise all 'config\: false' data is returned
    (e.g., including the applied configuration that is part of
    operational state)
    
    .. attribute:: data
    
    	List of operational state data items, each consisting of the data model path, and corresponding data encoded based on the requested format
    	**type**\: list of :py:class:`Data <ydk.models.openconfig.openconfig_rpc_api.GetOperationalRpc.Data>`
    
    .. attribute:: message
    
    	Error or information text associated with the return\-code value
    	**type**\: str
    
    .. attribute:: oper_only
    
    	When this is set to true, the device should return only the operational state data that is marked as operational\: true. Otherwise, it should return all operational state date (config\: false)
    	**type**\: bool
    
    .. attribute:: path
    
    	List of data model paths to retrieve
    	**type**\: list of str
    
    .. attribute:: request_id
    
    	Identifier sent in request messages
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: request_id
    
    	The request id corresponding to the request
    	**type**\: int
    
    	**range:** 0..18446744073709551615
    
    .. attribute:: response_code
    
    	Numerical code corresponding to the returned message
    	**type**\: :py:class:`OpenconfigRpcResponseTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigRpcResponseTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.data = YList()
        self.data.parent = self
        self.data.name = 'data'
        self.message = None
        self.oper_only = None
        self.path = []
        self.request_id = None
        self.request_id = None
        self.response_code = None


    class Data(object):
        """
        List of operational state data items, each consisting of the
        data model path, and corresponding data encoded based on
        the requested format
        
        .. attribute:: path
        
        	Data model path corresponding to the data in the message
        	**type**\: str
        
        .. attribute:: values
        
        	Data encoded using the encoding specified in setDataEncoding, or the device's default encoding.  This data may be specified by the management system, e.g., when sending configuration data, or by the device when returning configuration or operational state / telemetry data
        	**type**\: str
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.path = None
            self.values = None

        @property
        def _common_path(self):
            if self.path is None:
                raise YPYDataValidationError('Key property path is None')

            return '/openconfig-rpc-api:getOperational/openconfig-rpc-api:data[openconfig-rpc-api:path = ' + str(self.path) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                return True

            if self.values is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['GetOperationalRpc.Data']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:getOperational'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.data is not None:
            for child_ref in self.data:
                if child_ref._has_data():
                    return True

        if self.message is not None:
            return True

        if self.oper_only is not None:
            return True

        if self.path is not None:
            for child in self.path:
                if child is not None:
                    return True

        if self.request_id is not None:
            return True

        if self.request_id is not None:
            return True

        if self.response_code is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['GetOperationalRpc']['meta_info']


class GetTelemetrySubscriptionsRpc(object):
    """
    Get the list of current telemetry subscriptions from the
    target.  This command returns a list of existing subscriptions
    not including those that are established via configuration.
    
    .. attribute:: subscription
    
    	List of current telemetry subscriptions
    	**type**\: list of :py:class:`Subscription <ydk.models.openconfig.openconfig_rpc_api.GetTelemetrySubscriptionsRpc.Subscription>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.subscription = YList()
        self.subscription.parent = self
        self.subscription.name = 'subscription'


    class Subscription(object):
        """
        List of current telemetry subscriptions
        
        .. attribute:: subscription_id
        
        	Unique id for the subscription on the device.  This is generated by the device and returned in a subscription request or when listing existing subscriptions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: collectors
        
        	List of optional collector endpoints to send data for this subscription, specified as an ip+port combination. If no collector destinations are specified, the collector destination is inferred from requester on the rpc channel
        	**type**\: list of :py:class:`Collectors <ydk.models.openconfig.openconfig_rpc_api.GetTelemetrySubscriptionsRpc.Subscription.Collectors>`
        
        .. attribute:: export_dscp_marking
        
        	The DSCP code point value to be set on telemetry messages to the collector platform
        	**type**\: int
        
        	**range:** 0..63
        
        .. attribute:: paths
        
        	List of data model paths, keyed by path name
        	**type**\: list of :py:class:`Paths <ydk.models.openconfig.openconfig_rpc_api.GetTelemetrySubscriptionsRpc.Subscription.Paths>`
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.subscription_id = None
            self.collectors = YList()
            self.collectors.parent = self
            self.collectors.name = 'collectors'
            self.export_dscp_marking = None
            self.paths = YList()
            self.paths.parent = self
            self.paths.name = 'paths'


        class Collectors(object):
            """
            List of optional collector endpoints to send data for
            this subscription, specified as an ip+port combination.
            If no collector destinations are specified, the collector
            destination is inferred from requester on the rpc channel.
            
            .. attribute:: address
            
            	IP address of collector endpoint
            	**type**\: one of { str | str }
            
            .. attribute:: port
            
            	Transport protocol port number for the collector destination
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'oc-rpc'
            _revision = '2015-10-30'

            def __init__(self):
                self.parent = None
                self.address = None
                self.port = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                if self.address is None:
                    raise YPYDataValidationError('Key property address is None')
                if self.port is None:
                    raise YPYDataValidationError('Key property port is None')

                return self.parent._common_path +'/openconfig-rpc-api:collectors[openconfig-rpc-api:address = ' + str(self.address) + '][openconfig-rpc-api:port = ' + str(self.port) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.address is not None:
                    return True

                if self.port is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
                return meta._meta_table['GetTelemetrySubscriptionsRpc.Subscription.Collectors']['meta_info']


        class Paths(object):
            """
            List of data model paths, keyed by path name
            
            .. attribute:: path
            
            	Data model path of interest
            	**type**\: str
            
            .. attribute:: filter
            
            	Regular expression to be used in filtering state leaves
            	**type**\: str
            
            .. attribute:: max_silent_interval
            
            	Maximum time in ms the target device may go without sending a message to the collector. If this time expires with suppress\-unchanged set, the target device must send an update message regardless if the data values have changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sample_frequency
            
            	Time in ms between collection and transmission of the specified data to the collector platform. The target device will sample the corresponding data (e.g,. a counter) and immediately send to the collector destination.  If sample\-frequency is set to 0, then the network device must emit an update upon every datum change
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: suppress_unchanged
            
            	If this is set to true, the target device will only send updates to the collector upon a change in data value
            	**type**\: bool
            
            

            """

            _prefix = 'oc-rpc'
            _revision = '2015-10-30'

            def __init__(self):
                self.parent = None
                self.path = None
                self.filter = None
                self.max_silent_interval = None
                self.sample_frequency = None
                self.suppress_unchanged = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                if self.path is None:
                    raise YPYDataValidationError('Key property path is None')

                return self.parent._common_path +'/openconfig-rpc-api:paths[openconfig-rpc-api:path = ' + str(self.path) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.path is not None:
                    return True

                if self.filter is not None:
                    return True

                if self.max_silent_interval is not None:
                    return True

                if self.sample_frequency is not None:
                    return True

                if self.suppress_unchanged is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
                return meta._meta_table['GetTelemetrySubscriptionsRpc.Subscription.Paths']['meta_info']

        @property
        def _common_path(self):
            if self.subscription_id is None:
                raise YPYDataValidationError('Key property subscription_id is None')

            return '/openconfig-rpc-api:getTelemetrySubscriptions/openconfig-rpc-api:subscription[openconfig-rpc-api:subscription-id = ' + str(self.subscription_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.subscription_id is not None:
                return True

            if self.collectors is not None:
                for child_ref in self.collectors:
                    if child_ref._has_data():
                        return True

            if self.export_dscp_marking is not None:
                return True

            if self.paths is not None:
                for child_ref in self.paths:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['GetTelemetrySubscriptionsRpc.Subscription']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:getTelemetrySubscriptions'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.subscription is not None:
            for child_ref in self.subscription:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['GetTelemetrySubscriptionsRpc']['meta_info']


class OpenconfigDataEncodingTypes_Identity(object):
    """
    Base identity for supported encoding for configuration and
    operational state data
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['OpenconfigDataEncodingTypes_Identity']['meta_info']


class OpenconfigRpcResponseTypes_Identity(object):
    """
    Base identity for RPC response codes
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['OpenconfigRpcResponseTypes_Identity']['meta_info']


class OpenconfigSchemaFormatTypes_Identity(object):
    """
    Base identity for supported schema formats
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['OpenconfigSchemaFormatTypes_Identity']['meta_info']


class OpenconfigSchemaModeTypes_Identity(object):
    """
    Base identity for schema retrieval modes
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['OpenconfigSchemaModeTypes_Identity']['meta_info']


class SetDataEncodingRpc(object):
    """
    Select and set one of the data encodings returned by
    getDataEncodings
    
    .. attribute:: encoding
    
    	Identifier for the encoding scheme
    	**type**\: :py:class:`OpenconfigDataEncodingTypes_Identity <ydk.models.openconfig.openconfig_rpc_api.OpenconfigDataEncodingTypes_Identity>`
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.encoding = None

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:setDataEncoding'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.encoding is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['SetDataEncodingRpc']['meta_info']


class TelemetrySubscribeRpc(object):
    """
    Request an inline subscription for data at the specified path.
    The device should send telemetry data back on the same
    connection as the subscription request.
    
    .. attribute:: collectors
    
    	List of optional collector endpoints to send data for this subscription, specified as an ip+port combination. If no collector destinations are specified, the collector destination is assumed to be the requester on the rpc channel
    	**type**\: list of :py:class:`Collectors <ydk.models.openconfig.openconfig_rpc_api.TelemetrySubscribeRpc.Collectors>`
    
    .. attribute:: collectors
    
    	List of optional collector endpoints to send data for this subscription, specified as an ip+port combination. If no collector destinations are specified, the collector destination is inferred from requester on the rpc channel
    	**type**\: list of :py:class:`Collectors <ydk.models.openconfig.openconfig_rpc_api.TelemetrySubscribeRpc.Collectors>`
    
    .. attribute:: export_dscp_marking
    
    	The DSCP code point value to be set on telemetry messages to the collector platform
    	**type**\: int
    
    	**range:** 0..63
    
    .. attribute:: export_dscp_marking
    
    	The DSCP code point value to be set on telemetry messages to the collector platform
    	**type**\: int
    
    	**range:** 0..63
    
    .. attribute:: paths
    
    	List of data model paths, keyed by path name
    	**type**\: list of :py:class:`Paths <ydk.models.openconfig.openconfig_rpc_api.TelemetrySubscribeRpc.Paths>`
    
    .. attribute:: paths
    
    	List of data model paths, keyed by path name
    	**type**\: list of :py:class:`Paths <ydk.models.openconfig.openconfig_rpc_api.TelemetrySubscribeRpc.Paths>`
    
    .. attribute:: subscription_id
    
    	Unique id for the subscription on the device.  This is generated by the device and returned in a subscription request or when listing existing subscriptions
    	**type**\: int
    
    	**range:** 0..4294967295
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        self.collectors = YList()
        self.collectors.parent = self
        self.collectors.name = 'collectors'
        self.collectors = YList()
        self.collectors.parent = self
        self.collectors.name = 'collectors'
        self.export_dscp_marking = None
        self.export_dscp_marking = None
        self.paths = YList()
        self.paths.parent = self
        self.paths.name = 'paths'
        self.paths = YList()
        self.paths.parent = self
        self.paths.name = 'paths'
        self.subscription_id = None


    class Collectors(object):
        """
        List of optional collector endpoints to send data for
        this subscription, specified as an ip+port combination.
        If no collector destinations are specified, the collector
        destination is assumed to be the requester on the rpc channel
        
        .. attribute:: address
        
        	IP address of collector endpoint
        	**type**\: one of { str | str }
        
        .. attribute:: port
        
        	Transport protocol port number for the collector destination
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.address = None
            self.port = None

        @property
        def _common_path(self):
            if self.address is None:
                raise YPYDataValidationError('Key property address is None')
            if self.port is None:
                raise YPYDataValidationError('Key property port is None')

            return '/openconfig-rpc-api:telemetrySubscribe/openconfig-rpc-api:collectors[openconfig-rpc-api:address = ' + str(self.address) + '][openconfig-rpc-api:port = ' + str(self.port) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.address is not None:
                return True

            if self.port is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['TelemetrySubscribeRpc.Collectors']['meta_info']


    class Collectors(object):
        """
        List of optional collector endpoints to send data for
        this subscription, specified as an ip+port combination.
        If no collector destinations are specified, the collector
        destination is inferred from requester on the rpc channel.
        
        .. attribute:: address
        
        	IP address of collector endpoint
        	**type**\: one of { str | str }
        
        .. attribute:: port
        
        	Transport protocol port number for the collector destination
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.address = None
            self.port = None

        @property
        def _common_path(self):
            if self.address is None:
                raise YPYDataValidationError('Key property address is None')
            if self.port is None:
                raise YPYDataValidationError('Key property port is None')

            return '/openconfig-rpc-api:telemetrySubscribe/openconfig-rpc-api:collectors[openconfig-rpc-api:address = ' + str(self.address) + '][openconfig-rpc-api:port = ' + str(self.port) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.address is not None:
                return True

            if self.port is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['TelemetrySubscribeRpc.Collectors']['meta_info']


    class Paths(object):
        """
        List of data model paths, keyed by path name
        
        .. attribute:: path
        
        	Data model path of interest
        	**type**\: str
        
        .. attribute:: filter
        
        	Regular expression to be used in filtering state leaves
        	**type**\: str
        
        .. attribute:: max_silent_interval
        
        	Maximum time in ms the target device may go without sending a message to the collector. If this time expires with suppress\-unchanged set, the target device must send an update message regardless if the data values have changed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sample_frequency
        
        	Time in ms between collection and transmission of the specified data to the collector platform. The target device will sample the corresponding data (e.g,. a counter) and immediately send to the collector destination.  If sample\-frequency is set to 0, then the network device must emit an update upon every datum change
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: suppress_unchanged
        
        	If this is set to true, the target device will only send updates to the collector upon a change in data value
        	**type**\: bool
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.path = None
            self.filter = None
            self.max_silent_interval = None
            self.sample_frequency = None
            self.suppress_unchanged = None

        @property
        def _common_path(self):
            if self.path is None:
                raise YPYDataValidationError('Key property path is None')

            return '/openconfig-rpc-api:telemetrySubscribe/openconfig-rpc-api:paths[openconfig-rpc-api:path = ' + str(self.path) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                return True

            if self.filter is not None:
                return True

            if self.max_silent_interval is not None:
                return True

            if self.sample_frequency is not None:
                return True

            if self.suppress_unchanged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['TelemetrySubscribeRpc.Paths']['meta_info']


    class Paths(object):
        """
        List of data model paths, keyed by path name
        
        .. attribute:: path
        
        	Data model path of interest
        	**type**\: str
        
        .. attribute:: filter
        
        	Regular expression to be used in filtering state leaves
        	**type**\: str
        
        .. attribute:: max_silent_interval
        
        	Maximum time in ms the target device may go without sending a message to the collector. If this time expires with suppress\-unchanged set, the target device must send an update message regardless if the data values have changed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sample_frequency
        
        	Time in ms between collection and transmission of the specified data to the collector platform. The target device will sample the corresponding data (e.g,. a counter) and immediately send to the collector destination.  If sample\-frequency is set to 0, then the network device must emit an update upon every datum change
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: suppress_unchanged
        
        	If this is set to true, the target device will only send updates to the collector upon a change in data value
        	**type**\: bool
        
        

        """

        _prefix = 'oc-rpc'
        _revision = '2015-10-30'

        def __init__(self):
            self.parent = None
            self.path = None
            self.filter = None
            self.max_silent_interval = None
            self.sample_frequency = None
            self.suppress_unchanged = None

        @property
        def _common_path(self):
            if self.path is None:
                raise YPYDataValidationError('Key property path is None')

            return '/openconfig-rpc-api:telemetrySubscribe/openconfig-rpc-api:paths[openconfig-rpc-api:path = ' + str(self.path) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                return True

            if self.filter is not None:
                return True

            if self.max_silent_interval is not None:
                return True

            if self.sample_frequency is not None:
                return True

            if self.suppress_unchanged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
            return meta._meta_table['TelemetrySubscribeRpc.Paths']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rpc-api:telemetrySubscribe'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.collectors is not None:
            for child_ref in self.collectors:
                if child_ref._has_data():
                    return True

        if self.collectors is not None:
            for child_ref in self.collectors:
                if child_ref._has_data():
                    return True

        if self.export_dscp_marking is not None:
            return True

        if self.export_dscp_marking is not None:
            return True

        if self.paths is not None:
            for child_ref in self.paths:
                if child_ref._has_data():
                    return True

        if self.paths is not None:
            for child_ref in self.paths:
                if child_ref._has_data():
                    return True

        if self.subscription_id is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['TelemetrySubscribeRpc']['meta_info']


class DeleteConfig_Identity(EditConfigCommands_Identity):
    """
    Deletes the configuration at the target device. If the
    specified data does not exist, the device returns success.
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        EditConfigCommands_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['DeleteConfig_Identity']['meta_info']


class EncodingJsonIetf_Identity(OpenconfigDataEncodingTypes_Identity):
    """
    JSON encoded based on IETF draft standard
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigDataEncodingTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['EncodingJsonIetf_Identity']['meta_info']


class EncodingProto3_Identity(OpenconfigDataEncodingTypes_Identity):
    """
    Protocol buffers v3
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigDataEncodingTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['EncodingProto3_Identity']['meta_info']


class EncodingXml_Identity(OpenconfigDataEncodingTypes_Identity):
    """
    XML encoding
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigDataEncodingTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['EncodingXml_Identity']['meta_info']


class FileMode_Identity(OpenconfigSchemaModeTypes_Identity):
    """
    Schema delivered in a file
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigSchemaModeTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['FileMode_Identity']['meta_info']


class JsonSchema_Identity(OpenconfigSchemaFormatTypes_Identity):
    """
    JSON\-Schema
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigSchemaFormatTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['JsonSchema_Identity']['meta_info']


class ReplaceConfig_Identity(EditConfigCommands_Identity):
    """
    Replaces the configuration at the target device at the
    specified path(s). If the specified data exists, it is
    overwritten by the contents of the message.  Configuration data
    that is not specified is deleted by the server.
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        EditConfigCommands_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['ReplaceConfig_Identity']['meta_info']


class UpdateConfig_Identity(EditConfigCommands_Identity):
    """
    Updates the configuration at the target device at the
    specified path(s). Data in the request is added to the current
    device configuration (this is referred to as 'merge' in
    NETCONF, for example).  If the specified data exists, it is
    overwritten by the contents of the message.  If the path
    specifies a list node, the configuration data is considered an
    addition (append) to the list with the new element.
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        EditConfigCommands_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['UpdateConfig_Identity']['meta_info']


class UriMode_Identity(OpenconfigSchemaModeTypes_Identity):
    """
    Retrieve schema using a supplied URI
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigSchemaModeTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['UriMode_Identity']['meta_info']


class XsdSchema_Identity(OpenconfigSchemaFormatTypes_Identity):
    """
    XML Schema Definition
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigSchemaFormatTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['XsdSchema_Identity']['meta_info']


class YangSchema_Identity(OpenconfigSchemaFormatTypes_Identity):
    """
    YANG model
    
    

    """

    _prefix = 'oc-rpc'
    _revision = '2015-10-30'

    def __init__(self):
        OpenconfigSchemaFormatTypes_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rpc_api as meta
        return meta._meta_table['YangSchema_Identity']['meta_info']


