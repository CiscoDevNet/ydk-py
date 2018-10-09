""" DOCS_IETF_BPI2_MIB 

This is the MIB module for the DOCSIS Baseline
Privacy Plus Interface (BPI+) at cable modems (CMs)
and cable modem termination systems (CMTSs).

Copyright (C) The Internet Society (2004). This
version of this MIB module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DocsBpkmDataAuthentAlg(Enum):
    """
    DocsBpkmDataAuthentAlg (Enum Class)

    The list of data integrity algorithms defined for the

    DOCSIS interface in the BPKM cryptographic\-suite parameter.

    The value 'none' indicates no data integrity is used for

    the SAID being referenced.

    .. data:: none = 0

    .. data:: hmacSha196 = 1

    """

    none = Enum.YLeaf(0, "none")

    hmacSha196 = Enum.YLeaf(1, "hmacSha196")


class DocsBpkmDataEncryptAlg(Enum):
    """
    DocsBpkmDataEncryptAlg (Enum Class)

    The list of data encryption algorithms defined for

    the DOCSIS interface in the BPKM cryptographic\-suite

    parameter.  The Value 'none' is indicates that the SAID

    being referenced has no data encryption.

    .. data:: none = 0

    .. data:: des56CbcMode = 1

    .. data:: des40CbcMode = 2

    .. data:: t3Des128CbcMode = 3

    .. data:: aes128CbcMode = 4

    .. data:: aes256CbcMode = 5

    """

    none = Enum.YLeaf(0, "none")

    des56CbcMode = Enum.YLeaf(1, "des56CbcMode")

    des40CbcMode = Enum.YLeaf(2, "des40CbcMode")

    t3Des128CbcMode = Enum.YLeaf(3, "t3Des128CbcMode")

    aes128CbcMode = Enum.YLeaf(4, "aes128CbcMode")

    aes256CbcMode = Enum.YLeaf(5, "aes256CbcMode")


class DocsBpkmSAType(Enum):
    """
    DocsBpkmSAType (Enum Class)

    The type of security association (SA).

    The values of the named\-numbers are associated

    with the BPKM SA\-Type attributes\:

    'primary' corresponds to code '1', 'static' to code '2'

    'dynamic' to code '3'.

    'none' value must only be used if the SA type has yet

    to be determined.

    .. data:: none = 0

    .. data:: primary = 1

    .. data:: static = 2

    .. data:: dynamic = 3

    """

    none = Enum.YLeaf(0, "none")

    primary = Enum.YLeaf(1, "primary")

    static = Enum.YLeaf(2, "static")

    dynamic = Enum.YLeaf(3, "dynamic")



class DOCSIETFBPI2MIB(Entity):
    """
    
    
    .. attribute:: docsietfbpi2codedownloadcontrol
    
    	
    	**type**\:  :py:class:`DocsIetfBpi2CodeDownloadControl <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl>`
    
    .. attribute:: docsietfbpi2cmbasetable
    
    	This table describes the basic and authorization related Baseline Privacy Plus attributes of each CM MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmBaseTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable>`
    
    .. attribute:: docsietfbpi2cmtektable
    
    	This table describes the attributes of each CM Traffic Encryption Key (TEK) association. The CM maintains (no more than) one TEK association per SAID per CM MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmTEKTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable>`
    
    .. attribute:: docsietfbpi2cmipmulticastmaptable
    
    	This table maps multicast IP addresses to SAIDs per CM MAC Interface. It is intended to map multicast IP addresses associated with SA MAP Request messages
    	**type**\:  :py:class:`DocsIetfBpi2CmIpMulticastMapTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable>`
    
    .. attribute:: docsietfbpi2cmdevicecerttable
    
    	This table describes the Baseline Privacy Plus device certificates for each CM MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmDeviceCertTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable>`
    
    .. attribute:: docsietfbpi2cmcryptosuitetable
    
    	This table describes the Baseline Privacy Plus cryptographic suite capabilities for each CM MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmCryptoSuiteTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable>`
    
    .. attribute:: docsietfbpi2cmtsbasetable
    
    	This table describes the basic Baseline Privacy attributes of each CMTS MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmtsBaseTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable>`
    
    .. attribute:: docsietfbpi2cmtsauthtable
    
    	This table describes the attributes of each CM authorization association. The CMTS maintains one authorization association with each Baseline Privacy\- enabled CM, registered on each CMTS MAC interface, regardless of whether the CM is authorized or rejected
    	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable>`
    
    .. attribute:: docsietfbpi2cmtstektable
    
    	This table describes the attributes of each Traffic Encryption Key (TEK) association. The CMTS Maintains one TEK association per SAID on each CMTS MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmtsTEKTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable>`
    
    .. attribute:: docsietfbpi2cmtsipmulticastmaptable
    
    	This table maps multicast IP addresses to SAIDs. If a multicast IP address is mapped by multiple rows in the table, the row with the lowest docsIetfBpi2CmtsIpMulticastIndex must be utilized for the mapping
    	**type**\:  :py:class:`DocsIetfBpi2CmtsIpMulticastMapTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable>`
    
    .. attribute:: docsietfbpi2cmtsmulticastauthtable
    
    	This table describes the multicast SAID authorization for each CM on each CMTS MAC interface
    	**type**\:  :py:class:`DocsIetfBpi2CmtsMulticastAuthTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable>`
    
    .. attribute:: docsietfbpi2cmtsprovisionedcmcerttable
    
    	A table of CM certificate trust entries provisioned to the CMTS.  The trust object for a certificate in this table has an overriding effect on the validity object of a certificate in the authorization table, as long as the entire contents of the two certificates are identical
    	**type**\:  :py:class:`DocsIetfBpi2CmtsProvisionedCmCertTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable>`
    
    .. attribute:: docsietfbpi2cmtscacerttable
    
    	The table of known Certificate Authority certificates acquired by this device
    	**type**\:  :py:class:`DocsIetfBpi2CmtsCACertTable <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable>`
    
    

    """

    _prefix = 'DOCS-IETF-BPI2-MIB'
    _revision = '2004-09-07'

    def __init__(self):
        super(DOCSIETFBPI2MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-IETF-BPI2-MIB"
        self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsIetfBpi2CodeDownloadControl", ("docsietfbpi2codedownloadcontrol", DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl)), ("docsIetfBpi2CmBaseTable", ("docsietfbpi2cmbasetable", DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable)), ("docsIetfBpi2CmTEKTable", ("docsietfbpi2cmtektable", DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable)), ("docsIetfBpi2CmIpMulticastMapTable", ("docsietfbpi2cmipmulticastmaptable", DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable)), ("docsIetfBpi2CmDeviceCertTable", ("docsietfbpi2cmdevicecerttable", DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable)), ("docsIetfBpi2CmCryptoSuiteTable", ("docsietfbpi2cmcryptosuitetable", DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable)), ("docsIetfBpi2CmtsBaseTable", ("docsietfbpi2cmtsbasetable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable)), ("docsIetfBpi2CmtsAuthTable", ("docsietfbpi2cmtsauthtable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable)), ("docsIetfBpi2CmtsTEKTable", ("docsietfbpi2cmtstektable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable)), ("docsIetfBpi2CmtsIpMulticastMapTable", ("docsietfbpi2cmtsipmulticastmaptable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable)), ("docsIetfBpi2CmtsMulticastAuthTable", ("docsietfbpi2cmtsmulticastauthtable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable)), ("docsIetfBpi2CmtsProvisionedCmCertTable", ("docsietfbpi2cmtsprovisionedcmcerttable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable)), ("docsIetfBpi2CmtsCACertTable", ("docsietfbpi2cmtscacerttable", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable))])
        self._leafs = OrderedDict()

        self.docsietfbpi2codedownloadcontrol = DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl()
        self.docsietfbpi2codedownloadcontrol.parent = self
        self._children_name_map["docsietfbpi2codedownloadcontrol"] = "docsIetfBpi2CodeDownloadControl"

        self.docsietfbpi2cmbasetable = DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable()
        self.docsietfbpi2cmbasetable.parent = self
        self._children_name_map["docsietfbpi2cmbasetable"] = "docsIetfBpi2CmBaseTable"

        self.docsietfbpi2cmtektable = DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable()
        self.docsietfbpi2cmtektable.parent = self
        self._children_name_map["docsietfbpi2cmtektable"] = "docsIetfBpi2CmTEKTable"

        self.docsietfbpi2cmipmulticastmaptable = DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable()
        self.docsietfbpi2cmipmulticastmaptable.parent = self
        self._children_name_map["docsietfbpi2cmipmulticastmaptable"] = "docsIetfBpi2CmIpMulticastMapTable"

        self.docsietfbpi2cmdevicecerttable = DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable()
        self.docsietfbpi2cmdevicecerttable.parent = self
        self._children_name_map["docsietfbpi2cmdevicecerttable"] = "docsIetfBpi2CmDeviceCertTable"

        self.docsietfbpi2cmcryptosuitetable = DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable()
        self.docsietfbpi2cmcryptosuitetable.parent = self
        self._children_name_map["docsietfbpi2cmcryptosuitetable"] = "docsIetfBpi2CmCryptoSuiteTable"

        self.docsietfbpi2cmtsbasetable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable()
        self.docsietfbpi2cmtsbasetable.parent = self
        self._children_name_map["docsietfbpi2cmtsbasetable"] = "docsIetfBpi2CmtsBaseTable"

        self.docsietfbpi2cmtsauthtable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable()
        self.docsietfbpi2cmtsauthtable.parent = self
        self._children_name_map["docsietfbpi2cmtsauthtable"] = "docsIetfBpi2CmtsAuthTable"

        self.docsietfbpi2cmtstektable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable()
        self.docsietfbpi2cmtstektable.parent = self
        self._children_name_map["docsietfbpi2cmtstektable"] = "docsIetfBpi2CmtsTEKTable"

        self.docsietfbpi2cmtsipmulticastmaptable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable()
        self.docsietfbpi2cmtsipmulticastmaptable.parent = self
        self._children_name_map["docsietfbpi2cmtsipmulticastmaptable"] = "docsIetfBpi2CmtsIpMulticastMapTable"

        self.docsietfbpi2cmtsmulticastauthtable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable()
        self.docsietfbpi2cmtsmulticastauthtable.parent = self
        self._children_name_map["docsietfbpi2cmtsmulticastauthtable"] = "docsIetfBpi2CmtsMulticastAuthTable"

        self.docsietfbpi2cmtsprovisionedcmcerttable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable()
        self.docsietfbpi2cmtsprovisionedcmcerttable.parent = self
        self._children_name_map["docsietfbpi2cmtsprovisionedcmcerttable"] = "docsIetfBpi2CmtsProvisionedCmCertTable"

        self.docsietfbpi2cmtscacerttable = DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable()
        self.docsietfbpi2cmtscacerttable.parent = self
        self._children_name_map["docsietfbpi2cmtscacerttable"] = "docsIetfBpi2CmtsCACertTable"
        self._segment_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSIETFBPI2MIB, [], name, value)


    class DocsIetfBpi2CodeDownloadControl(Entity):
        """
        
        
        .. attribute:: docsietfbpi2codedownloadstatuscode
        
        	The value indicates the result of the latest config file CVC verification, SNMP CVC verification, or code file verification
        	**type**\:  :py:class:`DocsIetfBpi2CodeDownloadStatusCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl.DocsIetfBpi2CodeDownloadStatusCode>`
        
        .. attribute:: docsietfbpi2codedownloadstatusstring
        
        	The value of this object indicates the additional information to the status code.  The value will include the error code and error description which will be defined separately
        	**type**\: str
        
        .. attribute:: docsietfbpi2codemfgorgname
        
        	The value of this object is the device manufacturer's organizationName
        	**type**\: str
        
        .. attribute:: docsietfbpi2codemfgcodeaccessstart
        
        	The value of this object is the device manufacturer's current codeAccessStart value. This value always be referenced to Greenwich Mean Time (GMT) and the value format must contain TimeZone information (fields 8\-10)
        	**type**\: str
        
        	**length:** 11
        
        .. attribute:: docsietfbpi2codemfgcvcaccessstart
        
        	The value of this object is the device manufacturer's current cvcAccessStart value. This value always be referenced to Greenwich Mean Time (GMT) and the value format must contain TimeZone information (fields 8\-10)
        	**type**\: str
        
        	**length:** 11
        
        .. attribute:: docsietfbpi2codecosignerorgname
        
        	The value of this object is the Co\-Signer's organizationName.  The value is a zero length string if the co\-signer is not specified
        	**type**\: str
        
        .. attribute:: docsietfbpi2codecosignercodeaccessstart
        
        	The value of this object is the Co\-Signer's current codeAccessStart value. This value always be referenced to Greenwich Mean Time (GMT) and the value format must contain TimeZone information (fields 8\-10). If docsIetfBpi2CodeCoSignerOrgName is a zero length string, the value of this object is meaningless
        	**type**\: str
        
        	**length:** 11
        
        .. attribute:: docsietfbpi2codecosignercvcaccessstart
        
        	The value of this object is the Co\-Signer's current cvcAccessStart value. This value always be referenced to Greenwich Mean Time (GMT) and the value format must contain TimeZone information (fields 8\-10). If docsIetfBpi2CodeCoSignerOrgName is a zero length string, the value of this object is meaningless
        	**type**\: str
        
        	**length:** 11
        
        .. attribute:: docsietfbpi2codecvcupdate
        
        	Setting a CVC to this object triggers the device to verify the CVC and update the cvcAccessStart values, then the content of this object is discarded.. If the device is not enabled to upgrade codefiles, or the CVC verification fails, the CVC will be rejected. Reading this object always returns the zero\-length OCTET STRING
        	**type**\: str
        
        	**length:** 0..4096
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl, self).__init__()

            self.yang_name = "docsIetfBpi2CodeDownloadControl"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsietfbpi2codedownloadstatuscode', (YLeaf(YType.enumeration, 'docsIetfBpi2CodeDownloadStatusCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CodeDownloadControl.DocsIetfBpi2CodeDownloadStatusCode')])),
                ('docsietfbpi2codedownloadstatusstring', (YLeaf(YType.str, 'docsIetfBpi2CodeDownloadStatusString'), ['str'])),
                ('docsietfbpi2codemfgorgname', (YLeaf(YType.str, 'docsIetfBpi2CodeMfgOrgName'), ['str'])),
                ('docsietfbpi2codemfgcodeaccessstart', (YLeaf(YType.str, 'docsIetfBpi2CodeMfgCodeAccessStart'), ['str'])),
                ('docsietfbpi2codemfgcvcaccessstart', (YLeaf(YType.str, 'docsIetfBpi2CodeMfgCvcAccessStart'), ['str'])),
                ('docsietfbpi2codecosignerorgname', (YLeaf(YType.str, 'docsIetfBpi2CodeCoSignerOrgName'), ['str'])),
                ('docsietfbpi2codecosignercodeaccessstart', (YLeaf(YType.str, 'docsIetfBpi2CodeCoSignerCodeAccessStart'), ['str'])),
                ('docsietfbpi2codecosignercvcaccessstart', (YLeaf(YType.str, 'docsIetfBpi2CodeCoSignerCvcAccessStart'), ['str'])),
                ('docsietfbpi2codecvcupdate', (YLeaf(YType.str, 'docsIetfBpi2CodeCvcUpdate'), ['str'])),
            ])
            self.docsietfbpi2codedownloadstatuscode = None
            self.docsietfbpi2codedownloadstatusstring = None
            self.docsietfbpi2codemfgorgname = None
            self.docsietfbpi2codemfgcodeaccessstart = None
            self.docsietfbpi2codemfgcvcaccessstart = None
            self.docsietfbpi2codecosignerorgname = None
            self.docsietfbpi2codecosignercodeaccessstart = None
            self.docsietfbpi2codecosignercvcaccessstart = None
            self.docsietfbpi2codecvcupdate = None
            self._segment_path = lambda: "docsIetfBpi2CodeDownloadControl"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CodeDownloadControl, [u'docsietfbpi2codedownloadstatuscode', u'docsietfbpi2codedownloadstatusstring', u'docsietfbpi2codemfgorgname', u'docsietfbpi2codemfgcodeaccessstart', u'docsietfbpi2codemfgcvcaccessstart', u'docsietfbpi2codecosignerorgname', u'docsietfbpi2codecosignercodeaccessstart', u'docsietfbpi2codecosignercvcaccessstart', u'docsietfbpi2codecvcupdate'], name, value)

        class DocsIetfBpi2CodeDownloadStatusCode(Enum):
            """
            DocsIetfBpi2CodeDownloadStatusCode (Enum Class)

            The value indicates the result of the latest config

            file CVC verification, SNMP CVC verification, or code file

            verification.

            .. data:: configFileCvcVerified = 1

            .. data:: configFileCvcRejected = 2

            .. data:: snmpCvcVerified = 3

            .. data:: snmpCvcRejected = 4

            .. data:: codeFileVerified = 5

            .. data:: codeFileRejected = 6

            .. data:: other = 7

            """

            configFileCvcVerified = Enum.YLeaf(1, "configFileCvcVerified")

            configFileCvcRejected = Enum.YLeaf(2, "configFileCvcRejected")

            snmpCvcVerified = Enum.YLeaf(3, "snmpCvcVerified")

            snmpCvcRejected = Enum.YLeaf(4, "snmpCvcRejected")

            codeFileVerified = Enum.YLeaf(5, "codeFileVerified")

            codeFileRejected = Enum.YLeaf(6, "codeFileRejected")

            other = Enum.YLeaf(7, "other")



    class DocsIetfBpi2CmBaseTable(Entity):
        """
        This table describes the basic and authorization
        related Baseline Privacy Plus attributes of each CM MAC
        interface.
        
        .. attribute:: docsietfbpi2cmbaseentry
        
        	Each entry contains objects describing attributes of one CM MAC interface. An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmBaseEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmBaseTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmBaseEntry", ("docsietfbpi2cmbaseentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmbaseentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmBaseTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable, [], name, value)


        class DocsIetfBpi2CmBaseEntry(Entity):
            """
            Each entry contains objects describing attributes of
            one CM MAC interface. An entry in this table exists for
            each ifEntry with an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmprivacyenable
            
            	This object identifies whether this CM is provisioned to run Baseline Privacy Plus
            	**type**\: bool
            
            .. attribute:: docsietfbpi2cmpublickey
            
            	The value of this object is a DER\-encoded RSAPublicKey ASN.1 type string, as defined in the RSA Encryption Standard (PKCS #1), corresponding to the public key of the CM
            	**type**\: str
            
            	**length:** 0..524
            
            .. attribute:: docsietfbpi2cmauthstate
            
            	The value of this object is the state of the CM authorization FSM.  The start state indicates that FSM is in its initial state
            	**type**\:  :py:class:`DocsIetfBpi2CmAuthState <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthState>`
            
            .. attribute:: docsietfbpi2cmauthkeysequencenumber
            
            	The value of this object is the most recent authorization key sequence number for this FSM
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: docsietfbpi2cmauthexpiresold
            
            	The value of this object is the actual clock time for expiration of the immediate predecessor of the most recent authorization key for this FSM.  If this FSM has only one authorization key, then the value is the time of activation of this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmauthexpiresnew
            
            	The value of this object is the actual clock time for expiration of the most recent authorization key for this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmauthreset
            
            	Setting this object to 'true' generates a Reauthorize event in the authorization FSM. Reading this object always returns FALSE. This object is for testing purposes only and therefore it does not require to be associated with a last reset object
            	**type**\: bool
            
            .. attribute:: docsietfbpi2cmauthgracetime
            
            	The value of this object is the grace time for an authorization key in seconds.  A CM is expected to start trying to get a new authorization key beginning AuthGraceTime seconds before the most recent authorization key actually expires
            	**type**\: int
            
            	**range:** 1..6047999
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmtekgracetime
            
            	The value of this object is the grace time for the TEK in seconds.  The CM is expected to start trying to acquire a new TEK beginning TEK GraceTime seconds before the expiration of the most recent TEK
            	**type**\: int
            
            	**range:** 1..302399
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmauthwaittimeout
            
            	The value of this object is the Authorize Wait Timeout in second
            	**type**\: int
            
            	**range:** 1..30
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmreauthwaittimeout
            
            	The value of this object is the Reauthorize Wait Timeout in seconds
            	**type**\: int
            
            	**range:** 1..30
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmopwaittimeout
            
            	The value of this object is the Operational Wait Timeout in seconds
            	**type**\: int
            
            	**range:** 1..10
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmrekeywaittimeout
            
            	The value of this object is the Rekey Wait Timeout in seconds
            	**type**\: int
            
            	**range:** 1..10
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmauthrejectwaittimeout
            
            	The value of this object is the Authorization Reject Wait Timeout in seconds
            	**type**\: int
            
            	**range:** 1..600
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmsamapwaittimeout
            
            	The value of this object is the retransmission interval, in seconds, of SA Map Requests from the MAP Wait state
            	**type**\: int
            
            	**range:** 1..10
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmsamapmaxretries
            
            	The value of this object is the maximum number of Map Request retries allowed
            	**type**\: int
            
            	**range:** 0..10
            
            	**units**\: count
            
            .. attribute:: docsietfbpi2cmauthentinfos
            
            	The value of this object is the count of times the CM has transmitted an Authentication Information message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmauthrequests
            
            	The value of this object is the count of times the CM has transmitted an Authorization Request message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmauthreplies
            
            	The value of this object is the count of times the CM has received an Authorization Reply message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmauthrejects
            
            	The value of this object is the count of times the CM has received an Authorization Reject message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmauthinvalids
            
            	The value of this object is the count of times the CM has received an Authorization Invalid message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmauthrejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent Authorization Reject message received by the CM.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Authorization Reject message has been received since reboot
            	**type**\:  :py:class:`DocsIetfBpi2CmAuthRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmauthrejecterrorstring
            
            	The value of this object is the text string in most recent Authorization Reject message received by the CM.  This is a zero length string if no Authorization Reject message has been received since reboot
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmauthinvaliderrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent Authorization Invalid message received by the CM.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Authorization Invalid message has been received since reboot
            	**type**\:  :py:class:`DocsIetfBpi2CmAuthInvalidErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthInvalidErrorCode>`
            
            .. attribute:: docsietfbpi2cmauthinvaliderrorstring
            
            	The value of this object is the text string in most recent Authorization Invalid message received by the CM. This is a zero length string if no Authorization Invalid message has been received since reboot
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmBaseEntry"
                self.yang_parent_name = "docsIetfBpi2CmBaseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmprivacyenable', (YLeaf(YType.boolean, 'docsIetfBpi2CmPrivacyEnable'), ['bool'])),
                    ('docsietfbpi2cmpublickey', (YLeaf(YType.str, 'docsIetfBpi2CmPublicKey'), ['str'])),
                    ('docsietfbpi2cmauthstate', (YLeaf(YType.enumeration, 'docsIetfBpi2CmAuthState'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthState')])),
                    ('docsietfbpi2cmauthkeysequencenumber', (YLeaf(YType.int32, 'docsIetfBpi2CmAuthKeySequenceNumber'), ['int'])),
                    ('docsietfbpi2cmauthexpiresold', (YLeaf(YType.str, 'docsIetfBpi2CmAuthExpiresOld'), ['str'])),
                    ('docsietfbpi2cmauthexpiresnew', (YLeaf(YType.str, 'docsIetfBpi2CmAuthExpiresNew'), ['str'])),
                    ('docsietfbpi2cmauthreset', (YLeaf(YType.boolean, 'docsIetfBpi2CmAuthReset'), ['bool'])),
                    ('docsietfbpi2cmauthgracetime', (YLeaf(YType.int32, 'docsIetfBpi2CmAuthGraceTime'), ['int'])),
                    ('docsietfbpi2cmtekgracetime', (YLeaf(YType.int32, 'docsIetfBpi2CmTEKGraceTime'), ['int'])),
                    ('docsietfbpi2cmauthwaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmAuthWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmreauthwaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmReauthWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmopwaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmOpWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmrekeywaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmRekeyWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmauthrejectwaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmAuthRejectWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmsamapwaittimeout', (YLeaf(YType.int32, 'docsIetfBpi2CmSAMapWaitTimeout'), ['int'])),
                    ('docsietfbpi2cmsamapmaxretries', (YLeaf(YType.int32, 'docsIetfBpi2CmSAMapMaxRetries'), ['int'])),
                    ('docsietfbpi2cmauthentinfos', (YLeaf(YType.uint32, 'docsIetfBpi2CmAuthentInfos'), ['int'])),
                    ('docsietfbpi2cmauthrequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmAuthRequests'), ['int'])),
                    ('docsietfbpi2cmauthreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmAuthReplies'), ['int'])),
                    ('docsietfbpi2cmauthrejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmAuthRejects'), ['int'])),
                    ('docsietfbpi2cmauthinvalids', (YLeaf(YType.uint32, 'docsIetfBpi2CmAuthInvalids'), ['int'])),
                    ('docsietfbpi2cmauthrejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmAuthRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthRejectErrorCode')])),
                    ('docsietfbpi2cmauthrejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmAuthRejectErrorString'), ['str'])),
                    ('docsietfbpi2cmauthinvaliderrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmAuthInvalidErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry.DocsIetfBpi2CmAuthInvalidErrorCode')])),
                    ('docsietfbpi2cmauthinvaliderrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmAuthInvalidErrorString'), ['str'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmprivacyenable = None
                self.docsietfbpi2cmpublickey = None
                self.docsietfbpi2cmauthstate = None
                self.docsietfbpi2cmauthkeysequencenumber = None
                self.docsietfbpi2cmauthexpiresold = None
                self.docsietfbpi2cmauthexpiresnew = None
                self.docsietfbpi2cmauthreset = None
                self.docsietfbpi2cmauthgracetime = None
                self.docsietfbpi2cmtekgracetime = None
                self.docsietfbpi2cmauthwaittimeout = None
                self.docsietfbpi2cmreauthwaittimeout = None
                self.docsietfbpi2cmopwaittimeout = None
                self.docsietfbpi2cmrekeywaittimeout = None
                self.docsietfbpi2cmauthrejectwaittimeout = None
                self.docsietfbpi2cmsamapwaittimeout = None
                self.docsietfbpi2cmsamapmaxretries = None
                self.docsietfbpi2cmauthentinfos = None
                self.docsietfbpi2cmauthrequests = None
                self.docsietfbpi2cmauthreplies = None
                self.docsietfbpi2cmauthrejects = None
                self.docsietfbpi2cmauthinvalids = None
                self.docsietfbpi2cmauthrejecterrorcode = None
                self.docsietfbpi2cmauthrejecterrorstring = None
                self.docsietfbpi2cmauthinvaliderrorcode = None
                self.docsietfbpi2cmauthinvaliderrorstring = None
                self._segment_path = lambda: "docsIetfBpi2CmBaseEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmBaseTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmBaseTable.DocsIetfBpi2CmBaseEntry, [u'ifindex', u'docsietfbpi2cmprivacyenable', u'docsietfbpi2cmpublickey', u'docsietfbpi2cmauthstate', u'docsietfbpi2cmauthkeysequencenumber', u'docsietfbpi2cmauthexpiresold', u'docsietfbpi2cmauthexpiresnew', u'docsietfbpi2cmauthreset', u'docsietfbpi2cmauthgracetime', u'docsietfbpi2cmtekgracetime', u'docsietfbpi2cmauthwaittimeout', u'docsietfbpi2cmreauthwaittimeout', u'docsietfbpi2cmopwaittimeout', u'docsietfbpi2cmrekeywaittimeout', u'docsietfbpi2cmauthrejectwaittimeout', u'docsietfbpi2cmsamapwaittimeout', u'docsietfbpi2cmsamapmaxretries', u'docsietfbpi2cmauthentinfos', u'docsietfbpi2cmauthrequests', u'docsietfbpi2cmauthreplies', u'docsietfbpi2cmauthrejects', u'docsietfbpi2cmauthinvalids', u'docsietfbpi2cmauthrejecterrorcode', u'docsietfbpi2cmauthrejecterrorstring', u'docsietfbpi2cmauthinvaliderrorcode', u'docsietfbpi2cmauthinvaliderrorstring'], name, value)

            class DocsIetfBpi2CmAuthInvalidErrorCode(Enum):
                """
                DocsIetfBpi2CmAuthInvalidErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent Authorization

                Invalid message received by the CM.  This has value

                unknown(2) if the last Error\-Code value was 0, and none(1)

                if no Authorization Invalid message has been received since

                reboot.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedCm = 3

                .. data:: unsolicited = 5

                .. data:: invalidKeySequence = 6

                .. data:: keyRequestAuthenticationFailure = 7

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedCm = Enum.YLeaf(3, "unauthorizedCm")

                unsolicited = Enum.YLeaf(5, "unsolicited")

                invalidKeySequence = Enum.YLeaf(6, "invalidKeySequence")

                keyRequestAuthenticationFailure = Enum.YLeaf(7, "keyRequestAuthenticationFailure")


            class DocsIetfBpi2CmAuthRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmAuthRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent Authorization

                Reject message received by the CM.  This has value

                unknown(2) if the last Error\-Code value was 0, and none(1)

                if no Authorization Reject message has been received since

                reboot.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedCm = 3

                .. data:: unauthorizedSaid = 4

                .. data:: permanentAuthorizationFailure = 8

                .. data:: timeOfDayNotAcquired = 11

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedCm = Enum.YLeaf(3, "unauthorizedCm")

                unauthorizedSaid = Enum.YLeaf(4, "unauthorizedSaid")

                permanentAuthorizationFailure = Enum.YLeaf(8, "permanentAuthorizationFailure")

                timeOfDayNotAcquired = Enum.YLeaf(11, "timeOfDayNotAcquired")


            class DocsIetfBpi2CmAuthState(Enum):
                """
                DocsIetfBpi2CmAuthState (Enum Class)

                The value of this object is the state of the CM

                authorization FSM.  The start state indicates that FSM is

                in its initial state.

                .. data:: start = 1

                .. data:: authWait = 2

                .. data:: authorized = 3

                .. data:: reauthWait = 4

                .. data:: authRejectWait = 5

                .. data:: silent = 6

                """

                start = Enum.YLeaf(1, "start")

                authWait = Enum.YLeaf(2, "authWait")

                authorized = Enum.YLeaf(3, "authorized")

                reauthWait = Enum.YLeaf(4, "reauthWait")

                authRejectWait = Enum.YLeaf(5, "authRejectWait")

                silent = Enum.YLeaf(6, "silent")



    class DocsIetfBpi2CmTEKTable(Entity):
        """
        This table describes the attributes of each CM
        Traffic Encryption Key (TEK) association. The CM maintains
        (no more than) one TEK association per SAID per CM MAC
        interface.
        
        .. attribute:: docsietfbpi2cmtekentry
        
        	Each entry contains objects describing the TEK association attributes of one SAID. The CM MUST create one entry per SAID, regardless of whether the SAID was obtained from a Registration Response message, from an Authorization Reply message, or from any dynamic SAID establishment mechanisms
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmTEKEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmTEKTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmTEKEntry", ("docsietfbpi2cmtekentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtekentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmTEKTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable, [], name, value)


        class DocsIetfBpi2CmTEKEntry(Entity):
            """
            Each entry contains objects describing the TEK
            association attributes of one SAID. The CM MUST create one
            entry per SAID, regardless of whether the SAID was obtained
            from a Registration Response message, from an Authorization
            Reply message, or from any dynamic SAID establishment
            mechanisms.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmteksaid  (key)
            
            	The value of this object is the DOCSIS Security Association ID (SAID)
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsietfbpi2cmteksatype
            
            	The value of this object is the type of security association
            	**type**\:  :py:class:`DocsBpkmSAType <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmSAType>`
            
            .. attribute:: docsietfbpi2cmtekdataencryptalg
            
            	The value of this object is the data encryption algorithm for this SAID
            	**type**\:  :py:class:`DocsBpkmDataEncryptAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataEncryptAlg>`
            
            .. attribute:: docsietfbpi2cmtekdataauthentalg
            
            	The value of this object is the data authentication algorithm for this SAID
            	**type**\:  :py:class:`DocsBpkmDataAuthentAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataAuthentAlg>`
            
            .. attribute:: docsietfbpi2cmtekstate
            
            	The value of this object is the state of the indicated TEK FSM.  The start(1) state indicates that FSM is in its initial state
            	**type**\:  :py:class:`DocsIetfBpi2CmTEKState <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKState>`
            
            .. attribute:: docsietfbpi2cmtekkeysequencenumber
            
            	The value of this object is the most recent TEK key sequence number for this TEK FSM
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: docsietfbpi2cmtekexpiresold
            
            	The value of this object is the actual clock time for expiration of the immediate predecessor of the most recent TEK for this FSM.  If this FSM has only one TEK, then the value is the time of activation of this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtekexpiresnew
            
            	The value of this object is the actual clock time for expiration of the most recent TEK for this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtekkeyrequests
            
            	The value of this object is the count of times the CM has transmitted a Key Request message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtekkeyreplies
            
            	The value of this object is the count of times the CM has received a Key Reply message, including a message whose authentication failed. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtekkeyrejects
            
            	The value of this object is the count of times the CM has received a Key Reject message, including a message whose authentication failed. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtekinvalids
            
            	The value of this object is the count of times the CM has received a TEK Invalid message, including a message whose authentication failed. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtekauthpends
            
            	The value of this object is the count of times an Authorization Pending (Auth Pend) event occurred in this FSM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtekkeyrejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent Key Reject message received by the CM. This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Key Reject message has been received since registration
            	**type**\:  :py:class:`DocsIetfBpi2CmTEKKeyRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKKeyRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmtekkeyrejecterrorstring
            
            	The value of this object is the text string in most recent Key Reject message received by the CM. This is a zero length string if no Key Reject message has been received since registration
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmtekinvaliderrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent TEK Invalid message received by the CM.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no TEK Invalid message has been received since registration
            	**type**\:  :py:class:`DocsIetfBpi2CmTEKInvalidErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKInvalidErrorCode>`
            
            .. attribute:: docsietfbpi2cmtekinvaliderrorstring
            
            	The value of this object is the text string in most recent TEK Invalid message received by the CM. This is a zero length string if no TEK Invalid message has been received since registration
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmTEKEntry"
                self.yang_parent_name = "docsIetfBpi2CmTEKTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmteksaid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmteksaid', (YLeaf(YType.int32, 'docsIetfBpi2CmTEKSAId'), ['int'])),
                    ('docsietfbpi2cmteksatype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKSAType'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmSAType', '')])),
                    ('docsietfbpi2cmtekdataencryptalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKDataEncryptAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataEncryptAlg', '')])),
                    ('docsietfbpi2cmtekdataauthentalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKDataAuthentAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataAuthentAlg', '')])),
                    ('docsietfbpi2cmtekstate', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKState'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKState')])),
                    ('docsietfbpi2cmtekkeysequencenumber', (YLeaf(YType.int32, 'docsIetfBpi2CmTEKKeySequenceNumber'), ['int'])),
                    ('docsietfbpi2cmtekexpiresold', (YLeaf(YType.str, 'docsIetfBpi2CmTEKExpiresOld'), ['str'])),
                    ('docsietfbpi2cmtekexpiresnew', (YLeaf(YType.str, 'docsIetfBpi2CmTEKExpiresNew'), ['str'])),
                    ('docsietfbpi2cmtekkeyrequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmTEKKeyRequests'), ['int'])),
                    ('docsietfbpi2cmtekkeyreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmTEKKeyReplies'), ['int'])),
                    ('docsietfbpi2cmtekkeyrejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmTEKKeyRejects'), ['int'])),
                    ('docsietfbpi2cmtekinvalids', (YLeaf(YType.uint32, 'docsIetfBpi2CmTEKInvalids'), ['int'])),
                    ('docsietfbpi2cmtekauthpends', (YLeaf(YType.uint32, 'docsIetfBpi2CmTEKAuthPends'), ['int'])),
                    ('docsietfbpi2cmtekkeyrejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKKeyRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKKeyRejectErrorCode')])),
                    ('docsietfbpi2cmtekkeyrejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmTEKKeyRejectErrorString'), ['str'])),
                    ('docsietfbpi2cmtekinvaliderrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmTEKInvalidErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry.DocsIetfBpi2CmTEKInvalidErrorCode')])),
                    ('docsietfbpi2cmtekinvaliderrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmTEKInvalidErrorString'), ['str'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmteksaid = None
                self.docsietfbpi2cmteksatype = None
                self.docsietfbpi2cmtekdataencryptalg = None
                self.docsietfbpi2cmtekdataauthentalg = None
                self.docsietfbpi2cmtekstate = None
                self.docsietfbpi2cmtekkeysequencenumber = None
                self.docsietfbpi2cmtekexpiresold = None
                self.docsietfbpi2cmtekexpiresnew = None
                self.docsietfbpi2cmtekkeyrequests = None
                self.docsietfbpi2cmtekkeyreplies = None
                self.docsietfbpi2cmtekkeyrejects = None
                self.docsietfbpi2cmtekinvalids = None
                self.docsietfbpi2cmtekauthpends = None
                self.docsietfbpi2cmtekkeyrejecterrorcode = None
                self.docsietfbpi2cmtekkeyrejecterrorstring = None
                self.docsietfbpi2cmtekinvaliderrorcode = None
                self.docsietfbpi2cmtekinvaliderrorstring = None
                self._segment_path = lambda: "docsIetfBpi2CmTEKEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmTEKSAId='" + str(self.docsietfbpi2cmteksaid) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmTEKTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmTEKTable.DocsIetfBpi2CmTEKEntry, [u'ifindex', u'docsietfbpi2cmteksaid', u'docsietfbpi2cmteksatype', u'docsietfbpi2cmtekdataencryptalg', u'docsietfbpi2cmtekdataauthentalg', u'docsietfbpi2cmtekstate', u'docsietfbpi2cmtekkeysequencenumber', u'docsietfbpi2cmtekexpiresold', u'docsietfbpi2cmtekexpiresnew', u'docsietfbpi2cmtekkeyrequests', u'docsietfbpi2cmtekkeyreplies', u'docsietfbpi2cmtekkeyrejects', u'docsietfbpi2cmtekinvalids', u'docsietfbpi2cmtekauthpends', u'docsietfbpi2cmtekkeyrejecterrorcode', u'docsietfbpi2cmtekkeyrejecterrorstring', u'docsietfbpi2cmtekinvaliderrorcode', u'docsietfbpi2cmtekinvaliderrorstring'], name, value)

            class DocsIetfBpi2CmTEKInvalidErrorCode(Enum):
                """
                DocsIetfBpi2CmTEKInvalidErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent TEK Invalid

                message received by the CM.  This has value unknown(2) if

                the last Error\-Code value was 0, and none(1) if no TEK

                Invalid message has been received since registration.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: invalidKeySequence = 6

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                invalidKeySequence = Enum.YLeaf(6, "invalidKeySequence")


            class DocsIetfBpi2CmTEKKeyRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmTEKKeyRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent Key Reject

                message received by the CM. This has value unknown(2) if

                the last Error\-Code value was 0, and none(1) if no Key

                Reject message has been received since registration.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedSaid = 4

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedSaid = Enum.YLeaf(4, "unauthorizedSaid")


            class DocsIetfBpi2CmTEKState(Enum):
                """
                DocsIetfBpi2CmTEKState (Enum Class)

                The value of this object is the state of the

                indicated TEK FSM.  The start(1) state indicates that FSM

                is in its initial state.

                .. data:: start = 1

                .. data:: opWait = 2

                .. data:: opReauthWait = 3

                .. data:: operational = 4

                .. data:: rekeyWait = 5

                .. data:: rekeyReauthWait = 6

                """

                start = Enum.YLeaf(1, "start")

                opWait = Enum.YLeaf(2, "opWait")

                opReauthWait = Enum.YLeaf(3, "opReauthWait")

                operational = Enum.YLeaf(4, "operational")

                rekeyWait = Enum.YLeaf(5, "rekeyWait")

                rekeyReauthWait = Enum.YLeaf(6, "rekeyReauthWait")



    class DocsIetfBpi2CmIpMulticastMapTable(Entity):
        """
        This table maps multicast IP addresses to SAIDs per
        CM MAC Interface.
        It is intended to map multicast IP addresses associated
        with SA MAP Request messages.
        
        .. attribute:: docsietfbpi2cmipmulticastmapentry
        
        	Each entry contains objects describing the mapping of one multicast IP address to one SAID, as well as associated state, message counters, and error information.  An entry may be removed from this table upon the reception of an SA Map Reject
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmIpMulticastMapEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmIpMulticastMapTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmIpMulticastMapEntry", ("docsietfbpi2cmipmulticastmapentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmipmulticastmapentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmIpMulticastMapTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable, [], name, value)


        class DocsIetfBpi2CmIpMulticastMapEntry(Entity):
            """
            Each entry contains objects describing the mapping of
            one multicast IP address to one SAID, as well as
            associated state, message counters, and error information.
            
            An entry may be removed from this table upon the reception
            of an SA Map Reject.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmipmulticastindex  (key)
            
            	The index of this row
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsietfbpi2cmipmulticastaddresstype
            
            	The type of internet address for docsIetfBpi2CmIpMulticastAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsietfbpi2cmipmulticastaddress
            
            	This object represents the IP multicast address to be mapped. The type of this address is determined by the value of the docsIetfBpi2CmIpMulticastAddressType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsietfbpi2cmipmulticastsaid
            
            	This object represents the SAID to which the IP multicast address has been mapped.  If no SA Map Reply has been received for the IP address, this object should have the value 0
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsietfbpi2cmipmulticastsamapstate
            
            	The value of this object is the state of the SA Mapping FSM for this IP
            	**type**\:  :py:class:`DocsIetfBpi2CmIpMulticastSAMapState <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry.DocsIetfBpi2CmIpMulticastSAMapState>`
            
            .. attribute:: docsietfbpi2cmipmulticastsamaprequests
            
            	The value of this object is the count of times the CM has transmitted an SA Map Request message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmipmulticastsamapreplies
            
            	The value of this object is the count of times the CM has received an SA Map Reply message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmipmulticastsamaprejects
            
            	The value of this object is the count of times the CM has received an SA MAP Reject message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmipmulticastsamaprejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in the most recent SA Map Reject message sent in response to an SA Map Request for This IP.  It has the value none(1) if no SA MAP Reject message has been received since entry creation
            	**type**\:  :py:class:`DocsIetfBpi2CmIpMulticastSAMapRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry.DocsIetfBpi2CmIpMulticastSAMapRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmipmulticastsamaprejecterrorstring
            
            	The value of this object is the text string in the most recent SA Map Reject message sent in response to an SA Map Request for this IP.  It is a zero length string if no SA Map Reject message has been received since entry creation
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmIpMulticastMapEntry"
                self.yang_parent_name = "docsIetfBpi2CmIpMulticastMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmipmulticastindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmipmulticastindex', (YLeaf(YType.uint32, 'docsIetfBpi2CmIpMulticastIndex'), ['int'])),
                    ('docsietfbpi2cmipmulticastaddresstype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmIpMulticastAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsietfbpi2cmipmulticastaddress', (YLeaf(YType.str, 'docsIetfBpi2CmIpMulticastAddress'), ['str'])),
                    ('docsietfbpi2cmipmulticastsaid', (YLeaf(YType.uint32, 'docsIetfBpi2CmIpMulticastSAId'), ['int'])),
                    ('docsietfbpi2cmipmulticastsamapstate', (YLeaf(YType.enumeration, 'docsIetfBpi2CmIpMulticastSAMapState'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry.DocsIetfBpi2CmIpMulticastSAMapState')])),
                    ('docsietfbpi2cmipmulticastsamaprequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmIpMulticastSAMapRequests'), ['int'])),
                    ('docsietfbpi2cmipmulticastsamapreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmIpMulticastSAMapReplies'), ['int'])),
                    ('docsietfbpi2cmipmulticastsamaprejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmIpMulticastSAMapRejects'), ['int'])),
                    ('docsietfbpi2cmipmulticastsamaprejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmIpMulticastSAMapRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry.DocsIetfBpi2CmIpMulticastSAMapRejectErrorCode')])),
                    ('docsietfbpi2cmipmulticastsamaprejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmIpMulticastSAMapRejectErrorString'), ['str'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmipmulticastindex = None
                self.docsietfbpi2cmipmulticastaddresstype = None
                self.docsietfbpi2cmipmulticastaddress = None
                self.docsietfbpi2cmipmulticastsaid = None
                self.docsietfbpi2cmipmulticastsamapstate = None
                self.docsietfbpi2cmipmulticastsamaprequests = None
                self.docsietfbpi2cmipmulticastsamapreplies = None
                self.docsietfbpi2cmipmulticastsamaprejects = None
                self.docsietfbpi2cmipmulticastsamaprejecterrorcode = None
                self.docsietfbpi2cmipmulticastsamaprejecterrorstring = None
                self._segment_path = lambda: "docsIetfBpi2CmIpMulticastMapEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmIpMulticastIndex='" + str(self.docsietfbpi2cmipmulticastindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmIpMulticastMapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmIpMulticastMapTable.DocsIetfBpi2CmIpMulticastMapEntry, [u'ifindex', u'docsietfbpi2cmipmulticastindex', u'docsietfbpi2cmipmulticastaddresstype', u'docsietfbpi2cmipmulticastaddress', u'docsietfbpi2cmipmulticastsaid', u'docsietfbpi2cmipmulticastsamapstate', u'docsietfbpi2cmipmulticastsamaprequests', u'docsietfbpi2cmipmulticastsamapreplies', u'docsietfbpi2cmipmulticastsamaprejects', u'docsietfbpi2cmipmulticastsamaprejecterrorcode', u'docsietfbpi2cmipmulticastsamaprejecterrorstring'], name, value)

            class DocsIetfBpi2CmIpMulticastSAMapRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmIpMulticastSAMapRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in the most recent SA Map

                Reject message sent in response to an SA Map Request for

                This IP.  It has the value none(1) if no SA MAP Reject

                message has been received since entry creation.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: noAuthForRequestedDSFlow = 9

                .. data:: dsFlowNotMappedToSA = 10

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                noAuthForRequestedDSFlow = Enum.YLeaf(9, "noAuthForRequestedDSFlow")

                dsFlowNotMappedToSA = Enum.YLeaf(10, "dsFlowNotMappedToSA")


            class DocsIetfBpi2CmIpMulticastSAMapState(Enum):
                """
                DocsIetfBpi2CmIpMulticastSAMapState (Enum Class)

                The value of this object is the state of the SA

                Mapping FSM for this IP.

                .. data:: start = 1

                .. data:: mapWait = 2

                .. data:: mapped = 3

                """

                start = Enum.YLeaf(1, "start")

                mapWait = Enum.YLeaf(2, "mapWait")

                mapped = Enum.YLeaf(3, "mapped")



    class DocsIetfBpi2CmDeviceCertTable(Entity):
        """
        This table describes the Baseline Privacy Plus
        device certificates for each CM MAC interface.
        
        .. attribute:: docsietfbpi2cmdevicecertentry
        
        	Each entry contains the device certificates of one CM MAC interface.  An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmDeviceCertEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable.DocsIetfBpi2CmDeviceCertEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmDeviceCertTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmDeviceCertEntry", ("docsietfbpi2cmdevicecertentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable.DocsIetfBpi2CmDeviceCertEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmdevicecertentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmDeviceCertTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable, [], name, value)


        class DocsIetfBpi2CmDeviceCertEntry(Entity):
            """
            Each entry contains the device certificates of
            one CM MAC interface.  An entry in this table exists for
            each ifEntry with an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmdevicecmcert
            
            	The X509 DER\-encoded cable modem certificate. Note\:  This object can be set only when the value is the zero\-length OCTET STRING, otherwise an error 'inconsistentValue' is returned.  Once the object contains  the certificate, its access MUST be read\-only and persists after re\-initialization of the managed system
            	**type**\: str
            
            	**length:** 0..4096
            
            .. attribute:: docsietfbpi2cmdevicemanufcert
            
            	The X509 DER\-encoded manufacturer certificate which signed the cable modem certificate
            	**type**\: str
            
            	**length:** 0..4096
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable.DocsIetfBpi2CmDeviceCertEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmDeviceCertEntry"
                self.yang_parent_name = "docsIetfBpi2CmDeviceCertTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmdevicecmcert', (YLeaf(YType.str, 'docsIetfBpi2CmDeviceCmCert'), ['str'])),
                    ('docsietfbpi2cmdevicemanufcert', (YLeaf(YType.str, 'docsIetfBpi2CmDeviceManufCert'), ['str'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmdevicecmcert = None
                self.docsietfbpi2cmdevicemanufcert = None
                self._segment_path = lambda: "docsIetfBpi2CmDeviceCertEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmDeviceCertTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmDeviceCertTable.DocsIetfBpi2CmDeviceCertEntry, [u'ifindex', u'docsietfbpi2cmdevicecmcert', u'docsietfbpi2cmdevicemanufcert'], name, value)


    class DocsIetfBpi2CmCryptoSuiteTable(Entity):
        """
        This table describes the Baseline Privacy Plus
        cryptographic suite capabilities for each CM MAC
        interface.
        
        .. attribute:: docsietfbpi2cmcryptosuiteentry
        
        	Each entry contains a cryptographic suite pair which this CM MAC supports
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmCryptoSuiteEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable.DocsIetfBpi2CmCryptoSuiteEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmCryptoSuiteTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmCryptoSuiteEntry", ("docsietfbpi2cmcryptosuiteentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable.DocsIetfBpi2CmCryptoSuiteEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmcryptosuiteentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmCryptoSuiteTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable, [], name, value)


        class DocsIetfBpi2CmCryptoSuiteEntry(Entity):
            """
            Each entry contains a cryptographic suite pair
            which this CM MAC supports.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmcryptosuiteindex  (key)
            
            	The index for a cryptographic suite row
            	**type**\: int
            
            	**range:** 1..1000
            
            .. attribute:: docsietfbpi2cmcryptosuitedataencryptalg
            
            	The value of this object is the data encryption algorithm for this cryptographic suite capability
            	**type**\:  :py:class:`DocsBpkmDataEncryptAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataEncryptAlg>`
            
            .. attribute:: docsietfbpi2cmcryptosuitedataauthentalg
            
            	The value of this object is the data authentication algorithm for this cryptographic suite capability
            	**type**\:  :py:class:`DocsBpkmDataAuthentAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataAuthentAlg>`
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable.DocsIetfBpi2CmCryptoSuiteEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmCryptoSuiteEntry"
                self.yang_parent_name = "docsIetfBpi2CmCryptoSuiteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmcryptosuiteindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmcryptosuiteindex', (YLeaf(YType.uint32, 'docsIetfBpi2CmCryptoSuiteIndex'), ['int'])),
                    ('docsietfbpi2cmcryptosuitedataencryptalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmCryptoSuiteDataEncryptAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataEncryptAlg', '')])),
                    ('docsietfbpi2cmcryptosuitedataauthentalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmCryptoSuiteDataAuthentAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataAuthentAlg', '')])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmcryptosuiteindex = None
                self.docsietfbpi2cmcryptosuitedataencryptalg = None
                self.docsietfbpi2cmcryptosuitedataauthentalg = None
                self._segment_path = lambda: "docsIetfBpi2CmCryptoSuiteEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmCryptoSuiteIndex='" + str(self.docsietfbpi2cmcryptosuiteindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmCryptoSuiteTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmCryptoSuiteTable.DocsIetfBpi2CmCryptoSuiteEntry, [u'ifindex', u'docsietfbpi2cmcryptosuiteindex', u'docsietfbpi2cmcryptosuitedataencryptalg', u'docsietfbpi2cmcryptosuitedataauthentalg'], name, value)


    class DocsIetfBpi2CmtsBaseTable(Entity):
        """
        This table describes the basic Baseline Privacy
        attributes of each CMTS MAC interface.
        
        .. attribute:: docsietfbpi2cmtsbaseentry
        
        	Each entry contains objects describing attributes of one CMTS MAC interface.  An entry in this table exists for each ifEntry with an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsBaseEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsBaseTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsBaseEntry", ("docsietfbpi2cmtsbaseentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtsbaseentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsBaseTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable, [], name, value)


        class DocsIetfBpi2CmtsBaseEntry(Entity):
            """
            Each entry contains objects describing attributes of
            one CMTS MAC interface.  An entry in this table exists for
            each ifEntry with an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmtsdefaultauthlifetime
            
            	The value of this object is the default lifetime, in seconds, the CMTS assigns to a new authorization key. This object value persist after re\-initialization of the managed system
            	**type**\: int
            
            	**range:** 1..6048000
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmtsdefaultteklifetime
            
            	The value of this object is the default lifetime, in seconds, the CMTS assigns to a new Traffic Encryption Key (TEK). This object value persist after re\-initialization of the managed system
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmtsdefaultselfsignedmanufcerttrust
            
            	This object determines the default trust of self\-signed  manufacturer certificate entries, contained in docsIetfBpi2CmtsCACertTable, created after setting this object. This object needs not to persist after re\-initialization  of the managed system
            	**type**\:  :py:class:`DocsIetfBpi2CmtsDefaultSelfSignedManufCertTrust <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry.DocsIetfBpi2CmtsDefaultSelfSignedManufCertTrust>`
            
            .. attribute:: docsietfbpi2cmtscheckcertvalidityperiods
            
            	Setting this object to 'true' causes all chained and root certificates in the chain to have their validity periods checked against the current time of day, when the CMTS receives an Authorization Request from the CM. A 'false' setting causes all certificates in the chain not to have their validity periods checked against the current time of day. This object needs not to persist after re\-initialization  of the managed system
            	**type**\: bool
            
            .. attribute:: docsietfbpi2cmtsauthentinfos
            
            	The value of this object is the count of times the CMTS has received an Authentication Information message from any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthrequests
            
            	The value of this object is the count of times the CMTS has received an Authorization Request message from any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthreplies
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Reply message to any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthrejects
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Reject message to any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthinvalids
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Invalid message to any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtssamaprequests
            
            	The value of this object is the count of times the CMTS has received an SA Map Request message from any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtssamapreplies
            
            	The value of this object is the count of times the CMTS has transmitted an SA Map Reply message to any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtssamaprejects
            
            	The value of this object is the count of times the CMTS has transmitted an SA Map Reject message to any CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsBaseEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsBaseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmtsdefaultauthlifetime', (YLeaf(YType.int32, 'docsIetfBpi2CmtsDefaultAuthLifetime'), ['int'])),
                    ('docsietfbpi2cmtsdefaultteklifetime', (YLeaf(YType.int32, 'docsIetfBpi2CmtsDefaultTEKLifetime'), ['int'])),
                    ('docsietfbpi2cmtsdefaultselfsignedmanufcerttrust', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsDefaultSelfSignedManufCertTrust'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry.DocsIetfBpi2CmtsDefaultSelfSignedManufCertTrust')])),
                    ('docsietfbpi2cmtscheckcertvalidityperiods', (YLeaf(YType.boolean, 'docsIetfBpi2CmtsCheckCertValidityPeriods'), ['bool'])),
                    ('docsietfbpi2cmtsauthentinfos', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthentInfos'), ['int'])),
                    ('docsietfbpi2cmtsauthrequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthRequests'), ['int'])),
                    ('docsietfbpi2cmtsauthreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthReplies'), ['int'])),
                    ('docsietfbpi2cmtsauthrejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthRejects'), ['int'])),
                    ('docsietfbpi2cmtsauthinvalids', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthInvalids'), ['int'])),
                    ('docsietfbpi2cmtssamaprequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsSAMapRequests'), ['int'])),
                    ('docsietfbpi2cmtssamapreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsSAMapReplies'), ['int'])),
                    ('docsietfbpi2cmtssamaprejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsSAMapRejects'), ['int'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmtsdefaultauthlifetime = None
                self.docsietfbpi2cmtsdefaultteklifetime = None
                self.docsietfbpi2cmtsdefaultselfsignedmanufcerttrust = None
                self.docsietfbpi2cmtscheckcertvalidityperiods = None
                self.docsietfbpi2cmtsauthentinfos = None
                self.docsietfbpi2cmtsauthrequests = None
                self.docsietfbpi2cmtsauthreplies = None
                self.docsietfbpi2cmtsauthrejects = None
                self.docsietfbpi2cmtsauthinvalids = None
                self.docsietfbpi2cmtssamaprequests = None
                self.docsietfbpi2cmtssamapreplies = None
                self.docsietfbpi2cmtssamaprejects = None
                self._segment_path = lambda: "docsIetfBpi2CmtsBaseEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsBaseTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsBaseTable.DocsIetfBpi2CmtsBaseEntry, [u'ifindex', u'docsietfbpi2cmtsdefaultauthlifetime', u'docsietfbpi2cmtsdefaultteklifetime', u'docsietfbpi2cmtsdefaultselfsignedmanufcerttrust', u'docsietfbpi2cmtscheckcertvalidityperiods', u'docsietfbpi2cmtsauthentinfos', u'docsietfbpi2cmtsauthrequests', u'docsietfbpi2cmtsauthreplies', u'docsietfbpi2cmtsauthrejects', u'docsietfbpi2cmtsauthinvalids', u'docsietfbpi2cmtssamaprequests', u'docsietfbpi2cmtssamapreplies', u'docsietfbpi2cmtssamaprejects'], name, value)

            class DocsIetfBpi2CmtsDefaultSelfSignedManufCertTrust(Enum):
                """
                DocsIetfBpi2CmtsDefaultSelfSignedManufCertTrust (Enum Class)

                This object determines the default trust of

                self\-signed  manufacturer certificate entries, contained

                in docsIetfBpi2CmtsCACertTable, created after setting this

                object.

                This object needs not to persist after re\-initialization

                 of the managed system.

                .. data:: trusted = 1

                .. data:: untrusted = 2

                """

                trusted = Enum.YLeaf(1, "trusted")

                untrusted = Enum.YLeaf(2, "untrusted")



    class DocsIetfBpi2CmtsAuthTable(Entity):
        """
        This table describes the attributes of each CM
        authorization association. The CMTS maintains one
        authorization association with each Baseline Privacy\-
        enabled CM, registered on each CMTS MAC interface,
        regardless of whether the CM is authorized or rejected.
        
        .. attribute:: docsietfbpi2cmtsauthentry
        
        	Each entry contains objects describing attributes of one authorization association. The CMTS MUST create one entry per CM per MAC interface, based on the receipt of an Authorization Request message, and MUST not delete the entry until the CM loses registration
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsAuthEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsAuthTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsAuthEntry", ("docsietfbpi2cmtsauthentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtsauthentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsAuthTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable, [], name, value)


        class DocsIetfBpi2CmtsAuthEntry(Entity):
            """
            Each entry contains objects describing attributes of
            one authorization association. The CMTS MUST create one
            entry per CM per MAC interface, based on the receipt of an
            Authorization Request message, and MUST not delete the
            entry until the CM loses registration.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmtsauthcmmacaddress  (key)
            
            	The value of this object is the physical address of the CM to which the authorization association applies
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsietfbpi2cmtsauthcmbpiversion
            
            	The value of this object is the version of Baseline Privacy for which this CM has registered. The value 'bpiplus' represents the value of BPI\-Version Attribute of the Baseline Privacy Key Management BPKM attribute BPI\-Version (1). The value 'bpi' is used to represent the CM registered using DOCSIS 1.0 Baseline Privacy
            	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthCmBpiVersion <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthCmBpiVersion>`
            
            .. attribute:: docsietfbpi2cmtsauthcmpublickey
            
            	The value of this object is a DER\-encoded RSAPublicKey ASN.1 type string, as defined in the RSA Encryption Standard (PKCS #1), corresponding to the public key of the CM.  This is the zero\-length OCTET STRING if the CMTS does not retain the public key
            	**type**\: str
            
            	**length:** 0..524
            
            .. attribute:: docsietfbpi2cmtsauthcmkeysequencenumber
            
            	The value of this object is the most recent authorization key sequence number for this CM
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: docsietfbpi2cmtsauthcmexpiresold
            
            	The value of this object is the actual clock time for expiration of the immediate predecessor of the most recent authorization key for this FSM. If this FSM has only one authorization key, then the value is the time of activation of this FSM. Note\: This object has no meaning for CMs running in BPI mode, therefore this object is not instantiated for entries associated to those CMs
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtsauthcmexpiresnew
            
            	The value of this object is the actual clock time for expiration of the most recent authorization key for this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtsauthcmlifetime
            
            	The value of this object is the lifetime, in seconds, the CMTS assigns to an authorization key for this CM
            	**type**\: int
            
            	**range:** 1..6048000
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmtsauthcmreset
            
            	Setting this object to invalidateAuth(2) causes the CMTS to invalidate the current CM authorization key(s), but not to transmit an Authorization Invalid message nor to invalidate the primary SAID's TEKs.  Setting this object to sendAuthInvalid(3) causes the CMTS to invalidate the current CM authorization key(s), and to transmit an Authorization Invalid message to the CM, but not to invalidate the primary SAID's TEKs.  Setting this object to invalidateTeks(4) causes the CMTS to invalidate the current CM authorization key(s), to transmit an Authorization Invalid message to the CM, and to invalidate the TEKs associated with this CM's primary SAID. For BPI mode, substitute all of the CM's unicast TEK(s) for the primary SAID's TEKs in the previous paragraph. Reading this object returns the most recently set value of this object, or returns noResetRequested(1) if the object has not been set since entry creation
            	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthCmReset <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthCmReset>`
            
            .. attribute:: docsietfbpi2cmtsauthcminfos
            
            	The value of this object is the count of times the CMTS has received an Authentication Information message from this CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthcmrequests
            
            	The value of this object is the count of times the CMTS has received an Authorization Request message from this CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthcmreplies
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Reply message to this CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthcmrejects
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Reject message to this CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthcminvalids
            
            	The value of this object is the count of times the CMTS has transmitted an Authorization Invalid message to this CM. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsauthrejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent Authorization Reject message transmitted to the CM.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Authorization Reject message has been transmitted to the CM, since entry creation
            	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmtsauthrejecterrorstring
            
            	The value of this object is the text string in most recent Authorization Reject message transmitted to the CM.  This is a zero length string if no Authorization Reject message has been transmitted to the CM, since entry creation
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmtsauthinvaliderrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in most recent Authorization Invalid message transmitted to the CM.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Authorization Invalid message has been transmitted to the CM since entry creation
            	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthInvalidErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthInvalidErrorCode>`
            
            .. attribute:: docsietfbpi2cmtsauthinvaliderrorstring
            
            	The value of this object is the text string in most recent Authorization Invalid message transmitted to the CM.  This is a zero length string if no Authorization Invalid message has been transmitted to the CM since entry creation
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmtsauthprimarysaid
            
            	The value of this object is the Primary Security Association identifier.  For BPI mode, the value must be any unicast SID
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsietfbpi2cmtsauthbpkmcmcertvalid
            
            	Contains the reason why a CM's certificate is deemed valid or invalid. Return unknown(0) if the CM is running BPI mode. ValidCmChained(1) means the certificate is valid    because it chains to a valid certificate. ValidCmTrusted(2) means the certificate is valid    because it has been provisioned (in the    docsIetfBpi2CmtsProvisionedCmCert table) to be trusted. InvalidCmUntrusted(3) means the certificate is invalid      because it has been provisioned (in the      docsIetfBpi2CmtsProvisionedCmCert table) to be untrusted. InvalidCAUntrusted(4) means the certificate is invalid      because it chains to an untrusted certificate. InvalidCmOther(5) and InvalidCAOther(6) refer to      errors in parsing, validity periods, etc, which are      attributable to the CM certificate or its chain      respectively; additional information may be found      in docsIetfBpi2AuthRejectErrorString for these types      of errors. InvalidCmRevoked(7) means the certificate is    invalid as it was marked as revoked.  InvalidCARevoked(8) means the CA certificate is    invalid as it was marked as revoked
            	**type**\:  :py:class:`DocsIetfBpi2CmtsAuthBpkmCmCertValid <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthBpkmCmCertValid>`
            
            .. attribute:: docsietfbpi2cmtsauthbpkmcmcert
            
            	The X509 CM Certificate sent as part of a BPKM Authorization Request. Note\: The zero\-length OCTET STRING must be returned if the Entire certificate is not retained in the CMTS
            	**type**\: str
            
            	**length:** 0..4096
            
            .. attribute:: docsietfbpi2cmtsauthcacertindexptr
            
            	A row index into docsIetfBpi2CmtsCACertTable. Returns the index in docsIetfBpi2CmtsCACertTable which CA certificate this CM is chained to.  A value of 0 means it could not be found or not applicable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsAuthEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsAuthTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmtsauthcmmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmtsauthcmmacaddress', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthCmMacAddress'), ['str'])),
                    ('docsietfbpi2cmtsauthcmbpiversion', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsAuthCmBpiVersion'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthCmBpiVersion')])),
                    ('docsietfbpi2cmtsauthcmpublickey', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthCmPublicKey'), ['str'])),
                    ('docsietfbpi2cmtsauthcmkeysequencenumber', (YLeaf(YType.int32, 'docsIetfBpi2CmtsAuthCmKeySequenceNumber'), ['int'])),
                    ('docsietfbpi2cmtsauthcmexpiresold', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthCmExpiresOld'), ['str'])),
                    ('docsietfbpi2cmtsauthcmexpiresnew', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthCmExpiresNew'), ['str'])),
                    ('docsietfbpi2cmtsauthcmlifetime', (YLeaf(YType.int32, 'docsIetfBpi2CmtsAuthCmLifetime'), ['int'])),
                    ('docsietfbpi2cmtsauthcmreset', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsAuthCmReset'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthCmReset')])),
                    ('docsietfbpi2cmtsauthcminfos', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCmInfos'), ['int'])),
                    ('docsietfbpi2cmtsauthcmrequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCmRequests'), ['int'])),
                    ('docsietfbpi2cmtsauthcmreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCmReplies'), ['int'])),
                    ('docsietfbpi2cmtsauthcmrejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCmRejects'), ['int'])),
                    ('docsietfbpi2cmtsauthcminvalids', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCmInvalids'), ['int'])),
                    ('docsietfbpi2cmtsauthrejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsAuthRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthRejectErrorCode')])),
                    ('docsietfbpi2cmtsauthrejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthRejectErrorString'), ['str'])),
                    ('docsietfbpi2cmtsauthinvaliderrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsAuthInvalidErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthInvalidErrorCode')])),
                    ('docsietfbpi2cmtsauthinvaliderrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthInvalidErrorString'), ['str'])),
                    ('docsietfbpi2cmtsauthprimarysaid', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthPrimarySAId'), ['int'])),
                    ('docsietfbpi2cmtsauthbpkmcmcertvalid', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsAuthBpkmCmCertValid'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry.DocsIetfBpi2CmtsAuthBpkmCmCertValid')])),
                    ('docsietfbpi2cmtsauthbpkmcmcert', (YLeaf(YType.str, 'docsIetfBpi2CmtsAuthBpkmCmCert'), ['str'])),
                    ('docsietfbpi2cmtsauthcacertindexptr', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsAuthCACertIndexPtr'), ['int'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmtsauthcmmacaddress = None
                self.docsietfbpi2cmtsauthcmbpiversion = None
                self.docsietfbpi2cmtsauthcmpublickey = None
                self.docsietfbpi2cmtsauthcmkeysequencenumber = None
                self.docsietfbpi2cmtsauthcmexpiresold = None
                self.docsietfbpi2cmtsauthcmexpiresnew = None
                self.docsietfbpi2cmtsauthcmlifetime = None
                self.docsietfbpi2cmtsauthcmreset = None
                self.docsietfbpi2cmtsauthcminfos = None
                self.docsietfbpi2cmtsauthcmrequests = None
                self.docsietfbpi2cmtsauthcmreplies = None
                self.docsietfbpi2cmtsauthcmrejects = None
                self.docsietfbpi2cmtsauthcminvalids = None
                self.docsietfbpi2cmtsauthrejecterrorcode = None
                self.docsietfbpi2cmtsauthrejecterrorstring = None
                self.docsietfbpi2cmtsauthinvaliderrorcode = None
                self.docsietfbpi2cmtsauthinvaliderrorstring = None
                self.docsietfbpi2cmtsauthprimarysaid = None
                self.docsietfbpi2cmtsauthbpkmcmcertvalid = None
                self.docsietfbpi2cmtsauthbpkmcmcert = None
                self.docsietfbpi2cmtsauthcacertindexptr = None
                self._segment_path = lambda: "docsIetfBpi2CmtsAuthEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmtsAuthCmMacAddress='" + str(self.docsietfbpi2cmtsauthcmmacaddress) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsAuthTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsAuthTable.DocsIetfBpi2CmtsAuthEntry, [u'ifindex', u'docsietfbpi2cmtsauthcmmacaddress', u'docsietfbpi2cmtsauthcmbpiversion', u'docsietfbpi2cmtsauthcmpublickey', u'docsietfbpi2cmtsauthcmkeysequencenumber', u'docsietfbpi2cmtsauthcmexpiresold', u'docsietfbpi2cmtsauthcmexpiresnew', u'docsietfbpi2cmtsauthcmlifetime', u'docsietfbpi2cmtsauthcmreset', u'docsietfbpi2cmtsauthcminfos', u'docsietfbpi2cmtsauthcmrequests', u'docsietfbpi2cmtsauthcmreplies', u'docsietfbpi2cmtsauthcmrejects', u'docsietfbpi2cmtsauthcminvalids', u'docsietfbpi2cmtsauthrejecterrorcode', u'docsietfbpi2cmtsauthrejecterrorstring', u'docsietfbpi2cmtsauthinvaliderrorcode', u'docsietfbpi2cmtsauthinvaliderrorstring', u'docsietfbpi2cmtsauthprimarysaid', u'docsietfbpi2cmtsauthbpkmcmcertvalid', u'docsietfbpi2cmtsauthbpkmcmcert', u'docsietfbpi2cmtsauthcacertindexptr'], name, value)

            class DocsIetfBpi2CmtsAuthBpkmCmCertValid(Enum):
                """
                DocsIetfBpi2CmtsAuthBpkmCmCertValid (Enum Class)

                Contains the reason why a CM's certificate is deemed

                valid or invalid.

                Return unknown(0) if the CM is running BPI mode.

                ValidCmChained(1) means the certificate is valid

                   because it chains to a valid certificate.

                ValidCmTrusted(2) means the certificate is valid

                   because it has been provisioned (in the

                   docsIetfBpi2CmtsProvisionedCmCert table) to be trusted.

                InvalidCmUntrusted(3) means the certificate is invalid

                     because it has been provisioned (in the

                     docsIetfBpi2CmtsProvisionedCmCert table) to be untrusted.

                InvalidCAUntrusted(4) means the certificate is invalid

                     because it chains to an untrusted certificate.

                InvalidCmOther(5) and InvalidCAOther(6) refer to

                     errors in parsing, validity periods, etc, which are

                     attributable to the CM certificate or its chain

                     respectively; additional information may be found

                     in docsIetfBpi2AuthRejectErrorString for these types

                     of errors.

                InvalidCmRevoked(7) means the certificate is

                   invalid as it was marked as revoked. 

                InvalidCARevoked(8) means the CA certificate is

                   invalid as it was marked as revoked.

                .. data:: unknown = 0

                .. data:: validCmChained = 1

                .. data:: validCmTrusted = 2

                .. data:: invalidCmUntrusted = 3

                .. data:: invalidCAUntrusted = 4

                .. data:: invalidCmOther = 5

                .. data:: invalidCAOther = 6

                .. data:: invalidCmRevoked = 7

                .. data:: invalidCARevoked = 8

                """

                unknown = Enum.YLeaf(0, "unknown")

                validCmChained = Enum.YLeaf(1, "validCmChained")

                validCmTrusted = Enum.YLeaf(2, "validCmTrusted")

                invalidCmUntrusted = Enum.YLeaf(3, "invalidCmUntrusted")

                invalidCAUntrusted = Enum.YLeaf(4, "invalidCAUntrusted")

                invalidCmOther = Enum.YLeaf(5, "invalidCmOther")

                invalidCAOther = Enum.YLeaf(6, "invalidCAOther")

                invalidCmRevoked = Enum.YLeaf(7, "invalidCmRevoked")

                invalidCARevoked = Enum.YLeaf(8, "invalidCARevoked")


            class DocsIetfBpi2CmtsAuthCmBpiVersion(Enum):
                """
                DocsIetfBpi2CmtsAuthCmBpiVersion (Enum Class)

                The value of this object is the version of Baseline

                Privacy for which this CM has registered. The value

                'bpiplus' represents the value of BPI\-Version Attribute of

                the Baseline Privacy Key Management BPKM attribute

                BPI\-Version (1). The value 'bpi' is used to represent the

                CM registered using DOCSIS 1.0 Baseline Privacy.

                .. data:: bpi = 0

                .. data:: bpiPlus = 1

                """

                bpi = Enum.YLeaf(0, "bpi")

                bpiPlus = Enum.YLeaf(1, "bpiPlus")


            class DocsIetfBpi2CmtsAuthCmReset(Enum):
                """
                DocsIetfBpi2CmtsAuthCmReset (Enum Class)

                Setting this object to invalidateAuth(2) causes the

                CMTS to invalidate the current CM authorization key(s), but

                not to transmit an Authorization Invalid message nor to

                invalidate the primary SAID's TEKs.  Setting this object to

                sendAuthInvalid(3) causes the CMTS to invalidate the

                current CM authorization key(s), and to transmit an

                Authorization Invalid message to the CM, but not to

                invalidate the primary SAID's TEKs.  Setting this object to

                invalidateTeks(4) causes the CMTS to invalidate the current

                CM authorization key(s), to transmit an Authorization

                Invalid message to the CM, and to invalidate the TEKs

                associated with this CM's primary SAID.

                For BPI mode, substitute all of the CM's unicast

                TEK(s) for the primary SAID's TEKs in the previous

                paragraph.

                Reading this object returns the most recently set

                value of this object, or returns noResetRequested(1) if the

                object has not been set since entry creation.

                .. data:: noResetRequested = 1

                .. data:: invalidateAuth = 2

                .. data:: sendAuthInvalid = 3

                .. data:: invalidateTeks = 4

                """

                noResetRequested = Enum.YLeaf(1, "noResetRequested")

                invalidateAuth = Enum.YLeaf(2, "invalidateAuth")

                sendAuthInvalid = Enum.YLeaf(3, "sendAuthInvalid")

                invalidateTeks = Enum.YLeaf(4, "invalidateTeks")


            class DocsIetfBpi2CmtsAuthInvalidErrorCode(Enum):
                """
                DocsIetfBpi2CmtsAuthInvalidErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent Authorization

                Invalid message transmitted to the CM.  This has value

                unknown(2) if the last Error\-Code value was 0, and none(1)

                if no Authorization Invalid message has been transmitted to

                the CM since entry creation.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedCm = 3

                .. data:: unsolicited = 5

                .. data:: invalidKeySequence = 6

                .. data:: keyRequestAuthenticationFailure = 7

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedCm = Enum.YLeaf(3, "unauthorizedCm")

                unsolicited = Enum.YLeaf(5, "unsolicited")

                invalidKeySequence = Enum.YLeaf(6, "invalidKeySequence")

                keyRequestAuthenticationFailure = Enum.YLeaf(7, "keyRequestAuthenticationFailure")


            class DocsIetfBpi2CmtsAuthRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmtsAuthRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in most recent Authorization

                Reject message transmitted to the CM.  This has value

                unknown(2) if the last Error\-Code value was 0, and none(1)

                if no Authorization Reject message has been transmitted to

                the CM, since entry creation.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedCm = 3

                .. data:: unauthorizedSaid = 4

                .. data:: permanentAuthorizationFailure = 8

                .. data:: timeOfDayNotAcquired = 11

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedCm = Enum.YLeaf(3, "unauthorizedCm")

                unauthorizedSaid = Enum.YLeaf(4, "unauthorizedSaid")

                permanentAuthorizationFailure = Enum.YLeaf(8, "permanentAuthorizationFailure")

                timeOfDayNotAcquired = Enum.YLeaf(11, "timeOfDayNotAcquired")



    class DocsIetfBpi2CmtsTEKTable(Entity):
        """
        This table describes the attributes of each
        Traffic Encryption Key (TEK) association. The CMTS
        Maintains one TEK association per SAID on each CMTS MAC
        interface.
        
        .. attribute:: docsietfbpi2cmtstekentry
        
        	Each entry contains objects describing attributes of one TEK association on a particular CMTS MAC interface. The CMTS MUST create one entry per SAID per MAC interface, based on the receipt of a Key Request message, and MUST not delete the entry before the CM authorization for the SAID permanently expires
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsTEKEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsTEKTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsTEKEntry", ("docsietfbpi2cmtstekentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtstekentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsTEKTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable, [], name, value)


        class DocsIetfBpi2CmtsTEKEntry(Entity):
            """
            Each entry contains objects describing attributes of
            one TEK association on a particular CMTS MAC interface. The
            CMTS MUST create one entry per SAID per MAC interface,
            based on the receipt of a Key Request message, and MUST not
            delete the entry before the CM authorization for the SAID
            permanently expires.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmtsteksaid  (key)
            
            	The value of this object is the DOCSIS Security Association ID (SAID)
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsietfbpi2cmtsteksatype
            
            	The value of this object is the type of security association.  'dynamic' does not apply to CMs running in BPI mode.  Unicast BPI TEKs must utilize the 'primary' encoding and multicast BPI TEKs must utilize the 'static' encoding
            	**type**\:  :py:class:`DocsBpkmSAType <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmSAType>`
            
            .. attribute:: docsietfbpi2cmtstekdataencryptalg
            
            	The value of this object is the data encryption algorithm for this SAID
            	**type**\:  :py:class:`DocsBpkmDataEncryptAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataEncryptAlg>`
            
            .. attribute:: docsietfbpi2cmtstekdataauthentalg
            
            	The value of this object is the data authentication algorithm for this SAID
            	**type**\:  :py:class:`DocsBpkmDataAuthentAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataAuthentAlg>`
            
            .. attribute:: docsietfbpi2cmtsteklifetime
            
            	The value of this object is the lifetime, in seconds, the CMTS assigns to keys for this TEK association
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: docsietfbpi2cmtstekkeysequencenumber
            
            	The value of this object is the most recent TEK key sequence number for this SAID
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: docsietfbpi2cmtstekexpiresold
            
            	The value of this object is the actual clock time for expiration of the immediate predecessor of the most recent TEK for this FSM. If this FSM has only one TEK, then the value is the time of activation of this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtstekexpiresnew
            
            	The value of this object is the actual clock time for expiration of the most recent TEK for this FSM
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtstekreset
            
            	Setting this object to 'true' causes the CMTS to invalidate all currently active TEK(s) and to generate new TEK(s) for the associated SAID; the CMTS MAY also generate unsolicited TEK Invalid message(s), to optimize the TEK synchronization between the CMTS and the CM(s). Reading this object always returns FALSE
            	**type**\: bool
            
            .. attribute:: docsietfbpi2cmtskeyrequests
            
            	The value of this object is the count of times the CMTS has received a Key Request message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtskeyreplies
            
            	The value of this object is the count of times the CMTS has transmitted a Key Reply message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtskeyrejects
            
            	The value of this object is the count of times the CMTS has transmitted a Key Reject message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtstekinvalids
            
            	The value of this object is the count of times the CMTS has transmitted a TEK Invalid message. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtskeyrejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in the most recent Key Reject message sent in response to a Key Request for this SAID. This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no Key Reject message has been received since registration
            	**type**\:  :py:class:`DocsIetfBpi2CmtsKeyRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry.DocsIetfBpi2CmtsKeyRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmtskeyrejecterrorstring
            
            	The value of this object is the text string in the most recent Key Reject message sent in response to a Key Request for this SAID. This is a zero length string if no Key Reject message has been received since registration
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmtstekinvaliderrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in the most recent TEK Invalid message sent in association with this SAID.  This has value unknown(2) if the last Error\-Code value was 0, and none(1) if no TEK Invalid message has been received since registration
            	**type**\:  :py:class:`DocsIetfBpi2CmtsTEKInvalidErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry.DocsIetfBpi2CmtsTEKInvalidErrorCode>`
            
            .. attribute:: docsietfbpi2cmtstekinvaliderrorstring
            
            	The value of this object is the text string in the most recent TEK Invalid message sent in association with this SAID.  This is a zero length string if no TEK Invalid message has been received since registration
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsTEKEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsTEKTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmtsteksaid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmtsteksaid', (YLeaf(YType.int32, 'docsIetfBpi2CmtsTEKSAId'), ['int'])),
                    ('docsietfbpi2cmtsteksatype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsTEKSAType'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmSAType', '')])),
                    ('docsietfbpi2cmtstekdataencryptalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsTEKDataEncryptAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataEncryptAlg', '')])),
                    ('docsietfbpi2cmtstekdataauthentalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsTEKDataAuthentAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataAuthentAlg', '')])),
                    ('docsietfbpi2cmtsteklifetime', (YLeaf(YType.int32, 'docsIetfBpi2CmtsTEKLifetime'), ['int'])),
                    ('docsietfbpi2cmtstekkeysequencenumber', (YLeaf(YType.int32, 'docsIetfBpi2CmtsTEKKeySequenceNumber'), ['int'])),
                    ('docsietfbpi2cmtstekexpiresold', (YLeaf(YType.str, 'docsIetfBpi2CmtsTEKExpiresOld'), ['str'])),
                    ('docsietfbpi2cmtstekexpiresnew', (YLeaf(YType.str, 'docsIetfBpi2CmtsTEKExpiresNew'), ['str'])),
                    ('docsietfbpi2cmtstekreset', (YLeaf(YType.boolean, 'docsIetfBpi2CmtsTEKReset'), ['bool'])),
                    ('docsietfbpi2cmtskeyrequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsKeyRequests'), ['int'])),
                    ('docsietfbpi2cmtskeyreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsKeyReplies'), ['int'])),
                    ('docsietfbpi2cmtskeyrejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsKeyRejects'), ['int'])),
                    ('docsietfbpi2cmtstekinvalids', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsTEKInvalids'), ['int'])),
                    ('docsietfbpi2cmtskeyrejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsKeyRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry.DocsIetfBpi2CmtsKeyRejectErrorCode')])),
                    ('docsietfbpi2cmtskeyrejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmtsKeyRejectErrorString'), ['str'])),
                    ('docsietfbpi2cmtstekinvaliderrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsTEKInvalidErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry.DocsIetfBpi2CmtsTEKInvalidErrorCode')])),
                    ('docsietfbpi2cmtstekinvaliderrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmtsTEKInvalidErrorString'), ['str'])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmtsteksaid = None
                self.docsietfbpi2cmtsteksatype = None
                self.docsietfbpi2cmtstekdataencryptalg = None
                self.docsietfbpi2cmtstekdataauthentalg = None
                self.docsietfbpi2cmtsteklifetime = None
                self.docsietfbpi2cmtstekkeysequencenumber = None
                self.docsietfbpi2cmtstekexpiresold = None
                self.docsietfbpi2cmtstekexpiresnew = None
                self.docsietfbpi2cmtstekreset = None
                self.docsietfbpi2cmtskeyrequests = None
                self.docsietfbpi2cmtskeyreplies = None
                self.docsietfbpi2cmtskeyrejects = None
                self.docsietfbpi2cmtstekinvalids = None
                self.docsietfbpi2cmtskeyrejecterrorcode = None
                self.docsietfbpi2cmtskeyrejecterrorstring = None
                self.docsietfbpi2cmtstekinvaliderrorcode = None
                self.docsietfbpi2cmtstekinvaliderrorstring = None
                self._segment_path = lambda: "docsIetfBpi2CmtsTEKEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmtsTEKSAId='" + str(self.docsietfbpi2cmtsteksaid) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsTEKTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsTEKTable.DocsIetfBpi2CmtsTEKEntry, [u'ifindex', u'docsietfbpi2cmtsteksaid', u'docsietfbpi2cmtsteksatype', u'docsietfbpi2cmtstekdataencryptalg', u'docsietfbpi2cmtstekdataauthentalg', u'docsietfbpi2cmtsteklifetime', u'docsietfbpi2cmtstekkeysequencenumber', u'docsietfbpi2cmtstekexpiresold', u'docsietfbpi2cmtstekexpiresnew', u'docsietfbpi2cmtstekreset', u'docsietfbpi2cmtskeyrequests', u'docsietfbpi2cmtskeyreplies', u'docsietfbpi2cmtskeyrejects', u'docsietfbpi2cmtstekinvalids', u'docsietfbpi2cmtskeyrejecterrorcode', u'docsietfbpi2cmtskeyrejecterrorstring', u'docsietfbpi2cmtstekinvaliderrorcode', u'docsietfbpi2cmtstekinvaliderrorstring'], name, value)

            class DocsIetfBpi2CmtsKeyRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmtsKeyRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in the most recent Key Reject

                message sent in response to a Key Request for this SAID.

                This has value unknown(2) if the last Error\-Code value

                was 0, and none(1) if no Key Reject message has been

                received since registration.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: unauthorizedSaid = 4

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                unauthorizedSaid = Enum.YLeaf(4, "unauthorizedSaid")


            class DocsIetfBpi2CmtsTEKInvalidErrorCode(Enum):
                """
                DocsIetfBpi2CmtsTEKInvalidErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in the most recent TEK

                Invalid message sent in association with this SAID.  This

                has value unknown(2) if the last Error\-Code value was 0,

                and none(1) if no TEK Invalid message has been received

                since registration.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: invalidKeySequence = 6

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                invalidKeySequence = Enum.YLeaf(6, "invalidKeySequence")



    class DocsIetfBpi2CmtsIpMulticastMapTable(Entity):
        """
        This table maps multicast IP addresses to SAIDs.
        If a multicast IP address is mapped by multiple rows
        in the table, the row with the lowest
        docsIetfBpi2CmtsIpMulticastIndex must be utilized for the
        mapping.
        
        .. attribute:: docsietfbpi2cmtsipmulticastmapentry
        
        	Each entry contains objects describing the mapping of a set of multicast IP address and mask to one SAID associated to a CMTS MAC Interface, as well as associated message counters and error information
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsIpMulticastMapEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsIpMulticastMapTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsIpMulticastMapEntry", ("docsietfbpi2cmtsipmulticastmapentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtsipmulticastmapentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsIpMulticastMapTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable, [], name, value)


        class DocsIetfBpi2CmtsIpMulticastMapEntry(Entity):
            """
            Each entry contains objects describing the mapping of
            a set of multicast IP address and mask to one SAID
            associated to a CMTS MAC Interface, as well as associated
            message
            counters and error information.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastindex  (key)
            
            	The index of this row. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsietfbpi2cmtsipmulticastaddresstype
            
            	The type of internet address for docsIetfBpi2CmtsIpMulticastAddress and docsIetfBpi2CmtsIpMulticastMask
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastaddress
            
            	This object represents the IP multicast address to be mapped, in conjunction with docsIetfBpi2CmtsIpMulticastMask. The type of this address is determined by the value of the object docsIetfBpi2CmtsIpMulticastAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsietfbpi2cmtsipmulticastmask
            
            	This object represents the IP multicast address mask for this row. An IP multicast address matches this row if the logical AND of the address with docsIetfBpi2CmtsIpMulticastMask is identical to the logical AND of docsIetfBpi2CmtsIpMulticastAddr with docsIetfBpi2CmtsIpMulticastMask. The type of this address is determined by the value of the object docsIetfBpi2CmtsIpMulticastAddressType.  Note\: For IPv6 this object needs not to represent a  contiguous netmask, e.g. to associate an SAID to a  multicast group matching 'any' multicast scope. The TC  InetAddressPrefixLength is not used because it only  represents contiguous netmask
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsietfbpi2cmtsipmulticastsaid
            
            	This object represents the multicast SAID to be used in this IP multicast address mapping entry
            	**type**\: int
            
            	**range:** 0..16383
            
            .. attribute:: docsietfbpi2cmtsipmulticastsatype
            
            	The value of this object is the type of security association.  'dynamic' does not apply to CMs running in BPI mode.  Unicast BPI TEKs must utilize the 'primary' encoding and multicast BPI TEKs must utilize the 'static' encoding.  SNMP created entries set this object by default to 'static' if not set at row creation
            	**type**\:  :py:class:`DocsBpkmSAType <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmSAType>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastdataencryptalg
            
            	The value of this object is the data encryption algorithm for this IP
            	**type**\:  :py:class:`DocsBpkmDataEncryptAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataEncryptAlg>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastdataauthentalg
            
            	The value of this object is the data authentication algorithm for this IP
            	**type**\:  :py:class:`DocsBpkmDataAuthentAlg <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DocsBpkmDataAuthentAlg>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastsamaprequests
            
            	The value of this object is the count of times the CMTS has received an SA Map Request message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsipmulticastsamapreplies
            
            	The value of this object is the count of times the CMTS has transmitted an SA Map Reply message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsipmulticastsamaprejects
            
            	The value of this object is the count of times the CMTS has transmitted an SA Map Reject message for this IP. Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsietfbpi2cmtsipmulticastsamaprejecterrorcode
            
            	The value of this object is the enumerated description of the Error\-Code in the most recent SA Map Reject message sent in response to a SA Map Request for This IP.  It has value unknown(2) if the last Error\-Code Value was 0, and none(1) if no SA MAP Reject message has been received since entry creation
            	**type**\:  :py:class:`DocsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry.DocsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastsamaprejecterrorstring
            
            	The value of this object is the text string in the most recent SA Map Reject message sent in response to an SA Map Request for this IP.  It is a zero length string if no SA Map Reject message has been received since entry creation
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: docsietfbpi2cmtsipmulticastmapcontrol
            
            	This object controls and reflects the IP multicast address mapping entry.  There is no restriction on the ability to change values in this row while the row is active. A created row can be set to active only after the Corresponding instances of docsIetfBpi2CmtsIpMulticastAddress, docsIetfBpi2CmtsIpMulticastMask, docsIetfBpi2CmtsIpMulticastSAId and docsIetfBpi2CmtsIpMulticastSAType have all been set
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsietfbpi2cmtsipmulticastmapstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsIpMulticastMapEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsIpMulticastMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmtsipmulticastindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastindex', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsIpMulticastIndex'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastaddresstype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsietfbpi2cmtsipmulticastaddress', (YLeaf(YType.str, 'docsIetfBpi2CmtsIpMulticastAddress'), ['str'])),
                    ('docsietfbpi2cmtsipmulticastmask', (YLeaf(YType.str, 'docsIetfBpi2CmtsIpMulticastMask'), ['str'])),
                    ('docsietfbpi2cmtsipmulticastsaid', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsIpMulticastSAId'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastsatype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastSAType'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmSAType', '')])),
                    ('docsietfbpi2cmtsipmulticastdataencryptalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastDataEncryptAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataEncryptAlg', '')])),
                    ('docsietfbpi2cmtsipmulticastdataauthentalg', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastDataAuthentAlg'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DocsBpkmDataAuthentAlg', '')])),
                    ('docsietfbpi2cmtsipmulticastsamaprequests', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsIpMulticastSAMapRequests'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastsamapreplies', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsIpMulticastSAMapReplies'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastsamaprejects', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsIpMulticastSAMapRejects'), ['int'])),
                    ('docsietfbpi2cmtsipmulticastsamaprejecterrorcode', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry.DocsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode')])),
                    ('docsietfbpi2cmtsipmulticastsamaprejecterrorstring', (YLeaf(YType.str, 'docsIetfBpi2CmtsIpMulticastSAMapRejectErrorString'), ['str'])),
                    ('docsietfbpi2cmtsipmulticastmapcontrol', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastMapControl'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsietfbpi2cmtsipmulticastmapstoragetype', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsIpMulticastMapStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmtsipmulticastindex = None
                self.docsietfbpi2cmtsipmulticastaddresstype = None
                self.docsietfbpi2cmtsipmulticastaddress = None
                self.docsietfbpi2cmtsipmulticastmask = None
                self.docsietfbpi2cmtsipmulticastsaid = None
                self.docsietfbpi2cmtsipmulticastsatype = None
                self.docsietfbpi2cmtsipmulticastdataencryptalg = None
                self.docsietfbpi2cmtsipmulticastdataauthentalg = None
                self.docsietfbpi2cmtsipmulticastsamaprequests = None
                self.docsietfbpi2cmtsipmulticastsamapreplies = None
                self.docsietfbpi2cmtsipmulticastsamaprejects = None
                self.docsietfbpi2cmtsipmulticastsamaprejecterrorcode = None
                self.docsietfbpi2cmtsipmulticastsamaprejecterrorstring = None
                self.docsietfbpi2cmtsipmulticastmapcontrol = None
                self.docsietfbpi2cmtsipmulticastmapstoragetype = None
                self._segment_path = lambda: "docsIetfBpi2CmtsIpMulticastMapEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmtsIpMulticastIndex='" + str(self.docsietfbpi2cmtsipmulticastindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsIpMulticastMapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsIpMulticastMapTable.DocsIetfBpi2CmtsIpMulticastMapEntry, [u'ifindex', u'docsietfbpi2cmtsipmulticastindex', u'docsietfbpi2cmtsipmulticastaddresstype', u'docsietfbpi2cmtsipmulticastaddress', u'docsietfbpi2cmtsipmulticastmask', u'docsietfbpi2cmtsipmulticastsaid', u'docsietfbpi2cmtsipmulticastsatype', u'docsietfbpi2cmtsipmulticastdataencryptalg', u'docsietfbpi2cmtsipmulticastdataauthentalg', u'docsietfbpi2cmtsipmulticastsamaprequests', u'docsietfbpi2cmtsipmulticastsamapreplies', u'docsietfbpi2cmtsipmulticastsamaprejects', u'docsietfbpi2cmtsipmulticastsamaprejecterrorcode', u'docsietfbpi2cmtsipmulticastsamaprejecterrorstring', u'docsietfbpi2cmtsipmulticastmapcontrol', u'docsietfbpi2cmtsipmulticastmapstoragetype'], name, value)

            class DocsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode(Enum):
                """
                DocsIetfBpi2CmtsIpMulticastSAMapRejectErrorCode (Enum Class)

                The value of this object is the enumerated

                description of the Error\-Code in the most recent SA Map

                Reject message sent in response to a SA Map Request for

                This IP.  It has value unknown(2) if the last Error\-Code

                Value was 0, and none(1) if no SA MAP Reject message has

                been received since entry creation.

                .. data:: none = 1

                .. data:: unknown = 2

                .. data:: noAuthForRequestedDSFlow = 9

                .. data:: dsFlowNotMappedToSA = 10

                """

                none = Enum.YLeaf(1, "none")

                unknown = Enum.YLeaf(2, "unknown")

                noAuthForRequestedDSFlow = Enum.YLeaf(9, "noAuthForRequestedDSFlow")

                dsFlowNotMappedToSA = Enum.YLeaf(10, "dsFlowNotMappedToSA")



    class DocsIetfBpi2CmtsMulticastAuthTable(Entity):
        """
        This table describes the multicast SAID
        authorization for each CM on each CMTS MAC interface.
        
        .. attribute:: docsietfbpi2cmtsmulticastauthentry
        
        	Each entry contains objects describing the key authorization of one cable modem for one multicast SAID for one CMTS MAC interface. Row entries persist after re\-initialization of the managed system
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsMulticastAuthEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable.DocsIetfBpi2CmtsMulticastAuthEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsMulticastAuthTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsMulticastAuthEntry", ("docsietfbpi2cmtsmulticastauthentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable.DocsIetfBpi2CmtsMulticastAuthEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtsmulticastauthentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsMulticastAuthTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable, [], name, value)


        class DocsIetfBpi2CmtsMulticastAuthEntry(Entity):
            """
            Each entry contains objects describing the key
            authorization of one cable modem for one multicast SAID
            for one CMTS MAC interface.
            Row entries persist after re\-initialization of
            the managed system.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: docsietfbpi2cmtsmulticastauthsaid  (key)
            
            	This object represents the multicast SAID for authorization
            	**type**\: int
            
            	**range:** 1..16383
            
            .. attribute:: docsietfbpi2cmtsmulticastauthcmmacaddress  (key)
            
            	This object represents the MAC address of the CM to which the multicast SAID authorization applies
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsietfbpi2cmtsmulticastauthcontrol
            
            	The status of this conceptual row for the authorization of  multicast SAIDs to CMs. 
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable.DocsIetfBpi2CmtsMulticastAuthEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsMulticastAuthEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsMulticastAuthTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsietfbpi2cmtsmulticastauthsaid','docsietfbpi2cmtsmulticastauthcmmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsietfbpi2cmtsmulticastauthsaid', (YLeaf(YType.int32, 'docsIetfBpi2CmtsMulticastAuthSAId'), ['int'])),
                    ('docsietfbpi2cmtsmulticastauthcmmacaddress', (YLeaf(YType.str, 'docsIetfBpi2CmtsMulticastAuthCmMacAddress'), ['str'])),
                    ('docsietfbpi2cmtsmulticastauthcontrol', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsMulticastAuthControl'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.docsietfbpi2cmtsmulticastauthsaid = None
                self.docsietfbpi2cmtsmulticastauthcmmacaddress = None
                self.docsietfbpi2cmtsmulticastauthcontrol = None
                self._segment_path = lambda: "docsIetfBpi2CmtsMulticastAuthEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsIetfBpi2CmtsMulticastAuthSAId='" + str(self.docsietfbpi2cmtsmulticastauthsaid) + "']" + "[docsIetfBpi2CmtsMulticastAuthCmMacAddress='" + str(self.docsietfbpi2cmtsmulticastauthcmmacaddress) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsMulticastAuthTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsMulticastAuthTable.DocsIetfBpi2CmtsMulticastAuthEntry, [u'ifindex', u'docsietfbpi2cmtsmulticastauthsaid', u'docsietfbpi2cmtsmulticastauthcmmacaddress', u'docsietfbpi2cmtsmulticastauthcontrol'], name, value)


    class DocsIetfBpi2CmtsProvisionedCmCertTable(Entity):
        """
        A table of CM certificate trust entries provisioned
        to the CMTS.  The trust object for a certificate in this
        table has an overriding effect on the validity object of a
        certificate in the authorization table, as long as the
        entire contents of the two certificates are identical.
        
        .. attribute:: docsietfbpi2cmtsprovisionedcmcertentry
        
        	An entry in the CMTS's provisioned CM certificate table.  Row entries persist after re\-initialization of the managed system
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsProvisionedCmCertEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsProvisionedCmCertTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsProvisionedCmCertEntry", ("docsietfbpi2cmtsprovisionedcmcertentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtsprovisionedcmcertentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsProvisionedCmCertTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable, [], name, value)


        class DocsIetfBpi2CmtsProvisionedCmCertEntry(Entity):
            """
            An entry in the CMTS's provisioned CM certificate
            table.  Row entries persist after re\-initialization of
            the managed system.
            
            .. attribute:: docsietfbpi2cmtsprovisionedcmcertmacaddress  (key)
            
            	The index of this row
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docsietfbpi2cmtsprovisionedcmcerttrust
            
            	Trust state for the provisioned CM certificate entry. Note\: Setting this object need only override the validity of CM certificates sent in future authorization requests; instantaneous effect need not occur
            	**type**\:  :py:class:`DocsIetfBpi2CmtsProvisionedCmCertTrust <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry.DocsIetfBpi2CmtsProvisionedCmCertTrust>`
            
            .. attribute:: docsietfbpi2cmtsprovisionedcmcertsource
            
            	This object indicates how the certificate reached the CMTS.  Other(4) means is originated from a source not identified above
            	**type**\:  :py:class:`DocsIetfBpi2CmtsProvisionedCmCertSource <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry.DocsIetfBpi2CmtsProvisionedCmCertSource>`
            
            .. attribute:: docsietfbpi2cmtsprovisionedcmcertstatus
            
            	The status of this conceptual row. Values in this row cannot be changed while the row is 'active'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsietfbpi2cmtsprovisionedcmcert
            
            	An X509 DER\-encoded Certificate Authority certificate. Note\: The zero\-length OCTET STRING must be returned, on reads, if the entire certificate is not retained in the CMTS
            	**type**\: str
            
            	**length:** 0..4096
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsProvisionedCmCertEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsProvisionedCmCertTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsietfbpi2cmtsprovisionedcmcertmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsietfbpi2cmtsprovisionedcmcertmacaddress', (YLeaf(YType.str, 'docsIetfBpi2CmtsProvisionedCmCertMacAddress'), ['str'])),
                    ('docsietfbpi2cmtsprovisionedcmcerttrust', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsProvisionedCmCertTrust'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry.DocsIetfBpi2CmtsProvisionedCmCertTrust')])),
                    ('docsietfbpi2cmtsprovisionedcmcertsource', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsProvisionedCmCertSource'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry.DocsIetfBpi2CmtsProvisionedCmCertSource')])),
                    ('docsietfbpi2cmtsprovisionedcmcertstatus', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsProvisionedCmCertStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsietfbpi2cmtsprovisionedcmcert', (YLeaf(YType.str, 'docsIetfBpi2CmtsProvisionedCmCert'), ['str'])),
                ])
                self.docsietfbpi2cmtsprovisionedcmcertmacaddress = None
                self.docsietfbpi2cmtsprovisionedcmcerttrust = None
                self.docsietfbpi2cmtsprovisionedcmcertsource = None
                self.docsietfbpi2cmtsprovisionedcmcertstatus = None
                self.docsietfbpi2cmtsprovisionedcmcert = None
                self._segment_path = lambda: "docsIetfBpi2CmtsProvisionedCmCertEntry" + "[docsIetfBpi2CmtsProvisionedCmCertMacAddress='" + str(self.docsietfbpi2cmtsprovisionedcmcertmacaddress) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsProvisionedCmCertTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsProvisionedCmCertTable.DocsIetfBpi2CmtsProvisionedCmCertEntry, [u'docsietfbpi2cmtsprovisionedcmcertmacaddress', u'docsietfbpi2cmtsprovisionedcmcerttrust', u'docsietfbpi2cmtsprovisionedcmcertsource', u'docsietfbpi2cmtsprovisionedcmcertstatus', u'docsietfbpi2cmtsprovisionedcmcert'], name, value)

            class DocsIetfBpi2CmtsProvisionedCmCertSource(Enum):
                """
                DocsIetfBpi2CmtsProvisionedCmCertSource (Enum Class)

                This object indicates how the certificate reached the

                CMTS.  Other(4) means is originated from a source not

                identified above.

                .. data:: snmp = 1

                .. data:: configurationFile = 2

                .. data:: externalDatabase = 3

                .. data:: other = 4

                """

                snmp = Enum.YLeaf(1, "snmp")

                configurationFile = Enum.YLeaf(2, "configurationFile")

                externalDatabase = Enum.YLeaf(3, "externalDatabase")

                other = Enum.YLeaf(4, "other")


            class DocsIetfBpi2CmtsProvisionedCmCertTrust(Enum):
                """
                DocsIetfBpi2CmtsProvisionedCmCertTrust (Enum Class)

                Trust state for the provisioned CM certificate entry.

                Note\: Setting this object need only override the validity

                of CM certificates sent in future authorization requests;

                instantaneous effect need not occur.

                .. data:: trusted = 1

                .. data:: untrusted = 2

                """

                trusted = Enum.YLeaf(1, "trusted")

                untrusted = Enum.YLeaf(2, "untrusted")



    class DocsIetfBpi2CmtsCACertTable(Entity):
        """
        The table of known Certificate Authority certificates
        acquired by this device.
        
        .. attribute:: docsietfbpi2cmtscacertentry
        
        	A row in the Certificate Authority certificate table.  Row entries with trust status 'trusted', 'untrusted', or 'root' persist after re\-initialization  of the managed system
        	**type**\: list of  		 :py:class:`DocsIetfBpi2CmtsCACertEntry <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry>`
        
        

        """

        _prefix = 'DOCS-IETF-BPI2-MIB'
        _revision = '2004-09-07'

        def __init__(self):
            super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable, self).__init__()

            self.yang_name = "docsIetfBpi2CmtsCACertTable"
            self.yang_parent_name = "DOCS-IETF-BPI2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsIetfBpi2CmtsCACertEntry", ("docsietfbpi2cmtscacertentry", DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry))])
            self._leafs = OrderedDict()

            self.docsietfbpi2cmtscacertentry = YList(self)
            self._segment_path = lambda: "docsIetfBpi2CmtsCACertTable"
            self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable, [], name, value)


        class DocsIetfBpi2CmtsCACertEntry(Entity):
            """
            A row in the Certificate Authority certificate
            table.  Row entries with trust status 'trusted',
            'untrusted', or 'root' persist after re\-initialization
             of the managed system.
            
            .. attribute:: docsietfbpi2cmtscacertindex  (key)
            
            	The index for this row
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: docsietfbpi2cmtscacertsubject
            
            	The subject name exactly as it is encoded in the X509 certificate. The organizationName portion of the certificate's subject name must be present.  All other fields are optional.  Any optional field present must be pre pended with <CR> (carriage return, U+000D) <LF> (line feed, U+000A). Ordering of fields present must conform to\: organizationName <CR> <LF> countryName <CR> <LF> stateOrProvinceName <CR> <LF> localityName <CR> <LF> organizationalUnitName <CR> <LF> organizationalUnitName=<Manufacturing Location> <CR> <LF> commonName
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtscacertissuer
            
            	The issuer name exactly as it is encoded in the X509 certificate. The commonName portion of the certificate's issuer name must be present.  All other fields are optional.  Any optional field present must be pre pended with <CR> (carriage return, U+000D) <LF> (line feed, U+000A). Ordering of fields present must conform to\:  CommonName <CR><LF> countryName <CR><LF> stateOrProvinceName <CR><LF> localityName <CR><LF> organizationName <CR><LF> organizationalUnitName <CR><LF> organizationalUnitName=<Manufacturing Location>
            	**type**\: str
            
            .. attribute:: docsietfbpi2cmtscacertserialnumber
            
            	This CA certificate's serial number represented as an octet string
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: docsietfbpi2cmtscacerttrust
            
            	This object controls the trust status of this certificate.  Root certificates must be given root(4) trust; manufacturer certificates must not be given root(4) trust.  Trust on root certificates must not change. Note\: Setting this object need only affect the validity of CM certificates sent in future authorization requests; instantaneous effect need not occur
            	**type**\:  :py:class:`DocsIetfBpi2CmtsCACertTrust <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry.DocsIetfBpi2CmtsCACertTrust>`
            
            .. attribute:: docsietfbpi2cmtscacertsource
            
            	This object indicates how the certificate reached the CMTS.  Other(4) means it originated from a source not identified above
            	**type**\:  :py:class:`DocsIetfBpi2CmtsCACertSource <ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB.DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry.DocsIetfBpi2CmtsCACertSource>`
            
            .. attribute:: docsietfbpi2cmtscacertstatus
            
            	The status of this conceptual row. An attempt to set writable columnar values while this row is active behaves as follows\: \- Sets to the object docsIetfBpi2CmtsCACertTrust are allowed. \- Sets to the object docsIetfBpi2CmtsCACert will return an   error inconsistentValue'. A newly create entry cannot be set to active until the value of docsIetfBpi2CmtsCACert is being set
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsietfbpi2cmtscacert
            
            	An X509 DER\-encoded Certificate Authority certificate. To help identify certificates, either this object or docsIetfBpi2CmtsCACertThumbprint must be returned by a CMTS for self\-signed CA certificates.  Note\: The zero\-length OCTET STRING must be returned, on reads, if the entire certificate is not retained in the CMTS
            	**type**\: str
            
            	**length:** 0..4096
            
            .. attribute:: docsietfbpi2cmtscacertthumbprint
            
            	The SHA\-1 hash of a CA certificate. To help identify certificates, either this object or docsIetfBpi2CmtsCACert must be returned by a CMTS for self\-signed CA certificates.  Note\: The zero\-length OCTET STRING must be returned, on reads, if the CA certificate thumb print is not retained in the CMTS
            	**type**\: str
            
            	**length:** 20
            
            

            """

            _prefix = 'DOCS-IETF-BPI2-MIB'
            _revision = '2004-09-07'

            def __init__(self):
                super(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry, self).__init__()

                self.yang_name = "docsIetfBpi2CmtsCACertEntry"
                self.yang_parent_name = "docsIetfBpi2CmtsCACertTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsietfbpi2cmtscacertindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsietfbpi2cmtscacertindex', (YLeaf(YType.uint32, 'docsIetfBpi2CmtsCACertIndex'), ['int'])),
                    ('docsietfbpi2cmtscacertsubject', (YLeaf(YType.str, 'docsIetfBpi2CmtsCACertSubject'), ['str'])),
                    ('docsietfbpi2cmtscacertissuer', (YLeaf(YType.str, 'docsIetfBpi2CmtsCACertIssuer'), ['str'])),
                    ('docsietfbpi2cmtscacertserialnumber', (YLeaf(YType.str, 'docsIetfBpi2CmtsCACertSerialNumber'), ['str'])),
                    ('docsietfbpi2cmtscacerttrust', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsCACertTrust'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry.DocsIetfBpi2CmtsCACertTrust')])),
                    ('docsietfbpi2cmtscacertsource', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsCACertSource'), [('ydk.models.cisco_ios_xe.DOCS_IETF_BPI2_MIB', 'DOCSIETFBPI2MIB', 'DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry.DocsIetfBpi2CmtsCACertSource')])),
                    ('docsietfbpi2cmtscacertstatus', (YLeaf(YType.enumeration, 'docsIetfBpi2CmtsCACertStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsietfbpi2cmtscacert', (YLeaf(YType.str, 'docsIetfBpi2CmtsCACert'), ['str'])),
                    ('docsietfbpi2cmtscacertthumbprint', (YLeaf(YType.str, 'docsIetfBpi2CmtsCACertThumbprint'), ['str'])),
                ])
                self.docsietfbpi2cmtscacertindex = None
                self.docsietfbpi2cmtscacertsubject = None
                self.docsietfbpi2cmtscacertissuer = None
                self.docsietfbpi2cmtscacertserialnumber = None
                self.docsietfbpi2cmtscacerttrust = None
                self.docsietfbpi2cmtscacertsource = None
                self.docsietfbpi2cmtscacertstatus = None
                self.docsietfbpi2cmtscacert = None
                self.docsietfbpi2cmtscacertthumbprint = None
                self._segment_path = lambda: "docsIetfBpi2CmtsCACertEntry" + "[docsIetfBpi2CmtsCACertIndex='" + str(self.docsietfbpi2cmtscacertindex) + "']"
                self._absolute_path = lambda: "DOCS-IETF-BPI2-MIB:DOCS-IETF-BPI2-MIB/docsIetfBpi2CmtsCACertTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSIETFBPI2MIB.DocsIetfBpi2CmtsCACertTable.DocsIetfBpi2CmtsCACertEntry, [u'docsietfbpi2cmtscacertindex', u'docsietfbpi2cmtscacertsubject', u'docsietfbpi2cmtscacertissuer', u'docsietfbpi2cmtscacertserialnumber', u'docsietfbpi2cmtscacerttrust', u'docsietfbpi2cmtscacertsource', u'docsietfbpi2cmtscacertstatus', u'docsietfbpi2cmtscacert', u'docsietfbpi2cmtscacertthumbprint'], name, value)

            class DocsIetfBpi2CmtsCACertSource(Enum):
                """
                DocsIetfBpi2CmtsCACertSource (Enum Class)

                This object indicates how the certificate reached

                the CMTS.  Other(4) means it originated from a source not

                identified above.

                .. data:: snmp = 1

                .. data:: configurationFile = 2

                .. data:: externalDatabase = 3

                .. data:: other = 4

                .. data:: authentInfo = 5

                .. data:: compiledIntoCode = 6

                """

                snmp = Enum.YLeaf(1, "snmp")

                configurationFile = Enum.YLeaf(2, "configurationFile")

                externalDatabase = Enum.YLeaf(3, "externalDatabase")

                other = Enum.YLeaf(4, "other")

                authentInfo = Enum.YLeaf(5, "authentInfo")

                compiledIntoCode = Enum.YLeaf(6, "compiledIntoCode")


            class DocsIetfBpi2CmtsCACertTrust(Enum):
                """
                DocsIetfBpi2CmtsCACertTrust (Enum Class)

                This object controls the trust status of this

                certificate.  Root certificates must be given root(4)

                trust; manufacturer certificates must not be given root(4)

                trust.  Trust on root certificates must not change.

                Note\: Setting this object need only affect the validity of

                CM certificates sent in future authorization requests;

                instantaneous effect need not occur.

                .. data:: trusted = 1

                .. data:: untrusted = 2

                .. data:: chained = 3

                .. data:: root = 4

                """

                trusted = Enum.YLeaf(1, "trusted")

                untrusted = Enum.YLeaf(2, "untrusted")

                chained = Enum.YLeaf(3, "chained")

                root = Enum.YLeaf(4, "root")


    def clone_ptr(self):
        self._top_entity = DOCSIETFBPI2MIB()
        return self._top_entity

