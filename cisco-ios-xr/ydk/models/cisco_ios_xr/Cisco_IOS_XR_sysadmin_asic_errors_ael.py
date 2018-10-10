""" Cisco_IOS_XR_sysadmin_asic_errors_ael 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class AsicErrors(Entity):
    """
    
    
    .. attribute:: device_name  (key)
    
    	
    	**type**\: str
    
    .. attribute:: instance
    
    	
    	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance>`
    
    .. attribute:: show_all_instances
    
    	
    	**type**\:  :py:class:`ShowAllInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances>`
    
    

    """

    _prefix = 'ael'
    _revision = '2017-07-05'

    def __init__(self):
        super(AsicErrors, self).__init__()
        self._top_entity = None

        self.yang_name = "asic-errors"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-asic-errors-ael"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = ['device_name']
        self._child_classes = OrderedDict([("instance", ("instance", AsicErrors.Instance)), ("show-all-instances", ("show_all_instances", AsicErrors.ShowAllInstances))])
        self._leafs = OrderedDict([
            ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
        ])
        self.device_name = None

        self.show_all_instances = AsicErrors.ShowAllInstances()
        self.show_all_instances.parent = self
        self._children_name_map["show_all_instances"] = "show-all-instances"

        self.instance = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-asic-errors-ael:asic-errors" + "[device-name='" + str(self.device_name) + "']"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AsicErrors, ['device_name'], name, value)


    class Instance(Entity):
        """
        
        
        .. attribute:: instance_num  (key)
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sbe
        
        	
        	**type**\:  :py:class:`Sbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Sbe>`
        
        .. attribute:: mbe
        
        	
        	**type**\:  :py:class:`Mbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Mbe>`
        
        .. attribute:: parity
        
        	
        	**type**\:  :py:class:`Parity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Parity>`
        
        .. attribute:: generic
        
        	
        	**type**\:  :py:class:`Generic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Generic>`
        
        .. attribute:: crc
        
        	
        	**type**\:  :py:class:`Crc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Crc>`
        
        .. attribute:: reset
        
        	
        	**type**\:  :py:class:`Reset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Reset>`
        
        .. attribute:: barrier
        
        	
        	**type**\:  :py:class:`Barrier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Barrier>`
        
        .. attribute:: unexpected
        
        	
        	**type**\:  :py:class:`Unexpected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Unexpected>`
        
        .. attribute:: link
        
        	
        	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Link>`
        
        .. attribute:: oor_thresh
        
        	
        	**type**\:  :py:class:`OorThresh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.OorThresh>`
        
        .. attribute:: bp
        
        	
        	**type**\:  :py:class:`Bp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Bp>`
        
        .. attribute:: io
        
        	
        	**type**\:  :py:class:`Io <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Io>`
        
        .. attribute:: ucode
        
        	
        	**type**\:  :py:class:`Ucode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Ucode>`
        
        .. attribute:: config
        
        	
        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Config>`
        
        .. attribute:: indirect
        
        	
        	**type**\:  :py:class:`Indirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Indirect>`
        
        .. attribute:: nonerr
        
        	
        	**type**\:  :py:class:`Nonerr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Nonerr>`
        
        .. attribute:: summary
        
        	
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Summary>`
        
        .. attribute:: all
        
        	
        	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All>`
        
        

        """

        _prefix = 'ael'
        _revision = '2017-07-05'

        def __init__(self):
            super(AsicErrors.Instance, self).__init__()

            self.yang_name = "instance"
            self.yang_parent_name = "asic-errors"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self.ylist_key_names = ['instance_num']
            self._child_classes = OrderedDict([("sbe", ("sbe", AsicErrors.Instance.Sbe)), ("mbe", ("mbe", AsicErrors.Instance.Mbe)), ("parity", ("parity", AsicErrors.Instance.Parity)), ("generic", ("generic", AsicErrors.Instance.Generic)), ("crc", ("crc", AsicErrors.Instance.Crc)), ("reset", ("reset", AsicErrors.Instance.Reset)), ("barrier", ("barrier", AsicErrors.Instance.Barrier)), ("unexpected", ("unexpected", AsicErrors.Instance.Unexpected)), ("link", ("link", AsicErrors.Instance.Link)), ("oor-thresh", ("oor_thresh", AsicErrors.Instance.OorThresh)), ("bp", ("bp", AsicErrors.Instance.Bp)), ("io", ("io", AsicErrors.Instance.Io)), ("ucode", ("ucode", AsicErrors.Instance.Ucode)), ("config", ("config", AsicErrors.Instance.Config)), ("indirect", ("indirect", AsicErrors.Instance.Indirect)), ("nonerr", ("nonerr", AsicErrors.Instance.Nonerr)), ("summary", ("summary", AsicErrors.Instance.Summary)), ("all", ("all", AsicErrors.Instance.All))])
            self._leafs = OrderedDict([
                ('instance_num', (YLeaf(YType.uint32, 'instance-num'), ['int'])),
            ])
            self.instance_num = None

            self.sbe = AsicErrors.Instance.Sbe()
            self.sbe.parent = self
            self._children_name_map["sbe"] = "sbe"

            self.mbe = AsicErrors.Instance.Mbe()
            self.mbe.parent = self
            self._children_name_map["mbe"] = "mbe"

            self.parity = AsicErrors.Instance.Parity()
            self.parity.parent = self
            self._children_name_map["parity"] = "parity"

            self.generic = AsicErrors.Instance.Generic()
            self.generic.parent = self
            self._children_name_map["generic"] = "generic"

            self.crc = AsicErrors.Instance.Crc()
            self.crc.parent = self
            self._children_name_map["crc"] = "crc"

            self.reset = AsicErrors.Instance.Reset()
            self.reset.parent = self
            self._children_name_map["reset"] = "reset"

            self.barrier = AsicErrors.Instance.Barrier()
            self.barrier.parent = self
            self._children_name_map["barrier"] = "barrier"

            self.unexpected = AsicErrors.Instance.Unexpected()
            self.unexpected.parent = self
            self._children_name_map["unexpected"] = "unexpected"

            self.link = AsicErrors.Instance.Link()
            self.link.parent = self
            self._children_name_map["link"] = "link"

            self.oor_thresh = AsicErrors.Instance.OorThresh()
            self.oor_thresh.parent = self
            self._children_name_map["oor_thresh"] = "oor-thresh"

            self.bp = AsicErrors.Instance.Bp()
            self.bp.parent = self
            self._children_name_map["bp"] = "bp"

            self.io = AsicErrors.Instance.Io()
            self.io.parent = self
            self._children_name_map["io"] = "io"

            self.ucode = AsicErrors.Instance.Ucode()
            self.ucode.parent = self
            self._children_name_map["ucode"] = "ucode"

            self.config = AsicErrors.Instance.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.indirect = AsicErrors.Instance.Indirect()
            self.indirect.parent = self
            self._children_name_map["indirect"] = "indirect"

            self.nonerr = AsicErrors.Instance.Nonerr()
            self.nonerr.parent = self
            self._children_name_map["nonerr"] = "nonerr"

            self.summary = AsicErrors.Instance.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"

            self.all = AsicErrors.Instance.All()
            self.all.parent = self
            self._children_name_map["all"] = "all"
            self._segment_path = lambda: "instance" + "[instance-num='" + str(self.instance_num) + "']"
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AsicErrors.Instance, ['instance_num'], name, value)


        class Sbe(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Sbe.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Sbe, self).__init__()

                self.yang_name = "sbe"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Sbe.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "sbe"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Sbe, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Sbe.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Sbe.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "sbe"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Sbe.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Sbe.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Sbe.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Sbe.Location.LogLst, ['log_line'], name, value)


        class Mbe(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Mbe.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Mbe, self).__init__()

                self.yang_name = "mbe"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Mbe.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "mbe"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Mbe, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Mbe.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Mbe.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "mbe"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Mbe.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Mbe.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Mbe.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Mbe.Location.LogLst, ['log_line'], name, value)


        class Parity(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Parity.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Parity, self).__init__()

                self.yang_name = "parity"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Parity.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "parity"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Parity, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Parity.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Parity.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "parity"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Parity.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Parity.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Parity.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Parity.Location.LogLst, ['log_line'], name, value)


        class Generic(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Generic.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Generic, self).__init__()

                self.yang_name = "generic"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Generic.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "generic"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Generic, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Generic.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Generic.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "generic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Generic.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Generic.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Generic.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Generic.Location.LogLst, ['log_line'], name, value)


        class Crc(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Crc.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Crc, self).__init__()

                self.yang_name = "crc"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Crc.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "crc"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Crc, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Crc.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Crc.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "crc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Crc.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Crc.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Crc.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Crc.Location.LogLst, ['log_line'], name, value)


        class Reset(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Reset.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Reset, self).__init__()

                self.yang_name = "reset"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Reset.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "reset"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Reset, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Reset.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Reset.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "reset"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Reset.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Reset.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Reset.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Reset.Location.LogLst, ['log_line'], name, value)


        class Barrier(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Barrier.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Barrier, self).__init__()

                self.yang_name = "barrier"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Barrier.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "barrier"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Barrier, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Barrier.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Barrier.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "barrier"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Barrier.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Barrier.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Barrier.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Barrier.Location.LogLst, ['log_line'], name, value)


        class Unexpected(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Unexpected.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Unexpected, self).__init__()

                self.yang_name = "unexpected"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Unexpected.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "unexpected"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Unexpected, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Unexpected.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Unexpected.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "unexpected"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Unexpected.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Unexpected.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Unexpected.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Unexpected.Location.LogLst, ['log_line'], name, value)


        class Link(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Link.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Link, self).__init__()

                self.yang_name = "link"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Link.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "link"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Link, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Link.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Link.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "link"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Link.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Link.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Link.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Link.Location.LogLst, ['log_line'], name, value)


        class OorThresh(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.OorThresh.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.OorThresh, self).__init__()

                self.yang_name = "oor-thresh"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.OorThresh.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "oor-thresh"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.OorThresh, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.OorThresh.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.OorThresh.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "oor-thresh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.OorThresh.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.OorThresh.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.OorThresh.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.OorThresh.Location.LogLst, ['log_line'], name, value)


        class Bp(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Bp.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Bp, self).__init__()

                self.yang_name = "bp"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Bp.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "bp"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Bp, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Bp.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Bp.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "bp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Bp.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Bp.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Bp.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Bp.Location.LogLst, ['log_line'], name, value)


        class Io(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Io.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Io, self).__init__()

                self.yang_name = "io"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Io.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "io"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Io, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Io.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Io.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "io"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Io.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Io.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Io.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Io.Location.LogLst, ['log_line'], name, value)


        class Ucode(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Ucode.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Ucode, self).__init__()

                self.yang_name = "ucode"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Ucode.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "ucode"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Ucode, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Ucode.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Ucode.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "ucode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Ucode.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Ucode.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Ucode.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Ucode.Location.LogLst, ['log_line'], name, value)


        class Config(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Config.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Config.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "config"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Config, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Config.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Config.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "config"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Config.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Config.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Config.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Config.Location.LogLst, ['log_line'], name, value)


        class Indirect(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Indirect.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Indirect, self).__init__()

                self.yang_name = "indirect"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Indirect.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "indirect"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Indirect, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Indirect.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Indirect.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "indirect"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Indirect.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Indirect.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Indirect.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Indirect.Location.LogLst, ['log_line'], name, value)


        class Nonerr(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Nonerr.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Nonerr, self).__init__()

                self.yang_name = "nonerr"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Nonerr.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "nonerr"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Nonerr, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Nonerr.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Nonerr.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "nonerr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Nonerr.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Nonerr.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Nonerr.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Nonerr.Location.LogLst, ['log_line'], name, value)


        class Summary(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Summary.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.Summary.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "summary"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.Summary, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.Summary.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.Summary.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.Summary.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.Summary.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.Summary.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.Summary.Location.LogLst, ['log_line'], name, value)


        class All(Entity):
            """
            
            
            .. attribute:: history
            
            	
            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All.History>`
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.Instance.All, self).__init__()

                self.yang_name = "all"
                self.yang_parent_name = "instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("history", ("history", AsicErrors.Instance.All.History)), ("location", ("location", AsicErrors.Instance.All.Location))])
                self._leafs = OrderedDict()

                self.history = AsicErrors.Instance.All.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"

                self.location = YList(self)
                self._segment_path = lambda: "all"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Instance.All, [], name, value)


            class History(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All.History.Location>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.All.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "all"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", AsicErrors.Instance.All.History.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "history"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.All.History, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location_name  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                    
                    .. attribute:: log_lst
                    
                    	
                    	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All.History.Location.LogLst>`
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.All.History.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['location_name']
                        self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.All.History.Location.LogLst))])
                        self._leafs = OrderedDict([
                            ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                        ])
                        self.location_name = None

                        self.log_lst = YList(self)
                        self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.All.History.Location, ['location_name'], name, value)


                    class LogLst(Entity):
                        """
                        
                        
                        .. attribute:: log_line
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ael'
                        _revision = '2017-07-05'

                        def __init__(self):
                            super(AsicErrors.Instance.All.History.Location.LogLst, self).__init__()

                            self.yang_name = "log-lst"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                            ])
                            self.log_line = None
                            self._segment_path = lambda: "log-lst"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AsicErrors.Instance.All.History.Location.LogLst, ['log_line'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.Instance.All.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.Instance.All.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "all"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.Instance.All.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Instance.All.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.Instance.All.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Instance.All.Location.LogLst, ['log_line'], name, value)


    class ShowAllInstances(Entity):
        """
        
        
        .. attribute:: sbe
        
        	
        	**type**\:  :py:class:`Sbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Sbe>`
        
        .. attribute:: mbe
        
        	
        	**type**\:  :py:class:`Mbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Mbe>`
        
        .. attribute:: parity
        
        	
        	**type**\:  :py:class:`Parity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Parity>`
        
        .. attribute:: generic
        
        	
        	**type**\:  :py:class:`Generic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Generic>`
        
        .. attribute:: crc
        
        	
        	**type**\:  :py:class:`Crc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Crc>`
        
        .. attribute:: reset
        
        	
        	**type**\:  :py:class:`Reset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Reset>`
        
        .. attribute:: barrier
        
        	
        	**type**\:  :py:class:`Barrier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Barrier>`
        
        .. attribute:: unexpected
        
        	
        	**type**\:  :py:class:`Unexpected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Unexpected>`
        
        .. attribute:: link
        
        	
        	**type**\:  :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Link>`
        
        .. attribute:: oor_thresh
        
        	
        	**type**\:  :py:class:`OorThresh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.OorThresh>`
        
        .. attribute:: bp
        
        	
        	**type**\:  :py:class:`Bp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Bp>`
        
        .. attribute:: io
        
        	
        	**type**\:  :py:class:`Io <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Io>`
        
        .. attribute:: ucode
        
        	
        	**type**\:  :py:class:`Ucode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Ucode>`
        
        .. attribute:: config
        
        	
        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Config>`
        
        .. attribute:: indirect
        
        	
        	**type**\:  :py:class:`Indirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Indirect>`
        
        .. attribute:: nonerr
        
        	
        	**type**\:  :py:class:`Nonerr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Nonerr>`
        
        .. attribute:: summary
        
        	
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Summary>`
        
        .. attribute:: all
        
        	
        	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.All>`
        
        

        """

        _prefix = 'ael'
        _revision = '2017-07-05'

        def __init__(self):
            super(AsicErrors.ShowAllInstances, self).__init__()

            self.yang_name = "show-all-instances"
            self.yang_parent_name = "asic-errors"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sbe", ("sbe", AsicErrors.ShowAllInstances.Sbe)), ("mbe", ("mbe", AsicErrors.ShowAllInstances.Mbe)), ("parity", ("parity", AsicErrors.ShowAllInstances.Parity)), ("generic", ("generic", AsicErrors.ShowAllInstances.Generic)), ("crc", ("crc", AsicErrors.ShowAllInstances.Crc)), ("reset", ("reset", AsicErrors.ShowAllInstances.Reset)), ("barrier", ("barrier", AsicErrors.ShowAllInstances.Barrier)), ("unexpected", ("unexpected", AsicErrors.ShowAllInstances.Unexpected)), ("link", ("link", AsicErrors.ShowAllInstances.Link)), ("oor-thresh", ("oor_thresh", AsicErrors.ShowAllInstances.OorThresh)), ("bp", ("bp", AsicErrors.ShowAllInstances.Bp)), ("io", ("io", AsicErrors.ShowAllInstances.Io)), ("ucode", ("ucode", AsicErrors.ShowAllInstances.Ucode)), ("config", ("config", AsicErrors.ShowAllInstances.Config)), ("indirect", ("indirect", AsicErrors.ShowAllInstances.Indirect)), ("nonerr", ("nonerr", AsicErrors.ShowAllInstances.Nonerr)), ("summary", ("summary", AsicErrors.ShowAllInstances.Summary)), ("all", ("all", AsicErrors.ShowAllInstances.All))])
            self._leafs = OrderedDict()

            self.sbe = AsicErrors.ShowAllInstances.Sbe()
            self.sbe.parent = self
            self._children_name_map["sbe"] = "sbe"

            self.mbe = AsicErrors.ShowAllInstances.Mbe()
            self.mbe.parent = self
            self._children_name_map["mbe"] = "mbe"

            self.parity = AsicErrors.ShowAllInstances.Parity()
            self.parity.parent = self
            self._children_name_map["parity"] = "parity"

            self.generic = AsicErrors.ShowAllInstances.Generic()
            self.generic.parent = self
            self._children_name_map["generic"] = "generic"

            self.crc = AsicErrors.ShowAllInstances.Crc()
            self.crc.parent = self
            self._children_name_map["crc"] = "crc"

            self.reset = AsicErrors.ShowAllInstances.Reset()
            self.reset.parent = self
            self._children_name_map["reset"] = "reset"

            self.barrier = AsicErrors.ShowAllInstances.Barrier()
            self.barrier.parent = self
            self._children_name_map["barrier"] = "barrier"

            self.unexpected = AsicErrors.ShowAllInstances.Unexpected()
            self.unexpected.parent = self
            self._children_name_map["unexpected"] = "unexpected"

            self.link = AsicErrors.ShowAllInstances.Link()
            self.link.parent = self
            self._children_name_map["link"] = "link"

            self.oor_thresh = AsicErrors.ShowAllInstances.OorThresh()
            self.oor_thresh.parent = self
            self._children_name_map["oor_thresh"] = "oor-thresh"

            self.bp = AsicErrors.ShowAllInstances.Bp()
            self.bp.parent = self
            self._children_name_map["bp"] = "bp"

            self.io = AsicErrors.ShowAllInstances.Io()
            self.io.parent = self
            self._children_name_map["io"] = "io"

            self.ucode = AsicErrors.ShowAllInstances.Ucode()
            self.ucode.parent = self
            self._children_name_map["ucode"] = "ucode"

            self.config = AsicErrors.ShowAllInstances.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.indirect = AsicErrors.ShowAllInstances.Indirect()
            self.indirect.parent = self
            self._children_name_map["indirect"] = "indirect"

            self.nonerr = AsicErrors.ShowAllInstances.Nonerr()
            self.nonerr.parent = self
            self._children_name_map["nonerr"] = "nonerr"

            self.summary = AsicErrors.ShowAllInstances.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"

            self.all = AsicErrors.ShowAllInstances.All()
            self.all.parent = self
            self._children_name_map["all"] = "all"
            self._segment_path = lambda: "show-all-instances"
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AsicErrors.ShowAllInstances, [], name, value)


        class Sbe(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Sbe.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Sbe, self).__init__()

                self.yang_name = "sbe"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Sbe.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "sbe"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Sbe, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Sbe.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Sbe.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "sbe"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Sbe.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Sbe.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Sbe.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Sbe.Location.LogLst, ['log_line'], name, value)


        class Mbe(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Mbe.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Mbe, self).__init__()

                self.yang_name = "mbe"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Mbe.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "mbe"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Mbe, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Mbe.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Mbe.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "mbe"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Mbe.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Mbe.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Mbe.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Mbe.Location.LogLst, ['log_line'], name, value)


        class Parity(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Parity.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Parity, self).__init__()

                self.yang_name = "parity"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Parity.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "parity"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Parity, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Parity.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Parity.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "parity"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Parity.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Parity.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Parity.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Parity.Location.LogLst, ['log_line'], name, value)


        class Generic(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Generic.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Generic, self).__init__()

                self.yang_name = "generic"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Generic.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "generic"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Generic, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Generic.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Generic.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "generic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Generic.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Generic.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Generic.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Generic.Location.LogLst, ['log_line'], name, value)


        class Crc(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Crc.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Crc, self).__init__()

                self.yang_name = "crc"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Crc.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "crc"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Crc, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Crc.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Crc.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "crc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Crc.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Crc.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Crc.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Crc.Location.LogLst, ['log_line'], name, value)


        class Reset(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Reset.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Reset, self).__init__()

                self.yang_name = "reset"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Reset.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "reset"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Reset, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Reset.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Reset.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "reset"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Reset.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Reset.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Reset.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Reset.Location.LogLst, ['log_line'], name, value)


        class Barrier(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Barrier.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Barrier, self).__init__()

                self.yang_name = "barrier"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Barrier.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "barrier"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Barrier, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Barrier.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Barrier.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "barrier"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Barrier.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Barrier.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Barrier.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Barrier.Location.LogLst, ['log_line'], name, value)


        class Unexpected(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Unexpected.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Unexpected, self).__init__()

                self.yang_name = "unexpected"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Unexpected.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "unexpected"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Unexpected, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Unexpected.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Unexpected.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "unexpected"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Unexpected.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Unexpected.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Unexpected.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Unexpected.Location.LogLst, ['log_line'], name, value)


        class Link(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Link.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Link, self).__init__()

                self.yang_name = "link"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Link.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "link"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Link, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Link.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Link.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "link"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Link.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Link.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Link.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Link.Location.LogLst, ['log_line'], name, value)


        class OorThresh(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.OorThresh.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.OorThresh, self).__init__()

                self.yang_name = "oor-thresh"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.OorThresh.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "oor-thresh"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.OorThresh, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.OorThresh.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.OorThresh.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "oor-thresh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.OorThresh.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.OorThresh.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.OorThresh.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.OorThresh.Location.LogLst, ['log_line'], name, value)


        class Bp(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Bp.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Bp, self).__init__()

                self.yang_name = "bp"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Bp.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "bp"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Bp, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Bp.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Bp.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "bp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Bp.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Bp.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Bp.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Bp.Location.LogLst, ['log_line'], name, value)


        class Io(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Io.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Io, self).__init__()

                self.yang_name = "io"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Io.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "io"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Io, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Io.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Io.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "io"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Io.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Io.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Io.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Io.Location.LogLst, ['log_line'], name, value)


        class Ucode(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Ucode.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Ucode, self).__init__()

                self.yang_name = "ucode"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Ucode.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "ucode"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Ucode, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Ucode.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Ucode.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "ucode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Ucode.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Ucode.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Ucode.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Ucode.Location.LogLst, ['log_line'], name, value)


        class Config(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Config.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Config.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "config"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Config, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Config.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Config.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "config"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Config.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Config.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Config.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Config.Location.LogLst, ['log_line'], name, value)


        class Indirect(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Indirect.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Indirect, self).__init__()

                self.yang_name = "indirect"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Indirect.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "indirect"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Indirect, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Indirect.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Indirect.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "indirect"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Indirect.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Indirect.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Indirect.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Indirect.Location.LogLst, ['log_line'], name, value)


        class Nonerr(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Nonerr.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Nonerr, self).__init__()

                self.yang_name = "nonerr"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Nonerr.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "nonerr"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Nonerr, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Nonerr.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Nonerr.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "nonerr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Nonerr.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Nonerr.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Nonerr.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Nonerr.Location.LogLst, ['log_line'], name, value)


        class Summary(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Summary.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.Summary.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "summary"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.Summary, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.Summary.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.Summary.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.Summary.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.Summary.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.Summary.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.Summary.Location.LogLst, ['log_line'], name, value)


        class All(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.All.Location>`
            
            

            """

            _prefix = 'ael'
            _revision = '2017-07-05'

            def __init__(self):
                super(AsicErrors.ShowAllInstances.All, self).__init__()

                self.yang_name = "all"
                self.yang_parent_name = "show-all-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AsicErrors.ShowAllInstances.All.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "all"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.ShowAllInstances.All, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                .. attribute:: log_lst
                
                	
                	**type**\: list of  		 :py:class:`LogLst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_asic_errors_ael.AsicErrors.ShowAllInstances.All.Location.LogLst>`
                
                

                """

                _prefix = 'ael'
                _revision = '2017-07-05'

                def __init__(self):
                    super(AsicErrors.ShowAllInstances.All.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "all"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("log-lst", ("log_lst", AsicErrors.ShowAllInstances.All.Location.LogLst))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                    ])
                    self.location_name = None

                    self.log_lst = YList(self)
                    self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.ShowAllInstances.All.Location, ['location_name'], name, value)


                class LogLst(Entity):
                    """
                    
                    
                    .. attribute:: log_line
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ael'
                    _revision = '2017-07-05'

                    def __init__(self):
                        super(AsicErrors.ShowAllInstances.All.Location.LogLst, self).__init__()

                        self.yang_name = "log-lst"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_line', (YLeaf(YType.str, 'log-line'), ['str'])),
                        ])
                        self.log_line = None
                        self._segment_path = lambda: "log-lst"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.ShowAllInstances.All.Location.LogLst, ['log_line'], name, value)

    def clone_ptr(self):
        self._top_entity = AsicErrors()
        return self._top_entity

