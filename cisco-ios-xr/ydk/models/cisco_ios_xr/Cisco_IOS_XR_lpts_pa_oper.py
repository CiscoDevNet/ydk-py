""" Cisco_IOS_XR_lpts_pa_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pa package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pa\: lpts pre\-ifib data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class LptsPa(Entity):
    """
    lpts pre\-ifib data
    
    .. attribute:: entry_xr
    
    	lpts pa bindings
    	**type**\:  :py:class:`EntryXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr>`
    
    .. attribute:: entries
    
    	lpts pa clients
    	**type**\:  :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.Entries>`
    
    

    """

    _prefix = 'lpts-pa-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(LptsPa, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-pa"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-pa-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("entry-xr", ("entry_xr", LptsPa.EntryXr)), ("entries", ("entries", LptsPa.Entries))])
        self._leafs = OrderedDict()

        self.entry_xr = LptsPa.EntryXr()
        self.entry_xr.parent = self
        self._children_name_map["entry_xr"] = "entry-xr"

        self.entries = LptsPa.Entries()
        self.entries.parent = self
        self._children_name_map["entries"] = "entries"
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LptsPa, [], name, value)


    class EntryXr(Entity):
        """
        lpts pa bindings
        
        .. attribute:: entry
        
        	Data for single PA Binding
        	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry>`
        
        

        """

        _prefix = 'lpts-pa-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(LptsPa.EntryXr, self).__init__()

            self.yang_name = "entry-xr"
            self.yang_parent_name = "lpts-pa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entry", ("entry", LptsPa.EntryXr.Entry))])
            self._leafs = OrderedDict()

            self.entry = YList(self)
            self._segment_path = lambda: "entry-xr"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPa.EntryXr, [], name, value)


        class Entry(Entity):
            """
            Data for single PA Binding
            
            .. attribute:: entry  (key)
            
            	Single Binding entry
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ctime
            
            	Creation Time
            	**type**\:  :py:class:`Ctime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry.Ctime>`
            
            .. attribute:: utime
            
            	Update Time
            	**type**\:  :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry.Utime>`
            
            .. attribute:: location
            
            	Rack/slot/instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_id
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vid
            
            	VR/VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cookie
            
            	Cookie
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l3protocol
            
            	Layer 3 protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l4protocol
            
            	Layer 4 protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: smask
            
            	Filter operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifs
            
            	Ifhandle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ptype
            
            	Packet type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ip
            
            	Local address
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: remote_ip
            
            	Remote address
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: local_len
            
            	Local address length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: remote_len
            
            	Remote address length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: local_port
            
            	Local port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: packet_misc
            
            	L5 info
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: scope
            
            	Scope
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_flags
            
            	Client flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: min_ttl
            
            	Minimum TTL
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: lazy_bindq_delay
            
            	 lazy binding queue delay
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ptq_delay
            
            	 pending transactions queue delay
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'lpts-pa-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(LptsPa.EntryXr.Entry, self).__init__()

                self.yang_name = "entry"
                self.yang_parent_name = "entry-xr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entry']
                self._child_classes = OrderedDict([("ctime", ("ctime", LptsPa.EntryXr.Entry.Ctime)), ("utime", ("utime", LptsPa.EntryXr.Entry.Utime))])
                self._leafs = OrderedDict([
                    ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                    ('location', (YLeaf(YType.uint32, 'location'), ['int'])),
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('vid', (YLeaf(YType.uint32, 'vid'), ['int'])),
                    ('cookie', (YLeaf(YType.uint32, 'cookie'), ['int'])),
                    ('l3protocol', (YLeaf(YType.uint32, 'l3protocol'), ['int'])),
                    ('l4protocol', (YLeaf(YType.uint32, 'l4protocol'), ['int'])),
                    ('smask', (YLeaf(YType.uint32, 'smask'), ['int'])),
                    ('ifs', (YLeaf(YType.uint32, 'ifs'), ['int'])),
                    ('ptype', (YLeaf(YType.uint32, 'ptype'), ['int'])),
                    ('local_ip', (YLeaf(YType.str, 'local-ip'), ['str'])),
                    ('remote_ip', (YLeaf(YType.str, 'remote-ip'), ['str'])),
                    ('local_len', (YLeaf(YType.uint8, 'local-len'), ['int'])),
                    ('remote_len', (YLeaf(YType.uint8, 'remote-len'), ['int'])),
                    ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                    ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                    ('packet_misc', (YLeaf(YType.uint32, 'packet-misc'), ['int'])),
                    ('scope', (YLeaf(YType.uint32, 'scope'), ['int'])),
                    ('client_flags', (YLeaf(YType.uint32, 'client-flags'), ['int'])),
                    ('min_ttl', (YLeaf(YType.uint8, 'min-ttl'), ['int'])),
                    ('lazy_bindq_delay', (YLeaf(YType.uint32, 'lazy-bindq-delay'), ['int'])),
                    ('ptq_delay', (YLeaf(YType.uint32, 'ptq-delay'), ['int'])),
                ])
                self.entry = None
                self.location = None
                self.client_id = None
                self.vid = None
                self.cookie = None
                self.l3protocol = None
                self.l4protocol = None
                self.smask = None
                self.ifs = None
                self.ptype = None
                self.local_ip = None
                self.remote_ip = None
                self.local_len = None
                self.remote_len = None
                self.local_port = None
                self.remote_port = None
                self.packet_misc = None
                self.scope = None
                self.client_flags = None
                self.min_ttl = None
                self.lazy_bindq_delay = None
                self.ptq_delay = None

                self.ctime = LptsPa.EntryXr.Entry.Ctime()
                self.ctime.parent = self
                self._children_name_map["ctime"] = "ctime"

                self.utime = LptsPa.EntryXr.Entry.Utime()
                self.utime.parent = self
                self._children_name_map["utime"] = "utime"
                self._segment_path = lambda: "entry" + "[entry='" + str(self.entry) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/entry-xr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPa.EntryXr.Entry, ['entry', u'location', u'client_id', u'vid', u'cookie', u'l3protocol', u'l4protocol', u'smask', u'ifs', u'ptype', u'local_ip', u'remote_ip', u'local_len', u'remote_len', u'local_port', u'remote_port', u'packet_misc', u'scope', u'client_flags', u'min_ttl', u'lazy_bindq_delay', u'ptq_delay'], name, value)


            class Ctime(Entity):
                """
                Creation Time
                
                .. attribute:: tv_sec
                
                	Time Sec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tv_nsec
                
                	Time Nanosec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pa-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LptsPa.EntryXr.Entry.Ctime, self).__init__()

                    self.yang_name = "ctime"
                    self.yang_parent_name = "entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                        ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                    ])
                    self.tv_sec = None
                    self.tv_nsec = None
                    self._segment_path = lambda: "ctime"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPa.EntryXr.Entry.Ctime, [u'tv_sec', u'tv_nsec'], name, value)


            class Utime(Entity):
                """
                Update Time
                
                .. attribute:: tv_sec
                
                	Time Sec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tv_nsec
                
                	Time Nanosec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pa-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LptsPa.EntryXr.Entry.Utime, self).__init__()

                    self.yang_name = "utime"
                    self.yang_parent_name = "entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tv_sec', (YLeaf(YType.uint32, 'tv-sec'), ['int'])),
                        ('tv_nsec', (YLeaf(YType.uint32, 'tv-nsec'), ['int'])),
                    ])
                    self.tv_sec = None
                    self.tv_nsec = None
                    self._segment_path = lambda: "utime"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPa.EntryXr.Entry.Utime, [u'tv_sec', u'tv_nsec'], name, value)


    class Entries(Entity):
        """
        lpts pa clients
        
        .. attribute:: entry
        
        	Data for single PA Client
        	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.Entries.Entry>`
        
        

        """

        _prefix = 'lpts-pa-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(LptsPa.Entries, self).__init__()

            self.yang_name = "entries"
            self.yang_parent_name = "lpts-pa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("entry", ("entry", LptsPa.Entries.Entry))])
            self._leafs = OrderedDict()

            self.entry = YList(self)
            self._segment_path = lambda: "entries"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPa.Entries, [], name, value)


        class Entry(Entity):
            """
            Data for single PA Client
            
            .. attribute:: entry  (key)
            
            	Single Client entry
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: flags
            
            	Client flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_flags
            
            	Open flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: location
            
            	Rack/slot/instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_id
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: times
            
            	Transaction statisitics
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            

            """

            _prefix = 'lpts-pa-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(LptsPa.Entries.Entry, self).__init__()

                self.yang_name = "entry"
                self.yang_parent_name = "entries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entry']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                    ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                    ('open_flags', (YLeaf(YType.uint32, 'open-flags'), ['int'])),
                    ('location', (YLeaf(YType.uint32, 'location'), ['int'])),
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('times', (YLeaf(YType.str, 'times'), ['str'])),
                ])
                self.entry = None
                self.flags = None
                self.open_flags = None
                self.location = None
                self.client_id = None
                self.times = None
                self._segment_path = lambda: "entry" + "[entry='" + str(self.entry) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/entries/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPa.Entries.Entry, ['entry', u'flags', u'open_flags', u'location', u'client_id', u'times'], name, value)

    def clone_ptr(self):
        self._top_entity = LptsPa()
        return self._top_entity

