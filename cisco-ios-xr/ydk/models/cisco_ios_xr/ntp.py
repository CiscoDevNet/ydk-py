""" ntp 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG definitions
for Cisco IOS\-XR syadmin NTP configuration.

This module contains definitions
for the following management objects\:
NTP configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ntp(_Entity_):
    """
    
    
    .. attribute:: peer
    
    	
    	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.ntp.Ntp.Peer>`
    
    .. attribute:: server
    
    	
    	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.ntp.Ntp.Server>`
    
    .. attribute:: trusted_key
    
    	
    	**type**\: list of int
    
    	**range:** 1..65534
    
    .. attribute:: authenticate
    
    	
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: authentication_key
    
    	
    	**type**\: list of  		 :py:class:`AuthenticationKey <ydk.models.cisco_ios_xr.ntp.Ntp.AuthenticationKey>`
    
    .. attribute:: trace
    
    	
    	**type**\:  :py:class:`Trace <ydk.models.cisco_ios_xr.ntp.Ntp.Trace>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ntp'
    _revision = '2016-07-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "ntp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("peer", ("peer", Ntp.Peer)), ("server", ("server", Ntp.Server)), ("authentication-key", ("authentication_key", Ntp.AuthenticationKey)), ("trace", ("trace", Ntp.Trace))])
        self._leafs = OrderedDict([
            ('trusted_key', (YLeafList(YType.int32, 'trusted-key'), ['int'])),
            ('authenticate', (YLeaf(YType.empty, 'authenticate'), ['Empty'])),
        ])
        self.trusted_key = []
        self.authenticate = None

        self.trace = Ntp.Trace()
        self.trace.parent = self
        self._children_name_map["trace"] = "trace"

        self.peer = YList(self)
        self.server = YList(self)
        self.authentication_key = YList(self)
        self._segment_path = lambda: "ntp:ntp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ntp, ['trusted_key', 'authenticate'], name, value)


    class Peer(_Entity_):
        """
        
        
        .. attribute:: name  (key)
        
        	
        	**type**\: str
        
        .. attribute:: version
        
        	
        	**type**\: int
        
        	**range:** 1..4
        
        .. attribute:: key_id
        
        	
        	**type**\: int
        
        	**range:** 1..65534
        
        .. attribute:: prefer
        
        	
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ntp'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ntp.Peer, self).__init__()

            self.yang_name = "peer"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('version', (YLeaf(YType.int32, 'version'), ['int'])),
                ('key_id', (YLeaf(YType.int32, 'key-id'), ['int'])),
                ('prefer', (YLeaf(YType.empty, 'prefer'), ['Empty'])),
            ])
            self.name = None
            self.version = None
            self.key_id = None
            self.prefer = None
            self._segment_path = lambda: "peer" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "ntp:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Peer, ['name', 'version', 'key_id', 'prefer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _ntp as meta
            return meta._meta_table['Ntp.Peer']['meta_info']


    class Server(_Entity_):
        """
        
        
        .. attribute:: name  (key)
        
        	
        	**type**\: str
        
        .. attribute:: version
        
        	
        	**type**\: int
        
        	**range:** 1..4
        
        .. attribute:: key_id
        
        	
        	**type**\: int
        
        	**range:** 1..65534
        
        .. attribute:: prefer
        
        	
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ntp'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ntp.Server, self).__init__()

            self.yang_name = "server"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('version', (YLeaf(YType.int32, 'version'), ['int'])),
                ('key_id', (YLeaf(YType.int32, 'key-id'), ['int'])),
                ('prefer', (YLeaf(YType.empty, 'prefer'), ['Empty'])),
            ])
            self.name = None
            self.version = None
            self.key_id = None
            self.prefer = None
            self._segment_path = lambda: "server" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "ntp:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Server, ['name', 'version', 'key_id', 'prefer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _ntp as meta
            return meta._meta_table['Ntp.Server']['meta_info']


    class AuthenticationKey(_Entity_):
        """
        
        
        .. attribute:: key_number  (key)
        
        	
        	**type**\: int
        
        	**range:** 1..65534
        
        .. attribute:: md5_keyword
        
        	
        	**type**\:  :py:class:`Md5Keyword <ydk.models.cisco_ios_xr.ntp.Ntp.AuthenticationKey.Md5Keyword>`
        
        	**mandatory**\: True
        
        .. attribute:: encryption
        
        	
        	**type**\:  :py:class:`Encryption <ydk.models.cisco_ios_xr.ntp.Ntp.AuthenticationKey.Encryption>`
        
        .. attribute:: keyname
        
        	
        	**type**\: str
        
        	**length:** 0..32
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ntp'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ntp.AuthenticationKey, self).__init__()

            self.yang_name = "authentication-key"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['key_number']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('key_number', (YLeaf(YType.int32, 'key-number'), ['int'])),
                ('md5_keyword', (YLeaf(YType.enumeration, 'md5-keyword'), [('ydk.models.cisco_ios_xr.ntp', 'Ntp', 'AuthenticationKey.Md5Keyword')])),
                ('encryption', (YLeaf(YType.enumeration, 'encryption'), [('ydk.models.cisco_ios_xr.ntp', 'Ntp', 'AuthenticationKey.Encryption')])),
                ('keyname', (YLeaf(YType.str, 'keyname'), ['str'])),
            ])
            self.key_number = None
            self.md5_keyword = None
            self.encryption = None
            self.keyname = None
            self._segment_path = lambda: "authentication-key" + "[key-number='" + str(self.key_number) + "']"
            self._absolute_path = lambda: "ntp:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.AuthenticationKey, ['key_number', 'md5_keyword', 'encryption', 'keyname'], name, value)

        class Encryption(Enum):
            """
            Encryption (Enum Class)

            .. data:: clear = 0

            .. data:: encrypted = 1

            """

            clear = Enum.YLeaf(0, "clear")

            encrypted = Enum.YLeaf(1, "encrypted")


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _ntp as meta
                return meta._meta_table['Ntp.AuthenticationKey.Encryption']


        class Md5Keyword(Enum):
            """
            Md5Keyword (Enum Class)

            .. data:: md5 = 0

            """

            md5 = Enum.YLeaf(0, "md5")


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _ntp as meta
                return meta._meta_table['Ntp.AuthenticationKey.Md5Keyword']


        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _ntp as meta
            return meta._meta_table['Ntp.AuthenticationKey']['meta_info']


    class Trace(_Entity_):
        """
        
        
        .. attribute:: ntp_helper
        
        	
        	**type**\:  :py:class:`NtpHelper <ydk.models.cisco_ios_xr.ntp.Ntp.Trace.NtpHelper>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ntp'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ntp.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ntp_helper", ("ntp_helper", Ntp.Trace.NtpHelper))])
            self._leafs = OrderedDict()

            self.ntp_helper = Ntp.Trace.NtpHelper()
            self.ntp_helper.parent = self
            self._children_name_map["ntp_helper"] = "ntp_helper"
            self._segment_path = lambda: "trace"
            self._absolute_path = lambda: "ntp:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Trace, [], name, value)


        class NtpHelper(_Entity_):
            """
            
            
            .. attribute:: trace
            
            	show traceable processes
            	**type**\: list of  		 :py:class:`Trace_ <ydk.models.cisco_ios_xr.ntp.Ntp.Trace.NtpHelper.Trace_>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ntp'
            _revision = '2016-07-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ntp.Trace.NtpHelper, self).__init__()

                self.yang_name = "ntp_helper"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trace", ("trace", Ntp.Trace.NtpHelper.Trace_))])
                self._leafs = OrderedDict()

                self.trace = YList(self)
                self._segment_path = lambda: "ntp_helper"
                self._absolute_path = lambda: "ntp:ntp/trace/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Trace.NtpHelper, [], name, value)


            class Trace_(_Entity_):
                """
                show traceable processes
                
                .. attribute:: buffer  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.ntp.Ntp.Trace.NtpHelper.Trace_.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ntp'
                _revision = '2016-07-04'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ntp.Trace.NtpHelper.Trace_, self).__init__()

                    self.yang_name = "trace"
                    self.yang_parent_name = "ntp_helper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['buffer']
                    self._child_classes = OrderedDict([("location", ("location", Ntp.Trace.NtpHelper.Trace_.Location))])
                    self._leafs = OrderedDict([
                        ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                    ])
                    self.buffer = None

                    self.location = YList(self)
                    self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                    self._absolute_path = lambda: "ntp:ntp/trace/ntp_helper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Trace.NtpHelper.Trace_, ['buffer'], name, value)


                class Location(_Entity_):
                    """
                    
                    
                    .. attribute:: location_name  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: all_options
                    
                    	
                    	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.ntp.Ntp.Trace.NtpHelper.Trace_.Location.AllOptions>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ntp'
                    _revision = '2016-07-04'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ntp.Trace.NtpHelper.Trace_.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['location_name']
                        self._child_classes = OrderedDict([("all-options", ("all_options", Ntp.Trace.NtpHelper.Trace_.Location.AllOptions))])
                        self._leafs = OrderedDict([
                            ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                        ])
                        self.location_name = None

                        self.all_options = YList(self)
                        self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Trace.NtpHelper.Trace_.Location, ['location_name'], name, value)


                    class AllOptions(_Entity_):
                        """
                        
                        
                        .. attribute:: option  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: trace_blocks
                        
                        	
                        	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.ntp.Ntp.Trace.NtpHelper.Trace_.Location.AllOptions.TraceBlocks>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ntp'
                        _revision = '2016-07-04'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Trace.NtpHelper.Trace_.Location.AllOptions, self).__init__()

                            self.yang_name = "all-options"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['option']
                            self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Ntp.Trace.NtpHelper.Trace_.Location.AllOptions.TraceBlocks))])
                            self._leafs = OrderedDict([
                                ('option', (YLeaf(YType.str, 'option'), ['str'])),
                            ])
                            self.option = None

                            self.trace_blocks = YList(self)
                            self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Trace.NtpHelper.Trace_.Location.AllOptions, ['option'], name, value)


                        class TraceBlocks(_Entity_):
                            """
                            
                            
                            .. attribute:: data
                            
                            	Trace output block
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ntp'
                            _revision = '2016-07-04'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Trace.NtpHelper.Trace_.Location.AllOptions.TraceBlocks, self).__init__()

                                self.yang_name = "trace-blocks"
                                self.yang_parent_name = "all-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data', (YLeaf(YType.str, 'data'), ['str'])),
                                ])
                                self.data = None
                                self._segment_path = lambda: "trace-blocks"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Trace.NtpHelper.Trace_.Location.AllOptions.TraceBlocks, ['data'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _ntp as meta
                                return meta._meta_table['Ntp.Trace.NtpHelper.Trace_.Location.AllOptions.TraceBlocks']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _ntp as meta
                            return meta._meta_table['Ntp.Trace.NtpHelper.Trace_.Location.AllOptions']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _ntp as meta
                        return meta._meta_table['Ntp.Trace.NtpHelper.Trace_.Location']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _ntp as meta
                    return meta._meta_table['Ntp.Trace.NtpHelper.Trace_']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _ntp as meta
                return meta._meta_table['Ntp.Trace.NtpHelper']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _ntp as meta
            return meta._meta_table['Ntp.Trace']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _ntp as meta
        return meta._meta_table['Ntp']['meta_info']


class ClockAction(_Entity_):
    """
    
    
    .. attribute:: clock
    
    	
    	**type**\:  :py:class:`Clock <ydk.models.cisco_ios_xr.ntp.ClockAction.Clock>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ntp'
    _revision = '2016-07-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ClockAction, self).__init__()
        self._top_entity = None

        self.yang_name = "clock-action"
        self.yang_parent_name = "ntp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clock", ("clock", ClockAction.Clock))])
        self._leafs = OrderedDict()

        self.clock = ClockAction.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"
        self._segment_path = lambda: "ntp:clock-action"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ClockAction, [], name, value)


    class Clock(_Entity_):
        """
        
        
        .. attribute:: action
        
        	
        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.ntp.ClockAction.Clock.Action>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ntp'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ClockAction.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "clock-action"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("Action", ("action", ClockAction.Clock.Action))])
            self._leafs = OrderedDict()

            self.action = ClockAction.Clock.Action()
            self.action.parent = self
            self._children_name_map["action"] = "Action"
            self._segment_path = lambda: "clock"
            self._absolute_path = lambda: "ntp:clock-action/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClockAction.Clock, [], name, value)


        class Action(_Entity_):
            """
            
            
            

            """

            _prefix = 'ntp'
            _revision = '2016-07-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ClockAction.Clock.Action, self).__init__()

                self.yang_name = "Action"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "Action"
                self._absolute_path = lambda: "ntp:clock-action/clock/%s" % self._segment_path()
                self._is_frozen = True

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _ntp as meta
                return meta._meta_table['ClockAction.Clock.Action']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _ntp as meta
            return meta._meta_table['ClockAction.Clock']['meta_info']

    def clone_ptr(self):
        self._top_entity = ClockAction()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _ntp as meta
        return meta._meta_table['ClockAction']['meta_info']


