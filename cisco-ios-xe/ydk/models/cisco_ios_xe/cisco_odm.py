""" cisco_odm 

Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Parsername(Identity):
    """
     ODM parser names
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Parsername, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:parsername")


class BGP(Identity):
    """
    show bgp
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(BGP, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BGP")


class IPRoute(Identity):
    """
    show ip route
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(IPRoute, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:IPRoute")


class FlowMonitor(Identity):
    """
    show flow monitor
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(FlowMonitor, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:FlowMonitor")


class BFDNeighbors(Identity):
    """
    show bfd neighbors
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(BFDNeighbors, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BFDNeighbors")


class BridgeDomain(Identity):
    """
    show bridge domain
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(BridgeDomain, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BridgeDomain")


class Diffserv(Identity):
    """
    show policy\-map interface
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Diffserv, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:Diffserv")


class VirtualService(Identity):
    """
    show virtual\-service
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(VirtualService, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:VirtualService")


class MPLSLDPNeighbors(Identity):
    """
    show mpls ldp neighbor detail
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(MPLSLDPNeighbors, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSLDPNeighbors")


class PlatformSoftware(Identity):
    """
    show platform software
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(PlatformSoftware, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:PlatformSoftware")


class MPLSStaticBinding(Identity):
    """
    show mpls static binding
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(MPLSStaticBinding, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSStaticBinding")


class MPLSForwardingTable(Identity):
    """
    show mpls forwarding\-table
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(MPLSForwardingTable, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSForwardingTable")


class OSPF(Identity):
    """
    show ospf
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(OSPF, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:OSPF")


class EthernetCFMStats(Identity):
    """
    show ethernet cfm statistics
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(EthernetCFMStats, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:EthernetCFMStats")


