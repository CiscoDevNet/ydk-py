""" Cisco_IOS_XR_mpls_lsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-lsd package configuration.

This module contains definitions
for the following management objects\:
  mpls\-lsd\: MPLS LSD configuration data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MplsIpTtlPropagateDisableEnum(Enum):
    """
    MplsIpTtlPropagateDisableEnum

    Mpls ip ttl propagate disable

    .. data:: ALL = 0

    	Disable IP TTL propagation for all MPLS packets

    .. data:: FORWARD = 1

    	Disable IP TTL propagation for only forwarded

    	MPLS packets

    .. data:: LOCAL = 2

    	Disable IP TTL propagation for only locally

    	generated MPLS packets

    """

    ALL = 0

    FORWARD = 1

    LOCAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['MplsIpTtlPropagateDisableEnum']



class MplsLsd(object):
    """
    MPLS LSD configuration data
    
    .. attribute:: label_databases
    
    	Table of label databases
    	**type**\: :py:class:`LabelDatabases <ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases>`
    
    .. attribute:: mpls_ip_ttl_expiration_pop
    
    	Number of labels to pop upon MPLS TTL expiry
    	**type**\: int
    
    	**range:** 1..10
    
    .. attribute:: app_reg_delay_disable
    
    	Disable LSD application reg delay
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: mpls_entropy_label
    
    	Enable MPLS Entropy Label
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: mpls_ip_ttl_propagate_disable
    
    	Disable Propagation of IP TTL onto the label stack
    	**type**\: :py:class:`MplsIpTtlPropagateDisableEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg.MplsIpTtlPropagateDisableEnum>`
    
    

    """

    _prefix = 'mpls-lsd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.label_databases = MplsLsd.LabelDatabases()
        self.label_databases.parent = self
        self.mpls_ip_ttl_expiration_pop = None
        self.app_reg_delay_disable = None
        self.mpls_entropy_label = None
        self.mpls_ip_ttl_propagate_disable = None


    class LabelDatabases(object):
        """
        Table of label databases
        
        .. attribute:: label_database
        
        	A label database
        	**type**\: list of :py:class:`LabelDatabase <ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase>`
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.label_database = YList()
            self.label_database.parent = self
            self.label_database.name = 'label_database'


        class LabelDatabase(object):
            """
            A label database
            
            .. attribute:: label_database_id  <key>
            
            	Label database identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_range
            
            	Label range
            	**type**\: :py:class:`LabelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelRange>`
            
            

            """

            _prefix = 'mpls-lsd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.label_database_id = None
                self.label_range = MplsLsd.LabelDatabases.LabelDatabase.LabelRange()
                self.label_range.parent = self


            class LabelRange(object):
                """
                Label range
                
                .. attribute:: minvalue
                
                	Minimum label value
                	**type**\: int
                
                	**range:** 16000..1048575
                
                .. attribute:: max_value
                
                	Maximum label value
                	**type**\: int
                
                	**range:** 16000..1048575
                
                .. attribute:: min_static_value
                
                	Minimum static label value
                	**type**\: int
                
                	**range:** 0..1048575
                
                .. attribute:: max_static_value
                
                	Maximum static label value
                	**type**\: int
                
                	**range:** 0..1048575
                
                

                """

                _prefix = 'mpls-lsd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.minvalue = None
                    self.max_value = None
                    self.min_static_value = None
                    self.max_static_value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-lsd-cfg:label-range'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.minvalue is not None:
                        return True

                    if self.max_value is not None:
                        return True

                    if self.min_static_value is not None:
                        return True

                    if self.max_static_value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                    return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelRange']['meta_info']

            @property
            def _common_path(self):
                if self.label_database_id is None:
                    raise YPYDataValidationError('Key property label_database_id is None')

                return '/Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/Cisco-IOS-XR-mpls-lsd-cfg:label-databases/Cisco-IOS-XR-mpls-lsd-cfg:label-database[Cisco-IOS-XR-mpls-lsd-cfg:label-database-id = ' + str(self.label_database_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.label_database_id is not None:
                    return True

                if self.label_range is not None and self.label_range._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/Cisco-IOS-XR-mpls-lsd-cfg:label-databases'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.label_database is not None:
                for child_ref in self.label_database:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
            return meta._meta_table['MplsLsd.LabelDatabases']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.label_databases is not None and self.label_databases._has_data():
            return True

        if self.mpls_ip_ttl_expiration_pop is not None:
            return True

        if self.app_reg_delay_disable is not None:
            return True

        if self.mpls_entropy_label is not None:
            return True

        if self.mpls_ip_ttl_propagate_disable is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['MplsLsd']['meta_info']


