""" tailf_netconf_monitoring 

This module augments ietf\-netconf\-monitoring with extra
monitoring data.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CliTcp(Identity):
    """
    CLI over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(CliTcp, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:cli-tcp")


class CliConsole(Identity):
    """
    CLI on the console.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(CliConsole, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:cli-console")


class CliSsh(Identity):
    """
    CLI over SSH.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(CliSsh, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:cli-ssh")


class SnmpUdp(Identity):
    """
    SNMP over UDP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(SnmpUdp, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:snmp-udp")


class RestHttp(Identity):
    """
    REST over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(RestHttp, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:rest-http")


class NetconfTcp(Identity):
    """
    NETCONF over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(NetconfTcp, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:netconf-tcp")


class WebuiHttp(Identity):
    """
    WebUI over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(WebuiHttp, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:webui-http")


class RestHttps(Identity):
    """
    REST over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(RestHttps, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:rest-https")


class WebuiHttps(Identity):
    """
    WebUI over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self):
        super(WebuiHttps, self).__init__("http://tail-f.com/yang/netconf-monitoring", "tailf-netconf-monitoring", "tailf-netconf-monitoring:webui-https")


