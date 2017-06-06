""" CISCO_RADIUS_EXT_MIB 

This MIB module defines objects describing RADIUS (Remote
Access Dialin User Service), serving as an extension of the
following MIB modules\: 
\- 
    \- RADIUS\-AUTH\-CLIENT\-MIB [RFC4668] 
    \- RADIUS\-AUTH\-SERVER\-MIB [RFC4669] 
    \- RADIUS\-ACC\-CLIENT\-MIB [RFC4670] 
    \- RADIUS\-ACC\-SERVER\-MIB [RFC4671] 
    \- RADIUS\-DYNAUTH\-CLIENT\-MIB [RFC4672] 
    \- RADIUS\-DYNAUTH\-SERVER\-MIB [RFC4673] 
\- 
[RFC4668] D. Nelson, RADIUS Authentication Client MIB for IPv6,

RFC\-4668, August 2006. 
\- 
[RFC4669] D. Nelson, RADIUS Authentication Server MIB for IPv6,

RFC\-4669, August 2006. 
\- 
[RFC4670] D. Nelson, RADIUS Accounting Client MIB for IPv6,
RFC\-4670, August 2006. 
\- 
[RFC4671] D. Nelson, RADIUS Accounting Server MIB for IPv6,
RFC\-4671, August 2006. 
\- 
[RFC4672] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic 
Authorization Client MIB, RFC\-4672, September 2006. 
\- 
[RFC4673] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic 
Authorization Server MIB, RFC\-4673, September 2006.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoRadiusExtMib(object):
    """
    
    
    .. attribute:: creclientaccounting
    
    	
    	**type**\:   :py:class:`Creclientaccounting <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientaccounting>`
    
    .. attribute:: creclientauthentication
    
    	
    	**type**\:   :py:class:`Creclientauthentication <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientauthentication>`
    
    .. attribute:: creclientglobal
    
    	
    	**type**\:   :py:class:`Creclientglobal <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientglobal>`
    
    

    """

    _prefix = 'CISCO-RADIUS-EXT-MIB'
    _revision = '2010-05-25'

    def __init__(self):
        self.creclientaccounting = CiscoRadiusExtMib.Creclientaccounting()
        self.creclientaccounting.parent = self
        self.creclientauthentication = CiscoRadiusExtMib.Creclientauthentication()
        self.creclientauthentication.parent = self
        self.creclientglobal = CiscoRadiusExtMib.Creclientglobal()
        self.creclientglobal.parent = self


    class Creclientglobal(object):
        """
        
        
        .. attribute:: creclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS packet when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication or an accounting packet is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creclientlastusedsourceport
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the last source port that was used to send out a RADIUS authentication or accounting request
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclientsourceportrangeend
        
        	If the 'extended RADIUS source port' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value where this range ends
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclientsourceportrangestart
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value from where this range starts
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclienttotalaccessrejects
        
        	This object indicates the number of access reject packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalaverageresponsedelay
        
        	This object indicates the overall response delay experienced by RADIUS packets (both authentication and accounting)
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creclienttotalmaxdoneqlength
        
        	This object indicates the maximum length of the queue which stores those RADIUS packets for which the responses are received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxinqlength
        
        	This object indicates the maximum length of the queue which stores the incoming RADIUS packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxwaitqlength
        
        	This object indicates the maximum length of the queue which stores the pending RADIUS packets for which the responses are outstanding
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            self.parent = None
            self.creclientlastusedsourceid = None
            self.creclientlastusedsourceport = None
            self.creclientsourceportrangeend = None
            self.creclientsourceportrangestart = None
            self.creclienttotalaccessrejects = None
            self.creclienttotalaverageresponsedelay = None
            self.creclienttotalmaxdoneqlength = None
            self.creclienttotalmaxinqlength = None
            self.creclienttotalmaxwaitqlength = None

        @property
        def _common_path(self):

            return '/CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/CISCO-RADIUS-EXT-MIB:creClientGlobal'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.creclientlastusedsourceid is not None:
                return True

            if self.creclientlastusedsourceport is not None:
                return True

            if self.creclientsourceportrangeend is not None:
                return True

            if self.creclientsourceportrangestart is not None:
                return True

            if self.creclienttotalaccessrejects is not None:
                return True

            if self.creclienttotalaverageresponsedelay is not None:
                return True

            if self.creclienttotalmaxdoneqlength is not None:
                return True

            if self.creclienttotalmaxinqlength is not None:
                return True

            if self.creclienttotalmaxwaitqlength is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RADIUS_EXT_MIB as meta
            return meta._meta_table['CiscoRadiusExtMib.Creclientglobal']['meta_info']


    class Creclientauthentication(object):
        """
        
        
        .. attribute:: creauthclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS authentication requests
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creauthclientbadauthenticators
        
        	This object indicates the number of RADIUS authentication response packets received which contained invalid authenticators
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered during RADIUS request formation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: buffer failures
        
        .. attribute:: creauthclientdupids
        
        	This object indicates the number of times client has received duplicate authentication responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS authentication request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication request is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creauthclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS authentication responses received.  Malformed packets include packets with an invalid length
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS authentication packet
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: bytes
        
        .. attribute:: creauthclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS authentication requests
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creauthclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS authentication.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: timeouts
        
        .. attribute:: creauthclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS authentication packets that never received a response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS authentication packets that received responses
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalresponses
        
        	This object indicates the number of RADIUS authentication response packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientunknownresponses
        
        	This object indicates the number of unknown RADIUS authentication responses received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            self.parent = None
            self.creauthclientaverageresponsedelay = None
            self.creauthclientbadauthenticators = None
            self.creauthclientbufferallocfailures = None
            self.creauthclientdupids = None
            self.creauthclientlastusedsourceid = None
            self.creauthclientmalformedresponses = None
            self.creauthclientmaxbuffersize = None
            self.creauthclientmaxresponsedelay = None
            self.creauthclienttimeouts = None
            self.creauthclienttotalpacketswithoutresponses = None
            self.creauthclienttotalpacketswithresponses = None
            self.creauthclienttotalresponses = None
            self.creauthclientunknownresponses = None

        @property
        def _common_path(self):

            return '/CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/CISCO-RADIUS-EXT-MIB:creClientAuthentication'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.creauthclientaverageresponsedelay is not None:
                return True

            if self.creauthclientbadauthenticators is not None:
                return True

            if self.creauthclientbufferallocfailures is not None:
                return True

            if self.creauthclientdupids is not None:
                return True

            if self.creauthclientlastusedsourceid is not None:
                return True

            if self.creauthclientmalformedresponses is not None:
                return True

            if self.creauthclientmaxbuffersize is not None:
                return True

            if self.creauthclientmaxresponsedelay is not None:
                return True

            if self.creauthclienttimeouts is not None:
                return True

            if self.creauthclienttotalpacketswithoutresponses is not None:
                return True

            if self.creauthclienttotalpacketswithresponses is not None:
                return True

            if self.creauthclienttotalresponses is not None:
                return True

            if self.creauthclientunknownresponses is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RADIUS_EXT_MIB as meta
            return meta._meta_table['CiscoRadiusExtMib.Creclientauthentication']['meta_info']


    class Creclientaccounting(object):
        """
        
        
        .. attribute:: creacctclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS accounting
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creacctclientbadauthenticators
        
        	This object indicates the number of RADIUS Accounting\-Response packets received with invalid authenticators
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered for RADIUS accounting request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: buffer failures
        
        .. attribute:: creacctclientdupids
        
        	This object indicates the number of times client has received duplicate accounting responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS accounting request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS accounting request is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creacctclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS accounting responses received.  Malformed packets include packets with an invalid length
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS accounting packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: bytes
        
        .. attribute:: creacctclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS accounting
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creacctclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS accounting.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: timeouts
        
        .. attribute:: creacctclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS accounting packets that never received a response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS accounting packets that received responses
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalresponses
        
        	This object indicates the number of RADIUS accounting response packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientunknownresponses
        
        	This object indicates the number of unknown RADIUS accounting responses received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            self.parent = None
            self.creacctclientaverageresponsedelay = None
            self.creacctclientbadauthenticators = None
            self.creacctclientbufferallocfailures = None
            self.creacctclientdupids = None
            self.creacctclientlastusedsourceid = None
            self.creacctclientmalformedresponses = None
            self.creacctclientmaxbuffersize = None
            self.creacctclientmaxresponsedelay = None
            self.creacctclienttimeouts = None
            self.creacctclienttotalpacketswithoutresponses = None
            self.creacctclienttotalpacketswithresponses = None
            self.creacctclienttotalresponses = None
            self.creacctclientunknownresponses = None

        @property
        def _common_path(self):

            return '/CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/CISCO-RADIUS-EXT-MIB:creClientAccounting'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.creacctclientaverageresponsedelay is not None:
                return True

            if self.creacctclientbadauthenticators is not None:
                return True

            if self.creacctclientbufferallocfailures is not None:
                return True

            if self.creacctclientdupids is not None:
                return True

            if self.creacctclientlastusedsourceid is not None:
                return True

            if self.creacctclientmalformedresponses is not None:
                return True

            if self.creacctclientmaxbuffersize is not None:
                return True

            if self.creacctclientmaxresponsedelay is not None:
                return True

            if self.creacctclienttimeouts is not None:
                return True

            if self.creacctclienttotalpacketswithoutresponses is not None:
                return True

            if self.creacctclienttotalpacketswithresponses is not None:
                return True

            if self.creacctclienttotalresponses is not None:
                return True

            if self.creacctclientunknownresponses is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RADIUS_EXT_MIB as meta
            return meta._meta_table['CiscoRadiusExtMib.Creclientaccounting']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.creclientaccounting is not None and self.creclientaccounting._has_data():
            return True

        if self.creclientauthentication is not None and self.creclientauthentication._has_data():
            return True

        if self.creclientglobal is not None and self.creclientglobal._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RADIUS_EXT_MIB as meta
        return meta._meta_table['CiscoRadiusExtMib']['meta_info']


