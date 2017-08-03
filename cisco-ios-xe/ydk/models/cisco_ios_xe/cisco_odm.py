""" cisco_odm 

Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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


class Bridgedomain(Identity):
    """
    show bridge domain
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Bridgedomain, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BridgeDomain")


class Mplsstaticbinding(Identity):
    """
    show mpls static binding
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Mplsstaticbinding, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSStaticBinding")


class Diffserv(Identity):
    """
    show policy\-map interface
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Diffserv, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:Diffserv")


class Ospf(Identity):
    """
    show ospf
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Ospf, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:OSPF")


class Ethernetcfmstats(Identity):
    """
    show ethernet cfm statistics
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Ethernetcfmstats, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:EthernetCFMStats")


class Mplsldpneighbors(Identity):
    """
    show mpls ldp neighbor detail
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Mplsldpneighbors, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSLDPNeighbors")


class Flowmonitor(Identity):
    """
    show flow monitor
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Flowmonitor, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:FlowMonitor")


class Bfdneighbors(Identity):
    """
    show bfd neighbors
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Bfdneighbors, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BFDNeighbors")


class Virtualservice(Identity):
    """
    show virtual\-service
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Virtualservice, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:VirtualService")


class Mplsforwardingtable(Identity):
    """
    show mpls forwarding\-table
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Mplsforwardingtable, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:MPLSForwardingTable")


class Iproute(Identity):
    """
    show ip route
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Iproute, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:IPRoute")


class Platformsoftware(Identity):
    """
    show platform software
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Platformsoftware, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:PlatformSoftware")


class Bgp(Identity):
    """
    show bgp
    
    

    """

    _prefix = 'codm'
    _revision = '2017-04-25'

    def __init__(self):
        super(Bgp, self).__init__("http://cisco.com/yang/cisco-odm", "cisco-odm", "cisco-odm:BGP")


