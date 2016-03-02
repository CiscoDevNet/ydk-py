""" CISCO_QINQ_VLAN_MIB 

This MIB defines configuration and monitoring capabilities
relating to 802.1QinQ interfaces.  QinQ interfaces are capable
of terminating QinQ traffic and translating QinQ tags.

IEEE 802.1Q VLAN specification provides for an option to tag
Ethernet frames with two VLAN tags\:

\- An inner tag that specifies the customer's VLAN ID.  This tag
  is called the 'CE VLAN'.

\- An outer tag that specifies the service provider's VLAN ID.
  This tag is called the 'metro tag', or the 'PE VLAN'.

The combination of inner and outer VLAN tags is used to uniquely
identify a particular customer's service flow.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class CqvEncapsulationType_Enum(Enum):
    """
    CqvEncapsulationType_Enum

    This textual convention defines the different types of VLAN
    trunking.
    
    isl \- Inter Switch Link, the Cisco proprietary trunking
    protocol.
    
    dot1Q \- IEEE 802.1Q trunking standard.

    """

    ISL = 1

    DOT1Q = 2


    @staticmethod
    def _meta_info():
        from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
        return meta._meta_table['CqvEncapsulationType_Enum']



class CISCOQINQVLANMIB(object):
    """
    
    
    .. attribute:: cqvterminationtable
    
    	This table contains attributes pertaining to QinQ terminated interfaces.  The ifIndex in the INDEX clause identifies the interface that terminates QinQ traffic.  A management application can create a conceptual row in this table by setting the cqvTerminationRowStatus to 'createAndWait' or 'createAndGo'.  A conceptual row in this table cannot be modified while cqvTerminationRowStatus is set to 'active'
    	**type**\: :py:class:`CqvTerminationTable <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTerminationTable>`
    
    .. attribute:: cqvtranslationtable
    
    	This table defines the translations performed on QinQ capable interfaces.  The ifIndex in the INDEX clause identifies the QinQ interface.  A QinQ interface performs the following translations\:  \- Double Tagged to Single Tagged \- the inner and outer tags of   the frames internal to the switch are replaced with a single   trunk VLAN tag when the outgoing frame is transmitted.  \- Double Tagged to Double Tagged \- the outer tag of the frames   internal to the switch are replaced with an outer trunk   VLAN tag when the outgoing frame is transmitted.  The inner   tag remains unchanged in the transmitted frame.  The following picture illustrates QinQ translations.         <\-\-\-\-\- Provider Side \-\-\-\-\-\|\-\-\-\-\- Customer Side \-\-\-\-\->               Switch +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|                                \| \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\|     +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  \| Double Tagged \|     \|  QinQ \|     \| Single or Double \| \|  \| Frames        \| \-\-> \|  Intf \| \-\-> \| Tagged Frames    \| \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\|     +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|                                \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  Also, the QinQ interface sets the IEEE 802.1P prioritization bits (P bits) in the outgoing frames by copying the P bits either from the internal frame's outer or inner VLAN tag.  A management application can create a conceptual row in this table by setting the cqvTranslationRowStatus to 'createAndWait' or 'createAndGo'.  A conceptual row in this table cannot be modified while cqvTranslationRowStatus is set to 'active'
    	**type**\: :py:class:`CqvTranslationTable <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTranslationTable>`
    
    

    """

    _prefix = 'cisco-qinq'
    _revision = '2004-11-29'

    def __init__(self):
        self.cqvterminationtable = CISCOQINQVLANMIB.CqvTerminationTable()
        self.cqvterminationtable.parent = self
        self.cqvtranslationtable = CISCOQINQVLANMIB.CqvTranslationTable()
        self.cqvtranslationtable.parent = self


    class CqvTerminationTable(object):
        """
        This table contains attributes pertaining to QinQ
        terminated interfaces.
        
        The ifIndex in the INDEX clause identifies the interface
        that terminates QinQ traffic.
        
        A management application can create a conceptual row in this
        table by setting the cqvTerminationRowStatus to
        'createAndWait' or 'createAndGo'.
        
        A conceptual row in this table cannot be modified while
        cqvTerminationRowStatus is set to 'active'.
        
        .. attribute:: cqvterminationentry
        
        	An entry in this table defines a QinQ terminated interface
        	**type**\: list of :py:class:`CqvTerminationEntry <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry>`
        
        

        """

        _prefix = 'cisco-qinq'
        _revision = '2004-11-29'

        def __init__(self):
            self.parent = None
            self.cqvterminationentry = YList()
            self.cqvterminationentry.parent = self
            self.cqvterminationentry.name = 'cqvterminationentry'


        class CqvTerminationEntry(object):
            """
            An entry in this table defines a QinQ terminated interface.
            
            .. attribute:: cqvterminationcevlanid
            
            	The VLAN ID of the inner tag of a QinQ frame
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cqvterminationpevlanid
            
            	The VLAN ID of the outer tag of a QinQ frame
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cqvterminationpeencap
            
            	The encapsulation type of the PE VLAN (cqvTerminationPeVlanId) of a QinQ frame
            	**type**\: :py:class:`CqvEncapsulationType_Enum <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CqvEncapsulationType_Enum>`
            
            .. attribute:: cqvterminationrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-qinq'
            _revision = '2004-11-29'

            def __init__(self):
                self.parent = None
                self.cqvterminationcevlanid = None
                self.cqvterminationpevlanid = None
                self.ifindex = None
                self.cqvterminationpeencap = None
                self.cqvterminationrowstatus = None

            @property
            def _common_path(self):
                if self.cqvterminationcevlanid is None:
                    raise YPYDataValidationError('Key property cqvterminationcevlanid is None')
                if self.cqvterminationpevlanid is None:
                    raise YPYDataValidationError('Key property cqvterminationpevlanid is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-QINQ-VLAN-MIB:CISCO-QINQ-VLAN-MIB/CISCO-QINQ-VLAN-MIB:cqvTerminationTable/CISCO-QINQ-VLAN-MIB:cqvTerminationEntry[CISCO-QINQ-VLAN-MIB:cqvTerminationCeVlanId = ' + str(self.cqvterminationcevlanid) + '][CISCO-QINQ-VLAN-MIB:cqvTerminationPeVlanId = ' + str(self.cqvterminationpevlanid) + '][CISCO-QINQ-VLAN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cqvterminationcevlanid is not None:
                    return True

                if self.cqvterminationpevlanid is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cqvterminationpeencap is not None:
                    return True

                if self.cqvterminationrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
                return meta._meta_table['CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QINQ-VLAN-MIB:CISCO-QINQ-VLAN-MIB/CISCO-QINQ-VLAN-MIB:cqvTerminationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cqvterminationentry is not None:
                for child_ref in self.cqvterminationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
            return meta._meta_table['CISCOQINQVLANMIB.CqvTerminationTable']['meta_info']


    class CqvTranslationTable(object):
        """
        This table defines the translations performed on QinQ capable
        interfaces.
        
        The ifIndex in the INDEX clause identifies the QinQ interface.
        
        A QinQ interface performs the following translations\:
        
        \- Double Tagged to Single Tagged \- the inner and outer tags of
          the frames internal to the switch are replaced with a single
          trunk VLAN tag when the outgoing frame is transmitted.
        
        \- Double Tagged to Double Tagged \- the outer tag of the frames
          internal to the switch are replaced with an outer trunk
          VLAN tag when the outgoing frame is transmitted.  The inner
          tag remains unchanged in the transmitted frame.
        
        The following picture illustrates QinQ translations.
        
               <\-\-\-\-\- Provider Side \-\-\-\-\-\|\-\-\-\-\- Customer Side \-\-\-\-\->
        
                     Switch
        +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
        \|                                \|
        \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\|     +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
        \|  \| Double Tagged \|     \|  QinQ \|     \| Single or Double \|
        \|  \| Frames        \| \-\-> \|  Intf \| \-\-> \| Tagged Frames    \|
        \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\|     +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
        \|                                \|
        +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
        
        Also, the QinQ interface sets the IEEE 802.1P prioritization
        bits (P bits) in the outgoing frames by copying the P bits
        either from the internal frame's outer or inner VLAN tag.
        
        A management application can create a conceptual row in this
        table by setting the cqvTranslationRowStatus to
        'createAndWait' or 'createAndGo'.
        
        A conceptual row in this table cannot be modified while
        cqvTranslationRowStatus is set to 'active'.
        
        .. attribute:: cqvtranslationentry
        
        	An entry in this table contains translation information for a particular QinQ interface
        	**type**\: list of :py:class:`CqvTranslationEntry <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry>`
        
        

        """

        _prefix = 'cisco-qinq'
        _revision = '2004-11-29'

        def __init__(self):
            self.parent = None
            self.cqvtranslationentry = YList()
            self.cqvtranslationentry.parent = self
            self.cqvtranslationentry.name = 'cqvtranslationentry'


        class CqvTranslationEntry(object):
            """
            An entry in this table contains translation information for
            a particular QinQ interface.
            
            .. attribute:: cqvtranslationinternalcevlanid
            
            	The QinQ inner VLAN ID of an internal double tagged frame.  This object will have the value of zero as described in the cqvTranslationType object
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cqvtranslationinternalpevlanid
            
            	The QinQ outer VLAN ID of an internal double tagged frame.  This object will have the value of zero as described in the cqvTranslationType object
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cqvtranslationcospbits
            
            	This object indicates how the IEEE 802.1P bits (P bits) in the IEEE 802.1Q header of the trunk VLAN are to be set.  The P bits in the trunk VLAN can be set by copying the P bits of the outer PE tag or the inner CE tag.      'copyFromOuterTag' \- Copy the P bits from the outer PE tag.      'copyFromInnerTag' \- Copy the P bits from the inner CE tag
            	**type**\: :py:class:`CqvTranslationCosPBits_Enum <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationCosPBits_Enum>`
            
            .. attribute:: cqvtranslationrowstatus
            
            	This object facilitates the creation, modification, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cqvtranslationtrunkcevlanid
            
            	The QinQ inner VLAN ID of a trunk VLAN frame.  This object will have the value of zero as described in the cqvTranslationType object
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cqvtranslationtrunkpevlanid
            
            	The QinQ outer VLAN ID of a trunk VLAN frame.  This object will have the value of zero as described in the cqvTranslationType object
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cqvtranslationtype
            
            	The QinQ translation type being performed on the interface.  'doubleToSingle' \- Double tagged to single tagged traffic.                    The value of cqvTranslationTrunkPeVlanId                    will be zero.  This indicates that the PE                    VLAN tag will be absent in the trunk                    interface.  'doubleToDouble' \- Double tagged to double tagged traffic.                    The value of the internal PE and CE, and                    the trunk PE and CE VLAN IDs are                    non\-zero.  'doubleToDoubleOutOfRange' \- Double tagged to double tagged                    traffic that does not have a defined                    translation. The value of                    cqvTranslationInternalCeVlanId  will be                    zero.  This indicates that the CE                    VLAN tag is being used as a wildcard
            	**type**\: :py:class:`CqvTranslationType_Enum <ydk.models.qinq.CISCO_QINQ_VLAN_MIB.CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationType_Enum>`
            
            

            """

            _prefix = 'cisco-qinq'
            _revision = '2004-11-29'

            def __init__(self):
                self.parent = None
                self.cqvtranslationinternalcevlanid = None
                self.cqvtranslationinternalpevlanid = None
                self.ifindex = None
                self.cqvtranslationcospbits = None
                self.cqvtranslationrowstatus = None
                self.cqvtranslationtrunkcevlanid = None
                self.cqvtranslationtrunkpevlanid = None
                self.cqvtranslationtype = None

            class CqvTranslationCosPBits_Enum(Enum):
                """
                CqvTranslationCosPBits_Enum

                This object indicates how the IEEE 802.1P bits (P bits) in the
                IEEE 802.1Q header of the trunk VLAN are to be set.  The P bits
                in the trunk VLAN can be set by copying the P bits of the
                outer PE tag or the inner CE tag.
                
                    'copyFromOuterTag' \- Copy the P bits from the outer PE tag.
                
                    'copyFromInnerTag' \- Copy the P bits from the inner CE tag.

                """

                COPYFROMOUTERTAG = 1

                COPYFROMINNERTAG = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
                    return meta._meta_table['CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationCosPBits_Enum']


            class CqvTranslationType_Enum(Enum):
                """
                CqvTranslationType_Enum

                The QinQ translation type being performed on the interface.
                
                'doubleToSingle' \- Double tagged to single tagged traffic.
                                   The value of cqvTranslationTrunkPeVlanId
                                   will be zero.  This indicates that the PE
                                   VLAN tag will be absent in the trunk
                                   interface.
                
                'doubleToDouble' \- Double tagged to double tagged traffic.
                                   The value of the internal PE and CE, and
                                   the trunk PE and CE VLAN IDs are
                                   non\-zero.
                
                'doubleToDoubleOutOfRange' \- Double tagged to double tagged
                                   traffic that does not have a defined
                                   translation. The value of
                                   cqvTranslationInternalCeVlanId  will be
                                   zero.  This indicates that the CE
                                   VLAN tag is being used as a wildcard.

                """

                DOUBLETOSINGLE = 1

                DOUBLETODOUBLE = 2

                DOUBLETODOUBLEOUTOFRANGE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
                    return meta._meta_table['CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationType_Enum']


            @property
            def _common_path(self):
                if self.cqvtranslationinternalcevlanid is None:
                    raise YPYDataValidationError('Key property cqvtranslationinternalcevlanid is None')
                if self.cqvtranslationinternalpevlanid is None:
                    raise YPYDataValidationError('Key property cqvtranslationinternalpevlanid is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-QINQ-VLAN-MIB:CISCO-QINQ-VLAN-MIB/CISCO-QINQ-VLAN-MIB:cqvTranslationTable/CISCO-QINQ-VLAN-MIB:cqvTranslationEntry[CISCO-QINQ-VLAN-MIB:cqvTranslationInternalCeVlanId = ' + str(self.cqvtranslationinternalcevlanid) + '][CISCO-QINQ-VLAN-MIB:cqvTranslationInternalPeVlanId = ' + str(self.cqvtranslationinternalpevlanid) + '][CISCO-QINQ-VLAN-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cqvtranslationinternalcevlanid is not None:
                    return True

                if self.cqvtranslationinternalpevlanid is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cqvtranslationcospbits is not None:
                    return True

                if self.cqvtranslationrowstatus is not None:
                    return True

                if self.cqvtranslationtrunkcevlanid is not None:
                    return True

                if self.cqvtranslationtrunkpevlanid is not None:
                    return True

                if self.cqvtranslationtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
                return meta._meta_table['CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-QINQ-VLAN-MIB:CISCO-QINQ-VLAN-MIB/CISCO-QINQ-VLAN-MIB:cqvTranslationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cqvtranslationentry is not None:
                for child_ref in self.cqvtranslationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
            return meta._meta_table['CISCOQINQVLANMIB.CqvTranslationTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-QINQ-VLAN-MIB:CISCO-QINQ-VLAN-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cqvterminationtable is not None and self.cqvterminationtable._has_data():
            return True

        if self.cqvterminationtable is not None and self.cqvterminationtable.is_presence():
            return True

        if self.cqvtranslationtable is not None and self.cqvtranslationtable._has_data():
            return True

        if self.cqvtranslationtable is not None and self.cqvtranslationtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.qinq._meta import _CISCO_QINQ_VLAN_MIB as meta
        return meta._meta_table['CISCOQINQVLANMIB']['meta_info']


