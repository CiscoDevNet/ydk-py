""" ietf_mac 

MAC address forwarding.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BroadcastdomaintypeEnum(Enum):
    """
    BroadcastdomaintypeEnum

    Domain type.

    .. data:: VLAN = 0

    	VLAN Type.

    .. data:: VSI = 1

    	VSI Type.

    .. data:: BD = 2

    	BD Type.

    """

    VLAN = 0

    VSI = 1

    BD = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['BroadcastdomaintypeEnum']


class DirectiontypeEnum(Enum):
    """
    DirectiontypeEnum

    Direction type.

    .. data:: inbound = 0

    	Inbound.

    .. data:: outbound = 1

    	Outbound.

    """

    inbound = 0

    outbound = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['DirectiontypeEnum']


class DiscardtypeEnum(Enum):
    """
    DiscardtypeEnum

    Discard type.

    .. data:: broadcastDiscard = 0

    	Discard broadcast.

    .. data:: unknownMulticastDiscard = 1

    	Discard unknown multicast.

    .. data:: unknownUnicastDiscard = 2

    	Discard Unknown unicast.

    """

    broadcastDiscard = 0

    unknownMulticastDiscard = 1

    unknownUnicastDiscard = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['DiscardtypeEnum']


class LimittypeEnum(Enum):
    """
    LimittypeEnum

    MAC address limit type.

    .. data:: macLimit = 0

    	Interface MAC rule limit.

    .. data:: macApply = 1

    	Interface MAC rule application.

    """

    macLimit = 0

    macApply = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['LimittypeEnum']


class MacagetimetypeEnum(Enum):
    """
    MacagetimetypeEnum

    MAC address age time type.

    .. data:: enable = 0

    	Enable MAC address global aging.

    .. data:: disable = 1

    	Disable MAC address global aging.

    """

    enable = 0

    disable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MacagetimetypeEnum']


class MacenablestatusEnum(Enum):
    """
    MacenablestatusEnum

    MAC enable type.

    .. data:: enable = 0

    	Enable.

    .. data:: disable = 1

    	Disable.

    """

    enable = 0

    disable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MacenablestatusEnum']


class MaclimitforwardEnum(Enum):
    """
    MaclimitforwardEnum

    MAC address limit forward type.

    .. data:: forward = 0

    	Forward.

    .. data:: discard = 1

    	Discard.

    """

    forward = 0

    discard = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MaclimitforwardEnum']


class MacoutiftypeEnum(Enum):
    """
    MacoutiftypeEnum

    MAC out if type.

    .. data:: ac = 0

    	AC.

    .. data:: pw = 1

    	PW.

    """

    ac = 0

    pw = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MacoutiftypeEnum']


class MacpwencaptypeEnum(Enum):
    """
    MacpwencaptypeEnum

    MAC encapsulation type.

    .. data:: ethernet = 0

    	Ethernet.

    .. data:: vlan = 1

    	VLAN.

    """

    ethernet = 0

    vlan = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MacpwencaptypeEnum']


class MactypeEnum(Enum):
    """
    MactypeEnum

    MAC address type.

    .. data:: static = 0

    	Static MAC address entry.

    .. data:: dynamic = 1

    	Dynamic MAC address entry.

    .. data:: blackHole = 2

    	Blackhole MAC address entry

    .. data:: sticky = 3

    	sticky MAC address entry

    """

    static = 0

    dynamic = 1

    blackHole = 2

    sticky = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['MactypeEnum']



class Mac(object):
    """
    MAC address forwarding. 
    
    .. attribute:: bdfdbs
    
    	BD forwarding entries
    	**type**\:   :py:class:`Bdfdbs <ydk.models.ietf.ietf_mac.Mac.Bdfdbs>`
    
    .. attribute:: bdmaclimits
    
    	BD MAC address limit list
    	**type**\:   :py:class:`Bdmaclimits <ydk.models.ietf.ietf_mac.Mac.Bdmaclimits>`
    
    .. attribute:: globalattribute
    
    	MAC global attribute
    	**type**\:   :py:class:`Globalattribute <ydk.models.ietf.ietf_mac.Mac.Globalattribute>`
    
    .. attribute:: ifmaclimits
    
    	Interface MAC address limit list
    	**type**\:   :py:class:`Ifmaclimits <ydk.models.ietf.ietf_mac.Mac.Ifmaclimits>`
    
    .. attribute:: ifvlanmaclimits
    
    	Interface + VLAN MAC address limit list
    	**type**\:   :py:class:`Ifvlanmaclimits <ydk.models.ietf.ietf_mac.Mac.Ifvlanmaclimits>`
    
    .. attribute:: maclimitrules
    
    	Global MAC address learning limit rule
    	**type**\:   :py:class:`Maclimitrules <ydk.models.ietf.ietf_mac.Mac.Maclimitrules>`
    
    .. attribute:: vlanfdbs
    
    	VLAN forwarding table
    	**type**\:   :py:class:`Vlanfdbs <ydk.models.ietf.ietf_mac.Mac.Vlanfdbs>`
    
    .. attribute:: vlanmaclimits
    
    	VLAN MAC address limit list
    	**type**\:   :py:class:`Vlanmaclimits <ydk.models.ietf.ietf_mac.Mac.Vlanmaclimits>`
    
    .. attribute:: vsifdbdynamics
    
    	VSI Forwarding Table on Slot
    	**type**\:   :py:class:`Vsifdbdynamics <ydk.models.ietf.ietf_mac.Mac.Vsifdbdynamics>`
    
    .. attribute:: vsifdbs
    
    	VSI forwarding table
    	**type**\:   :py:class:`Vsifdbs <ydk.models.ietf.ietf_mac.Mac.Vsifdbs>`
    
    .. attribute:: vsimaclimits
    
    	VSI MAC address limit list
    	**type**\:   :py:class:`Vsimaclimits <ydk.models.ietf.ietf_mac.Mac.Vsimaclimits>`
    
    

    """

    _prefix = 'mac'
    _revision = '2016-12-30'

    def __init__(self):
        self.bdfdbs = Mac.Bdfdbs()
        self.bdfdbs.parent = self
        self.bdmaclimits = Mac.Bdmaclimits()
        self.bdmaclimits.parent = self
        self.globalattribute = Mac.Globalattribute()
        self.globalattribute.parent = self
        self.ifmaclimits = Mac.Ifmaclimits()
        self.ifmaclimits.parent = self
        self.ifvlanmaclimits = Mac.Ifvlanmaclimits()
        self.ifvlanmaclimits.parent = self
        self.maclimitrules = Mac.Maclimitrules()
        self.maclimitrules.parent = self
        self.vlanfdbs = Mac.Vlanfdbs()
        self.vlanfdbs.parent = self
        self.vlanmaclimits = Mac.Vlanmaclimits()
        self.vlanmaclimits.parent = self
        self.vsifdbdynamics = Mac.Vsifdbdynamics()
        self.vsifdbdynamics.parent = self
        self.vsifdbs = Mac.Vsifdbs()
        self.vsifdbs.parent = self
        self.vsimaclimits = Mac.Vsimaclimits()
        self.vsimaclimits.parent = self


    class Globalattribute(object):
        """
        MAC global attribute.
        
        .. attribute:: macagetimeenable
        
        	Whether MAC address aging is enabled
        	**type**\:   :py:class:`MacagetimetypeEnum <ydk.models.ietf.ietf_mac.MacagetimetypeEnum>`
        
        	**default value**\: enable
        
        .. attribute:: macagingtime
        
        	Aging time
        	**type**\:  int
        
        	**range:** 60..1000000
        
        	**default value**\: 300
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.macagetimeenable = None
            self.macagingtime = None

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:globalAttribute'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.macagetimeenable is not None:
                return True

            if self.macagingtime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Globalattribute']['meta_info']


    class Vlanfdbs(object):
        """
        VLAN forwarding table.
        
        .. attribute:: vlanfdb
        
        	VLAN forwarding entry
        	**type**\: list of    :py:class:`Vlanfdb <ydk.models.ietf.ietf_mac.Mac.Vlanfdbs.Vlanfdb>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.vlanfdb = YList()
            self.vlanfdb.parent = self
            self.vlanfdb.name = 'vlanfdb'


        class Vlanfdb(object):
            """
            VLAN forwarding entry.
            
            .. attribute:: macaddress  <key>
            
            	MAC address in the format of H\-H\-H
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: slotid  <key>
            
            	Slot ID
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: vlanid  <key>
            
            	VLAN ID
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: cevlanid
            
            	User VLAN ID
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: iscedefault
            
            	CE default VLAN
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: isflood
            
            	Flooding MAC
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: isimac
            
            	Ingress MAC
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: learnedperiod
            
            	Dynamic MAC Holding Time
            	**type**\:  int
            
            	**range:** 0..4294967294
            
            	**default value**\: 0
            
            .. attribute:: mactype
            
            	MAC address type, such as blackhole, static, and dynamic
            	**type**\:   :py:class:`MactypeEnum <ydk.models.ietf.ietf_mac.MactypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: outifname
            
            	Outbound interface name
            	**type**\:  str
            
            .. attribute:: outnickname
            
            	Nickname
            	**type**\:  str
            
            	**length:** 1..31
            
            	**mandatory**\: True
            
            .. attribute:: outpeerips
            
            	Out Peer IPs
            	**type**\:   :py:class:`Outpeerips <ydk.models.ietf.ietf_mac.Mac.Vlanfdbs.Vlanfdb.Outpeerips>`
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.macaddress = None
                self.slotid = None
                self.vlanid = None
                self.cevlanid = None
                self.iscedefault = None
                self.isflood = None
                self.isimac = None
                self.learnedperiod = None
                self.mactype = None
                self.outifname = None
                self.outnickname = None
                self.outpeerips = Mac.Vlanfdbs.Vlanfdb.Outpeerips()
                self.outpeerips.parent = self


            class Outpeerips(object):
                """
                Out Peer IPs.
                
                .. attribute:: outpeerip
                
                	Out Peer IP
                	**type**\: list of    :py:class:`Outpeerip <ydk.models.ietf.ietf_mac.Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip>`
                
                

                """

                _prefix = 'mac'
                _revision = '2016-12-30'

                def __init__(self):
                    self.parent = None
                    self.outpeerip = YList()
                    self.outpeerip.parent = self
                    self.outpeerip.name = 'outpeerip'


                class Outpeerip(object):
                    """
                    Out Peer IP.
                    
                    .. attribute:: outpeerip  <key>
                    
                    	Out Peer IP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'mac'
                    _revision = '2016-12-30'

                    def __init__(self):
                        self.parent = None
                        self.outpeerip = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.outpeerip is None:
                            raise YPYModelError('Key property outpeerip is None')

                        return self.parent._common_path +'/ietf-mac:outPeerIP[ietf-mac:outPeerIP = ' + str(self.outpeerip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.outpeerip is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_mac as meta
                        return meta._meta_table['Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-mac:outPeerIPs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.outpeerip is not None:
                        for child_ref in self.outpeerip:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_mac as meta
                    return meta._meta_table['Mac.Vlanfdbs.Vlanfdb.Outpeerips']['meta_info']

            @property
            def _common_path(self):
                if self.macaddress is None:
                    raise YPYModelError('Key property macaddress is None')
                if self.slotid is None:
                    raise YPYModelError('Key property slotid is None')
                if self.vlanid is None:
                    raise YPYModelError('Key property vlanid is None')

                return '/ietf-mac:mac/ietf-mac:vlanFdbs/ietf-mac:vlanFdb[ietf-mac:macAddress = ' + str(self.macaddress) + '][ietf-mac:slotId = ' + str(self.slotid) + '][ietf-mac:vlanId = ' + str(self.vlanid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.macaddress is not None:
                    return True

                if self.slotid is not None:
                    return True

                if self.vlanid is not None:
                    return True

                if self.cevlanid is not None:
                    return True

                if self.iscedefault is not None:
                    return True

                if self.isflood is not None:
                    return True

                if self.isimac is not None:
                    return True

                if self.learnedperiod is not None:
                    return True

                if self.mactype is not None:
                    return True

                if self.outifname is not None:
                    return True

                if self.outnickname is not None:
                    return True

                if self.outpeerips is not None and self.outpeerips._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Vlanfdbs.Vlanfdb']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:vlanFdbs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vlanfdb is not None:
                for child_ref in self.vlanfdb:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Vlanfdbs']['meta_info']


    class Vsifdbs(object):
        """
        VSI forwarding table.
        
        .. attribute:: vsifdb
        
        	VSI Forwarding entry
        	**type**\: list of    :py:class:`Vsifdb <ydk.models.ietf.ietf_mac.Mac.Vsifdbs.Vsifdb>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.vsifdb = YList()
            self.vsifdb.parent = self
            self.vsifdb.name = 'vsifdb'


        class Vsifdb(object):
            """
            VSI Forwarding entry.
            
            .. attribute:: macaddress  <key>
            
            	MAC address in the format of H\-H\-H
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: slotid  <key>
            
            	Slot ID
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: vlanid  <key>
            
            	VLAN ID
            	**type**\:  int
            
            	**range:** 0..4094
            
            .. attribute:: vsiname  <key>
            
            	VSI Name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: cevid
            
            	Inner VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: isimac
            
            	Ingress MAC
            	**type**\:  bool
            
            	**mandatory**\: True
            
            .. attribute:: learnedperiod
            
            	Dynamic MAC Holding Time
            	**type**\:  int
            
            	**range:** 0..4294967294
            
            	**default value**\: 0
            
            .. attribute:: mactype
            
            	MAC Type of an interface
            	**type**\:   :py:class:`MactypeEnum <ydk.models.ietf.ietf_mac.MactypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: outifname
            
            	Outbound interface name
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: outiftype
            
            	Outbound interface type
            	**type**\:   :py:class:`MacoutiftypeEnum <ydk.models.ietf.ietf_mac.MacoutiftypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: peerip
            
            	Peer IP address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: pevid
            
            	Outer VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: pwencap
            
            	PW encapsulation type
            	**type**\:   :py:class:`MacpwencaptypeEnum <ydk.models.ietf.ietf_mac.MacpwencaptypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: pwid
            
            	PW ID
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: pwname
            
            	PW Name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: vlanifname
            
            	VLANIF interface
            	**type**\:  str
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.macaddress = None
                self.slotid = None
                self.vlanid = None
                self.vsiname = None
                self.cevid = None
                self.isimac = None
                self.learnedperiod = None
                self.mactype = None
                self.outifname = None
                self.outiftype = None
                self.peerip = None
                self.pevid = None
                self.pwencap = None
                self.pwid = None
                self.pwname = None
                self.vlanifname = None

            @property
            def _common_path(self):
                if self.macaddress is None:
                    raise YPYModelError('Key property macaddress is None')
                if self.slotid is None:
                    raise YPYModelError('Key property slotid is None')
                if self.vlanid is None:
                    raise YPYModelError('Key property vlanid is None')
                if self.vsiname is None:
                    raise YPYModelError('Key property vsiname is None')

                return '/ietf-mac:mac/ietf-mac:vsiFdbs/ietf-mac:vsiFdb[ietf-mac:macAddress = ' + str(self.macaddress) + '][ietf-mac:slotId = ' + str(self.slotid) + '][ietf-mac:vlanid = ' + str(self.vlanid) + '][ietf-mac:vsiName = ' + str(self.vsiname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.macaddress is not None:
                    return True

                if self.slotid is not None:
                    return True

                if self.vlanid is not None:
                    return True

                if self.vsiname is not None:
                    return True

                if self.cevid is not None:
                    return True

                if self.isimac is not None:
                    return True

                if self.learnedperiod is not None:
                    return True

                if self.mactype is not None:
                    return True

                if self.outifname is not None:
                    return True

                if self.outiftype is not None:
                    return True

                if self.peerip is not None:
                    return True

                if self.pevid is not None:
                    return True

                if self.pwencap is not None:
                    return True

                if self.pwid is not None:
                    return True

                if self.pwname is not None:
                    return True

                if self.vlanifname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Vsifdbs.Vsifdb']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:vsiFdbs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vsifdb is not None:
                for child_ref in self.vsifdb:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Vsifdbs']['meta_info']


    class Vsifdbdynamics(object):
        """
        VSI Forwarding Table on Slot.
        
        .. attribute:: vsifdbdynamic
        
        	VSI Forwarding Table on Slot
        	**type**\: list of    :py:class:`Vsifdbdynamic <ydk.models.ietf.ietf_mac.Mac.Vsifdbdynamics.Vsifdbdynamic>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.vsifdbdynamic = YList()
            self.vsifdbdynamic.parent = self
            self.vsifdbdynamic.name = 'vsifdbdynamic'


        class Vsifdbdynamic(object):
            """
            VSI Forwarding Table on Slot.
            
            .. attribute:: macaddress  <key>
            
            	MAC address in the format of H\-H\-H
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: outifname  <key>
            
            	Outbound interface name
            	**type**\:  str
            
            .. attribute:: slotid  <key>
            
            	Slot ID
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: vlanid  <key>
            
            	VLAN ID
            	**type**\:  int
            
            	**range:** 0..4094
            
            .. attribute:: vsiname  <key>
            
            	VSI Name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: cevid
            
            	Inner VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: isimac
            
            	Ingress MAC
            	**type**\:  bool
            
            	**mandatory**\: True
            
            .. attribute:: mactype
            
            	MAC Type of an interface
            	**type**\:   :py:class:`MactypeEnum <ydk.models.ietf.ietf_mac.MactypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: outiftype
            
            	Outbound interface type
            	**type**\:   :py:class:`MacoutiftypeEnum <ydk.models.ietf.ietf_mac.MacoutiftypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: peerip
            
            	Peer IP address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: pevid
            
            	Outer VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: pwencap
            
            	PW encapsulation type
            	**type**\:   :py:class:`MacpwencaptypeEnum <ydk.models.ietf.ietf_mac.MacpwencaptypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: pwid
            
            	PW ID
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: pwname
            
            	PW Name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: vlanifname
            
            	VLANIF interface
            	**type**\:  str
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.macaddress = None
                self.outifname = None
                self.slotid = None
                self.vlanid = None
                self.vsiname = None
                self.cevid = None
                self.isimac = None
                self.mactype = None
                self.outiftype = None
                self.peerip = None
                self.pevid = None
                self.pwencap = None
                self.pwid = None
                self.pwname = None
                self.vlanifname = None

            @property
            def _common_path(self):
                if self.macaddress is None:
                    raise YPYModelError('Key property macaddress is None')
                if self.outifname is None:
                    raise YPYModelError('Key property outifname is None')
                if self.slotid is None:
                    raise YPYModelError('Key property slotid is None')
                if self.vlanid is None:
                    raise YPYModelError('Key property vlanid is None')
                if self.vsiname is None:
                    raise YPYModelError('Key property vsiname is None')

                return '/ietf-mac:mac/ietf-mac:vsiFdbDynamics/ietf-mac:vsiFdbDynamic[ietf-mac:macAddress = ' + str(self.macaddress) + '][ietf-mac:outIfName = ' + str(self.outifname) + '][ietf-mac:slotId = ' + str(self.slotid) + '][ietf-mac:vlanid = ' + str(self.vlanid) + '][ietf-mac:vsiName = ' + str(self.vsiname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.macaddress is not None:
                    return True

                if self.outifname is not None:
                    return True

                if self.slotid is not None:
                    return True

                if self.vlanid is not None:
                    return True

                if self.vsiname is not None:
                    return True

                if self.cevid is not None:
                    return True

                if self.isimac is not None:
                    return True

                if self.mactype is not None:
                    return True

                if self.outiftype is not None:
                    return True

                if self.peerip is not None:
                    return True

                if self.pevid is not None:
                    return True

                if self.pwencap is not None:
                    return True

                if self.pwid is not None:
                    return True

                if self.pwname is not None:
                    return True

                if self.vlanifname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Vsifdbdynamics.Vsifdbdynamic']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:vsiFdbDynamics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vsifdbdynamic is not None:
                for child_ref in self.vsifdbdynamic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Vsifdbdynamics']['meta_info']


    class Bdfdbs(object):
        """
        BD forwarding entries.
        
        .. attribute:: bdfdb
        
        	BD forwarding entry
        	**type**\: list of    :py:class:`Bdfdb <ydk.models.ietf.ietf_mac.Mac.Bdfdbs.Bdfdb>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.bdfdb = YList()
            self.bdfdb.parent = self
            self.bdfdb.name = 'bdfdb'


        class Bdfdb(object):
            """
            BD forwarding entry.
            
            .. attribute:: bdid  <key>
            
            	ID of a bridge domain
            	**type**\:  int
            
            	**range:** 1..16777215
            
            .. attribute:: macaddress  <key>
            
            	MAC address of a bridge domain
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: slotid  <key>
            
            	Slot number
            	**type**\:  str
            
            	**length:** 1..50
            
            .. attribute:: cedefault
            
            	CE default VLAN
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: cevid
            
            	Inner VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: learnedperiod
            
            	Dynamic MAC Holding Time
            	**type**\:  int
            
            	**range:** 0..4294967294
            
            	**default value**\: 0
            
            .. attribute:: mactype
            
            	MAC address type of a bridge domain
            	**type**\:   :py:class:`MactypeEnum <ydk.models.ietf.ietf_mac.MactypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: outifname
            
            	Outbound interface name
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: pedefault
            
            	PE default VLAN
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: untag
            
            	Packets without VLAN tags
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: vid
            
            	Outer VLAN tag
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.bdid = None
                self.macaddress = None
                self.slotid = None
                self.cedefault = None
                self.cevid = None
                self.learnedperiod = None
                self.mactype = None
                self.outifname = None
                self.pedefault = None
                self.untag = None
                self.vid = None

            @property
            def _common_path(self):
                if self.bdid is None:
                    raise YPYModelError('Key property bdid is None')
                if self.macaddress is None:
                    raise YPYModelError('Key property macaddress is None')
                if self.slotid is None:
                    raise YPYModelError('Key property slotid is None')

                return '/ietf-mac:mac/ietf-mac:bdFdbs/ietf-mac:bdFdb[ietf-mac:bdId = ' + str(self.bdid) + '][ietf-mac:macAddress = ' + str(self.macaddress) + '][ietf-mac:slotId = ' + str(self.slotid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bdid is not None:
                    return True

                if self.macaddress is not None:
                    return True

                if self.slotid is not None:
                    return True

                if self.cedefault is not None:
                    return True

                if self.cevid is not None:
                    return True

                if self.learnedperiod is not None:
                    return True

                if self.mactype is not None:
                    return True

                if self.outifname is not None:
                    return True

                if self.pedefault is not None:
                    return True

                if self.untag is not None:
                    return True

                if self.vid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Bdfdbs.Bdfdb']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:bdFdbs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bdfdb is not None:
                for child_ref in self.bdfdb:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Bdfdbs']['meta_info']


    class Maclimitrules(object):
        """
        Global MAC address learning limit rule.
        
        .. attribute:: maclimitrule
        
        	Global MAC address learning limit
        	**type**\: list of    :py:class:`Maclimitrule <ydk.models.ietf.ietf_mac.Mac.Maclimitrules.Maclimitrule>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.maclimitrule = YList()
            self.maclimitrule.parent = self
            self.maclimitrule.name = 'maclimitrule'


        class Maclimitrule(object):
            """
            Global MAC address learning limit.
            
            .. attribute:: rulename  <key>
            
            	Global MAC address learning limit rule name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: action
            
            	Discard or forward after the number of learned MAC  addresses reaches the maximum number
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of  learned MAC addresses reaches the maximum number
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: enable
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned
            	**type**\:  int
            
            	**range:** 0..131072
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval at which MAC addresses are learned
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**default value**\: 0
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.rulename = None
                self.action = None
                self.alarm = None
                self.maximum = None
                self.rate = None

            @property
            def _common_path(self):
                if self.rulename is None:
                    raise YPYModelError('Key property rulename is None')

                return '/ietf-mac:mac/ietf-mac:macLimitRules/ietf-mac:macLimitRule[ietf-mac:ruleName = ' + str(self.rulename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.rulename is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Maclimitrules.Maclimitrule']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:macLimitRules'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.maclimitrule is not None:
                for child_ref in self.maclimitrule:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Maclimitrules']['meta_info']


    class Vlanmaclimits(object):
        """
        VLAN MAC address limit list.
        
        .. attribute:: vlanmaclimit
        
        	VLAN MAC address limit
        	**type**\: list of    :py:class:`Vlanmaclimit <ydk.models.ietf.ietf_mac.Mac.Vlanmaclimits.Vlanmaclimit>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.vlanmaclimit = YList()
            self.vlanmaclimit.parent = self
            self.vlanmaclimit.name = 'vlanmaclimit'


        class Vlanmaclimit(object):
            """
            VLAN MAC address limit.
            
            .. attribute:: vlanid  <key>
            
            	VLAN ID
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: action
            
            	Discard or forward after the number of learned MAC  addresses reaches the maximum number in a VLAN
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of learned  MAC addresses reaches the maximum number in a VLAN
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: enable
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned  in a VLAN
            	**type**\:  int
            
            	**range:** 0..130048
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval at which MAC addresses are learned in a VLAN
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**default value**\: 0
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.vlanid = None
                self.action = None
                self.alarm = None
                self.maximum = None
                self.rate = None

            @property
            def _common_path(self):
                if self.vlanid is None:
                    raise YPYModelError('Key property vlanid is None')

                return '/ietf-mac:mac/ietf-mac:vlanMacLimits/ietf-mac:vlanMacLimit[ietf-mac:vlanId = ' + str(self.vlanid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vlanid is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Vlanmaclimits.Vlanmaclimit']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:vlanMacLimits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vlanmaclimit is not None:
                for child_ref in self.vlanmaclimit:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Vlanmaclimits']['meta_info']


    class Vsimaclimits(object):
        """
        VSI MAC address limit list.
        
        .. attribute:: vsimaclimit
        
        	VSI MAC address limit
        	**type**\: list of    :py:class:`Vsimaclimit <ydk.models.ietf.ietf_mac.Mac.Vsimaclimits.Vsimaclimit>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.vsimaclimit = YList()
            self.vsimaclimit.parent = self
            self.vsimaclimit.name = 'vsimaclimit'


        class Vsimaclimit(object):
            """
            VSI MAC address limit.
            
            .. attribute:: vsiname  <key>
            
            	VSI name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: action
            
            	Discard or forward after the number of learned MAC  addresses reaches the maximum number in a VSI
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of learned  MAC addresses reaches the maximum number in a VSI
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: disable
            
            .. attribute:: downthreshold
            
            	Upper limit for the number of MAC addresses
            	**type**\:  int
            
            	**range:** 60..100
            
            	**mandatory**\: True
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned in a  VSI
            	**type**\:  int
            
            	**range:** 0..524288
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval at which MAC addresses are learned in a VSI
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**default value**\: 0
            
            .. attribute:: upthreshold
            
            	Upper limit for the number of MAC addresses
            	**type**\:  int
            
            	**range:** 80..100
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.vsiname = None
                self.action = None
                self.alarm = None
                self.downthreshold = None
                self.maximum = None
                self.rate = None
                self.upthreshold = None

            @property
            def _common_path(self):
                if self.vsiname is None:
                    raise YPYModelError('Key property vsiname is None')

                return '/ietf-mac:mac/ietf-mac:vsiMacLimits/ietf-mac:vsiMacLimit[ietf-mac:vsiName = ' + str(self.vsiname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vsiname is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.downthreshold is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                if self.upthreshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Vsimaclimits.Vsimaclimit']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:vsiMacLimits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vsimaclimit is not None:
                for child_ref in self.vsimaclimit:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Vsimaclimits']['meta_info']


    class Bdmaclimits(object):
        """
        BD MAC address limit list.
        
        .. attribute:: bdmaclimit
        
        	BD MAC address limit
        	**type**\: list of    :py:class:`Bdmaclimit <ydk.models.ietf.ietf_mac.Mac.Bdmaclimits.Bdmaclimit>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.bdmaclimit = YList()
            self.bdmaclimit.parent = self
            self.bdmaclimit.name = 'bdmaclimit'


        class Bdmaclimit(object):
            """
            BD MAC address limit.
            
            .. attribute:: bdid  <key>
            
            	Specifies the ID of a bridge domain
            	**type**\:  int
            
            	**range:** 1..16777215
            
            .. attribute:: action
            
            	Forward or discard the packet
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of learned  MAC addresses reaches the maximum number
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: enable
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned in a  BD
            	**type**\:  int
            
            	**range:** 0..130048
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval at which MAC addresses are learned in a BD
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**default value**\: 0
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.bdid = None
                self.action = None
                self.alarm = None
                self.maximum = None
                self.rate = None

            @property
            def _common_path(self):
                if self.bdid is None:
                    raise YPYModelError('Key property bdid is None')

                return '/ietf-mac:mac/ietf-mac:bdMacLimits/ietf-mac:bdMacLimit[ietf-mac:bdId = ' + str(self.bdid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bdid is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Bdmaclimits.Bdmaclimit']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:bdMacLimits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bdmaclimit is not None:
                for child_ref in self.bdmaclimit:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Bdmaclimits']['meta_info']


    class Ifmaclimits(object):
        """
        Interface MAC address limit list.
        
        .. attribute:: ifmaclimit
        
        	Interface MAC address limit
        	**type**\: list of    :py:class:`Ifmaclimit <ydk.models.ietf.ietf_mac.Mac.Ifmaclimits.Ifmaclimit>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.ifmaclimit = YList()
            self.ifmaclimit.parent = self
            self.ifmaclimit.name = 'ifmaclimit'


        class Ifmaclimit(object):
            """
            Interface MAC address limit.
            
            .. attribute:: ifname  <key>
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: limittype  <key>
            
            	Interface MAC limit type
            	**type**\:   :py:class:`LimittypeEnum <ydk.models.ietf.ietf_mac.LimittypeEnum>`
            
            .. attribute:: action
            
            	Discard or forward after the number of learned MAC  addresses reaches the maximum number on an interface
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of learned  MAC addresses reaches the maximum number on an interface
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: enable
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned  on an interface
            	**type**\:  int
            
            	**range:** 0..131072
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval (ms) at which MAC addresses are learned on  an interface
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**default value**\: 0
            
            .. attribute:: rulename
            
            	Rule name
            	**type**\:  str
            
            	**length:** 1..31
            
            	**refers to**\:  :py:class:`rulename <ydk.models.ietf.ietf_mac.Mac.Maclimitrules.Maclimitrule>`
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.ifname = None
                self.limittype = None
                self.action = None
                self.alarm = None
                self.maximum = None
                self.rate = None
                self.rulename = None

            @property
            def _common_path(self):
                if self.ifname is None:
                    raise YPYModelError('Key property ifname is None')
                if self.limittype is None:
                    raise YPYModelError('Key property limittype is None')

                return '/ietf-mac:mac/ietf-mac:ifMacLimits/ietf-mac:ifMacLimit[ietf-mac:ifName = ' + str(self.ifname) + '][ietf-mac:limitType = ' + str(self.limittype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ifname is not None:
                    return True

                if self.limittype is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                if self.rulename is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Ifmaclimits.Ifmaclimit']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:ifMacLimits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ifmaclimit is not None:
                for child_ref in self.ifmaclimit:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Ifmaclimits']['meta_info']


    class Ifvlanmaclimits(object):
        """
        Interface + VLAN MAC address limit list.
        
        .. attribute:: ifvlanmaclimit
        
        	Interface + VLAN MAC address limit
        	**type**\: list of    :py:class:`Ifvlanmaclimit <ydk.models.ietf.ietf_mac.Mac.Ifvlanmaclimits.Ifvlanmaclimit>`
        
        

        """

        _prefix = 'mac'
        _revision = '2016-12-30'

        def __init__(self):
            self.parent = None
            self.ifvlanmaclimit = YList()
            self.ifvlanmaclimit.parent = self
            self.ifvlanmaclimit.name = 'ifvlanmaclimit'


        class Ifvlanmaclimit(object):
            """
            Interface + VLAN MAC address limit.
            
            .. attribute:: ifname  <key>
            
            	Name of an interface. 
            	**type**\:  str
            
            .. attribute:: limittype  <key>
            
            	Interface MAC limit type
            	**type**\:   :py:class:`LimittypeEnum <ydk.models.ietf.ietf_mac.LimittypeEnum>`
            
            .. attribute:: vlanbegin  <key>
            
            	Start VLAN ID
            	**type**\:  int
            
            	**range:** 1..4094
            
            .. attribute:: action
            
            	Discard or forward the packet
            	**type**\:   :py:class:`MaclimitforwardEnum <ydk.models.ietf.ietf_mac.MaclimitforwardEnum>`
            
            	**default value**\: discard
            
            .. attribute:: alarm
            
            	Whether an alarm is generated after the number of learned  MAC addresses reaches the maximum number
            	**type**\:   :py:class:`MacenablestatusEnum <ydk.models.ietf.ietf_mac.MacenablestatusEnum>`
            
            	**default value**\: enable
            
            .. attribute:: maximum
            
            	Maximum number of MAC addresses that can be learned on an interface
            	**type**\:  int
            
            	**range:** 0..131072
            
            	**mandatory**\: True
            
            .. attribute:: rate
            
            	Interval (ms) at which MAC addresses are learned on  an interface
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**mandatory**\: True
            
            .. attribute:: rulename
            
            	Rule name
            	**type**\:  str
            
            	**length:** 1..31
            
            	**refers to**\:  :py:class:`rulename <ydk.models.ietf.ietf_mac.Mac.Maclimitrules.Maclimitrule>`
            
            .. attribute:: vlanend
            
            	End VLAN ID
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'mac'
            _revision = '2016-12-30'

            def __init__(self):
                self.parent = None
                self.ifname = None
                self.limittype = None
                self.vlanbegin = None
                self.action = None
                self.alarm = None
                self.maximum = None
                self.rate = None
                self.rulename = None
                self.vlanend = None

            @property
            def _common_path(self):
                if self.ifname is None:
                    raise YPYModelError('Key property ifname is None')
                if self.limittype is None:
                    raise YPYModelError('Key property limittype is None')
                if self.vlanbegin is None:
                    raise YPYModelError('Key property vlanbegin is None')

                return '/ietf-mac:mac/ietf-mac:ifVlanMacLimits/ietf-mac:ifVlanMacLimit[ietf-mac:ifName = ' + str(self.ifname) + '][ietf-mac:limitType = ' + str(self.limittype) + '][ietf-mac:vlanBegin = ' + str(self.vlanbegin) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ifname is not None:
                    return True

                if self.limittype is not None:
                    return True

                if self.vlanbegin is not None:
                    return True

                if self.action is not None:
                    return True

                if self.alarm is not None:
                    return True

                if self.maximum is not None:
                    return True

                if self.rate is not None:
                    return True

                if self.rulename is not None:
                    return True

                if self.vlanend is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_mac as meta
                return meta._meta_table['Mac.Ifvlanmaclimits.Ifvlanmaclimit']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-mac:mac/ietf-mac:ifVlanMacLimits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.ifvlanmaclimit is not None:
                for child_ref in self.ifvlanmaclimit:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_mac as meta
            return meta._meta_table['Mac.Ifvlanmaclimits']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-mac:mac'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.bdfdbs is not None and self.bdfdbs._has_data():
            return True

        if self.bdmaclimits is not None and self.bdmaclimits._has_data():
            return True

        if self.globalattribute is not None and self.globalattribute._has_data():
            return True

        if self.ifmaclimits is not None and self.ifmaclimits._has_data():
            return True

        if self.ifvlanmaclimits is not None and self.ifvlanmaclimits._has_data():
            return True

        if self.maclimitrules is not None and self.maclimitrules._has_data():
            return True

        if self.vlanfdbs is not None and self.vlanfdbs._has_data():
            return True

        if self.vlanmaclimits is not None and self.vlanmaclimits._has_data():
            return True

        if self.vsifdbdynamics is not None and self.vsifdbdynamics._has_data():
            return True

        if self.vsifdbs is not None and self.vsifdbs._has_data():
            return True

        if self.vsimaclimits is not None and self.vsimaclimits._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_mac as meta
        return meta._meta_table['Mac']['meta_info']


