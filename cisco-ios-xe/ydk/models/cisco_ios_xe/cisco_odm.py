""" cisco_odm 

Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ParsernameIdentity(object):
    """
     ODM parser names
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['ParsernameIdentity']['meta_info']


class BridgedomainIdentity(ParsernameIdentity):
    """
    show bridge domain
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['BridgedomainIdentity']['meta_info']


class MplsforwardingtableIdentity(ParsernameIdentity):
    """
    show mpls forwarding\-table
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['MplsforwardingtableIdentity']['meta_info']


class MplsstaticbindingIdentity(ParsernameIdentity):
    """
    show mpls static binding
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['MplsstaticbindingIdentity']['meta_info']


class IprouteIdentity(ParsernameIdentity):
    """
    show ip route
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['IprouteIdentity']['meta_info']


class BgpIdentity(ParsernameIdentity):
    """
    show bgp
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['BgpIdentity']['meta_info']


class BfdneighborsIdentity(ParsernameIdentity):
    """
    show bfd neighbors
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['BfdneighborsIdentity']['meta_info']


class VirtualserviceIdentity(ParsernameIdentity):
    """
    show virtual\-service
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['VirtualserviceIdentity']['meta_info']


class MplsldpneighborsIdentity(ParsernameIdentity):
    """
    show mpls ldp neighbor detail
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['MplsldpneighborsIdentity']['meta_info']


class FlowmonitorIdentity(ParsernameIdentity):
    """
    show flow monitor
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['FlowmonitorIdentity']['meta_info']


class PlatformsoftwareIdentity(ParsernameIdentity):
    """
    show platform software
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['PlatformsoftwareIdentity']['meta_info']


class OspfIdentity(ParsernameIdentity):
    """
    show ospf
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['OspfIdentity']['meta_info']


class DiffservIdentity(ParsernameIdentity):
    """
    show policy\-map interface
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['DiffservIdentity']['meta_info']


class EthernetcfmstatsIdentity(ParsernameIdentity):
    """
    show ethernet cfm statistics
    
    

    """

    _prefix = 'codm'
    _revision = '2017-01-25'

    def __init__(self):
        ParsernameIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_odm as meta
        return meta._meta_table['EthernetcfmstatsIdentity']['meta_info']


