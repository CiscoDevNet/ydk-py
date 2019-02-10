""" tailf_netconf_monitoring 

This module augments ietf\-netconf\-monitoring with extra
monitoring data.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_netconf_monitoring import Transport



class RestHttps(Transport):
    """
    REST over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:rest-https"):
        super(RestHttps, self).__init__(ns, pref, tag)



class CliSsh(Transport):
    """
    CLI over SSH.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:cli-ssh"):
        super(CliSsh, self).__init__(ns, pref, tag)



class CliConsole(Transport):
    """
    CLI on the console.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:cli-console"):
        super(CliConsole, self).__init__(ns, pref, tag)



class WebuiHttps(Transport):
    """
    WebUI over HTTPS.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:webui-https"):
        super(WebuiHttps, self).__init__(ns, pref, tag)



class SnmpUdp(Transport):
    """
    SNMP over UDP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:snmp-udp"):
        super(SnmpUdp, self).__init__(ns, pref, tag)



class WebuiHttp(Transport):
    """
    WebUI over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:webui-http"):
        super(WebuiHttp, self).__init__(ns, pref, tag)



class RestHttp(Transport):
    """
    REST over HTTP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:rest-http"):
        super(RestHttp, self).__init__(ns, pref, tag)



class NetconfTcp(Transport):
    """
    NETCONF over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:netconf-tcp"):
        super(NetconfTcp, self).__init__(ns, pref, tag)



class CliTcp(Transport):
    """
    CLI over TCP.
    
    

    """

    _prefix = 'tncm'
    _revision = '2016-11-24'

    def __init__(self, ns="http://tail-f.com/yang/netconf-monitoring", pref="tailf-netconf-monitoring", tag="tailf-netconf-monitoring:cli-tcp"):
        super(CliTcp, self).__init__(ns, pref, tag)



