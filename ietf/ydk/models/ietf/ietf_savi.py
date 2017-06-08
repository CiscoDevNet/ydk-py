""" ietf_savi 

This YANG module defines essential components for the management
of a savi subsystem.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class BindingStateIdentity(object):
    """
    Base identity for the sates of binding entry.
    
    

    """

    _prefix = 'savi'
    _revision = '2017-02-15'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi as meta
        return meta._meta_table['BindingStateIdentity']['meta_info']


class SaviState(object):
    """
    State data of the savi subsystem.
    
    .. attribute:: binding_table
    
    	Container for binding table
    	**type**\:   :py:class:`BindingTable <ydk.models.ietf.ietf_savi.SaviState.BindingTable>`
    
    .. attribute:: savi_instances
    
    	Container of parameters for each savi method
    	**type**\:   :py:class:`SaviInstances <ydk.models.ietf.ietf_savi.SaviState.SaviInstances>`
    
    .. attribute:: statistics
    
    	Container of statistics parameters for savi subsystem
    	**type**\:   :py:class:`Statistics <ydk.models.ietf.ietf_savi.SaviState.Statistics>`
    
    

    """

    _prefix = 'savi'
    _revision = '2017-02-15'

    def __init__(self):
        self.binding_table = SaviState.BindingTable()
        self.binding_table.parent = self
        self.savi_instances = SaviState.SaviInstances()
        self.savi_instances.parent = self
        self.statistics = SaviState.Statistics()
        self.statistics.parent = self


    class SaviInstances(object):
        """
        Container of parameters for each savi method.
        
        .. attribute:: savi_instance
        
        	A list of parameters for each savi method
        	**type**\: list of    :py:class:`SaviInstance <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.savi_instance = YList()
            self.savi_instance.parent = self
            self.savi_instance.name = 'savi_instance'


        class SaviInstance(object):
            """
            A list of parameters for each savi method.
            
            .. attribute:: savi_method  <key>
            
            	IP address assignment methods
            	**type**\:  str
            
            .. attribute:: ietf_savi_dhcpv4_binding_state_table
            
            	Binding state table specific for SAVI DHCPv4
            	**type**\:   :py:class:`IetfSaviDhcpv4_BindingStateTable <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable>`
            
            .. attribute:: ietf_savi_dhcpv6_binding_state_table
            
            	Binding state table specific for SAVI DHCPv6
            	**type**\:   :py:class:`IetfSaviDhcpv6_BindingStateTable <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable>`
            
            .. attribute:: ietf_savi_fcfs_binding_state_table
            
            	Binding state table specific for SAVI FCFS
            	**type**\:   :py:class:`IetfSaviFcfs_BindingStateTable <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable>`
            
            .. attribute:: ietf_savi_send_binding_state_table
            
            	Binding state table specific for SAVI SEND
            	**type**\:   :py:class:`IetfSaviSend_BindingStateTable <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable>`
            
            .. attribute:: preference
            
            	Preference of the savi method
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.savi_method = None
                self.ietf_savi_dhcpv4_binding_state_table = SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable()
                self.ietf_savi_dhcpv4_binding_state_table.parent = self
                self.ietf_savi_dhcpv6_binding_state_table = SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable()
                self.ietf_savi_dhcpv6_binding_state_table.parent = self
                self.ietf_savi_fcfs_binding_state_table = SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable()
                self.ietf_savi_fcfs_binding_state_table.parent = self
                self.ietf_savi_send_binding_state_table = SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable()
                self.ietf_savi_send_binding_state_table.parent = self
                self.preference = None


            class IetfSaviDhcpv4_BindingStateTable(object):
                """
                Binding state table specific for SAVI DHCPv4.
                
                .. attribute:: binding_state_entry
                
                	A binding state entry specific for SAVI DHCPv4
                	**type**\: list of    :py:class:`BindingStateEntry <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry>`
                
                

                """

                _prefix = 'savi-dhcpv4'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.binding_state_entry = YList()
                    self.binding_state_entry.parent = self
                    self.binding_state_entry.name = 'binding_state_entry'


                class BindingStateEntry(object):
                    """
                    A binding state entry specific for SAVI DHCPv4.
                    
                    .. attribute:: address  <key>
                    
                    	The binding source IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ifname  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: lifetime
                    
                    	The remaining lifetime of the entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mac
                    
                    	The binding source mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: state
                    
                    	State of the entry as defined in SAVI DHCP\: NO\_BIND, INIT\_BIND, BOUND, DETECTION , RECOVERY, VERIFY
                    	**type**\:   :py:class:`SaviDhcpStateIdentity <ydk.models.ietf.ietf_savi_dhcpv4.SaviDhcpStateIdentity>`
                    
                    .. attribute:: tid
                    
                    	The Transaction ID of the corresponding DHCP transaction
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timeouts
                    
                    	the number of timeouts that expired in the current state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'savi-dhcpv4'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.ifname = None
                        self.lifetime = None
                        self.mac = None
                        self.state = None
                        self.tid = None
                        self.timeouts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.ifname is None:
                            raise YPYModelError('Key property ifname is None')

                        return self.parent._common_path +'/ietf-savi-dhcpv4:binding-state-entry[ietf-savi-dhcpv4:address = ' + str(self.address) + '][ietf-savi-dhcpv4:ifname = ' + str(self.ifname) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.ifname is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mac is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.tid is not None:
                            return True

                        if self.timeouts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-dhcpv4:ietf-savi-dhcpv4_binding-state-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.binding_state_entry is not None:
                        for child_ref in self.binding_state_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable']['meta_info']


            class IetfSaviDhcpv6_BindingStateTable(object):
                """
                Binding state table specific for SAVI DHCPv6.
                
                .. attribute:: binding_state_entry
                
                	A binding state entry specific for SAVI DHCPv6
                	**type**\: list of    :py:class:`BindingStateEntry <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry>`
                
                

                """

                _prefix = 'savi-dhcpv6'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.binding_state_entry = YList()
                    self.binding_state_entry.parent = self
                    self.binding_state_entry.name = 'binding_state_entry'


                class BindingStateEntry(object):
                    """
                    A binding state entry specific for SAVI DHCPv6.
                    
                    .. attribute:: address  <key>
                    
                    	The binding source IP address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ifname  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: lifetime
                    
                    	The remaining lifetime of the entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mac
                    
                    	The binding source mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: state
                    
                    	State of the entry as defined in SAVI DHCP\: NO\_BIND, INIT\_BIND, BOUND, DETECTION , RECOVERY, VERIFY
                    	**type**\:   :py:class:`SaviDhcpStateIdentity <ydk.models.ietf.ietf_savi_dhcpv6.SaviDhcpStateIdentity>`
                    
                    .. attribute:: tid
                    
                    	The Transaction ID of the corresponding DHCP transaction
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timeouts
                    
                    	The number of timeouts that expired in the current state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'savi-dhcpv6'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.ifname = None
                        self.lifetime = None
                        self.mac = None
                        self.state = None
                        self.tid = None
                        self.timeouts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.ifname is None:
                            raise YPYModelError('Key property ifname is None')

                        return self.parent._common_path +'/ietf-savi-dhcpv6:binding-state-entry[ietf-savi-dhcpv6:address = ' + str(self.address) + '][ietf-savi-dhcpv6:ifname = ' + str(self.ifname) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.ifname is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mac is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.tid is not None:
                            return True

                        if self.timeouts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-dhcpv6:ietf-savi-dhcpv6_binding-state-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.binding_state_entry is not None:
                        for child_ref in self.binding_state_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable']['meta_info']


            class IetfSaviFcfs_BindingStateTable(object):
                """
                Binding state table specific for SAVI FCFS.
                
                .. attribute:: binding_state_entry
                
                	A binding status entry specific for SAVI FCFS
                	**type**\: list of    :py:class:`BindingStateEntry <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry>`
                
                

                """

                _prefix = 'savi-fcfs'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.binding_state_entry = YList()
                    self.binding_state_entry.parent = self
                    self.binding_state_entry.name = 'binding_state_entry'


                class BindingStateEntry(object):
                    """
                    A binding status entry specific for SAVI FCFS.
                    
                    .. attribute:: address  <key>
                    
                    	The binding source IP address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ifname  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: lifetime
                    
                    	The remaining lifetime of the entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mac
                    
                    	The binding source mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: state
                    
                    	State of the entry as defined in SAVI FCFS\: NO\_BIND, TENTATIVE, VALID, TESTING\_VP, TESTING\_TP\-LT
                    	**type**\:   :py:class:`SaviFcfsStateIdentity <ydk.models.ietf.ietf_savi_fcfs.SaviFcfsStateIdentity>`
                    
                    

                    """

                    _prefix = 'savi-fcfs'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.ifname = None
                        self.lifetime = None
                        self.mac = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.ifname is None:
                            raise YPYModelError('Key property ifname is None')

                        return self.parent._common_path +'/ietf-savi-fcfs:binding-state-entry[ietf-savi-fcfs:address = ' + str(self.address) + '][ietf-savi-fcfs:ifname = ' + str(self.ifname) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.ifname is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mac is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-fcfs:ietf-savi-fcfs_binding-state-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.binding_state_entry is not None:
                        for child_ref in self.binding_state_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable']['meta_info']


            class IetfSaviSend_BindingStateTable(object):
                """
                Binding state table specific for SAVI SEND.
                
                .. attribute:: binding_state_entry
                
                	A binding state entry specific for SAVI SEND
                	**type**\: list of    :py:class:`BindingStateEntry <ydk.models.ietf.ietf_savi.SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry>`
                
                

                """

                _prefix = 'savi-send'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.binding_state_entry = YList()
                    self.binding_state_entry.parent = self
                    self.binding_state_entry.name = 'binding_state_entry'


                class BindingStateEntry(object):
                    """
                    A binding state entry specific for SAVI SEND.
                    
                    .. attribute:: address  <key>
                    
                    	The binding source IP address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ifname  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: alternative_if
                    
                    	Alternative interface is a parameter defined in SAVI SEND
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: lifetime
                    
                    	The remaining lifetime of the entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mac
                    
                    	The binding source mac address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: state
                    
                    	State of the entry as defined in SAVI SEND\: TENTATIVE\_DAD, TENTATIVE\_NUD, VALID, TESTING\_VP, TESTING\_VP'
                    	**type**\:   :py:class:`SaviSendStateIdentity <ydk.models.ietf.ietf_savi_send.SaviSendStateIdentity>`
                    
                    

                    """

                    _prefix = 'savi-send'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.ifname = None
                        self.alternative_if = None
                        self.lifetime = None
                        self.mac = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.ifname is None:
                            raise YPYModelError('Key property ifname is None')

                        return self.parent._common_path +'/ietf-savi-send:binding-state-entry[ietf-savi-send:address = ' + str(self.address) + '][ietf-savi-send:ifname = ' + str(self.ifname) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.ifname is not None:
                            return True

                        if self.alternative_if is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mac is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-send:ietf-savi-send_binding-state-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.binding_state_entry is not None:
                        for child_ref in self.binding_state_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable']['meta_info']

            @property
            def _common_path(self):
                if self.savi_method is None:
                    raise YPYModelError('Key property savi_method is None')

                return '/ietf-savi:savi-state/ietf-savi:savi-instances/ietf-savi:savi-instance[ietf-savi:savi-method = ' + str(self.savi_method) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.savi_method is not None:
                    return True

                if self.ietf_savi_dhcpv4_binding_state_table is not None and self.ietf_savi_dhcpv4_binding_state_table._has_data():
                    return True

                if self.ietf_savi_dhcpv6_binding_state_table is not None and self.ietf_savi_dhcpv6_binding_state_table._has_data():
                    return True

                if self.ietf_savi_fcfs_binding_state_table is not None and self.ietf_savi_fcfs_binding_state_table._has_data():
                    return True

                if self.ietf_savi_send_binding_state_table is not None and self.ietf_savi_send_binding_state_table._has_data():
                    return True

                if self.preference is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['SaviState.SaviInstances.SaviInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi-state/ietf-savi:savi-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.savi_instance is not None:
                for child_ref in self.savi_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['SaviState.SaviInstances']['meta_info']


    class BindingTable(object):
        """
        Container for binding table.
        
        .. attribute:: ipv4
        
        	Container for binding table for IPv4 protocol
        	**type**\:   :py:class:`Ipv4 <ydk.models.ietf.ietf_savi.SaviState.BindingTable.Ipv4>`
        
        .. attribute:: ipv6
        
        	Container for binding table for IPv4 protocol
        	**type**\:   :py:class:`Ipv6 <ydk.models.ietf.ietf_savi.SaviState.BindingTable.Ipv6>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.ipv4 = SaviState.BindingTable.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = SaviState.BindingTable.Ipv6()
            self.ipv6.parent = self


        class Ipv4(object):
            """
            Container for binding table for IPv4 protocol.
            
            .. attribute:: binding_entry
            
            	Definition of a binding entry
            	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_savi.SaviState.BindingTable.Ipv4.BindingEntry>`
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.binding_entry = YList()
                self.binding_entry.parent = self
                self.binding_entry.name = 'binding_entry'


            class BindingEntry(object):
                """
                Definition of a binding entry
                
                .. attribute:: address  <key>
                
                	IPv4 address of the binding host
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ifname  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: binding_method
                
                	IP address assignment methods
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: creationtime
                
                	The value of the local clock when the entry was firstly created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: lifetime
                
                	The remaining lifetime of the entry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: mac
                
                	The binding source mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'savi'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.ifname = None
                    self.binding_method = None
                    self.creationtime = None
                    self.lifetime = None
                    self.mac = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.ifname is None:
                        raise YPYModelError('Key property ifname is None')

                    return '/ietf-savi:savi-state/ietf-savi:binding-table/ietf-savi:ipv4/ietf-savi:binding-entry[ietf-savi:address = ' + str(self.address) + '][ietf-savi:ifname = ' + str(self.ifname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.ifname is not None:
                        return True

                    if self.binding_method is not None:
                        return True

                    if self.creationtime is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.mac is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.BindingTable.Ipv4.BindingEntry']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-savi:savi-state/ietf-savi:binding-table/ietf-savi:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.binding_entry is not None:
                    for child_ref in self.binding_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['SaviState.BindingTable.Ipv4']['meta_info']


        class Ipv6(object):
            """
            Container for binding table for IPv4 protocol.
            
            .. attribute:: binding_entry
            
            	Definition of a binding entry
            	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_savi.SaviState.BindingTable.Ipv6.BindingEntry>`
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.binding_entry = YList()
                self.binding_entry.parent = self
                self.binding_entry.name = 'binding_entry'


            class BindingEntry(object):
                """
                Definition of a binding entry
                
                .. attribute:: address  <key>
                
                	IPv6 address of the binding host
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ifname  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: binding_method
                
                	IP address assignment methods
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: creationtime
                
                	The value of the local clock when the entry was firstly created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: lifetime
                
                	The remaining lifetime of the entry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: mac
                
                	The binding source mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'savi'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.ifname = None
                    self.binding_method = None
                    self.creationtime = None
                    self.lifetime = None
                    self.mac = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.ifname is None:
                        raise YPYModelError('Key property ifname is None')

                    return '/ietf-savi:savi-state/ietf-savi:binding-table/ietf-savi:ipv6/ietf-savi:binding-entry[ietf-savi:address = ' + str(self.address) + '][ietf-savi:ifname = ' + str(self.ifname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.ifname is not None:
                        return True

                    if self.binding_method is not None:
                        return True

                    if self.creationtime is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.mac is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.BindingTable.Ipv6.BindingEntry']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-savi:savi-state/ietf-savi:binding-table/ietf-savi:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.binding_entry is not None:
                    for child_ref in self.binding_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['SaviState.BindingTable.Ipv6']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi-state/ietf-savi:binding-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['SaviState.BindingTable']['meta_info']


    class Statistics(object):
        """
        Container of statistics parameters for savi subsystem.
        
        .. attribute:: bst_entry_counts
        
        	The count of the binding state table
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: bst_entry_volume
        
        	The volume of the the binding state table
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: filtering_pks
        
        	Container of parameters for counting filtering packets
        	**type**\:   :py:class:`FilteringPks <ydk.models.ietf.ietf_savi.SaviState.Statistics.FilteringPks>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.bst_entry_counts = None
            self.bst_entry_volume = None
            self.filtering_pks = SaviState.Statistics.FilteringPks()
            self.filtering_pks.parent = self


        class FilteringPks(object):
            """
            Container of parameters for counting filtering packets.
            
            .. attribute:: if_filtering_pks
            
            	A list of parameters for counting filtering packets
            	**type**\: list of    :py:class:`IfFilteringPks <ydk.models.ietf.ietf_savi.SaviState.Statistics.FilteringPks.IfFilteringPks>`
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.if_filtering_pks = YList()
                self.if_filtering_pks.parent = self
                self.if_filtering_pks.name = 'if_filtering_pks'


            class IfFilteringPks(object):
                """
                A list of parameters for counting filtering packets.
                
                .. attribute:: ifname  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: filtering_pks
                
                	The count of filtering packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'savi'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.ifname = None
                    self.filtering_pks = None

                @property
                def _common_path(self):
                    if self.ifname is None:
                        raise YPYModelError('Key property ifname is None')

                    return '/ietf-savi:savi-state/ietf-savi:statistics/ietf-savi:filtering-pks/ietf-savi:if-filtering-pks[ietf-savi:ifname = ' + str(self.ifname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ifname is not None:
                        return True

                    if self.filtering_pks is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['SaviState.Statistics.FilteringPks.IfFilteringPks']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-savi:savi-state/ietf-savi:statistics/ietf-savi:filtering-pks'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.if_filtering_pks is not None:
                    for child_ref in self.if_filtering_pks:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['SaviState.Statistics.FilteringPks']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi-state/ietf-savi:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bst_entry_counts is not None:
                return True

            if self.bst_entry_volume is not None:
                return True

            if self.filtering_pks is not None and self.filtering_pks._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['SaviState.Statistics']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-savi:savi-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.binding_table is not None and self.binding_table._has_data():
            return True

        if self.savi_instances is not None and self.savi_instances._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi as meta
        return meta._meta_table['SaviState']['meta_info']


class Savi(object):
    """
    Configuration data of the savi subsystem.
    
    .. attribute:: binding_table
    
    	Container for binding table
    	**type**\:   :py:class:`BindingTable <ydk.models.ietf.ietf_savi.Savi.BindingTable>`
    
    .. attribute:: if_filtering_attributes
    
    	Container for defining filtering attributes of each interface, common for every savi instance
    	**type**\:   :py:class:`IfFilteringAttributes <ydk.models.ietf.ietf_savi.Savi.IfFilteringAttributes>`
    
    .. attribute:: savi_instances
    
    	Container of parameters for each savi method
    	**type**\:   :py:class:`SaviInstances <ydk.models.ietf.ietf_savi.Savi.SaviInstances>`
    
    

    """

    _prefix = 'savi'
    _revision = '2017-02-15'

    def __init__(self):
        self.binding_table = Savi.BindingTable()
        self.binding_table.parent = self
        self.if_filtering_attributes = Savi.IfFilteringAttributes()
        self.if_filtering_attributes.parent = self
        self.savi_instances = Savi.SaviInstances()
        self.savi_instances.parent = self


    class SaviInstances(object):
        """
        Container of parameters for each savi method.
        
        .. attribute:: savi_instance
        
        	A list of parameters for each savi method
        	**type**\: list of    :py:class:`SaviInstance <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.savi_instance = YList()
            self.savi_instance.parent = self
            self.savi_instance.name = 'savi_instance'


        class SaviInstance(object):
            """
            A list of parameters for each savi method.
            
            .. attribute:: savi_method  <key>
            
            	IP address assignment methods
            	**type**\:  str
            
            .. attribute:: enable
            
            	If the savi method is enabled?
            	**type**\:  bool
            
            .. attribute:: ietf_savi_dhcpv4_params
            
            	Parameters specific to SAVI DHCPv4
            	**type**\:   :py:class:`IetfSaviDhcpv4_Params <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params>`
            
            .. attribute:: ietf_savi_dhcpv6_params
            
            	Parameters specific to SAVI DHCPv6
            	**type**\:   :py:class:`IetfSaviDhcpv6_Params <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params>`
            
            .. attribute:: ietf_savi_fcfs_params
            
            	Parameters specific to SAVI FCFS
            	**type**\:   :py:class:`IetfSaviFcfs_Params <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params>`
            
            .. attribute:: ietf_savi_send_params
            
            	Parameters specific to SAVI SEND
            	**type**\:   :py:class:`IetfSaviSend_Params <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviSend_Params>`
            
            .. attribute:: preference
            
            	Preference of the savi method
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.savi_method = None
                self.enable = None
                self.ietf_savi_dhcpv4_params = Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params()
                self.ietf_savi_dhcpv4_params.parent = self
                self.ietf_savi_dhcpv6_params = Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params()
                self.ietf_savi_dhcpv6_params.parent = self
                self.ietf_savi_fcfs_params = Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params()
                self.ietf_savi_fcfs_params.parent = self
                self.ietf_savi_send_params = Savi.SaviInstances.SaviInstance.IetfSaviSend_Params()
                self.ietf_savi_send_params.parent = self
                self.preference = None


            class IetfSaviDhcpv4_Params(object):
                """
                Parameters specific to SAVI DHCPv4
                
                .. attribute:: datasnooping_interval
                
                	Minimum interval between two successive EVE\_DATA\_UNMATCH events triggered by an attachment. Recommended interval\: 60s and configurable
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 6000
                
                .. attribute:: detection_timeout
                
                	Maximum duration of a hardware address verification step in the VERIFY state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 50
                
                .. attribute:: if_attributes
                
                	Interface attributes specific to SAVI DHCPv4
                	**type**\:   :py:class:`IfAttributes <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes>`
                
                .. attribute:: max_dhcp_responsetime
                
                	Maximum Solicit timeout value. Default is 120s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 12000
                
                .. attribute:: max_leasequery_delay
                
                	Maximum LEASEQUERY timeout value. Default is 10s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 1000
                
                .. attribute:: offlink_delay
                
                	Period after a client is last detected before the binding anchor is being removed.  Recommended delay\: 30s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 3000
                
                

                """

                _prefix = 'savi-dhcpv4'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.datasnooping_interval = None
                    self.detection_timeout = None
                    self.if_attributes = Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes()
                    self.if_attributes.parent = self
                    self.max_dhcp_responsetime = None
                    self.max_leasequery_delay = None
                    self.offlink_delay = None


                class IfAttributes(object):
                    """
                    Interface attributes specific to SAVI DHCPv4.
                    
                    .. attribute:: if_attribute
                    
                    	A list of attributes for each interface
                    	**type**\: list of    :py:class:`IfAttribute <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute>`
                    
                    

                    """

                    _prefix = 'savi-dhcpv4'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.if_attribute = YList()
                        self.if_attribute.parent = self
                        self.if_attribute.name = 'if_attribute'


                    class IfAttribute(object):
                        """
                        A list of attributes for each interface.
                        
                        .. attribute:: ifname  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: data_snooping
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: dhcp_snooping
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: dhcp_trust
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: trust_attribute
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: validating
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'savi-dhcpv4'
                        _revision = '2017-02-15'

                        def __init__(self):
                            self.parent = None
                            self.ifname = None
                            self.data_snooping = None
                            self.dhcp_snooping = None
                            self.dhcp_trust = None
                            self.trust_attribute = None
                            self.validating = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ifname is None:
                                raise YPYModelError('Key property ifname is None')

                            return self.parent._common_path +'/ietf-savi-dhcpv4:if-attribute[ietf-savi-dhcpv4:ifname = ' + str(self.ifname) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ifname is not None:
                                return True

                            if self.data_snooping is not None:
                                return True

                            if self.dhcp_snooping is not None:
                                return True

                            if self.dhcp_trust is not None:
                                return True

                            if self.trust_attribute is not None:
                                return True

                            if self.validating is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_savi as meta
                            return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-savi-dhcpv4:if-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.if_attribute is not None:
                            for child_ref in self.if_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-dhcpv4:ietf-savi-dhcpv4_params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.datasnooping_interval is not None:
                        return True

                    if self.detection_timeout is not None:
                        return True

                    if self.if_attributes is not None and self.if_attributes._has_data():
                        return True

                    if self.max_dhcp_responsetime is not None:
                        return True

                    if self.max_leasequery_delay is not None:
                        return True

                    if self.offlink_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params']['meta_info']


            class IetfSaviDhcpv6_Params(object):
                """
                Parameters specific to SAVI DHCPv6
                
                .. attribute:: datasnooping_interval
                
                	Minimum interval between two successive EVE\_DATA\_UNMATCH events triggered by an attachment. Recommended interval\: 60s and configurable
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 6000
                
                .. attribute:: detection_timeout
                
                	Maximum duration of a hardware address verification step in the VERIFY state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 50
                
                .. attribute:: if_attributes
                
                	Interface attributes specific to SAVI DHCPv6
                	**type**\:   :py:class:`IfAttributes <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes>`
                
                .. attribute:: max_dhcp_responsetime
                
                	Maximum Solicit timeout value. Default is 120s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 12000
                
                .. attribute:: max_leasequery_delay
                
                	Maximum LEASEQUERY timeout value. Default is 10s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 1000
                
                .. attribute:: offlink_delay
                
                	Period after a client is last detected before the binding anchor is being removed.  Recommended delay\: 30s
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 3000
                
                

                """

                _prefix = 'savi-dhcpv6'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.datasnooping_interval = None
                    self.detection_timeout = None
                    self.if_attributes = Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes()
                    self.if_attributes.parent = self
                    self.max_dhcp_responsetime = None
                    self.max_leasequery_delay = None
                    self.offlink_delay = None


                class IfAttributes(object):
                    """
                    Interface attributes specific to SAVI DHCPv6.
                    
                    .. attribute:: if_attribute
                    
                    	A list of attributes for each interface
                    	**type**\: list of    :py:class:`IfAttribute <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute>`
                    
                    

                    """

                    _prefix = 'savi-dhcpv6'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.if_attribute = YList()
                        self.if_attribute.parent = self
                        self.if_attribute.name = 'if_attribute'


                    class IfAttribute(object):
                        """
                        A list of attributes for each interface.
                        
                        .. attribute:: ifname  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: data_snooping
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: dhcp_snooping
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: dhcp_trust
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: trust_attribute
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: validating
                        
                        	An attribute defined in SAVI DHCP
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'savi-dhcpv6'
                        _revision = '2017-02-15'

                        def __init__(self):
                            self.parent = None
                            self.ifname = None
                            self.data_snooping = None
                            self.dhcp_snooping = None
                            self.dhcp_trust = None
                            self.trust_attribute = None
                            self.validating = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ifname is None:
                                raise YPYModelError('Key property ifname is None')

                            return self.parent._common_path +'/ietf-savi-dhcpv6:if-attribute[ietf-savi-dhcpv6:ifname = ' + str(self.ifname) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ifname is not None:
                                return True

                            if self.data_snooping is not None:
                                return True

                            if self.dhcp_snooping is not None:
                                return True

                            if self.dhcp_trust is not None:
                                return True

                            if self.trust_attribute is not None:
                                return True

                            if self.validating is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_savi as meta
                            return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-savi-dhcpv6:if-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.if_attribute is not None:
                            for child_ref in self.if_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-dhcpv6:ietf-savi-dhcpv6_params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.datasnooping_interval is not None:
                        return True

                    if self.detection_timeout is not None:
                        return True

                    if self.if_attributes is not None and self.if_attributes._has_data():
                        return True

                    if self.max_dhcp_responsetime is not None:
                        return True

                    if self.max_leasequery_delay is not None:
                        return True

                    if self.offlink_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params']['meta_info']


            class IetfSaviFcfs_Params(object):
                """
                Parameters specific to SAVI FCFS.
                
                .. attribute:: default_lt
                
                	A default value defined in SAVI FCFS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 30000
                
                .. attribute:: if_attributes
                
                	Interface attributes specific to SAVI SEND
                	**type**\:   :py:class:`IfAttributes <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes>`
                
                .. attribute:: tent_lt
                
                	A default value defined in SAVI FCFS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 50
                
                .. attribute:: twait
                
                	A default value defined in SAVI FCFS
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 25
                
                

                """

                _prefix = 'savi-fcfs'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.default_lt = None
                    self.if_attributes = Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes()
                    self.if_attributes.parent = self
                    self.tent_lt = None
                    self.twait = None


                class IfAttributes(object):
                    """
                    Interface attributes specific to SAVI SEND.
                    
                    .. attribute:: if_attribute
                    
                    	A list of attributes for each interface
                    	**type**\: list of    :py:class:`IfAttribute <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute>`
                    
                    

                    """

                    _prefix = 'savi-fcfs'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.if_attribute = YList()
                        self.if_attribute.parent = self
                        self.if_attribute.name = 'if_attribute'


                    class IfAttribute(object):
                        """
                        A list of attributes for each interface.
                        
                        .. attribute:: ifname  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: trust
                        
                        	SAVI FCFS processing is not performed in the port
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: validating
                        
                        	SAVI FCFS processing is performed in the port
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'savi-fcfs'
                        _revision = '2017-02-15'

                        def __init__(self):
                            self.parent = None
                            self.ifname = None
                            self.trust = None
                            self.validating = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ifname is None:
                                raise YPYModelError('Key property ifname is None')

                            return self.parent._common_path +'/ietf-savi-fcfs:if-attribute[ietf-savi-fcfs:ifname = ' + str(self.ifname) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ifname is not None:
                                return True

                            if self.trust is not None:
                                return True

                            if self.validating is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_savi as meta
                            return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-savi-fcfs:if-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.if_attribute is not None:
                            for child_ref in self.if_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-fcfs:ietf-savi-fcfs_params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.default_lt is not None:
                        return True

                    if self.if_attributes is not None and self.if_attributes._has_data():
                        return True

                    if self.tent_lt is not None:
                        return True

                    if self.twait is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params']['meta_info']


            class IetfSaviSend_Params(object):
                """
                Parameters specific to SAVI SEND.
                
                .. attribute:: default_lt
                
                	A default value defined in SAVI SEND
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 30000
                
                .. attribute:: if_attributes
                
                	Interface attributes specific to SAVI SEND
                	**type**\:   :py:class:`IfAttributes <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes>`
                
                .. attribute:: tent_lt
                
                	A default value defined in SAVI SEND
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 50
                
                

                """

                _prefix = 'savi-send'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.default_lt = None
                    self.if_attributes = Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes()
                    self.if_attributes.parent = self
                    self.tent_lt = None


                class IfAttributes(object):
                    """
                    Interface attributes specific to SAVI SEND.
                    
                    .. attribute:: if_attribute
                    
                    	A list of attributes for each interface
                    	**type**\: list of    :py:class:`IfAttribute <ydk.models.ietf.ietf_savi.Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute>`
                    
                    

                    """

                    _prefix = 'savi-send'
                    _revision = '2017-02-15'

                    def __init__(self):
                        self.parent = None
                        self.if_attribute = YList()
                        self.if_attribute.parent = self
                        self.if_attribute.name = 'if_attribute'


                    class IfAttribute(object):
                        """
                        A list of attributes for each interface.
                        
                        .. attribute:: ifname  <key>
                        
                        	The name of the interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: trust
                        
                        	SAVI SEND processing is not performed in the port
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: validating
                        
                        	SAVI SEND processing is performed in the port
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'savi-send'
                        _revision = '2017-02-15'

                        def __init__(self):
                            self.parent = None
                            self.ifname = None
                            self.trust = None
                            self.validating = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ifname is None:
                                raise YPYModelError('Key property ifname is None')

                            return self.parent._common_path +'/ietf-savi-send:if-attribute[ietf-savi-send:ifname = ' + str(self.ifname) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ifname is not None:
                                return True

                            if self.trust is not None:
                                return True

                            if self.validating is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_savi as meta
                            return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-savi-send:if-attributes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.if_attribute is not None:
                            for child_ref in self.if_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_savi as meta
                        return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-savi-send:ietf-savi-send_params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.default_lt is not None:
                        return True

                    if self.if_attributes is not None and self.if_attributes._has_data():
                        return True

                    if self.tent_lt is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params']['meta_info']

            @property
            def _common_path(self):
                if self.savi_method is None:
                    raise YPYModelError('Key property savi_method is None')

                return '/ietf-savi:savi/ietf-savi:savi-instances/ietf-savi:savi-instance[ietf-savi:savi-method = ' + str(self.savi_method) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.savi_method is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.ietf_savi_dhcpv4_params is not None and self.ietf_savi_dhcpv4_params._has_data():
                    return True

                if self.ietf_savi_dhcpv6_params is not None and self.ietf_savi_dhcpv6_params._has_data():
                    return True

                if self.ietf_savi_fcfs_params is not None and self.ietf_savi_fcfs_params._has_data():
                    return True

                if self.ietf_savi_send_params is not None and self.ietf_savi_send_params._has_data():
                    return True

                if self.preference is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['Savi.SaviInstances.SaviInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi/ietf-savi:savi-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.savi_instance is not None:
                for child_ref in self.savi_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['Savi.SaviInstances']['meta_info']


    class IfFilteringAttributes(object):
        """
        Container for defining filtering attributes of each interface, common for every savi instance.
        
        .. attribute:: if_filtering_attribute
        
        	A list of filtering attributes for each interface
        	**type**\: list of    :py:class:`IfFilteringAttribute <ydk.models.ietf.ietf_savi.Savi.IfFilteringAttributes.IfFilteringAttribute>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.if_filtering_attribute = YList()
            self.if_filtering_attribute.parent = self
            self.if_filtering_attribute.name = 'if_filtering_attribute'


        class IfFilteringAttribute(object):
            """
            A list of filtering attributes for each interface.
            
            .. attribute:: ifname  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            .. attribute:: filtering_enabled
            
            	If the filtering attribute is enabled? 
            	**type**\:  bool
            
            	**default value**\: true
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.ifname = None
                self.filtering_enabled = None

            @property
            def _common_path(self):
                if self.ifname is None:
                    raise YPYModelError('Key property ifname is None')

                return '/ietf-savi:savi/ietf-savi:if-filtering-attributes/ietf-savi:if-filtering-attribute[ietf-savi:ifname = ' + str(self.ifname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ifname is not None:
                    return True

                if self.filtering_enabled is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['Savi.IfFilteringAttributes.IfFilteringAttribute']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi/ietf-savi:if-filtering-attributes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.if_filtering_attribute is not None:
                for child_ref in self.if_filtering_attribute:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['Savi.IfFilteringAttributes']['meta_info']


    class BindingTable(object):
        """
        Container for binding table.
        
        .. attribute:: ipv4
        
        	Container for binding table for IPv4 protocol
        	**type**\:   :py:class:`Ipv4 <ydk.models.ietf.ietf_savi.Savi.BindingTable.Ipv4>`
        
        .. attribute:: ipv6
        
        	Container for binding table for IPv4 protocol
        	**type**\:   :py:class:`Ipv6 <ydk.models.ietf.ietf_savi.Savi.BindingTable.Ipv6>`
        
        

        """

        _prefix = 'savi'
        _revision = '2017-02-15'

        def __init__(self):
            self.parent = None
            self.ipv4 = Savi.BindingTable.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Savi.BindingTable.Ipv6()
            self.ipv6.parent = self


        class Ipv4(object):
            """
            Container for binding table for IPv4 protocol.
            
            .. attribute:: binding_entry
            
            	Definition of a binding entry
            	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_savi.Savi.BindingTable.Ipv4.BindingEntry>`
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.binding_entry = YList()
                self.binding_entry.parent = self
                self.binding_entry.name = 'binding_entry'


            class BindingEntry(object):
                """
                Definition of a binding entry
                
                .. attribute:: address  <key>
                
                	IPv4 address of the binding host
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ifname  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: binding_method
                
                	IP address assignment methods
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: creationtime
                
                	The value of the local clock when the entry was firstly created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: lifetime
                
                	The remaining lifetime of the entry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: mac
                
                	The binding source mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'savi'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.ifname = None
                    self.binding_method = None
                    self.creationtime = None
                    self.lifetime = None
                    self.mac = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.ifname is None:
                        raise YPYModelError('Key property ifname is None')

                    return '/ietf-savi:savi/ietf-savi:binding-table/ietf-savi:ipv4/ietf-savi:binding-entry[ietf-savi:address = ' + str(self.address) + '][ietf-savi:ifname = ' + str(self.ifname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.ifname is not None:
                        return True

                    if self.binding_method is not None:
                        return True

                    if self.creationtime is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.mac is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.BindingTable.Ipv4.BindingEntry']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-savi:savi/ietf-savi:binding-table/ietf-savi:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.binding_entry is not None:
                    for child_ref in self.binding_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['Savi.BindingTable.Ipv4']['meta_info']


        class Ipv6(object):
            """
            Container for binding table for IPv4 protocol.
            
            .. attribute:: binding_entry
            
            	Definition of a binding entry
            	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_savi.Savi.BindingTable.Ipv6.BindingEntry>`
            
            

            """

            _prefix = 'savi'
            _revision = '2017-02-15'

            def __init__(self):
                self.parent = None
                self.binding_entry = YList()
                self.binding_entry.parent = self
                self.binding_entry.name = 'binding_entry'


            class BindingEntry(object):
                """
                Definition of a binding entry
                
                .. attribute:: address  <key>
                
                	IPv6 address of the binding host
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ifname  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: binding_method
                
                	IP address assignment methods
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: creationtime
                
                	The value of the local clock when the entry was firstly created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: lifetime
                
                	The remaining lifetime of the entry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: mac
                
                	The binding source mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'savi'
                _revision = '2017-02-15'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.ifname = None
                    self.binding_method = None
                    self.creationtime = None
                    self.lifetime = None
                    self.mac = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.ifname is None:
                        raise YPYModelError('Key property ifname is None')

                    return '/ietf-savi:savi/ietf-savi:binding-table/ietf-savi:ipv6/ietf-savi:binding-entry[ietf-savi:address = ' + str(self.address) + '][ietf-savi:ifname = ' + str(self.ifname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.ifname is not None:
                        return True

                    if self.binding_method is not None:
                        return True

                    if self.creationtime is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.mac is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_savi as meta
                    return meta._meta_table['Savi.BindingTable.Ipv6.BindingEntry']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-savi:savi/ietf-savi:binding-table/ietf-savi:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.binding_entry is not None:
                    for child_ref in self.binding_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_savi as meta
                return meta._meta_table['Savi.BindingTable.Ipv6']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-savi:savi/ietf-savi:binding-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_savi as meta
            return meta._meta_table['Savi.BindingTable']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-savi:savi'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.binding_table is not None and self.binding_table._has_data():
            return True

        if self.if_filtering_attributes is not None and self.if_filtering_attributes._has_data():
            return True

        if self.savi_instances is not None and self.savi_instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi as meta
        return meta._meta_table['Savi']['meta_info']


