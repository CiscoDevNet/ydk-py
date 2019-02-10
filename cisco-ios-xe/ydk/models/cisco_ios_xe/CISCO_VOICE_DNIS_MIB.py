""" CISCO_VOICE_DNIS_MIB 

The MIB module provides management support for Dialer
Number Information Service (DNIS) mapping.  A DNIS
entry is associated with a Voice XML (VXML) page to
provide audio play back features. Multiple DNIS
entries can be grouped together to form a DNIS
mapping with a unique map name.

\*\*\* ABBREVIATIONS, ACRONYMS, AND SYMBOLS \*\*\*

DNIS \- Dialer Number Information Service

XML  \- Extensible Markup Language

VXML \- Voice XML

URL  \- Uniform Resource Locator  

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOVOICEDNISMIB(Entity):
    """
    
    
    .. attribute:: cvdnismappingtable
    
    	The table contains the map name and a url specifying a file name. The file contains DNIS entries that belong to the DNIS mapping
    	**type**\:  :py:class:`CvDnisMappingTable <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisMappingTable>`
    
    	**config**\: False
    
    .. attribute:: cvdnisnodetable
    
    	The table contains a DNIS name and a url. The url is a pointer to a VXML page for the DNIS name. 
    	**type**\:  :py:class:`CvDnisNodeTable <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisNodeTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-VOICE-DNIS-MIB'
    _revision = '2002-05-01'

    def __init__(self):
        super(CISCOVOICEDNISMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-DNIS-MIB"
        self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cvDnisMappingTable", ("cvdnismappingtable", CISCOVOICEDNISMIB.CvDnisMappingTable)), ("cvDnisNodeTable", ("cvdnisnodetable", CISCOVOICEDNISMIB.CvDnisNodeTable))])
        self._leafs = OrderedDict()

        self.cvdnismappingtable = CISCOVOICEDNISMIB.CvDnisMappingTable()
        self.cvdnismappingtable.parent = self
        self._children_name_map["cvdnismappingtable"] = "cvDnisMappingTable"

        self.cvdnisnodetable = CISCOVOICEDNISMIB.CvDnisNodeTable()
        self.cvdnisnodetable.parent = self
        self._children_name_map["cvdnisnodetable"] = "cvDnisNodeTable"
        self._segment_path = lambda: "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOVOICEDNISMIB, [], name, value)


    class CvDnisMappingTable(Entity):
        """
        The table contains the map name and a url specifying
        a file name. The file contains DNIS entries that belong
        to the DNIS mapping.
        
        .. attribute:: cvdnismappingentry
        
        	Information about a single DNIS mapping. There is a unique DNIS map name. New DNIS mapping can be created using cvDnisMappingStatus.  The entry can be created with or without a file location  specified by cvDnisMappingUrl. The mapping file contains DNIS name and VXML page per line. For example, a  cvDnisMappingUrl could be tftp\://someserver/dnismap.txt. This file is a text file and the content format is   dnis <dnisname> url <urlname>. An example of the contents of the file itself can be   dnis 18004251234 url http\://www.b.com/p/vwelcome.vxml   dnis 18004253421 url http\://www.c.com/j/vxmlintf.vxml If a mapping file location is specified, then new rows corresponding to this map name are created and populated in cvDnisNodeTable from the contents of the file. The rows corresponding to this map name in cvDnisNodeTable cannot be created or modified or deleted but can be read.   If a mapping file location is not specified in cvDnisMappingUrl, then individual DNIS entries corresponding to this map name can be created, modified and deleted in cvDnisNodeTable.   Deleting an entry deletes all the related entries in cvDnisNodeTable. 
        	**type**\: list of  		 :py:class:`CvDnisMappingEntry <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VOICE-DNIS-MIB'
        _revision = '2002-05-01'

        def __init__(self):
            super(CISCOVOICEDNISMIB.CvDnisMappingTable, self).__init__()

            self.yang_name = "cvDnisMappingTable"
            self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvDnisMappingEntry", ("cvdnismappingentry", CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry))])
            self._leafs = OrderedDict()

            self.cvdnismappingentry = YList(self)
            self._segment_path = lambda: "cvDnisMappingTable"
            self._absolute_path = lambda: "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDNISMIB.CvDnisMappingTable, [], name, value)


        class CvDnisMappingEntry(Entity):
            """
            Information about a single DNIS mapping. There is a
            unique DNIS map name. New DNIS mapping can be created
            using cvDnisMappingStatus.
            
            The entry can be created with or without a file location 
            specified by cvDnisMappingUrl. The mapping file contains
            DNIS name and VXML page per line. For example, a 
            cvDnisMappingUrl could be tftp\://someserver/dnismap.txt.
            This file is a text file and the content format is
              dnis <dnisname> url <urlname>.
            An example of the contents of the file itself can be
              dnis 18004251234 url http\://www.b.com/p/vwelcome.vxml
              dnis 18004253421 url http\://www.c.com/j/vxmlintf.vxml
            If a mapping file location is specified, then new rows
            corresponding to this map name are created and populated
            in cvDnisNodeTable from the contents of the file. The
            rows corresponding to this map name in cvDnisNodeTable
            cannot be created or modified or deleted but can be
            read. 
            
            If a mapping file location is not specified in
            cvDnisMappingUrl, then individual DNIS entries
            corresponding to this map name can be created, modified
            and deleted in cvDnisNodeTable. 
            
            Deleting an entry deletes all the related entries in
            cvDnisNodeTable. 
            
            .. attribute:: cvdnismappingname  (key)
            
            	The name which uniquely identifies a DNIS mapping. 
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: cvdnismappingurl
            
            	The url specifies a file location. The file contains individual DNIS entries that belong to the DNIS map  name specified by cvDnisMappingName.  Once a url is created and associated with a map name (the association is complete when the row is made active(1)), it cannot be modified while cvDnisMappingStatus is active. If a different url needs to be associated with the current map name, the row status should be made notInService(2) and this object has to be modified to associate a new url. When a new association is made all the DNIS entries corresponding to the old association will be deleted from the cvDnisNodeTable.  The url is read when the row status is made active(1) or when the row status is active and the object   cvDnisMappingRefresh is explicitly set to refresh(2).   If the url is not accessible then a cvDnisMappingUrlInaccessible notification will be generted. 
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvdnismappingrefresh
            
            	Whenever there is a need to re\-read the contents of the file specified by cvDnisMappingUrl, this object can be set to refresh(2). This will cause the contents of the file to be re\-read and correspondingly update the cvDnisNodeTable. After the completion of this operation, the value of this object is reset to idle(1). The only operation allowed on this object is setting it to refresh(2). This can only be done when the current value is idle(1) and the rowstatus is active(1).  idle       \- The refreshing process is idle and the user              can modify this object to refresh. refresh    \- The refreshing process is currently busy and              the user have to wait till the object              becomes idle to issue new refresh
            	**type**\:  :py:class:`CvDnisMappingRefresh <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry.CvDnisMappingRefresh>`
            
            	**config**\: False
            
            .. attribute:: cvdnismappingurlaccesserror
            
            	ASCII text describing the error on last access of the url specified in cvDnisMappingUrl.  If the url access does not succeed, then this object is populated with an error message indicating the reason for failure. If the url access succeeds, this object is set to null string
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvdnismappingstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table. When making the status active(1), if a valid cvDnisMappingUrl is present the contents of the url is downloaded and during that time cvDnisMappingRefresh is set to refresh(2). When cvDnisMappingRefresh is set to refresh(2), only the destroy(6) operation is allowed
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VOICE-DNIS-MIB'
            _revision = '2002-05-01'

            def __init__(self):
                super(CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry, self).__init__()

                self.yang_name = "cvDnisMappingEntry"
                self.yang_parent_name = "cvDnisMappingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvdnismappingname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvdnismappingname', (YLeaf(YType.str, 'cvDnisMappingName'), ['str'])),
                    ('cvdnismappingurl', (YLeaf(YType.str, 'cvDnisMappingUrl'), ['str'])),
                    ('cvdnismappingrefresh', (YLeaf(YType.enumeration, 'cvDnisMappingRefresh'), [('ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CISCOVOICEDNISMIB', 'CvDnisMappingTable.CvDnisMappingEntry.CvDnisMappingRefresh')])),
                    ('cvdnismappingurlaccesserror', (YLeaf(YType.str, 'cvDnisMappingUrlAccessError'), ['str'])),
                    ('cvdnismappingstatus', (YLeaf(YType.enumeration, 'cvDnisMappingStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cvdnismappingname = None
                self.cvdnismappingurl = None
                self.cvdnismappingrefresh = None
                self.cvdnismappingurlaccesserror = None
                self.cvdnismappingstatus = None
                self._segment_path = lambda: "cvDnisMappingEntry" + "[cvDnisMappingName='" + str(self.cvdnismappingname) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/cvDnisMappingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry, ['cvdnismappingname', 'cvdnismappingurl', 'cvdnismappingrefresh', 'cvdnismappingurlaccesserror', 'cvdnismappingstatus'], name, value)

            class CvDnisMappingRefresh(Enum):
                """
                CvDnisMappingRefresh (Enum Class)

                Whenever there is a need to re\-read the contents of the

                file specified by cvDnisMappingUrl, this object can be

                set to refresh(2). This will cause the contents of the

                file to be re\-read and correspondingly update the

                cvDnisNodeTable. After the completion of this operation,

                the value of this object is reset to idle(1). The only

                operation allowed on this object is setting it to

                refresh(2). This can only be done when the current value

                is idle(1) and the rowstatus is active(1).

                idle       \- The refreshing process is idle and the user

                             can modify this object to refresh.

                refresh    \- The refreshing process is currently busy and

                             the user have to wait till the object

                             becomes idle to issue new refresh.

                .. data:: idle = 1

                .. data:: refresh = 2

                """

                idle = Enum.YLeaf(1, "idle")

                refresh = Enum.YLeaf(2, "refresh")





    class CvDnisNodeTable(Entity):
        """
        The table contains a DNIS name and a url. The url is a
        pointer to a VXML page for the DNIS name. 
        
        .. attribute:: cvdnisnodeentry
        
        	Each entry is a DNIS name and the location of the associated VXML page. New DNIS entries can be created or the existing entries can be modified or deleted only if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object.   If a file name is provided in cvDnisMappingUrl corresponding to this entry's map name, then this row will have read permission only
        	**type**\: list of  		 :py:class:`CvDnisNodeEntry <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisNodeTable.CvDnisNodeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VOICE-DNIS-MIB'
        _revision = '2002-05-01'

        def __init__(self):
            super(CISCOVOICEDNISMIB.CvDnisNodeTable, self).__init__()

            self.yang_name = "cvDnisNodeTable"
            self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvDnisNodeEntry", ("cvdnisnodeentry", CISCOVOICEDNISMIB.CvDnisNodeTable.CvDnisNodeEntry))])
            self._leafs = OrderedDict()

            self.cvdnisnodeentry = YList(self)
            self._segment_path = lambda: "cvDnisNodeTable"
            self._absolute_path = lambda: "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICEDNISMIB.CvDnisNodeTable, [], name, value)


        class CvDnisNodeEntry(Entity):
            """
            Each entry is a DNIS name and the location of the
            associated VXML page. New DNIS entries can be created or
            the existing entries can be modified or deleted only if
            the corresponding map name (defined in
            cvDnisMappingTable) does not have any file name provided
            in the cvDnisMappingUrl object. 
            
            If a file name is provided in cvDnisMappingUrl
            corresponding to this entry's map name, then this row
            will have read permission only.
            
            .. attribute:: cvdnismappingname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`cvdnismappingname <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CISCOVOICEDNISMIB.CvDnisMappingTable.CvDnisMappingEntry>`
            
            	**config**\: False
            
            .. attribute:: cvdnisnumber  (key)
            
            	The individual DNIS name. It is unique within a DNIS mapping
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvdnisnodeurl
            
            	The url specifies a VXML page. This page contains voice XML links to play audio data.  This url which is a VXML page is not read immediately when the row is made active(1), but only when a call that requires the use of this DNIS comes through
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvdnisnodemodifiable
            
            	This object specifies whether the object in a particular row is modifiable. The object is set to true(1) if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object. Otherwise this object is set to false(2) and the row becomes read only.  
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cvdnisnodestatus
            
            	This object is used to create a new row or modify or delete an existing row in this table. The objects in a row can be modified or deleted while the row status is active(1) and cvDnisNodeModifiable is true(1). The row status cannot be set to notInService(2) or createAndWait(5). 
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VOICE-DNIS-MIB'
            _revision = '2002-05-01'

            def __init__(self):
                super(CISCOVOICEDNISMIB.CvDnisNodeTable.CvDnisNodeEntry, self).__init__()

                self.yang_name = "cvDnisNodeEntry"
                self.yang_parent_name = "cvDnisNodeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvdnismappingname','cvdnisnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvdnismappingname', (YLeaf(YType.str, 'cvDnisMappingName'), ['str'])),
                    ('cvdnisnumber', (YLeaf(YType.str, 'cvDnisNumber'), ['str'])),
                    ('cvdnisnodeurl', (YLeaf(YType.str, 'cvDnisNodeUrl'), ['str'])),
                    ('cvdnisnodemodifiable', (YLeaf(YType.boolean, 'cvDnisNodeModifiable'), ['bool'])),
                    ('cvdnisnodestatus', (YLeaf(YType.enumeration, 'cvDnisNodeStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cvdnismappingname = None
                self.cvdnisnumber = None
                self.cvdnisnodeurl = None
                self.cvdnisnodemodifiable = None
                self.cvdnisnodestatus = None
                self._segment_path = lambda: "cvDnisNodeEntry" + "[cvDnisMappingName='" + str(self.cvdnismappingname) + "']" + "[cvDnisNumber='" + str(self.cvdnisnumber) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/cvDnisNodeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICEDNISMIB.CvDnisNodeTable.CvDnisNodeEntry, ['cvdnismappingname', 'cvdnisnumber', 'cvdnisnodeurl', 'cvdnisnodemodifiable', 'cvdnisnodestatus'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOVOICEDNISMIB()
        return self._top_entity



