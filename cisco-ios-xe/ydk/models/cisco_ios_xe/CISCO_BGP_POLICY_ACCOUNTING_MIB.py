""" CISCO_BGP_POLICY_ACCOUNTING_MIB 

BGP policy based accounting information

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoBgpPolicyAccountingMib(object):
    """
    
    
    .. attribute:: cbpaccttable
    
    	The cbpAcctTable provides statistics about ingress and egress  traffic on an interface. This data could be used for purposes  like billing
    	**type**\:   :py:class:`Cbpaccttable <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CiscoBgpPolicyAccountingMib.Cbpaccttable>`
    
    

    """

    _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
    _revision = '2002-07-26'

    def __init__(self):
        self.cbpaccttable = CiscoBgpPolicyAccountingMib.Cbpaccttable()
        self.cbpaccttable.parent = self


    class Cbpaccttable(object):
        """
        The cbpAcctTable provides statistics about ingress and egress 
        traffic on an interface. This data could be used for purposes 
        like billing.
        
        .. attribute:: cbpacctentry
        
        	Each cbpAcctEntry provides statistics for traffic of interest on an ingress and/or egress interfaces. The traffic of interest  may be used for purposes like billing, and is referred to from  here on in the MIB by the term 'traffic\-type', which corresponds to cbpAcctTrafficIndex. Traffic\-types are configured by the user on a per interface basis.  The statistics include ingress packet counts, ingress octet counts, egress packet counts and egress octet counts. Entries  are created when traffic\-type is configured on an interface. Entries are deleted automatically when the user  removes the corresponding traffic\-type configuration from an interface
        	**type**\: list of    :py:class:`Cbpacctentry <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry>`
        
        

        """

        _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
        _revision = '2002-07-26'

        def __init__(self):
            self.parent = None
            self.cbpacctentry = YList()
            self.cbpacctentry.parent = self
            self.cbpacctentry.name = 'cbpacctentry'


        class Cbpacctentry(object):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cbpaccttrafficindex  <key>
            
            	An integer value greater than 0, that uniquely identifies a traffic\-type. The traffic\-type has no intrinsic meaning. It just means the traffic coming into an interface can be differentiated into different types. It is up to the user to give meaning to and configure the various traffic\-types on an  interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbpacctinoctetcount
            
            	The total number of octets received for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctinpacketcount
            
            	The total number of packets received for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutoctetcount
            
            	The total number of octets transmitted for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutpacketcount
            
            	The total number of packets transmitted for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
            _revision = '2002-07-26'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cbpaccttrafficindex = None
                self.cbpacctinoctetcount = None
                self.cbpacctinpacketcount = None
                self.cbpacctoutoctetcount = None
                self.cbpacctoutpacketcount = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.cbpaccttrafficindex is None:
                    raise YPYModelError('Key property cbpaccttrafficindex is None')

                return '/CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/CISCO-BGP-POLICY-ACCOUNTING-MIB:cbpAcctTable/CISCO-BGP-POLICY-ACCOUNTING-MIB:cbpAcctEntry[CISCO-BGP-POLICY-ACCOUNTING-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-BGP-POLICY-ACCOUNTING-MIB:cbpAcctTrafficIndex = ' + str(self.cbpaccttrafficindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cbpaccttrafficindex is not None:
                    return True

                if self.cbpacctinoctetcount is not None:
                    return True

                if self.cbpacctinpacketcount is not None:
                    return True

                if self.cbpacctoutoctetcount is not None:
                    return True

                if self.cbpacctoutpacketcount is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP_POLICY_ACCOUNTING_MIB as meta
                return meta._meta_table['CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/CISCO-BGP-POLICY-ACCOUNTING-MIB:cbpAcctTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbpacctentry is not None:
                for child_ref in self.cbpacctentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP_POLICY_ACCOUNTING_MIB as meta
            return meta._meta_table['CiscoBgpPolicyAccountingMib.Cbpaccttable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cbpaccttable is not None and self.cbpaccttable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_BGP_POLICY_ACCOUNTING_MIB as meta
        return meta._meta_table['CiscoBgpPolicyAccountingMib']['meta_info']


