""" Cisco_IOS_XR_manageability_object_tracking_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package configuration.

This module contains definitions
for the following management objects\:
  object\-trackings\: Object Tracking configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ObjectTrackings(object):
    """
    Object Tracking configuration
    
    .. attribute:: object_tracking
    
    	Track name \- maximum 32 characters
    	**type**\: list of    :py:class:`ObjectTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking>`
    
    

    """

    _prefix = 'manageability-object-tracking-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.object_tracking = YList()
        self.object_tracking.parent = self
        self.object_tracking.name = 'object_tracking'


    class ObjectTracking(object):
        """
        Track name \- maximum 32 characters
        
        .. attribute:: track_name  <key>
        
        	Track name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: delay_down
        
        	Track delay down time
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: second
        
        .. attribute:: delay_up
        
        	Delay up in seconds
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: second
        
        .. attribute:: enable
        
        	Enable the Track
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list
        
        	Track type boolean list
        	**type**\:   :py:class:`TypeBooleanList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList>`
        
        .. attribute:: type_boolean_list_and_enable
        
        	Enable track type boolean list and
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list_or_enable
        
        	Enable track type boolean list or
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_interface
        
        	Track type line\-protocol
        	**type**\:   :py:class:`TypeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeInterface>`
        
        .. attribute:: type_interface_enable
        
        	Enable track type Interface
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_list
        
        	Track type boolean list
        	**type**\:   :py:class:`TypeList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList>`
        
        .. attribute:: type_route
        
        	Track type route ipv4
        	**type**\:   :py:class:`TypeRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute>`
        
        .. attribute:: type_route_enable
        
        	Enable track type Route
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'manageability-object-tracking-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_name = None
            self.delay_down = None
            self.delay_up = None
            self.enable = None
            self.type_boolean_list = ObjectTrackings.ObjectTracking.TypeBooleanList()
            self.type_boolean_list.parent = self
            self.type_boolean_list_and_enable = None
            self.type_boolean_list_or_enable = None
            self.type_interface = ObjectTrackings.ObjectTracking.TypeInterface()
            self.type_interface.parent = self
            self.type_interface_enable = None
            self.type_list = ObjectTrackings.ObjectTracking.TypeList()
            self.type_list.parent = self
            self.type_route = ObjectTrackings.ObjectTracking.TypeRoute()
            self.type_route.parent = self
            self.type_route_enable = None


        class TypeInterface(object):
            """
            Track type line\-protocol
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:type-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeInterface']['meta_info']


        class TypeList(object):
            """
            Track type boolean list
            
            .. attribute:: threshold_percentage
            
            	Track type threshold percentage
            	**type**\:   :py:class:`ThresholdPercentage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage>`
            
            .. attribute:: threshold_percentage_object
            
            	Track type threshold percentage
            	**type**\:   :py:class:`ThresholdPercentageObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject>`
            
            .. attribute:: threshold_weight
            
            	Track type threshold weight
            	**type**\:   :py:class:`ThresholdWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight>`
            
            .. attribute:: threshold_weight_object
            
            	Track type threshold weight
            	**type**\:   :py:class:`ThresholdWeightObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.threshold_percentage = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage()
                self.threshold_percentage.parent = self
                self.threshold_percentage_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject()
                self.threshold_percentage_object.parent = self
                self.threshold_weight = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight()
                self.threshold_weight.parent = self
                self.threshold_weight_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject()
                self.threshold_weight_object.parent = self


            class ThresholdWeight(object):
                """
                Track type threshold weight
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:   :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits()
                    self.threshold_limits.parent = self


                class ThresholdLimits(object):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:   :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self


                    class ThresholdUpValues(object):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of    :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold_up_value = YList()
                            self.threshold_up_value.parent = self
                            self.threshold_up_value.name = 'threshold_up_value'


                        class ThresholdUpValue(object):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  <key>
                            
                            	Up value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.up = None
                                self.threshold_down = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.up is None:
                                    raise YPYModelError('Key property up is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-up-value[Cisco-IOS-XR-manageability-object-tracking-cfg:up = ' + str(self.up) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.up is not None:
                                    return True

                                if self.threshold_down is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-up-values'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.threshold_up_value is not None:
                                for child_ref in self.threshold_up_value:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                            return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-limits'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.threshold_up_values is not None and self.threshold_up_values._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-weight'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.threshold_limits is not None and self.threshold_limits._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight']['meta_info']


            class ThresholdPercentageObject(object):
                """
                Track type threshold percentage
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
                    """
                    Track name object
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object = None
                        self.object_weight = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.object is None:
                            raise YPYModelError('Key property object is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:object[Cisco-IOS-XR-manageability-object-tracking-cfg:object = ' + str(self.object) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.object is not None:
                            return True

                        if self.object_weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-percentage-object'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject']['meta_info']


            class ThresholdPercentage(object):
                """
                Track type threshold percentage
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:   :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits()
                    self.threshold_limits.parent = self


                class ThresholdLimits(object):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:   :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self


                    class ThresholdUpValues(object):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of    :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.threshold_up_value = YList()
                            self.threshold_up_value.parent = self
                            self.threshold_up_value.name = 'threshold_up_value'


                        class ThresholdUpValue(object):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  <key>
                            
                            	Up value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.up = None
                                self.threshold_down = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.up is None:
                                    raise YPYModelError('Key property up is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-up-value[Cisco-IOS-XR-manageability-object-tracking-cfg:up = ' + str(self.up) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.up is not None:
                                    return True

                                if self.threshold_down is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-up-values'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.threshold_up_value is not None:
                                for child_ref in self.threshold_up_value:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                            return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-limits'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.threshold_up_values is not None and self.threshold_up_values._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-percentage'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.threshold_limits is not None and self.threshold_limits._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage']['meta_info']


            class ThresholdWeightObject(object):
                """
                Track type threshold weight
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YList()
                    self.object.parent = self
                    self.object.name = 'object'


                class Object(object):
                    """
                    Track name object
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object = None
                        self.object_weight = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.object is None:
                            raise YPYModelError('Key property object is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:object[Cisco-IOS-XR-manageability-object-tracking-cfg:object = ' + str(self.object) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.object is not None:
                            return True

                        if self.object_weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:threshold-weight-object'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.object is not None:
                        for child_ref in self.object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:type-list'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.threshold_percentage is not None and self.threshold_percentage._has_data():
                    return True

                if self.threshold_percentage_object is not None and self.threshold_percentage_object._has_data():
                    return True

                if self.threshold_weight is not None and self.threshold_weight._has_data():
                    return True

                if self.threshold_weight_object is not None and self.threshold_weight_object._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info']


        class TypeRoute(object):
            """
            Track type route ipv4
            
            .. attribute:: ip_address
            
            	set track IPv4 address
            	**type**\:   :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute.IpAddress>`
            
            	**presence node**\: True
            
            .. attribute:: vrf
            
            	VRF tag \- use 'default' for the DEFAULT vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ip_address = None
                self.vrf = None


            class IpAddress(object):
                """
                set track IPv4 address
                
                .. attribute:: address
                
                	IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mask
                
                	Mask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.address = None
                    self.mask = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:ip-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.address is not None:
                        return True

                    if self.mask is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeRoute.IpAddress']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:type-route'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ip_address is not None and self.ip_address._has_data():
                    return True

                if self.vrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeRoute']['meta_info']


        class TypeBooleanList(object):
            """
            Track type boolean list
            
            .. attribute:: and_objects
            
            	Track type boolean and list
            	**type**\:   :py:class:`AndObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects>`
            
            .. attribute:: or_objects
            
            	Track type boolean or list
            	**type**\:   :py:class:`OrObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.and_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects()
                self.and_objects.parent = self
                self.or_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects()
                self.or_objects.parent = self


            class OrObjects(object):
                """
                Track type boolean or list
                
                .. attribute:: or_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of    :py:class:`OrObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.or_object = YList()
                    self.or_object.parent = self
                    self.or_object.name = 'or_object'


                class OrObject(object):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:   :py:class:`ObjectTrackingBooleanSignEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSignEnum>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object = None
                        self.object_sign = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.object is None:
                            raise YPYModelError('Key property object is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:or-object[Cisco-IOS-XR-manageability-object-tracking-cfg:object = ' + str(self.object) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.object is not None:
                            return True

                        if self.object_sign is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:or-objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.or_object is not None:
                        for child_ref in self.or_object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects']['meta_info']


            class AndObjects(object):
                """
                Track type boolean and list
                
                .. attribute:: and_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of    :py:class:`AndObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.and_object = YList()
                    self.and_object.parent = self
                    self.and_object.name = 'and_object'


                class AndObject(object):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object_name  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:   :py:class:`ObjectTrackingBooleanSignEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSignEnum>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.object_name = None
                        self.object_sign = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.object_name is None:
                            raise YPYModelError('Key property object_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:and-object[Cisco-IOS-XR-manageability-object-tracking-cfg:object-name = ' + str(self.object_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.object_sign is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                        return meta._meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:and-objects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.and_object is not None:
                        for child_ref in self.and_object:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                    return meta._meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-cfg:type-boolean-list'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.and_objects is not None and self.and_objects._has_data():
                    return True

                if self.or_objects is not None and self.or_objects._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
                return meta._meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList']['meta_info']

        @property
        def _common_path(self):
            if self.track_name is None:
                raise YPYModelError('Key property track_name is None')

            return '/Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings/Cisco-IOS-XR-manageability-object-tracking-cfg:object-tracking[Cisco-IOS-XR-manageability-object-tracking-cfg:track-name = ' + str(self.track_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.track_name is not None:
                return True

            if self.delay_down is not None:
                return True

            if self.delay_up is not None:
                return True

            if self.enable is not None:
                return True

            if self.type_boolean_list is not None and self.type_boolean_list._has_data():
                return True

            if self.type_boolean_list_and_enable is not None:
                return True

            if self.type_boolean_list_or_enable is not None:
                return True

            if self.type_interface is not None and self.type_interface._has_data():
                return True

            if self.type_interface_enable is not None:
                return True

            if self.type_list is not None and self.type_list._has_data():
                return True

            if self.type_route is not None and self.type_route._has_data():
                return True

            if self.type_route_enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
            return meta._meta_table['ObjectTrackings.ObjectTracking']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.object_tracking is not None:
            for child_ref in self.object_tracking:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_cfg as meta
        return meta._meta_table['ObjectTrackings']['meta_info']


