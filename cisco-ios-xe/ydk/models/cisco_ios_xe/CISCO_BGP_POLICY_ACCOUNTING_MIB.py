""" CISCO_BGP_POLICY_ACCOUNTING_MIB 

BGP policy based accounting information

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOBGPPOLICYACCOUNTINGMIB(Entity):
    """
    
    
    .. attribute:: cbpaccttable
    
    	The cbpAcctTable provides statistics about ingress and egress  traffic on an interface. This data could be used for purposes  like billing
    	**type**\:  :py:class:`Cbpaccttable <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable>`
    
    

    """

    _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
    _revision = '2002-07-26'

    def __init__(self):
        super(CISCOBGPPOLICYACCOUNTINGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"
        self.yang_parent_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cbpAcctTable", ("cbpaccttable", CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cbpaccttable = CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable()
        self.cbpaccttable.parent = self
        self._children_name_map["cbpaccttable"] = "cbpAcctTable"
        self._children_yang_names.add("cbpAcctTable")
        self._segment_path = lambda: "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB"


    class Cbpaccttable(Entity):
        """
        The cbpAcctTable provides statistics about ingress and egress 
        traffic on an interface. This data could be used for purposes 
        like billing.
        
        .. attribute:: cbpacctentry
        
        	Each cbpAcctEntry provides statistics for traffic of interest on an ingress and/or egress interfaces. The traffic of interest  may be used for purposes like billing, and is referred to from  here on in the MIB by the term 'traffic\-type', which corresponds to cbpAcctTrafficIndex. Traffic\-types are configured by the user on a per interface basis.  The statistics include ingress packet counts, ingress octet counts, egress packet counts and egress octet counts. Entries  are created when traffic\-type is configured on an interface. Entries are deleted automatically when the user  removes the corresponding traffic\-type configuration from an interface
        	**type**\: list of  		 :py:class:`Cbpacctentry <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable.Cbpacctentry>`
        
        

        """

        _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
        _revision = '2002-07-26'

        def __init__(self):
            super(CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable, self).__init__()

            self.yang_name = "cbpAcctTable"
            self.yang_parent_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbpAcctEntry", ("cbpacctentry", CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable.Cbpacctentry))])
            self._leafs = OrderedDict()

            self.cbpacctentry = YList(self)
            self._segment_path = lambda: "cbpAcctTable"
            self._absolute_path = lambda: "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable, [], name, value)


        class Cbpacctentry(Entity):
            """
            Each cbpAcctEntry provides statistics for traffic of interest
            on an ingress and/or egress interfaces. The traffic of interest 
            may be used for purposes like billing, and is referred to from 
            here on in the MIB by the term 'traffic\-type', which corresponds
            to cbpAcctTrafficIndex. Traffic\-types are configured by the user
            on a per interface basis.
            
            The statistics include ingress packet counts, ingress octet
            counts, egress packet counts and egress octet counts. Entries 
            are created when traffic\-type is configured on an interface.
            Entries are deleted automatically when the user 
            removes the corresponding traffic\-type configuration from an
            interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cbpaccttrafficindex  (key)
            
            	An integer value greater than 0, that uniquely identifies a traffic\-type. The traffic\-type has no intrinsic meaning. It just means the traffic coming into an interface can be differentiated into different types. It is up to the user to give meaning to and configure the various traffic\-types on an  interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbpacctinpacketcount
            
            	The total number of packets received for a particular traffic\-type on an interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctinoctetcount
            
            	The total number of octets received for a particular traffic\-type on an interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutpacketcount
            
            	The total number of packets transmitted for a particular traffic\-type on an interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutoctetcount
            
            	The total number of octets transmitted for a particular traffic\-type on an interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
            _revision = '2002-07-26'

            def __init__(self):
                super(CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable.Cbpacctentry, self).__init__()

                self.yang_name = "cbpAcctEntry"
                self.yang_parent_name = "cbpAcctTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cbpaccttrafficindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cbpaccttrafficindex', YLeaf(YType.int32, 'cbpAcctTrafficIndex')),
                    ('cbpacctinpacketcount', YLeaf(YType.uint64, 'cbpAcctInPacketCount')),
                    ('cbpacctinoctetcount', YLeaf(YType.uint64, 'cbpAcctInOctetCount')),
                    ('cbpacctoutpacketcount', YLeaf(YType.uint64, 'cbpAcctOutPacketCount')),
                    ('cbpacctoutoctetcount', YLeaf(YType.uint64, 'cbpAcctOutOctetCount')),
                ])
                self.ifindex = None
                self.cbpaccttrafficindex = None
                self.cbpacctinpacketcount = None
                self.cbpacctinoctetcount = None
                self.cbpacctoutpacketcount = None
                self.cbpacctoutoctetcount = None
                self._segment_path = lambda: "cbpAcctEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cbpAcctTrafficIndex='" + str(self.cbpaccttrafficindex) + "']"
                self._absolute_path = lambda: "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/cbpAcctTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGPPOLICYACCOUNTINGMIB.Cbpaccttable.Cbpacctentry, ['ifindex', 'cbpaccttrafficindex', 'cbpacctinpacketcount', 'cbpacctinoctetcount', 'cbpacctoutpacketcount', 'cbpacctoutoctetcount'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOBGPPOLICYACCOUNTINGMIB()
        return self._top_entity

