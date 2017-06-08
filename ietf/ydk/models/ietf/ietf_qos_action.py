""" ietf_qos_action 

This module contains a collection of YANG definitions for
configuring qos specification implementations.
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_qos_policy import ActionTypeIdentity


class MinRateIdentity(ActionTypeIdentity):
    """
    min\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MinRateIdentity']['meta_info']


class MeterReferenceIdentity(ActionTypeIdentity):
    """
    meter reference action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterReferenceIdentity']['meta_info']


class MaxRateIdentity(ActionTypeIdentity):
    """
    max\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MaxRateIdentity']['meta_info']


class ChildPolicyIdentity(ActionTypeIdentity):
    """
    child\-policy action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['ChildPolicyIdentity']['meta_info']


class MeterInlineIdentity(ActionTypeIdentity):
    """
    meter\-inline action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterInlineIdentity']['meta_info']


class RateUnitTypeIdentity(object):
    """
    base rate\-unit type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['RateUnitTypeIdentity']['meta_info']


class DscpMarkingIdentity(ActionTypeIdentity):
    """
    dscp marking action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['DscpMarkingIdentity']['meta_info']


class DropTypeIdentity(object):
    """
    drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['DropTypeIdentity']['meta_info']


class MeterActionTypeIdentity(object):
    """
    action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterActionTypeIdentity']['meta_info']


class SchedularIdentity(ActionTypeIdentity):
    """
    schedular action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['SchedularIdentity']['meta_info']


class CountIdentity(ActionTypeIdentity):
    """
    discard action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['CountIdentity']['meta_info']


class MeterTypeIdentity(object):
    """
    This base identity type defines meter types
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterTypeIdentity']['meta_info']


class QueueIdentity(ActionTypeIdentity):
    """
    queue action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['QueueIdentity']['meta_info']


class DiscardIdentity(ActionTypeIdentity):
    """
    discard action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        ActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['DiscardIdentity']['meta_info']


class MeterTemplate(object):
    """
    list of meter templates
    
    .. attribute:: meter_entry
    
    	meter entry template
    	**type**\: list of    :py:class:`MeterEntry <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry>`
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        self.meter_entry = YList()
        self.meter_entry.parent = self
        self.meter_entry.name = 'meter_entry'


    class MeterEntry(object):
        """
        meter entry template
        
        .. attribute:: meter_name  <key>
        
        	meter identifier
        	**type**\:  str
        
        .. attribute:: one_rate_tri_color_meter
        
        	single rate three color meter
        	**type**\:   :py:class:`OneRateTriColorMeter <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter>`
        
        .. attribute:: one_rate_two_color_meter
        
        	single rate two color marker meter
        	**type**\:   :py:class:`OneRateTwoColorMeter <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTwoColorMeter>`
        
        .. attribute:: two_rate_tri_color_meter
        
        	two rate three color meter
        	**type**\:   :py:class:`TwoRateTriColorMeter <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter>`
        
        

        """

        _prefix = 'action'
        _revision = '2016-06-15'

        def __init__(self):
            self.parent = None
            self.meter_name = None
            self.one_rate_tri_color_meter = MeterTemplate.MeterEntry.OneRateTriColorMeter()
            self.one_rate_tri_color_meter.parent = self
            self.one_rate_two_color_meter = MeterTemplate.MeterEntry.OneRateTwoColorMeter()
            self.one_rate_two_color_meter.parent = self
            self.two_rate_tri_color_meter = MeterTemplate.MeterEntry.TwoRateTriColorMeter()
            self.two_rate_tri_color_meter.parent = self


        class OneRateTwoColorMeter(object):
            """
            single rate two color marker meter
            
            .. attribute:: conform_action
            
            	conform action
            	**type**\:   :py:class:`ConformAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction>`
            
            .. attribute:: exceed_action
            
            	exceed action
            	**type**\:   :py:class:`ExceedAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction>`
            
            .. attribute:: meter_burst
            
            	burst size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byes
            
            .. attribute:: meter_rate
            
            	meter rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits-per-second
            
            

            """

            _prefix = 'action'
            _revision = '2016-06-15'

            def __init__(self):
                self.parent = None
                self.conform_action = MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction()
                self.conform_action.parent = self
                self.exceed_action = MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction()
                self.exceed_action.parent = self
                self.meter_burst = None
                self.meter_rate = None


            class ConformAction(object):
                """
                conform action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:conform-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction']['meta_info']


            class ExceedAction(object):
                """
                exceed action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:exceed-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-qos-action:one-rate-two-color-meter'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.conform_action is not None and self.conform_action._has_data():
                    return True

                if self.exceed_action is not None and self.exceed_action._has_data():
                    return True

                if self.meter_burst is not None:
                    return True

                if self.meter_rate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_qos_action as meta
                return meta._meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter']['meta_info']


        class OneRateTriColorMeter(object):
            """
            single rate three color meter
            
            .. attribute:: committed_burst
            
            	commited burst size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byes
            
            .. attribute:: committed_rate
            
            	meter rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits-per-second
            
            .. attribute:: conform_action
            
            	conform, or green action
            	**type**\:   :py:class:`ConformAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction>`
            
            .. attribute:: exceed_action
            
            	exceed, or yellow action
            	**type**\:   :py:class:`ExceedAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction>`
            
            .. attribute:: excess_burst
            
            	excess burst size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byes
            
            .. attribute:: violate_action
            
            	violate, or red action
            	**type**\:   :py:class:`ViolateAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction>`
            
            

            """

            _prefix = 'action'
            _revision = '2016-06-15'

            def __init__(self):
                self.parent = None
                self.committed_burst = None
                self.committed_rate = None
                self.conform_action = MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction()
                self.conform_action.parent = self
                self.exceed_action = MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction()
                self.exceed_action.parent = self
                self.excess_burst = None
                self.violate_action = MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction()
                self.violate_action.parent = self


            class ConformAction(object):
                """
                conform, or green action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:conform-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction']['meta_info']


            class ExceedAction(object):
                """
                exceed, or yellow action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:exceed-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction']['meta_info']


            class ViolateAction(object):
                """
                violate, or red action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:violate-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-qos-action:one-rate-tri-color-meter'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.committed_burst is not None:
                    return True

                if self.committed_rate is not None:
                    return True

                if self.conform_action is not None and self.conform_action._has_data():
                    return True

                if self.exceed_action is not None and self.exceed_action._has_data():
                    return True

                if self.excess_burst is not None:
                    return True

                if self.violate_action is not None and self.violate_action._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_qos_action as meta
                return meta._meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter']['meta_info']


        class TwoRateTriColorMeter(object):
            """
            two rate three color meter
            
            .. attribute:: committed_burst
            
            	commited burst size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byes
            
            .. attribute:: committed_rate
            
            	meter rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits-per-second
            
            .. attribute:: conform_action
            
            	conform, or green action
            	**type**\:   :py:class:`ConformAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction>`
            
            .. attribute:: exceed_action
            
            	exceed, or yellow action
            	**type**\:   :py:class:`ExceedAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction>`
            
            .. attribute:: peak_burst
            
            	commited burst size
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byes
            
            .. attribute:: peak_rate
            
            	meter rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits-per-second
            
            .. attribute:: violate_action
            
            	exceed, or red action
            	**type**\:   :py:class:`ViolateAction <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction>`
            
            

            """

            _prefix = 'action'
            _revision = '2016-06-15'

            def __init__(self):
                self.parent = None
                self.committed_burst = None
                self.committed_rate = None
                self.conform_action = MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction()
                self.conform_action.parent = self
                self.exceed_action = MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction()
                self.exceed_action.parent = self
                self.peak_burst = None
                self.peak_rate = None
                self.violate_action = MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction()
                self.violate_action.parent = self


            class ConformAction(object):
                """
                conform, or green action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:conform-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction']['meta_info']


            class ExceedAction(object):
                """
                exceed, or yellow action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:exceed-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction']['meta_info']


            class ViolateAction(object):
                """
                exceed, or red action
                
                .. attribute:: meter_action_params
                
                	Configuration of basic\-meter & associated actions
                	**type**\: list of    :py:class:`MeterActionParams <ydk.models.ietf.ietf_qos_action.MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams>`
                
                

                """

                _prefix = 'action'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.meter_action_params = YList()
                    self.meter_action_params.parent = self
                    self.meter_action_params.name = 'meter_action_params'


                class MeterActionParams(object):
                    """
                    Configuration of basic\-meter & associated actions
                    
                    .. attribute:: meter_action_type  <key>
                    
                    	meter action type
                    	**type**\:   :py:class:`MeterActionTypeIdentity <ydk.models.ietf.ietf_qos_action.MeterActionTypeIdentity>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.meter_action_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_action_type is None:
                            raise YPYModelError('Key property meter_action_type is None')

                        return self.parent._common_path +'/ietf-qos-action:meter-action-params[ietf-qos-action:meter-action-type = ' + str(self.meter_action_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.meter_action_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_action as meta
                        return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-action:violate-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.meter_action_params is not None:
                        for child_ref in self.meter_action_params:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_action as meta
                    return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-qos-action:two-rate-tri-color-meter'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.committed_burst is not None:
                    return True

                if self.committed_rate is not None:
                    return True

                if self.conform_action is not None and self.conform_action._has_data():
                    return True

                if self.exceed_action is not None and self.exceed_action._has_data():
                    return True

                if self.peak_burst is not None:
                    return True

                if self.peak_rate is not None:
                    return True

                if self.violate_action is not None and self.violate_action._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_qos_action as meta
                return meta._meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter']['meta_info']

        @property
        def _common_path(self):
            if self.meter_name is None:
                raise YPYModelError('Key property meter_name is None')

            return '/ietf-qos-action:meter-template/ietf-qos-action:meter-entry[ietf-qos-action:meter-name = ' + str(self.meter_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.meter_name is not None:
                return True

            if self.one_rate_tri_color_meter is not None and self.one_rate_tri_color_meter._has_data():
                return True

            if self.one_rate_two_color_meter is not None and self.one_rate_two_color_meter._has_data():
                return True

            if self.two_rate_tri_color_meter is not None and self.two_rate_tri_color_meter._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_qos_action as meta
            return meta._meta_table['MeterTemplate.MeterEntry']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-qos-action:meter-template'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.meter_entry is not None:
            for child_ref in self.meter_entry:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterTemplate']['meta_info']


class KiloBitsPerSecondIdentity(RateUnitTypeIdentity):
    """
    kilo bits per second identity
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        RateUnitTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['KiloBitsPerSecondIdentity']['meta_info']


class TailDropIdentity(DropTypeIdentity):
    """
    tail drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        DropTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['TailDropIdentity']['meta_info']


class MeterActionMarkDscpIdentity(MeterActionTypeIdentity):
    """
    dscp mark action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        MeterActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterActionMarkDscpIdentity']['meta_info']


class OneRateTwoColorMeterTypeIdentity(MeterTypeIdentity):
    """
    one rate two color meter type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        MeterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['OneRateTwoColorMeterTypeIdentity']['meta_info']


class GigaBitsPerSecondIdentity(RateUnitTypeIdentity):
    """
    mega bits per second identity
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        RateUnitTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['GigaBitsPerSecondIdentity']['meta_info']


class MeterActionDropIdentity(MeterActionTypeIdentity):
    """
    drop action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        MeterActionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MeterActionDropIdentity']['meta_info']


class PercentIdentity(RateUnitTypeIdentity):
    """
    percentage
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        RateUnitTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['PercentIdentity']['meta_info']


class TwoRateTriColorMeterTypeIdentity(MeterTypeIdentity):
    """
    two rate three color meter action type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        MeterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['TwoRateTriColorMeterTypeIdentity']['meta_info']


class BitsPerSecondIdentity(RateUnitTypeIdentity):
    """
    bits per second identity
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        RateUnitTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['BitsPerSecondIdentity']['meta_info']


class OneRateTriColorMeterTypeIdentity(MeterTypeIdentity):
    """
    one rate three color meter type
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        MeterTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['OneRateTriColorMeterTypeIdentity']['meta_info']


class MegaBitsPerSecondIdentity(RateUnitTypeIdentity):
    """
    mega bits per second identity
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        RateUnitTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['MegaBitsPerSecondIdentity']['meta_info']


class RandomDetectIdentity(DropTypeIdentity):
    """
    random detect algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2016-06-15'

    def __init__(self):
        DropTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_action as meta
        return meta._meta_table['RandomDetectIdentity']['meta_info']


