""" tailf_netconf_monitoring 

This module augments ietf\-netconf\-monitoring with extra
monitoring data.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_netconf_monitoring import TransportIdentity


class NetconfTcpIdentity(TransportIdentity):
    """
    NETCONF over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['NetconfTcpIdentity']['meta_info']


class RestHttpIdentity(TransportIdentity):
    """
    REST over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['RestHttpIdentity']['meta_info']


class CliSshIdentity(TransportIdentity):
    """
    CLI over SSH.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['CliSshIdentity']['meta_info']


class WebuiHttpIdentity(TransportIdentity):
    """
    WebUI over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['WebuiHttpIdentity']['meta_info']


class CliConsoleIdentity(TransportIdentity):
    """
    CLI on the console.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['CliConsoleIdentity']['meta_info']


class CliTcpIdentity(TransportIdentity):
    """
    CLI over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['CliTcpIdentity']['meta_info']


class RestHttpsIdentity(TransportIdentity):
    """
    REST over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['RestHttpsIdentity']['meta_info']


class SnmpUdpIdentity(TransportIdentity):
    """
    SNMP over UDP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['SnmpUdpIdentity']['meta_info']


class WebuiHttpsIdentity(TransportIdentity):
    """
    WebUI over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2014-11-13'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_netconf_monitoring as meta
        return meta._meta_table['WebuiHttpsIdentity']['meta_info']


