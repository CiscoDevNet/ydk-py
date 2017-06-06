""" openconfig_vlan 

This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class VlanModeTypeEnum(Enum):
    """
    VlanModeTypeEnum

    VLAN interface mode (trunk or access)

    .. data:: ACCESS = 0

    	Access mode VLAN interface (No 802.1q header)

    .. data:: TRUNK = 1

    	Trunk mode VLAN interface

    """

    ACCESS = 0

    TRUNK = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_vlan as meta
        return meta._meta_table['VlanModeTypeEnum']



class Vlans(object):
    """
    Container for VLAN configuration and state
    variables
    
    .. attribute:: vlan
    
    	Configured VLANs keyed by id
    	**type**\: list of    :py:class:`Vlan <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan>`
    
    

    """

    _prefix = 'vlan'
    _revision = '2015-10-09'

    def __init__(self):
        self.vlan = YList()
        self.vlan.parent = self
        self.vlan.name = 'vlan'


    class Vlan(object):
        """
        Configured VLANs keyed by id
        
        .. attribute:: vlan_id  <key>
        
        	references the configured vlan\-id
        	**type**\:  int
        
        	**range:** 1..4094
        
        	**refers to**\:  :py:class:`vlan_id <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: config
        
        	Configuration parameters for VLANs
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: state
        
        	State variables for VLANs
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State>`
        
        

        """

        _prefix = 'vlan'
        _revision = '2015-10-09'

        def __init__(self):
            self.parent = None
            self.vlan_id = None
            self.config = Vlans.Vlan.Config()
            self.config.parent = self
            self.state = Vlans.Vlan.State()
            self.state.parent = self


        class Config(object):
            """
            Configuration parameters for VLANs
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`StatusEnum <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config.StatusEnum>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'vlan'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.status = None
                self.vlan_id = None

            class StatusEnum(Enum):
                """
                StatusEnum

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = 0

                SUSPENDED = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_vlan as meta
                    return meta._meta_table['Vlans.Vlan.Config.StatusEnum']


            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-vlan:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.status is not None:
                    return True

                if self.vlan_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_vlan as meta
                return meta._meta_table['Vlans.Vlan.Config']['meta_info']


        class State(object):
            """
            State variables for VLANs
            
            .. attribute:: member_ports
            
            	List of current member ports including access ports and trunk ports that support this vlan
            	**type**\:  list of str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`StatusEnum <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State.StatusEnum>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'vlan'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.member_ports = YLeafList()
                self.member_ports.parent = self
                self.member_ports.name = 'member_ports'
                self.name = None
                self.status = None
                self.vlan_id = None

            class StatusEnum(Enum):
                """
                StatusEnum

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = 0

                SUSPENDED = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_vlan as meta
                    return meta._meta_table['Vlans.Vlan.State.StatusEnum']


            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-vlan:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_ports is not None:
                    for child in self.member_ports:
                        if child is not None:
                            return True

                if self.name is not None:
                    return True

                if self.status is not None:
                    return True

                if self.vlan_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_vlan as meta
                return meta._meta_table['Vlans.Vlan.State']['meta_info']

        @property
        def _common_path(self):
            if self.vlan_id is None:
                raise YPYModelError('Key property vlan_id is None')

            return '/openconfig-vlan:vlans/openconfig-vlan:vlan[openconfig-vlan:vlan-id = ' + str(self.vlan_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vlan_id is not None:
                return True

            if self.config is not None and self.config._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_vlan as meta
            return meta._meta_table['Vlans.Vlan']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-vlan:vlans'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vlan is not None:
            for child_ref in self.vlan:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_vlan as meta
        return meta._meta_table['Vlans']['meta_info']


