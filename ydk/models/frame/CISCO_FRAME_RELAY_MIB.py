""" CISCO_FRAME_RELAY_MIB 

Cisco Frame Relay MIB

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CfrMapProtocols_Enum(Enum):
    """
    CfrMapProtocols_Enum

    Cisco link types (network protocols) that run
    over Frame Relay. Associated values, except for
    wildcard, match assigned values of internal software
    respectively.

    """

    ARP = 1

    SERIALARP = 6

    IP = 7

    XNS = 10

    NOVELL = 11

    APOLLO = 12

    VINES = 13

    APPLETALK = 16

    IEEESPANNING = 18

    DECNET = 22

    CLNS = 25

    RSRB = 37

    BRIDGE = 38

    STUN = 39

    FRARP = 40

    UNCOMPRESSEDTCP = 47

    COMPRESSEDTCP = 48

    LLC2 = 49

    FRSWITCH = 53

    DLSW = 63

    NHRP = 74

    COMPRESSEDRTP = 83

    WILDCARD = 999


    @staticmethod
    def _meta_info():
        from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
        return meta._meta_table['CfrMapProtocols_Enum']



class CISCOFRAMERELAYMIB(object):
    """
    
    
    .. attribute:: cfrconnectiontable
    
    	Table of Frame Relay/Frame Relay and Frame Relay/ATM Network/Service Interworking connection information.  These are specific to Cisco's implementation
    	**type**\: :py:class:`CfrConnectionTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable>`
    
    .. attribute:: cfrelmineighbortable
    
    	Table of CISCO Frame Relay Neighbor ELMI information that is specific to CISCO implementation
    	**type**\: :py:class:`CfrElmiNeighborTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiNeighborTable>`
    
    .. attribute:: cfrelmiobjs
    
    	
    	**type**\: :py:class:`CfrElmiObjs <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiObjs>`
    
    .. attribute:: cfrelmitable
    
    	Table of CISCO Frame Relay ELMI information that is specific to CISCO implementation
    	**type**\: :py:class:`CfrElmiTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiTable>`
    
    .. attribute:: cfrfragtable
    
    	Table of Frame Relay Fragmentation information.  These are specific to Cisco's implementation
    	**type**\: :py:class:`CfrFragTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrFragTable>`
    
    .. attribute:: cfrmaptable
    
    	Table of protocols and addresses mapping information of FR virtual circuit
    	**type**\: :py:class:`CfrMapTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable>`
    
    .. attribute:: cfrsvctable
    
    	Table of FR SVC specific, descriptive and statistics information
    	**type**\: :py:class:`CfrSvcTable <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrSvcTable>`
    
    

    """

    _prefix = 'cisco-frame'
    _revision = '2000-10-13'

    def __init__(self):
        self.cfrconnectiontable = CISCOFRAMERELAYMIB.CfrConnectionTable()
        self.cfrconnectiontable.parent = self
        self.cfrelmineighbortable = CISCOFRAMERELAYMIB.CfrElmiNeighborTable()
        self.cfrelmineighbortable.parent = self
        self.cfrelmiobjs = CISCOFRAMERELAYMIB.CfrElmiObjs()
        self.cfrelmiobjs.parent = self
        self.cfrelmitable = CISCOFRAMERELAYMIB.CfrElmiTable()
        self.cfrelmitable.parent = self
        self.cfrfragtable = CISCOFRAMERELAYMIB.CfrFragTable()
        self.cfrfragtable.parent = self
        self.cfrmaptable = CISCOFRAMERELAYMIB.CfrMapTable()
        self.cfrmaptable.parent = self
        self.cfrsvctable = CISCOFRAMERELAYMIB.CfrSvcTable()
        self.cfrsvctable.parent = self


    class CfrConnectionTable(object):
        """
        Table of Frame Relay/Frame Relay and Frame Relay/ATM
        Network/Service Interworking connection information. 
        These are specific to Cisco's implementation.
        
        .. attribute:: cfrconnectionentry
        
        	Each entry of the table contains information of a connection that is established for Frame Relay/Frame  Relay and Frame Relay/ATM Network/Service Interworking
        	**type**\: list of :py:class:`CfrConnectionEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrconnectionentry = YList()
            self.cfrconnectionentry.parent = self
            self.cfrconnectionentry.name = 'cfrconnectionentry'


        class CfrConnectionEntry(object):
            """
            Each entry of the table contains information of a
            connection that is established for Frame Relay/Frame 
            Relay and Frame Relay/ATM Network/Service Interworking.
            
            .. attribute:: frcircuitdlci
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrconnclpbit
            
            	The method of operation used to map loss priority mapping in the FR to ATM direction. Not supported in case of FR\-FR connection
            	**type**\: :py:class:`CfrConnClpBit_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnClpBit_Enum>`
            
            .. attribute:: cfrconndebit
            
            	The method of operation for loss priority mapping in the B\-ISDN to FR direction.. Not supported in case of FR\-FR connection
            	**type**\: :py:class:`CfrConnDeBit_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnDeBit_Enum>`
            
            .. attribute:: cfrconnefcibit
            
            	Shows whether the FECN field in the FR frame is mapped  to the ATM EFCI field of every cell generated out of the  FR frame. This is used to indicate congestion in FR to ATM direction in case of Frame Relay/ATM  Service PVC  Interworking. Not supported in FRF.5 (Frame Relay/ATM Network  Interworking and FR\-FR connections
            	**type**\: :py:class:`CfrConnEfciBit_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnEfciBit_Enum>`
            
            .. attribute:: cfrconnfrsscsdlci
            
            	The DLCI value used at the FR\-SSCS layer. This is one of connection multiplexing methods used in Frame Relay/ATM   Network Interworking. Not supported in case of FRF.8 (FR\-ATM Service PVC  Interworking) and FR\-FR connections
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: cfrconnid
            
            	The numerical identifier of a FR/FR or FR/ATM   Network/Service Interworking connection
            	**type**\: int
            
            	**range:** 1..2000
            
            .. attribute:: cfrconnname
            
            	The textual name of a for FR/FR or FR/ATM   Network/Service Interworking connection
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrconnsegment1dlci
            
            	The DLCI used as the first segment of a FR\-FR or FR\-ATM Network/Service Interworking connection
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: cfrconnsegment1name
            
            	The textual name used to identify the first segment of  a FR/FR or FR/ATM  Network/Service Interworking  connection
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrconnsegment1vcgroup
            
            	The textual name used to identify the VC\-Group in the first segment of a Frame Relay/ATM  Network Interworking (FRF.5)connection.  This field is not applicabe in case of,          FRF.8 (Frame Relay/ATM  Service Interworking)          and          FR\-FR connectione. 
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrconnsegment2name
            
            	The interface on which second segment of a FR\-FR or  FR\-ATM  Network/Service Interworking connection is  configured
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrconnsegment2vci
            
            	The value of  VCI, in the ATM connection, used as the second segment of a FR\-ATM  Network/Service Interworking connection. In case of FR\-FR connection, this is not  supported
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cfrconnsegment2vpi
            
            	The value of  VPI, in the ATM connection, used as the second segment of a FR\-ATM  Network/Service Interworking connection. In case of FR\-FR connection, the same will  be used to display the DLCI used as the second segment
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cfrconnservicetranslation
            
            	Shows whether Service Translation Mode is supported or not. Translation Mode is the interworking of  internetworking (routed and/or bridged) protocols used  in FR\-ATM  Service PVC Interworking(FRF.8). This is not supported in case of FRF.5 (FR\-ATM network Interworking) and FR\-FR connections
            	**type**\: :py:class:`CfrConnServiceTranslation_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnServiceTranslation_Enum>`
            
            .. attribute:: cfrconnstate
            
            	Status of a FR/FR or FR/ATM  Network/Service  Interworking connection
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.cfrconnclpbit = None
                self.cfrconndebit = None
                self.cfrconnefcibit = None
                self.cfrconnfrsscsdlci = None
                self.cfrconnid = None
                self.cfrconnname = None
                self.cfrconnsegment1dlci = None
                self.cfrconnsegment1name = None
                self.cfrconnsegment1vcgroup = None
                self.cfrconnsegment2name = None
                self.cfrconnsegment2vci = None
                self.cfrconnsegment2vpi = None
                self.cfrconnservicetranslation = None
                self.cfrconnstate = None

            class CfrConnClpBit_Enum(Enum):
                """
                CfrConnClpBit_Enum

                The method of operation used to map loss priority
                mapping in the FR to ATM direction.
                Not supported in case of FR\-FR connection.

                """

                SETCLPTO0ANDCOPYDETOFRSSCSDE = 1

                SETCLPTO1ANDCOPYDETOFRSSCSDE = 2

                COPYDETOFRSSCSDEANDCLP = 3

                COPYDETOCLP = 4

                SETCLP1 = 5

                SETCLP0 = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnClpBit_Enum']


            class CfrConnDeBit_Enum(Enum):
                """
                CfrConnDeBit_Enum

                The method of operation for loss priority mapping in the
                B\-ISDN to FR direction..
                Not supported in case of FR\-FR connection.

                """

                NOMAPCLP = 1

                MAPCLP = 2

                SETDE0 = 3

                SETDE1 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnDeBit_Enum']


            class CfrConnEfciBit_Enum(Enum):
                """
                CfrConnEfciBit_Enum

                Shows whether the FECN field in the FR frame is mapped 
                to the ATM EFCI field of every cell generated out of the 
                FR frame. This is used to indicate congestion in FR to
                ATM direction in case of Frame Relay/ATM  Service PVC 
                Interworking.
                Not supported in FRF.5 (Frame Relay/ATM Network 
                Interworking and FR\-FR connections.

                """

                MAPFECN = 1

                NOTMAPFECN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnEfciBit_Enum']


            class CfrConnServiceTranslation_Enum(Enum):
                """
                CfrConnServiceTranslation_Enum

                Shows whether Service Translation Mode is supported or
                not. Translation Mode is the interworking of 
                internetworking (routed and/or bridged) protocols used 
                in FR\-ATM  Service PVC Interworking(FRF.8).
                This is not supported in case of FRF.5 (FR\-ATM network
                Interworking) and FR\-FR connections.

                """

                SERVICETRANSLATIONENABLED = 1

                SERVICETRANSLATIONNOTENABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnServiceTranslation_Enum']


            @property
            def _common_path(self):
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrConnectionTable/CISCO-FRAME-RELAY-MIB:cfrConnectionEntry[CISCO-FRAME-RELAY-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][CISCO-FRAME-RELAY-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.cfrconnclpbit is not None:
                    return True

                if self.cfrconndebit is not None:
                    return True

                if self.cfrconnefcibit is not None:
                    return True

                if self.cfrconnfrsscsdlci is not None:
                    return True

                if self.cfrconnid is not None:
                    return True

                if self.cfrconnname is not None:
                    return True

                if self.cfrconnsegment1dlci is not None:
                    return True

                if self.cfrconnsegment1name is not None:
                    return True

                if self.cfrconnsegment1vcgroup is not None:
                    return True

                if self.cfrconnsegment2name is not None:
                    return True

                if self.cfrconnsegment2vci is not None:
                    return True

                if self.cfrconnsegment2vpi is not None:
                    return True

                if self.cfrconnservicetranslation is not None:
                    return True

                if self.cfrconnstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrConnectionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrconnectionentry is not None:
                for child_ref in self.cfrconnectionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable']['meta_info']


    class CfrElmiNeighborTable(object):
        """
        Table of CISCO Frame Relay Neighbor ELMI information
        that is specific to CISCO implementation.
        
        .. attribute:: cfrelmineighborentry
        
        	Each entry of the table contains information of the neighboring device connected to a physical interface. The entry will be present only if ELMI is enabled on the neighboring device interface. If the value of the cfrElmiRemoteStatus in the cfrElmiEntry is 1 then a  valid entry exists for the interface. If ELMI is not  supported on the remote end then, the neighbor  information for the interface will not be present
        	**type**\: list of :py:class:`CfrElmiNeighborEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrelmineighborentry = YList()
            self.cfrelmineighborentry.parent = self
            self.cfrelmineighborentry.name = 'cfrelmineighborentry'


        class CfrElmiNeighborEntry(object):
            """
            Each entry of the table contains information of the
            neighboring device connected to a physical interface.
            The entry will be present only if ELMI is enabled on
            the neighboring device interface. If the value of the
            cfrElmiRemoteStatus in the cfrElmiEntry is 1 then a 
            valid entry exists for the interface. If ELMI is not 
            supported on the remote end then, the neighbor 
            information for the interface will not be present
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cfrelmineighborarstatus
            
            	This variable indicates the status of ELMI Address  registration(AR) on the neighboring device. A value  of 1 indicates ELMI AR is not supported on the  neighboring device. A value of 2 indicates ELMI AR is enabled on the interface. A value of 3 indicates AR is supported, but user disabled the exchange of IP  address and ifIndex with the neighbor
            	**type**\: :py:class:`CfrElmiNeighborArStatus_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry.CfrElmiNeighborArStatus_Enum>`
            
            .. attribute:: cfrelmineighbordevicename
            
            	Device name of the neighboring device to which the other end of this interface is connected
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrelmineighborifindex
            
            	The Interface index of the neighboring device to  which this interface is connected. If the value of cfrElmiNeighborArStatus is 2 then this will have a valid value. If the value of cfrElmiNeighborArStatus is 3 or 1 then value of this object will be 0. NMS uses this object in the topology discovery of the network
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cfrelmineighboripaddress
            
            	The Management IP address of the neighboring device  to which the other end of this interface is  connected. Network management system can use this address to send management messages to the device. If address registration is not supported on the remote end then the value will be 0.0.0.0. NMS uses this object in the topology discovery of the network
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cfrelmineighborplatformname
            
            	Platform name of the neighboring device to which the other end of this interface is connected
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrelmineighborvendorname
            
            	Vendor name of the neighboring device to which the other end of this interface is connected
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cfrelmineighborarstatus = None
                self.cfrelmineighbordevicename = None
                self.cfrelmineighborifindex = None
                self.cfrelmineighboripaddress = None
                self.cfrelmineighborplatformname = None
                self.cfrelmineighborvendorname = None

            class CfrElmiNeighborArStatus_Enum(Enum):
                """
                CfrElmiNeighborArStatus_Enum

                This variable indicates the status of ELMI Address 
                registration(AR) on the neighboring device. A value 
                of 1 indicates ELMI AR is not supported on the 
                neighboring device. A value of 2 indicates ELMI AR is
                enabled on the interface. A value of 3 indicates AR is
                supported, but user disabled the exchange of IP 
                address and ifIndex with the neighbor.

                """

                NOTSUPPORTED = 1

                ENABLED = 2

                DISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry.CfrElmiNeighborArStatus_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrElmiNeighborTable/CISCO-FRAME-RELAY-MIB:cfrElmiNeighborEntry[CISCO-FRAME-RELAY-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cfrelmineighborarstatus is not None:
                    return True

                if self.cfrelmineighbordevicename is not None:
                    return True

                if self.cfrelmineighborifindex is not None:
                    return True

                if self.cfrelmineighboripaddress is not None:
                    return True

                if self.cfrelmineighborplatformname is not None:
                    return True

                if self.cfrelmineighborvendorname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrElmiNeighborTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrelmineighborentry is not None:
                for child_ref in self.cfrelmineighborentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable']['meta_info']


    class CfrElmiObjs(object):
        """
        
        
        .. attribute:: cfrelmiipaddr
        
        	This object represents the Management address of the device used for address registration.  Network management station can send management messages to this IP address. This can be  user configured address or the address of one of the interfaces on the device. If address registration is disabled then this will have a value of 0.0.0.0.  This object is accessible only if the ELMI protocol  is supported on the device
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrelmiipaddr = None

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrElmiObjs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrelmiipaddr is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiObjs']['meta_info']


    class CfrElmiTable(object):
        """
        Table of CISCO Frame Relay ELMI information that is
        specific to CISCO implementation
        
        .. attribute:: cfrelmientry
        
        	Each entry of the table contains information about a physical interface. The table can be accessible only if the device supports ELMI protocol and if LMI is enabled on the interface
        	**type**\: list of :py:class:`CfrElmiEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrelmientry = YList()
            self.cfrelmientry.parent = self
            self.cfrelmientry.name = 'cfrelmientry'


        class CfrElmiEntry(object):
            """
            Each entry of the table contains information about a
            physical interface. The table can be accessible only
            if the device supports ELMI protocol and if LMI is
            enabled on the interface.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cfrelmiarstatus
            
            	This variable states whether the Enhanced Link Management Interface(ELMI) address registration(AR) mechanism is enabled or not on a frame relay  interface. A value of 1 indicates ELMI AR is  supported on the interface. A value of 2 indicates ELMI AR is supported but the user disabled the exchange of IP address and ifIndex with the neighboring device. This object doesn't have any significance if cfrElmiLinkStatus is disabled on the interface
            	**type**\: :py:class:`CfrElmiArStatus_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiArStatus_Enum>`
            
            .. attribute:: cfrelmilinkstatus
            
            	This variable states whether Enhanced Link Management Interface(ELMI) protocol is enabled or not on a  frame relay interface
            	**type**\: :py:class:`CfrElmiLinkStatus_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiLinkStatus_Enum>`
            
            .. attribute:: cfrelmiremotestatus
            
            	This variable states the Enhanced Link  Management(ELMI) status on the other end of the interface. If cfrElmiLinkStatus is enabled on the other end a value of 1 will be returned, else 2 will be returned. This object doesn't have any significance if cfrElmiLinkStatus is disabled on the interface
            	**type**\: :py:class:`CfrElmiRemoteStatus_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiRemoteStatus_Enum>`
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cfrelmiarstatus = None
                self.cfrelmilinkstatus = None
                self.cfrelmiremotestatus = None

            class CfrElmiArStatus_Enum(Enum):
                """
                CfrElmiArStatus_Enum

                This variable states whether the Enhanced Link
                Management Interface(ELMI) address registration(AR)
                mechanism is enabled or not on a frame relay 
                interface. A value of 1 indicates ELMI AR is 
                supported on the interface. A value of 2 indicates
                ELMI AR is supported but the user disabled the
                exchange of IP address and ifIndex with the
                neighboring device. This object doesn't have any
                significance if cfrElmiLinkStatus is disabled
                on the interface.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiArStatus_Enum']


            class CfrElmiLinkStatus_Enum(Enum):
                """
                CfrElmiLinkStatus_Enum

                This variable states whether Enhanced Link Management
                Interface(ELMI) protocol is enabled or not on a 
                frame relay interface.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiLinkStatus_Enum']


            class CfrElmiRemoteStatus_Enum(Enum):
                """
                CfrElmiRemoteStatus_Enum

                This variable states the Enhanced Link 
                Management(ELMI) status on the other end of the
                interface. If cfrElmiLinkStatus is enabled on the
                other end a value of 1 will be returned,
                else 2 will be returned. This object doesn't have any
                significance if cfrElmiLinkStatus is disabled on the
                interface

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiRemoteStatus_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrElmiTable/CISCO-FRAME-RELAY-MIB:cfrElmiEntry[CISCO-FRAME-RELAY-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cfrelmiarstatus is not None:
                    return True

                if self.cfrelmilinkstatus is not None:
                    return True

                if self.cfrelmiremotestatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrElmiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrelmientry is not None:
                for child_ref in self.cfrelmientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrElmiTable']['meta_info']


    class CfrFragTable(object):
        """
        Table of Frame Relay Fragmentation information. 
        These are specific to Cisco's implementation.
        
        .. attribute:: cfrfragentry
        
        	Each entry of the table contains details of  fragmentation configured on  this circuit. 
        	**type**\: list of :py:class:`CfrFragEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrfragentry = YList()
            self.cfrfragentry.parent = self
            self.cfrfragentry.name = 'cfrfragentry'


        class CfrFragEntry(object):
            """
            Each entry of the table contains details of 
            fragmentation configured on  this circuit. 
            
            .. attribute:: frcircuitdlci
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrfragassembledinoctets
            
            	Total number of bytes received in fully reassembled  frames. It also counts the number of packets received without FR fragmentation header (i.e.in un\-fragmentated pkts)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragassembledinpkts
            
            	Total number of fully reassembled frames. It also  counts the number of packets received without FR  fragmentation header (i.e. in un\-fragmentated pkts)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragdroppedfragmentedoutpkts
            
            	Number of fragments dropped because of running  out of memory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragdroppedreassembledinpkts
            
            	Number of received fragments dropped for reasons such as \: running out of memory, receiving segments out of  sequence, receiving an unexpected frame with a B bit  set, timing out on a reassembling frame
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfraginoctets
            
            	Total number of bytes received in frames that have a  fragmentation header. The number of bytes include the FR header
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfraginpkts
            
            	Total number of frames received that have a  fragmentation header
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfraginterleavedoutpkts
            
            	Number of packets that have been interleaved between  segments
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragnotinoctets
            
            	Total number of bytes received in frames that do not  require reassembly and therefore will not contain the  fragmentation header. This counter is valid only when end\-to\-end fragmentation type is set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragnotinpkts
            
            	Total number of frames received that do not require  reassembly and therefore will not contain the  fragmentation header. This counter is valid only when end\-to\-end fragmentation type is set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragnotoutoctets
            
            	Total number of bytes transmitted in frames that are not fragmented and therefore will not contain the  fragmentation header. This counter is valid only when  end\-to\-end fragmentation type is set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragnotoutpkts
            
            	Total number of frames transmitted without fragmenting and therefore will not contain the fragmentation header. This counter is valid only when end\-to\-end fragmentation type is set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragoutoctets
            
            	Total number of bytes that are transmitted in frames with a fragmenation header. The number of bytes also includes the FR header
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragoutofseqfragpkts
            
            	Indicates the total number of packets received with an unexpected sequence number. All fragments being  reassembled are dropped. Start a new packet with the received segment only if the B bit is set on the  segment. Otherwise the new segment is also dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragoutpkts
            
            	Total number of fragments that are transmitted with a fragmenation header
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragpreoutoctets
            
            	Total number of bytes transmitted in fragmented frames. It also counts the number of bytes trasmitted in frames without FR fragmentation header (i.e. in un\-fragmentated pkts)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragpreoutpkts
            
            	Total number of frames fragmented and trasmitted. It  also counts the number of packets trasmitted without FR fragmentation header (i.e. in un\-fragmentated pkts)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragseqmissedpkts
            
            	Number of fragments received in this circuit with  skipped sequence number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfrfragsize
            
            	cfrFragSize defines the payload size of a fragment  and it excludes the FR headers and any FR fragmentation header
            	**type**\: int
            
            	**range:** 16..1600
            
            .. attribute:: cfrfragtimeoutsin
            
            	Number of reassemble timer timeouts for this circuit. A frame requiring more than two minutes to fully  reassemble is dropped and timeout will be incremented by one
            	**type**\: int
            
            	**range:** 0..1000
            
            .. attribute:: cfrfragtype
            
            	Fragmentation type configured by the user. The types supported are end\-to\-end, VoFR\-cisco and VoFR
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cfrfragunexpectedbbitsetpkts
            
            	Number of fragments received in this circuit with  a B bit set. All fragments being reassembled are dropped and a new packet is started with this segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.cfrfragassembledinoctets = None
                self.cfrfragassembledinpkts = None
                self.cfrfragdroppedfragmentedoutpkts = None
                self.cfrfragdroppedreassembledinpkts = None
                self.cfrfraginoctets = None
                self.cfrfraginpkts = None
                self.cfrfraginterleavedoutpkts = None
                self.cfrfragnotinoctets = None
                self.cfrfragnotinpkts = None
                self.cfrfragnotoutoctets = None
                self.cfrfragnotoutpkts = None
                self.cfrfragoutoctets = None
                self.cfrfragoutofseqfragpkts = None
                self.cfrfragoutpkts = None
                self.cfrfragpreoutoctets = None
                self.cfrfragpreoutpkts = None
                self.cfrfragseqmissedpkts = None
                self.cfrfragsize = None
                self.cfrfragtimeoutsin = None
                self.cfrfragtype = None
                self.cfrfragunexpectedbbitsetpkts = None

            @property
            def _common_path(self):
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrFragTable/CISCO-FRAME-RELAY-MIB:cfrFragEntry[CISCO-FRAME-RELAY-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][CISCO-FRAME-RELAY-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.cfrfragassembledinoctets is not None:
                    return True

                if self.cfrfragassembledinpkts is not None:
                    return True

                if self.cfrfragdroppedfragmentedoutpkts is not None:
                    return True

                if self.cfrfragdroppedreassembledinpkts is not None:
                    return True

                if self.cfrfraginoctets is not None:
                    return True

                if self.cfrfraginpkts is not None:
                    return True

                if self.cfrfraginterleavedoutpkts is not None:
                    return True

                if self.cfrfragnotinoctets is not None:
                    return True

                if self.cfrfragnotinpkts is not None:
                    return True

                if self.cfrfragnotoutoctets is not None:
                    return True

                if self.cfrfragnotoutpkts is not None:
                    return True

                if self.cfrfragoutoctets is not None:
                    return True

                if self.cfrfragoutofseqfragpkts is not None:
                    return True

                if self.cfrfragoutpkts is not None:
                    return True

                if self.cfrfragpreoutoctets is not None:
                    return True

                if self.cfrfragpreoutpkts is not None:
                    return True

                if self.cfrfragseqmissedpkts is not None:
                    return True

                if self.cfrfragsize is not None:
                    return True

                if self.cfrfragtimeoutsin is not None:
                    return True

                if self.cfrfragtype is not None:
                    return True

                if self.cfrfragunexpectedbbitsetpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrFragTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrfragentry is not None:
                for child_ref in self.cfrfragentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrFragTable']['meta_info']


    class CfrMapTable(object):
        """
        Table of protocols and addresses mapping
        information of FR virtual circuit.
        
        .. attribute:: cfrmapentry
        
        	Each entry of the table contains one mapping  information of a Frame Relay virtual circuit
        	**type**\: list of :py:class:`CfrMapEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrmapentry = YList()
            self.cfrmapentry.parent = self
            self.cfrmapentry.name = 'cfrmapentry'


        class CfrMapEntry(object):
            """
            Each entry of the table contains one mapping 
            information of a Frame Relay virtual circuit.
            
            .. attribute:: cfrmapindex
            
            	An arbitrary Index to the mapping information associated with a certain circuit. The maximum value is arbitrarily picked which is considered sufficient for usual configuration
            	**type**\: int
            
            	**range:** 1..999
            
            .. attribute:: frcircuitdlci
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrmapaddress
            
            	Mapping protocol address at remote end for this DLCI. NOTE\: For point\-to\-point DLCI, the string is fixed to be point\-to\-point
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cfrmapbroadcast
            
            	Broadcast enabled or disabled
            	**type**\: bool
            
            .. attribute:: cfrmapencaps
            
            	Indication of the encapsulation type for this mapping protocol
            	**type**\: :py:class:`CfrMapEncaps_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapEncaps_Enum>`
            
            .. attribute:: cfrmappayloadcompress
            
            	Indicate if payload compression is enabled
            	**type**\: bool
            
            .. attribute:: cfrmappayloadcompresstype
            
            	FR payload compression type, if applicable. FRF.9 is the Frame Relay Forum Implementation Agreement on FR payload compression. The compression can be done by either software or hardware (when equipped with the supporting hardware), depending on configuration
            	**type**\: :py:class:`CfrMapPayloadCompressType_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapPayloadCompressType_Enum>`
            
            .. attribute:: cfrmapprotocol
            
            	Mapping protocol for this circuit
            	**type**\: :py:class:`CfrMapProtocols_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CfrMapProtocols_Enum>`
            
            .. attribute:: cfrmaprtphdrcompress
            
            	RTP header compression type, if applicable. The value 'passive' means that the header of an outgoing RTP/IP packet is compressed only if an incoming RTP/IP packet had a compressed header. The value 'active' means the header of every outgoing RTP/IP packet is compressed
            	**type**\: :py:class:`CfrMapRtpHdrCompress_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapRtpHdrCompress_Enum>`
            
            .. attribute:: cfrmaptcphdrcompress
            
            	TCP header compression type, if applicable
            	**type**\: :py:class:`CfrMapTcpHdrCompress_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapTcpHdrCompress_Enum>`
            
            .. attribute:: cfrmaptype
            
            	Type for the map creation
            	**type**\: :py:class:`CfrMapType_Enum <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapType_Enum>`
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.cfrmapindex = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.cfrmapaddress = None
                self.cfrmapbroadcast = None
                self.cfrmapencaps = None
                self.cfrmappayloadcompress = None
                self.cfrmappayloadcompresstype = None
                self.cfrmapprotocol = None
                self.cfrmaprtphdrcompress = None
                self.cfrmaptcphdrcompress = None
                self.cfrmaptype = None

            class CfrMapEncaps_Enum(Enum):
                """
                CfrMapEncaps_Enum

                Indication of the encapsulation type for this
                mapping protocol.

                """

                IETF = 1

                CISCO = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapEncaps_Enum']


            class CfrMapPayloadCompressType_Enum(Enum):
                """
                CfrMapPayloadCompressType_Enum

                FR payload compression type, if applicable.
                FRF.9 is the Frame Relay Forum Implementation Agreement
                on FR payload compression. The compression can be done
                by either software or hardware (when equipped with the
                supporting hardware), depending on configuration.

                """

                INAPPLICABLE = 1

                CISCO = 2

                FRF9SOFTWARE = 3

                FRF9HARDWARE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapPayloadCompressType_Enum']


            class CfrMapRtpHdrCompress_Enum(Enum):
                """
                CfrMapRtpHdrCompress_Enum

                RTP header compression type, if applicable.
                The value 'passive' means that the header of an
                outgoing RTP/IP packet is compressed only if an
                incoming RTP/IP packet had a compressed header.
                The value 'active' means the header of every outgoing
                RTP/IP packet is compressed.

                """

                INAPPLICABLE = 1

                PASSIVE = 2

                ACTIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapRtpHdrCompress_Enum']


            class CfrMapTcpHdrCompress_Enum(Enum):
                """
                CfrMapTcpHdrCompress_Enum

                TCP header compression type, if applicable.

                """

                INAPPLICABLE = 1

                PASSIVE = 2

                ACTIVE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapTcpHdrCompress_Enum']


            class CfrMapType_Enum(Enum):
                """
                CfrMapType_Enum

                Type for the map creation.

                """

                STATIC = 1

                DYNAMIC = 2

                SVC = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                    return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapType_Enum']


            @property
            def _common_path(self):
                if self.cfrmapindex is None:
                    raise YPYDataValidationError('Key property cfrmapindex is None')
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrMapTable/CISCO-FRAME-RELAY-MIB:cfrMapEntry[CISCO-FRAME-RELAY-MIB:cfrMapIndex = ' + str(self.cfrmapindex) + '][CISCO-FRAME-RELAY-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][CISCO-FRAME-RELAY-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cfrmapindex is not None:
                    return True

                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.cfrmapaddress is not None:
                    return True

                if self.cfrmapbroadcast is not None:
                    return True

                if self.cfrmapencaps is not None:
                    return True

                if self.cfrmappayloadcompress is not None:
                    return True

                if self.cfrmappayloadcompresstype is not None:
                    return True

                if self.cfrmapprotocol is not None:
                    return True

                if self.cfrmaprtphdrcompress is not None:
                    return True

                if self.cfrmaptcphdrcompress is not None:
                    return True

                if self.cfrmaptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrmapentry is not None:
                for child_ref in self.cfrmapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrMapTable']['meta_info']


    class CfrSvcTable(object):
        """
        Table of FR SVC specific, descriptive
        and statistics information.
        
        .. attribute:: cfrsvcentry
        
        	Each entry of the table contains circuit information specific to a Frame Relay Switched Virtual Circuit
        	**type**\: list of :py:class:`CfrSvcEntry <ydk.models.frame.CISCO_FRAME_RELAY_MIB.CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry>`
        
        

        """

        _prefix = 'cisco-frame'
        _revision = '2000-10-13'

        def __init__(self):
            self.parent = None
            self.cfrsvcentry = YList()
            self.cfrsvcentry.parent = self
            self.cfrsvcentry.name = 'cfrsvcentry'


        class CfrSvcEntry(object):
            """
            Each entry of the table contains circuit information
            specific to a Frame Relay Switched Virtual Circuit.
            
            .. attribute:: frcircuitdlci
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitifindex
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrsvcaddrlocal
            
            	Local E.164/X.125 address for the circuit
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cfrsvcaddrremote
            
            	Remote E.164/X.125 address for the circuit
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cfrsvccommitburstin
            
            	Circuit's incoming Committed Burst Rate. See ANSI and/or ITU specifications for definition and calculations. For outgoing CBR, see frCircuitCommittedBurst per RFC 1315
            	**type**\: int
            
            	**range:** 9600..1544000
            
            .. attribute:: cfrsvcexcessburstin
            
            	Circuit's incoming Excess Burst Rate. See ANSI and/or ITU specifications for definition and calculations. For outgoing EBR, see frCircuitExcessBurst per RFC 1315
            	**type**\: int
            
            	**range:** 9600..2440000
            
            .. attribute:: cfrsvcidletime
            
            	Circuit's idle time period. If expires, the circuit is cleared
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cfrsvcminthruputin
            
            	Circuit's incoming minimal Throughput
            	**type**\: int
            
            	**range:** 9600..1544000
            
            .. attribute:: cfrsvcminthruputout
            
            	Circuit's outgoing minimal Throughput
            	**type**\: int
            
            	**range:** 9600..1544000
            
            .. attribute:: cfrsvcthroughputin
            
            	Circuit's incoming throughput. For outgoing  throughput (commonly referred to as CIR) see frCircuitThroughput per RFC1315
            	**type**\: int
            
            	**range:** 9600..1544000
            
            

            """

            _prefix = 'cisco-frame'
            _revision = '2000-10-13'

            def __init__(self):
                self.parent = None
                self.frcircuitdlci = None
                self.frcircuitifindex = None
                self.cfrsvcaddrlocal = None
                self.cfrsvcaddrremote = None
                self.cfrsvccommitburstin = None
                self.cfrsvcexcessburstin = None
                self.cfrsvcidletime = None
                self.cfrsvcminthruputin = None
                self.cfrsvcminthruputout = None
                self.cfrsvcthroughputin = None

            @property
            def _common_path(self):
                if self.frcircuitdlci is None:
                    raise YPYDataValidationError('Key property frcircuitdlci is None')
                if self.frcircuitifindex is None:
                    raise YPYDataValidationError('Key property frcircuitifindex is None')

                return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrSvcTable/CISCO-FRAME-RELAY-MIB:cfrSvcEntry[CISCO-FRAME-RELAY-MIB:frCircuitDlci = ' + str(self.frcircuitdlci) + '][CISCO-FRAME-RELAY-MIB:frCircuitIfIndex = ' + str(self.frcircuitifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.frcircuitdlci is not None:
                    return True

                if self.frcircuitifindex is not None:
                    return True

                if self.cfrsvcaddrlocal is not None:
                    return True

                if self.cfrsvcaddrremote is not None:
                    return True

                if self.cfrsvccommitburstin is not None:
                    return True

                if self.cfrsvcexcessburstin is not None:
                    return True

                if self.cfrsvcidletime is not None:
                    return True

                if self.cfrsvcminthruputin is not None:
                    return True

                if self.cfrsvcminthruputout is not None:
                    return True

                if self.cfrsvcthroughputin is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
                return meta._meta_table['CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB/CISCO-FRAME-RELAY-MIB:cfrSvcTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfrsvcentry is not None:
                for child_ref in self.cfrsvcentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
            return meta._meta_table['CISCOFRAMERELAYMIB.CfrSvcTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-FRAME-RELAY-MIB:CISCO-FRAME-RELAY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cfrconnectiontable is not None and self.cfrconnectiontable._has_data():
            return True

        if self.cfrconnectiontable is not None and self.cfrconnectiontable.is_presence():
            return True

        if self.cfrelmineighbortable is not None and self.cfrelmineighbortable._has_data():
            return True

        if self.cfrelmineighbortable is not None and self.cfrelmineighbortable.is_presence():
            return True

        if self.cfrelmiobjs is not None and self.cfrelmiobjs._has_data():
            return True

        if self.cfrelmiobjs is not None and self.cfrelmiobjs.is_presence():
            return True

        if self.cfrelmitable is not None and self.cfrelmitable._has_data():
            return True

        if self.cfrelmitable is not None and self.cfrelmitable.is_presence():
            return True

        if self.cfrfragtable is not None and self.cfrfragtable._has_data():
            return True

        if self.cfrfragtable is not None and self.cfrfragtable.is_presence():
            return True

        if self.cfrmaptable is not None and self.cfrmaptable._has_data():
            return True

        if self.cfrmaptable is not None and self.cfrmaptable.is_presence():
            return True

        if self.cfrsvctable is not None and self.cfrsvctable._has_data():
            return True

        if self.cfrsvctable is not None and self.cfrsvctable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.frame._meta import _CISCO_FRAME_RELAY_MIB as meta
        return meta._meta_table['CISCOFRAMERELAYMIB']['meta_info']


