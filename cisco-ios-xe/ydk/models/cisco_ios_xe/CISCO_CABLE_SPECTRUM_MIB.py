""" CISCO_CABLE_SPECTRUM_MIB 

This is the MIB Module for Cable Spectrum Management for
DOCSIS\-compliant Cable Modem Termination Systems (CMTS).

Spectrum management is a software/hardware feature provided
in the CMTS so that the CMTS may sense both downstream and
upstream plant impairments, report them to a management
entity, and automatically mitigate them where possible.

The CMTS directly senses upstream transmission errors.It
may also indirectly monitor the condition of the plant by
keeping a record of modem state changes.  It is desireable
to perform these functions without reducing throughput or
latency and without creating additional packet overhead on
the RF plant.

The purpose of cable Spectrum Management is to prevent long
term service interruptions caused by upstream noise events
in the cable plant.  It is also used for fault management
and trouble shooting the cable network.  When modems are
detected to go on\-line and off\-line by flap detectors, the
cable operators can look at the flap list and spectrum
tables to determine the possible causes.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CCSRequestOperState(Enum):
    """
    CCSRequestOperState (Enum Class)

    The CCSRequestOperState is used to represent the current test

    status.

    It has the following defined values\:

    \- 'idle', which indicates the test has not been initiated;

    \- 'pending', which indicates the test is in the pending queue;

    \- 'running', which indicates the test is in process;

    \- 'noError', which indicates the test has completed

      without error;

    \- 'aborted', which indicates the test was stopped

      before the test was completed;

    \- 'notOnLine', which indicates the Mac Address

      is not online;

    \- 'invalidMac', which indicates the Mac Address

      is not valid;

    \- 'timeOut', which indicates timeout has occurred while

      receiving data from DSP;

    \- 'fftBusy', which indicates the FFT is busy;

    \- 'fftFailed', which indicates the FFT is failed due to

      a hardware problem;

    \- 'others', other errors;

    .. data:: idle = 0

    .. data:: pending = 1

    .. data:: running = 2

    .. data:: noError = 3

    .. data:: aborted = 4

    .. data:: notOnLine = 5

    .. data:: invalidMac = 6

    .. data:: timeOut = 7

    .. data:: fftBusy = 8

    .. data:: fftFailed = 9

    .. data:: others = 10

    """

    idle = Enum.YLeaf(0, "idle")

    pending = Enum.YLeaf(1, "pending")

    running = Enum.YLeaf(2, "running")

    noError = Enum.YLeaf(3, "noError")

    aborted = Enum.YLeaf(4, "aborted")

    notOnLine = Enum.YLeaf(5, "notOnLine")

    invalidMac = Enum.YLeaf(6, "invalidMac")

    timeOut = Enum.YLeaf(7, "timeOut")

    fftBusy = Enum.YLeaf(8, "fftBusy")

    fftFailed = Enum.YLeaf(9, "fftFailed")

    others = Enum.YLeaf(10, "others")


class CCSRequestOperation(Enum):
    """
    CCSRequestOperation (Enum Class)

    The CCSRequestOperation is used to control various spectrum

    tests.  It has the following defined values\:

    \- 'none', initial value at row creation

              and also indicates test completion;

    \- 'start', which is used to start the test;

    \- 'abort', which is used to abort the test;

    .. data:: none = 0

    .. data:: start = 1

    .. data:: abort = 2

    """

    none = Enum.YLeaf(0, "none")

    start = Enum.YLeaf(1, "start")

    abort = Enum.YLeaf(2, "abort")



class CISCOCABLESPECTRUMMIB(Entity):
    """
    
    
    .. attribute:: ccsflapobjects
    
    	
    	**type**\:  :py:class:`CcsFlapObjects <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsFlapObjects>`
    
    .. attribute:: ccsflaptable
    
    	This table keeps the records of modem state changes. It can be used to identify the problematic cable modems. An entry can be deleted from the table but can not be added to the table
    	**type**\:  :py:class:`CcsFlapTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsFlapTable>`
    
    	**status**\: deprecated
    
    .. attribute:: ccscmflaptable
    
    	This table keeps the records of modem state changes, so it can be used to identify the problematic cable  modems. An entry per modem is added to the table automatically  by the system when it detects any state changes to the modem.  Therefore, it can be deleted but  can not be added by the management system
    	**type**\:  :py:class:`CcsCmFlapTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsCmFlapTable>`
    
    .. attribute:: ccsspectrumrequesttable
    
    	This table contains the spectrum data requests.  There are two types of request\: background noise and SNR. Refer to ccsSpectrumRequestIfIndex and ccsSpectrumRequestMacAddr DESCRIPTIONS on how the type of request is determined
    	**type**\:  :py:class:`CcsSpectrumRequestTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable>`
    
    .. attribute:: ccsspectrumdatatable
    
    	This table contains the receiving power or background noise measurement based on the criteria that is set in the ccsSpectrumRequestEntry
    	**type**\:  :py:class:`CcsSpectrumDataTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable>`
    
    .. attribute:: ccssnrrequesttable
    
    	A table of CNR requests
    	**type**\:  :py:class:`CcsSNRRequestTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSNRRequestTable>`
    
    .. attribute:: ccsupinspecgrouptable
    
    	This table contains the cable upstream interfaces assigned to a spectrum group. A spectrum group contains one or more fixed frequencies or frequency bands which can be assigned to cable upstream interfaces in the spectrum group
    	**type**\:  :py:class:`CcsUpInSpecGroupTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable>`
    
    .. attribute:: ccsupinfibernodetable
    
    	This table contains the cable upstream interfaces in a fiber\-node.Each fiber\-node uniquely represents an RF domain.Cable upstream interfaces in the same fiber\-node are physically combined together into the same RF domain
    	**type**\:  :py:class:`CcsUpInFiberNodeTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable>`
    
    .. attribute:: ccsupspecmgmttable
    
    	This table contains the attributes of the cable upstream interfaces, ifType of docsCableUpstream(129), to be used for improving performance and proactive hopping.  Proactive hopping is achieved by setting the SNR  polling period over the in\-use band without CM signals
    	**type**\:  :py:class:`CcsUpSpecMgmtTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable>`
    
    .. attribute:: ccsspecgroupfreqtable
    
    	This table contains the frequency and band configuration of the spectrum group
    	**type**\:  :py:class:`CcsSpecGroupFreqTable <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable>`
    
    

    """

    _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
    _revision = '2011-04-08'

    def __init__(self):
        super(CISCOCABLESPECTRUMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CABLE-SPECTRUM-MIB"
        self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ccsFlapObjects", ("ccsflapobjects", CISCOCABLESPECTRUMMIB.CcsFlapObjects)), ("ccsFlapTable", ("ccsflaptable", CISCOCABLESPECTRUMMIB.CcsFlapTable)), ("ccsCmFlapTable", ("ccscmflaptable", CISCOCABLESPECTRUMMIB.CcsCmFlapTable)), ("ccsSpectrumRequestTable", ("ccsspectrumrequesttable", CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable)), ("ccsSpectrumDataTable", ("ccsspectrumdatatable", CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable)), ("ccsSNRRequestTable", ("ccssnrrequesttable", CISCOCABLESPECTRUMMIB.CcsSNRRequestTable)), ("ccsUpInSpecGroupTable", ("ccsupinspecgrouptable", CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable)), ("ccsUpInFiberNodeTable", ("ccsupinfibernodetable", CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable)), ("ccsUpSpecMgmtTable", ("ccsupspecmgmttable", CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable)), ("ccsSpecGroupFreqTable", ("ccsspecgroupfreqtable", CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable))])
        self._leafs = OrderedDict()

        self.ccsflapobjects = CISCOCABLESPECTRUMMIB.CcsFlapObjects()
        self.ccsflapobjects.parent = self
        self._children_name_map["ccsflapobjects"] = "ccsFlapObjects"

        self.ccsflaptable = CISCOCABLESPECTRUMMIB.CcsFlapTable()
        self.ccsflaptable.parent = self
        self._children_name_map["ccsflaptable"] = "ccsFlapTable"

        self.ccscmflaptable = CISCOCABLESPECTRUMMIB.CcsCmFlapTable()
        self.ccscmflaptable.parent = self
        self._children_name_map["ccscmflaptable"] = "ccsCmFlapTable"

        self.ccsspectrumrequesttable = CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable()
        self.ccsspectrumrequesttable.parent = self
        self._children_name_map["ccsspectrumrequesttable"] = "ccsSpectrumRequestTable"

        self.ccsspectrumdatatable = CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable()
        self.ccsspectrumdatatable.parent = self
        self._children_name_map["ccsspectrumdatatable"] = "ccsSpectrumDataTable"

        self.ccssnrrequesttable = CISCOCABLESPECTRUMMIB.CcsSNRRequestTable()
        self.ccssnrrequesttable.parent = self
        self._children_name_map["ccssnrrequesttable"] = "ccsSNRRequestTable"

        self.ccsupinspecgrouptable = CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable()
        self.ccsupinspecgrouptable.parent = self
        self._children_name_map["ccsupinspecgrouptable"] = "ccsUpInSpecGroupTable"

        self.ccsupinfibernodetable = CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable()
        self.ccsupinfibernodetable.parent = self
        self._children_name_map["ccsupinfibernodetable"] = "ccsUpInFiberNodeTable"

        self.ccsupspecmgmttable = CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable()
        self.ccsupspecmgmttable.parent = self
        self._children_name_map["ccsupspecmgmttable"] = "ccsUpSpecMgmtTable"

        self.ccsspecgroupfreqtable = CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable()
        self.ccsspecgroupfreqtable.parent = self
        self._children_name_map["ccsspecgroupfreqtable"] = "ccsSpecGroupFreqTable"
        self._segment_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOCABLESPECTRUMMIB, [], name, value)


    class CcsFlapObjects(Entity):
        """
        
        
        .. attribute:: ccsflaplistmaxsize
        
        	The maximum number of flapped modem entries (ccsCmFlapEntry) per Cable downstream interface that  can be reported in the ccsCmFlapTable.  If the Cable downstream interface has more flapped modems than the ccsFlapListMaxSize, some of the flapped modems  will not be shown in the ccsCmFlapTable.  In this case, the users may want to increase the ccsFlapMaxSize
        	**type**\: int
        
        	**range:** 1..65536
        
        	**units**\: modems
        
        .. attribute:: ccsflaplistcurrentsize
        
        	The total number of flapped modem entries (ccsCmFlapEntry) that reported in the ccsCmFlapTable.  The maximum value  will be ccsFlapListMaxSize \* <no of downstreams>
        	**type**\: int
        
        	**range:** 0..65536
        
        	**units**\: modems
        
        .. attribute:: ccsflapaging
        
        	The flap entry aging threshold.  Periodically, the aging process scans through the flap list and removes the cable modems that have not flapped for that many minutes
        	**type**\: int
        
        	**range:** 1..86400
        
        	**units**\: minutes
        
        .. attribute:: ccsflapinsertiontime
        
        	The insertion\-time is an empirically derived, worst\-case number of seconds which the cable modem requires to complete registration.  The time taken by cable modems to complete their registration is measured by the cable operators and this information helps to determine the insertion time.  If the cable modem has not completed the registration stage within this insertion\-time setting, the cable modem will be inserted into the flap\-list
        	**type**\: int
        
        	**range:** 60..86400
        
        	**units**\: seconds
        
        .. attribute:: ccsflappoweradjustthreshold
        
        	The power adjust threshold.  When the power of the modem is adjusted beyond this threshold, the modem will be inserted into the flap\-list
        	**type**\: int
        
        	**range:** 1..10
        
        	**units**\: db
        
        	**status**\: deprecated
        
        .. attribute:: ccsflapmissthreshold
        
        	Per modem miss threshold which triggers polling flap detector. When the number of times a cable modem does not acknowledge a  MAC\-layer keepalive message from a cable modem card exceeds the  miss threshold, the cable modem is placed in the flap list
        	**type**\: int
        
        	**range:** 1..12
        
        	**status**\: deprecated
        
        .. attribute:: ccsflapresetall
        
        	Setting this object to true(1) causes ccsFlapInsertionFailNum, ccsFlapHitNum, ccsFlapMissNum, ccsFlapCrcErrorNum,  ccsFlapPowerAdjustmentNum and ccsFlapTotalNum objects of each entry in ccsFlapTable to be started from zero. Reading this  object always returns false(2)
        	**type**\: bool
        
        	**status**\: deprecated
        
        .. attribute:: ccsflapclearall
        
        	Setting this object to true(1) removes all cable modems from flap\-list and all the entries in the ccsFlapTable are destroyed. If a modem keeps flapping, the modem will be added again into the flap list and a new entry in the ccsFlapTable will be created.  The newly created entry for that modem will have new value of ccsFlapCreateTime and all the statistical objects will be started from zero. Reading this object always returns false(2)
        	**type**\: bool
        
        	**status**\: deprecated
        
        .. attribute:: ccsflaplastcleartime
        
        	The last time that all the entries in the ccsFlapTable are destroyed. There are several ways to destroy all the entries in the ccsFlapTable. Setting the object ccsFlapClearAll to true is one way, and the other way is through Command Line Interface. This timestamp can be used to know when all the entries in the ccsFlapTable are destroyed. The special value of all '00'Hs indicates that the entries in the ccsFlapTable have never been destroyed
        	**type**\: str
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsFlapObjects, self).__init__()

            self.yang_name = "ccsFlapObjects"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccsflaplistmaxsize', (YLeaf(YType.int32, 'ccsFlapListMaxSize'), ['int'])),
                ('ccsflaplistcurrentsize', (YLeaf(YType.uint32, 'ccsFlapListCurrentSize'), ['int'])),
                ('ccsflapaging', (YLeaf(YType.int32, 'ccsFlapAging'), ['int'])),
                ('ccsflapinsertiontime', (YLeaf(YType.int32, 'ccsFlapInsertionTime'), ['int'])),
                ('ccsflappoweradjustthreshold', (YLeaf(YType.int32, 'ccsFlapPowerAdjustThreshold'), ['int'])),
                ('ccsflapmissthreshold', (YLeaf(YType.uint32, 'ccsFlapMissThreshold'), ['int'])),
                ('ccsflapresetall', (YLeaf(YType.boolean, 'ccsFlapResetAll'), ['bool'])),
                ('ccsflapclearall', (YLeaf(YType.boolean, 'ccsFlapClearAll'), ['bool'])),
                ('ccsflaplastcleartime', (YLeaf(YType.str, 'ccsFlapLastClearTime'), ['str'])),
            ])
            self.ccsflaplistmaxsize = None
            self.ccsflaplistcurrentsize = None
            self.ccsflapaging = None
            self.ccsflapinsertiontime = None
            self.ccsflappoweradjustthreshold = None
            self.ccsflapmissthreshold = None
            self.ccsflapresetall = None
            self.ccsflapclearall = None
            self.ccsflaplastcleartime = None
            self._segment_path = lambda: "ccsFlapObjects"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsFlapObjects, ['ccsflaplistmaxsize', 'ccsflaplistcurrentsize', 'ccsflapaging', 'ccsflapinsertiontime', 'ccsflappoweradjustthreshold', 'ccsflapmissthreshold', 'ccsflapresetall', 'ccsflapclearall', 'ccsflaplastcleartime'], name, value)


    class CcsFlapTable(Entity):
        """
        This table keeps the records of modem state changes.
        It can be used to identify the problematic cable modems.
        An entry can be deleted from the table but can not be
        added to the table.
        
        .. attribute:: ccsflapentry
        
        	List of attributes for an entry in the ccsFlapTable. An entry in this table exists for each cable modem that triggered one of our flap detectors
        	**type**\: list of  		 :py:class:`CcsFlapEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsFlapTable.CcsFlapEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsFlapTable, self).__init__()

            self.yang_name = "ccsFlapTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsFlapEntry", ("ccsflapentry", CISCOCABLESPECTRUMMIB.CcsFlapTable.CcsFlapEntry))])
            self._leafs = OrderedDict()

            self.ccsflapentry = YList(self)
            self._segment_path = lambda: "ccsFlapTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsFlapTable, [], name, value)


        class CcsFlapEntry(Entity):
            """
            List of attributes for an entry in the ccsFlapTable.
            An entry in this table exists for each cable modem that
            triggered one of our flap detectors.
            
            .. attribute:: ccsflapmacaddr  (key)
            
            	MAC address of the Cable Modem's Cable interface which identifies a flap\-list entry for a flapping  Cable Modem
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapupstreamifindex
            
            	The ifIndex of the Cable upstream interface whose ifType is docsCableUpstream(129).  The CMTS detects a flapping Cable Modem from its Cable upstream interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapdownstreamifindex
            
            	The ifIndex of the Cable downstream interface whose ifType is docsCableDownstream(128)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapinsertionfails
            
            	The number of times a Cable Modem registered more frequently than expected.  Excessive registration is defined as the presence of a time span between two successive registration cycles which is less than a threshold span (ccsFlapInsertionTime).  A Cable Modem may fail the ranging or registration process due to not being able to get an IP address. When the Cable Modem can not finish registration within the insertion time, it retries the process and sends the Initial Maintenance packet again. CMTS will receive the Initial Maintenance packet from the Cable Modem sooner than expected and the Cable Modem is considered a flapping modem.  This count may indicate\:     Intermittent downstream sync loss, or     DHCP or modem registration problems.  The Flap Count (ccsFlapTotal) will be incremented when this counter is incremented.  Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaphits
            
            	The number of times the CMTS receives the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance transmit opportunity at a typical rate of once every 10 seconds and waits for a Ranging request from the Cable Modem.If the CMTS receives a Ranging request then the Hit count will be increased by 1  If the FlapTotal count is high,both Hits and Misses counts are high, and other counters are relatively low then the flapping is probably caused by the modem going up and down. The Hits and Misses counts are keep\-alive polling statistics. The Hits count should be much greater than the Misses count  Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapmisses
            
            	The number of times the CMTS misses the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance packet every 10 seconds and waits for a Ranging request from the Cable Modem. If the CMTS misses a Ranging request within 25 msec then the Misses count will be incremented.  If ccsFlapTotal is high, Hits and Misses are high but ccsFlapPowerAdjustments and ccsFlapInsertionFails are low then the flapping is probably caused by the modem going up and down.  Miss counts can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces  less output, until finally there is no more increase in  output.  This phenomena is called laser clipping.  Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapcrcerrors
            
            	The number of times the CMTS upstream receiver flagged a packet with a CRC error.  If ccsFlapCrcErrors is high, it indicates the cable upstream may have high noise level.  The modem may not be flapping yet but it may be a potential problem.  This count can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces  less output, until finally there is no more increase in  output.  This phenomena is called laser clipping. Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflappoweradjustments
            
            	The number of times the Cable Modem upstream transmit power is adjusted during station maintenance.  When the adjustment is greater than the power adjustment threshold the counter will be incremented. The power adjustment threshold is chosen in an implementation\-dependent manner.  The Flap Count (ccsFlapTotal) will be incremented when this counter is incremented.  If ccsFlapTotal is high, ccsFlapPowerAdjustments is high but the Hits and Misses are low and ccsFlapInsertionFails are low then the flapping is probably caused by an improper transmit power level setting at the modem end.  This count can indicate\:     Amplifier degradation,     Poor connections, or     Wind, moisture, or temperature sensitivity.  Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaptotal
            
            	Whenever the Cable Modem passes flap detection, then the flap counter is increased.  There are 3 flap detectors defined\: (1) When ccsFlapInsertionFails is increased the Flap count     will be increased. (2) When the CMTS receives a Miss followed by a Hit     then the Flap count will be increased. (3) When ccsFlapPowerAdjustments is increased the Flap     count will be increased.  Discontinuites in the value of this counter can occur if this entry is removed from the table and then re\-added, and are indicated by a change in the value of ccsFlapCreateTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaplastflaptime
            
            	The flap time is set whenever the Cable Modem triggers a flap detector
            	**type**\: str
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapcreatetime
            
            	The time that this entry was added to the table. If an entry is removed and then later re\-added, there may be a discontinuity in the counters associated with this entry. This timestamp can be used to detect those  discontinuities
            	**type**\: str
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaprowstatus
            
            	Controls and reflects the status of rows in this table.  When a cable modem triggers a flap detector, if an entry does not already exist for this cable modem, and ccsFlapListCurrentSize is less than ccsFlapListMaxSize, then an entry will be created in this table. The new  instance of this object will be set to active(1).  All  flapping modems have the status of active(1).  Active entries are removed from the table after they have not triggered any additional flap detectors for the period of time defined in ccsFlapAging. Alternatively, setting this instance to destroy(6) will remove the entry immediately.  createAndGo(4) and createAndWait(5) are not supported
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapinsertionfailnum
            
            	The number of times a Cable Modem registered more frequently than expected.  Excessive registration is defined as the presence of a time span between two successive registration cycles which is less than a threshold span (ccsFlapInsertionTime).  A Cable Modem may fail the ranging or registration process due to not being able to get an IP address. When the Cable Modem can not finish registration within the insertion time, it retries the process and sends the Initial Maintenance packet again. CMTS will receive the Initial Maintenance packet from the Cable Modem sooner than expected and the Cable Modem is considered a flapping modem.  This object may indicate\:     Intermittent downstream sync loss, or     DHCP or modem registration problems.  The Flap number (ccsFlapTotalNum) will be incremented when this object is incremented.  This object is going to replace the object ccsFlapInsertionFails and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if a user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaphitnum
            
            	The number of times the CMTS receives the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance transmit opportunity at a typical rate of once every 10 seconds and waits for a Ranging request from the Cable Modem. If the CMTS receives a Ranging request then the Hit number will be increased by 1  If the FlapTotal object is high, both Hit and Miss objects are high, and other statistical objects are relatively low then the flapping is probably caused by the modem going up and down. The Hit and Miss objects keep\-alive polling statistics. The Hit object should be much greater than the Misses count.  This object is going to replace the object ccsFlapHits and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if an user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapmissnum
            
            	The number of times the CMTS misses the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance packet every 10 seconds and waits for a Ranging request from the Cable Modem. If the CMTS misses a Ranging request within 25 msec then the Miss Object will be incremented.  If ccsFlapTotalNum is high, Hit and Miss are high but ccsFlapPowerAdjustmentNum and ccsFlapInsertionFailNum are low then the flapping is probably caused by the modem going up and down.  Miss object can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces less output, until finally there is no more increase in output. This phenomena is called laser clipping.  This object is going to replace the object ccsFlapMisses and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if an user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapcrcerrornum
            
            	The number of times the CMTS upstream receiver flagged a packet with a CRC error.  If ccsFlapCrcErrorNum is high, it indicates the cable upstream may have high noise level. The modem may not be flapping yet but it may be a potential problem.  This object can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces  less output, until finally there is no more increase in  output.  This phenomena is called laser clipping.  This object is going to replace the object ccsFlapCrcErrors and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if a user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflappoweradjustmentnum
            
            	The number of times the Cable Modem upstream transmit power is adjusted during station maintenance.  When the adjustment  is greater than the power adjustment threshold the number  will be incremented. The power adjustment threshold is chosen  in an implementation\-dependent manner  The Flap number (ccsFlapTotalNum) will be incremented when this object is incremented.  If ccsFlapTotalNum is high, ccsFlapPowerAdjustmentNum is high but the Hit and Miss are low and ccsFlapInsertionFailNum are low then the flapping is probably caused by an improper transmit power level setting at the modem end.  This object can indicate\:     Amplifier degradation,     Poor connections, or     Wind, moisture, or temperature sensitivity.  This object is going to replace the object ccsFlapPowerAdjustments and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if a user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaptotalnum
            
            	Whenever the Cable Modem passes flap detection, then the flap number is increased.  There are 3 flap detectors defined\: (1) When ccsFlapInsertionFailNum is increased the Flap number     will be increased. (2) When the CMTS receives a Miss followed by a Hit     then the Flap number will be increased. (3) When ccsFlapPowerAdjustmentNum is increased the Flap     number will be increased.  This object is going to replace the object ccsFlapTotal and the value of this object can be reset to zero if this entry is removed from the table and then re\-added, or if an user resets all the statistical objects for this entry. The value of the object ccsFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ccsflapresetnow
            
            	Setting this object to true(1) will set the following objects of this entry to 0\: ccsFlapInsertionFailsNum, ccsFlapHitsNum, ccsFlapMissesNum, ccsFlapCrcErrorsNum, ccsFlapPowerAdjustmentsNum and ccsFlapTotalNum. Setting this object to true does not destroy the entry, so the ccsFlapCreateTime will be unchanged. Reading this object always returns false(2)
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: ccsflaplastresettime
            
            	The last time that all the statistical objects of this entry are started from zero. There are several ways to restart the the statistical objects from zero. Setting the object ccsFlapResetNow or ccsFlapResetAll to true via SNMP is one way and and the other way is via command Line Interface. This timestamp can be used to know the last time the statistical objects are started from zero. The special value of all '00'Hs indicates that these statistical objects of this entry in the ccsFlapTable have never been reset
            	**type**\: str
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsFlapTable.CcsFlapEntry, self).__init__()

                self.yang_name = "ccsFlapEntry"
                self.yang_parent_name = "ccsFlapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsflapmacaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsflapmacaddr', (YLeaf(YType.str, 'ccsFlapMacAddr'), ['str'])),
                    ('ccsflapupstreamifindex', (YLeaf(YType.int32, 'ccsFlapUpstreamIfIndex'), ['int'])),
                    ('ccsflapdownstreamifindex', (YLeaf(YType.int32, 'ccsFlapDownstreamIfIndex'), ['int'])),
                    ('ccsflapinsertionfails', (YLeaf(YType.uint32, 'ccsFlapInsertionFails'), ['int'])),
                    ('ccsflaphits', (YLeaf(YType.uint32, 'ccsFlapHits'), ['int'])),
                    ('ccsflapmisses', (YLeaf(YType.uint32, 'ccsFlapMisses'), ['int'])),
                    ('ccsflapcrcerrors', (YLeaf(YType.uint32, 'ccsFlapCrcErrors'), ['int'])),
                    ('ccsflappoweradjustments', (YLeaf(YType.uint32, 'ccsFlapPowerAdjustments'), ['int'])),
                    ('ccsflaptotal', (YLeaf(YType.uint32, 'ccsFlapTotal'), ['int'])),
                    ('ccsflaplastflaptime', (YLeaf(YType.str, 'ccsFlapLastFlapTime'), ['str'])),
                    ('ccsflapcreatetime', (YLeaf(YType.str, 'ccsFlapCreateTime'), ['str'])),
                    ('ccsflaprowstatus', (YLeaf(YType.enumeration, 'ccsFlapRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ccsflapinsertionfailnum', (YLeaf(YType.uint32, 'ccsFlapInsertionFailNum'), ['int'])),
                    ('ccsflaphitnum', (YLeaf(YType.uint32, 'ccsFlapHitNum'), ['int'])),
                    ('ccsflapmissnum', (YLeaf(YType.uint32, 'ccsFlapMissNum'), ['int'])),
                    ('ccsflapcrcerrornum', (YLeaf(YType.uint32, 'ccsFlapCrcErrorNum'), ['int'])),
                    ('ccsflappoweradjustmentnum', (YLeaf(YType.uint32, 'ccsFlapPowerAdjustmentNum'), ['int'])),
                    ('ccsflaptotalnum', (YLeaf(YType.uint32, 'ccsFlapTotalNum'), ['int'])),
                    ('ccsflapresetnow', (YLeaf(YType.boolean, 'ccsFlapResetNow'), ['bool'])),
                    ('ccsflaplastresettime', (YLeaf(YType.str, 'ccsFlapLastResetTime'), ['str'])),
                ])
                self.ccsflapmacaddr = None
                self.ccsflapupstreamifindex = None
                self.ccsflapdownstreamifindex = None
                self.ccsflapinsertionfails = None
                self.ccsflaphits = None
                self.ccsflapmisses = None
                self.ccsflapcrcerrors = None
                self.ccsflappoweradjustments = None
                self.ccsflaptotal = None
                self.ccsflaplastflaptime = None
                self.ccsflapcreatetime = None
                self.ccsflaprowstatus = None
                self.ccsflapinsertionfailnum = None
                self.ccsflaphitnum = None
                self.ccsflapmissnum = None
                self.ccsflapcrcerrornum = None
                self.ccsflappoweradjustmentnum = None
                self.ccsflaptotalnum = None
                self.ccsflapresetnow = None
                self.ccsflaplastresettime = None
                self._segment_path = lambda: "ccsFlapEntry" + "[ccsFlapMacAddr='" + str(self.ccsflapmacaddr) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsFlapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsFlapTable.CcsFlapEntry, ['ccsflapmacaddr', 'ccsflapupstreamifindex', 'ccsflapdownstreamifindex', 'ccsflapinsertionfails', 'ccsflaphits', 'ccsflapmisses', 'ccsflapcrcerrors', 'ccsflappoweradjustments', 'ccsflaptotal', 'ccsflaplastflaptime', 'ccsflapcreatetime', 'ccsflaprowstatus', 'ccsflapinsertionfailnum', 'ccsflaphitnum', 'ccsflapmissnum', 'ccsflapcrcerrornum', 'ccsflappoweradjustmentnum', 'ccsflaptotalnum', 'ccsflapresetnow', 'ccsflaplastresettime'], name, value)


    class CcsCmFlapTable(Entity):
        """
        This table keeps the records of modem state changes,
        so it can be used to identify the problematic cable 
        modems.
        An entry per modem is added to the table automatically 
        by the system when it detects any state changes to
        the modem.  Therefore, it can be deleted but 
        can not be added by the management system.
        
        .. attribute:: ccscmflapentry
        
        	List of attributes for an entry in the ccsCmFlapTable. An entry in this table exists for each cable modem that triggered one of our flap detectors
        	**type**\: list of  		 :py:class:`CcsCmFlapEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsCmFlapTable.CcsCmFlapEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsCmFlapTable, self).__init__()

            self.yang_name = "ccsCmFlapTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsCmFlapEntry", ("ccscmflapentry", CISCOCABLESPECTRUMMIB.CcsCmFlapTable.CcsCmFlapEntry))])
            self._leafs = OrderedDict()

            self.ccscmflapentry = YList(self)
            self._segment_path = lambda: "ccsCmFlapTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsCmFlapTable, [], name, value)


        class CcsCmFlapEntry(Entity):
            """
            List of attributes for an entry in the ccsCmFlapTable.
            An entry in this table exists for each cable modem that
            triggered one of our flap detectors.
            
            .. attribute:: ccscmflapdownstreamifindex  (key)
            
            	The ifIndex of the Cable downstream interface whose ifType is docsCableDownstream(128)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccscmflapupstreamifindex  (key)
            
            	The ifIndex of the Cable upstream interface whose ifType is docsCableUpstream(129).  The CMTS detects a flapping Cable Modem from its Cable upstream interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccscmflapmacaddr  (key)
            
            	MAC address of the Cable Modem's Cable interface which identifies a flapping Cable Modem
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: ccscmflaplastflaptime
            
            	The flap time is set whenever the Cable Modem triggers a flap detector
            	**type**\: str
            
            .. attribute:: ccscmflapcreatetime
            
            	The time that this entry was added to the table. If an entry is removed and then later re\-added, there may be a discontinuity in the counters associated with this entry. This timestamp can be used to detect those  discontinuities
            	**type**\: str
            
            .. attribute:: ccscmflapinsertionfailnum
            
            	The number of times a Cable Modem registered more frequently than expected.  Excessive registration is defined as the presence of a time span between two successive registration cycles which is less than a threshold span (ccsFlapInsertionTime).  A Cable Modem may fail the ranging or registration process due to not being able to get an IP address. When the Cable Modem can not finish registration within the insertion time, it retries the process and sends the Initial Maintenance packet again. CMTS will receive the Initial Maintenance packet from the Cable Modem sooner than expected and the Cable Modem is considered a flapping modem.  This object may indicate\:     Intermittent downstream sync loss, or     DHCP or modem registration problems.  The Flap number (ccsCmFlapTotalNum) will be incremented when this object is incremented.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflaphitnum
            
            	The number of times the CMTS receives the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance transmit opportunity at a typical rate of once every 10 seconds and waits for a Ranging request from the Cable Modem. If the CMTS receives a Ranging request then the Hit number will be increased by 1  If the FlapTotal object is high, both Hit and Miss objects are high, and other statistical objects are relatively low then the flapping is probably caused by the modem going up and down. The Hit and Miss objects keep\-alive polling statistics. The Hit object should be much greater than the Misses count.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflapmissnum
            
            	The number of times the CMTS misses the Ranging request from the Cable Modem.  The CMTS issues a Station Maintenance packet every 10 seconds and waits for a Ranging request from the Cable Modem. If the CMTS misses a Ranging request within 25 msec then the Miss Object will be incremented.  If ccsCmFlapTotalNum is high, Hit and Miss are high but ccsCmFlapPowerAdjustmentNum and ccsCmFlapInsertionFailNum  are low then the flapping is probably caused by the modem  going up and down.  Miss object can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces less output, until finally there is no more increase in output. This phenomena is called laser clipping.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflapcrcerrornum
            
            	The number of times the CMTS upstream receiver flagged a packet with a CRC error.  If ccsCmFlapCrcErrorNum is high, it indicates the cable upstream may have high noise level. The modem may not be flapping yet but it may be a potential problem.  This object can indicate\:     Intermittent upstream,     Laser clipping, or     Noise bursts.  Laser clipping can happen if the signal power is too high when the upstream electrical signal is converted to an optical signal.  When it happens the more input produces less output, until finally there is no more increase in output. This phenomena is called laser clipping.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflappoweradjustmentnum
            
            	The number of times the Cable Modem upstream transmit power is adjusted during station maintenance. When the adjustment is greater than the power adjustment threshold the number will be incremented. The power adjustment threshold is chosen in an implementation\-dependent manner  The Flap number (ccsCmFlapTotalNum) will be incremented when this object is incremented.  If ccsCmFlapTotalNum is high, ccsCmFlapPowerAdjustmentNum is  high but the Hit and Miss are low and  ccsCmFlapInsertionFailNum are low then the flapping is  probably caused by an improper transmit power level  setting at the modem end.  This object can indicate\:     Amplifier degradation,     Poor connections, or     Wind, moisture, or temperature sensitivity.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflaptotalnum
            
            	Whenever the Cable Modem passes flap detection, then the flap number is increased.  There are 3 flap detectors defined\: (1) When ccsCmFlapInsertionFailNum is increased the Flap number     will be increased. (2) When the CMTS receives a Miss followed by a Hit     then the Flap number will be increased. (3) When ccsCmFlapPowerAdjustmentNum is increased the Flap     number will be increased.  The value of this object can be reset to zero if this entry  is removed from the table and then re\-added, or if the  ccsCmFlapResetNow object was set to true(1). The value of the  object ccsCmFlapLastResetTime indicates the last reset time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccscmflapresetnow
            
            	Setting this object to true(1) will set the value of certain objects in this table to 0 and does not destroy the entry, so the ccsCmFlapCreateTime will be  unchanged. Reading this object always returns false(2)
            	**type**\: bool
            
            .. attribute:: ccscmflaplastresettime
            
            	The last time that all the statistical objects of this entry are started from zero. There are several ways to restart the the statistical objects from zero. Setting the object ccsCmFlapResetNow or ccsCmFlapResetAll to true via SNMP is one way and and the other way is via command Line Interface. This timestamp can be used to know the last time the statistical objects are started from zero. The special value of all '00'Hs indicates that these statistical objects of this entry in the ccsCmFlapTable have never been reset
            	**type**\: str
            
            .. attribute:: ccscmflaprowstatus
            
            	Controls and reflects the status of rows in this table.  When a cable modem triggers a flap detector, if an entry does not already exist for this cable modem,  an entry will be created in this table.  The new instance of this object will be set to active(1).  All flapping modems have the status of active(1).  Active entries are removed from the table after they have not triggered any additional flap detectors for the period of time defined in ccsFlapAging. Alternatively, setting this instance to destroy(6) will remove the entry immediately.  createAndGo(4) and createAndWait(5) are not supported
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsCmFlapTable.CcsCmFlapEntry, self).__init__()

                self.yang_name = "ccsCmFlapEntry"
                self.yang_parent_name = "ccsCmFlapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccscmflapdownstreamifindex','ccscmflapupstreamifindex','ccscmflapmacaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccscmflapdownstreamifindex', (YLeaf(YType.int32, 'ccsCmFlapDownstreamIfIndex'), ['int'])),
                    ('ccscmflapupstreamifindex', (YLeaf(YType.int32, 'ccsCmFlapUpstreamIfIndex'), ['int'])),
                    ('ccscmflapmacaddr', (YLeaf(YType.str, 'ccsCmFlapMacAddr'), ['str'])),
                    ('ccscmflaplastflaptime', (YLeaf(YType.str, 'ccsCmFlapLastFlapTime'), ['str'])),
                    ('ccscmflapcreatetime', (YLeaf(YType.str, 'ccsCmFlapCreateTime'), ['str'])),
                    ('ccscmflapinsertionfailnum', (YLeaf(YType.uint32, 'ccsCmFlapInsertionFailNum'), ['int'])),
                    ('ccscmflaphitnum', (YLeaf(YType.uint32, 'ccsCmFlapHitNum'), ['int'])),
                    ('ccscmflapmissnum', (YLeaf(YType.uint32, 'ccsCmFlapMissNum'), ['int'])),
                    ('ccscmflapcrcerrornum', (YLeaf(YType.uint32, 'ccsCmFlapCrcErrorNum'), ['int'])),
                    ('ccscmflappoweradjustmentnum', (YLeaf(YType.uint32, 'ccsCmFlapPowerAdjustmentNum'), ['int'])),
                    ('ccscmflaptotalnum', (YLeaf(YType.uint32, 'ccsCmFlapTotalNum'), ['int'])),
                    ('ccscmflapresetnow', (YLeaf(YType.boolean, 'ccsCmFlapResetNow'), ['bool'])),
                    ('ccscmflaplastresettime', (YLeaf(YType.str, 'ccsCmFlapLastResetTime'), ['str'])),
                    ('ccscmflaprowstatus', (YLeaf(YType.enumeration, 'ccsCmFlapRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccscmflapdownstreamifindex = None
                self.ccscmflapupstreamifindex = None
                self.ccscmflapmacaddr = None
                self.ccscmflaplastflaptime = None
                self.ccscmflapcreatetime = None
                self.ccscmflapinsertionfailnum = None
                self.ccscmflaphitnum = None
                self.ccscmflapmissnum = None
                self.ccscmflapcrcerrornum = None
                self.ccscmflappoweradjustmentnum = None
                self.ccscmflaptotalnum = None
                self.ccscmflapresetnow = None
                self.ccscmflaplastresettime = None
                self.ccscmflaprowstatus = None
                self._segment_path = lambda: "ccsCmFlapEntry" + "[ccsCmFlapDownstreamIfIndex='" + str(self.ccscmflapdownstreamifindex) + "']" + "[ccsCmFlapUpstreamIfIndex='" + str(self.ccscmflapupstreamifindex) + "']" + "[ccsCmFlapMacAddr='" + str(self.ccscmflapmacaddr) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsCmFlapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsCmFlapTable.CcsCmFlapEntry, ['ccscmflapdownstreamifindex', 'ccscmflapupstreamifindex', 'ccscmflapmacaddr', 'ccscmflaplastflaptime', 'ccscmflapcreatetime', 'ccscmflapinsertionfailnum', 'ccscmflaphitnum', 'ccscmflapmissnum', 'ccscmflapcrcerrornum', 'ccscmflappoweradjustmentnum', 'ccscmflaptotalnum', 'ccscmflapresetnow', 'ccscmflaplastresettime', 'ccscmflaprowstatus'], name, value)


    class CcsSpectrumRequestTable(Entity):
        """
        This table contains the spectrum data requests.
        
        There are two types of request\: background noise and SNR.
        Refer to ccsSpectrumRequestIfIndex and ccsSpectrumRequestMacAddr
        DESCRIPTIONS on how the type of request is determined.
        
        .. attribute:: ccsspectrumrequestentry
        
        	Information about a spectrum data request.  The management system uses ccsSpectrumRequestStatus to control entry modification, creation, and deletion.  Setting ccsSpectrumRequestEntry to 'destroy' causes entry and its associated data (example\: ccsSpectrumDataEntry) to be cleaned up properly.  It is suggested the entry to be set to 'destroy' when the row is no longer in use
        	**type**\: list of  		 :py:class:`CcsSpectrumRequestEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable.CcsSpectrumRequestEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable, self).__init__()

            self.yang_name = "ccsSpectrumRequestTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsSpectrumRequestEntry", ("ccsspectrumrequestentry", CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable.CcsSpectrumRequestEntry))])
            self._leafs = OrderedDict()

            self.ccsspectrumrequestentry = YList(self)
            self._segment_path = lambda: "ccsSpectrumRequestTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable, [], name, value)


        class CcsSpectrumRequestEntry(Entity):
            """
            Information about a spectrum data request.  The management
            system uses ccsSpectrumRequestStatus to control entry
            modification, creation, and deletion.
            
            Setting ccsSpectrumRequestEntry to 'destroy' causes entry
            and its associated data (example\: ccsSpectrumDataEntry)
            to be cleaned up properly.  It is suggested the entry
            to be set to 'destroy' when the row is no longer in use.
            
            .. attribute:: ccsspectrumrequestindex  (key)
            
            	An arbitrary integer to uniquely identify the entry
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: ccsspectrumrequestifindex
            
            	The ifIndex of a docsCableUpstream(129) interface.  The background noise measurement is requested when ccsSpectrumRequestIfIndex is specified.  The receiving power measurement is requested when ccsSpectrumRequestMacAddr is specified; In this case, ccsSpectrumRequestIfIndex is the ifIndex of the remote CM's upstream
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ccsspectrumrequestmacaddr
            
            	A MAC address that identifies a remote CM.  The default value of 0000.0000.0000 indicates that the background noise will be measured for the upstream.  In this case, ccsSpectrumRequestIfIndex must be specified.  Other values indicate that the receiving power test is requested for the ccsSpectrumRequestMacAddr with CM signals
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: ccsspectrumrequestlowfreq
            
            	Start of frequency range.  The ccsSpectrumRequestLowFreq is adjusted slightly to accurately represent the actual starting point of the frequency range.  The adjustment is done as follows\:    aFactor = (center frequency \- ccsSpectrumRequestLowFreq)/12K   ccsSpectrumRequestLowFreq = center frequency \- (aFactor \* 12K)  where 12K is the FFT's bin size
            	**type**\: int
            
            	**range:** 5000..85000
            
            	**units**\: KHz
            
            .. attribute:: ccsspectrumrequestupperfreq
            
            	End of frequency range.  With the adjustment done to the ccsSpectrumRequestLowFreq, ccsSpectrumRequestUpperFreq will also be adjusted to the last frequency within the specified range divisible by the bin size.  Refer to the ccsSpectrumRequestLowFreq DESCRIPTION for the adjustment calculation
            	**type**\: int
            
            	**range:** 5000..85000
            
            	**units**\: KHz
            
            .. attribute:: ccsspectrumrequestresolution
            
            	A span between two frequencies.  ccsSpectrumRequestResolution dictates the amount of receiving power data to be returned in ccsSpectrumDataTable. The finer the resolution, the more data returned.  ccsSpectrumRequestResolution is adjusted to a value which is divisible by FFT's 12KHz bin size
            	**type**\: int
            
            	**range:** 12..37000
            
            	**units**\: KHz
            
            .. attribute:: ccsspectrumrequestoperation
            
            	The control that allows 'start' or 'abort' of the test.  Since there is only 1 FFT engine running on the CMTS, 'start' changes ccsSpectrumRequestOperState to 'pending' state if the FFT is busy; Otherwise, it changes ccsSpectrumRequestOperState to 'running'.  'abort' changes ccsSpectrumRequestOperState to 'aborted' state.  'abort' is only allowed when ccsSpectrumRequestOperState is in 'pending' state.  Only 'start' when request is to be started and 'abort' when request is to be aborted can be set by the user. It is set to 'none' only on completion of the request by the FFT engine.  Note\: The SNMP SET is rejected if ccsSpectrumRequestStatus is not 'active'
            	**type**\:  :py:class:`CCSRequestOperation <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CCSRequestOperation>`
            
            .. attribute:: ccsspectrumrequestoperstate
            
            	The operational state of the test.  ccsSpectrumRequestIfIndex, ccsSpectrumRequestMacAddr, ccsSpectrumRequestUpperFreq, ccsSpectrumRequestLowFreq and ccsSpectrumRequestResolution cannot be changed when CCSRequestOperState is in the 'running' state.  For a detailed description, see the CCSRequestOperState DESCRIPTION
            	**type**\:  :py:class:`CCSRequestOperState <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CCSRequestOperState>`
            
            .. attribute:: ccsspectrumrequeststarttime
            
            	The value of sysUpTime when the spectrum measurement operation starts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccsspectrumrequeststoppedtime
            
            	The value of sysUpTime when the spectrum measurement operation stops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccsspectrumrequeststatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules, see the ccsSpectrumRequestEntry DESCRIPTION
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable.CcsSpectrumRequestEntry, self).__init__()

                self.yang_name = "ccsSpectrumRequestEntry"
                self.yang_parent_name = "ccsSpectrumRequestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsspectrumrequestindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsspectrumrequestindex', (YLeaf(YType.int32, 'ccsSpectrumRequestIndex'), ['int'])),
                    ('ccsspectrumrequestifindex', (YLeaf(YType.int32, 'ccsSpectrumRequestIfIndex'), ['int'])),
                    ('ccsspectrumrequestmacaddr', (YLeaf(YType.str, 'ccsSpectrumRequestMacAddr'), ['str'])),
                    ('ccsspectrumrequestlowfreq', (YLeaf(YType.int32, 'ccsSpectrumRequestLowFreq'), ['int'])),
                    ('ccsspectrumrequestupperfreq', (YLeaf(YType.int32, 'ccsSpectrumRequestUpperFreq'), ['int'])),
                    ('ccsspectrumrequestresolution', (YLeaf(YType.int32, 'ccsSpectrumRequestResolution'), ['int'])),
                    ('ccsspectrumrequestoperation', (YLeaf(YType.enumeration, 'ccsSpectrumRequestOperation'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CCSRequestOperation', '')])),
                    ('ccsspectrumrequestoperstate', (YLeaf(YType.enumeration, 'ccsSpectrumRequestOperState'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CCSRequestOperState', '')])),
                    ('ccsspectrumrequeststarttime', (YLeaf(YType.uint32, 'ccsSpectrumRequestStartTime'), ['int'])),
                    ('ccsspectrumrequeststoppedtime', (YLeaf(YType.uint32, 'ccsSpectrumRequestStoppedTime'), ['int'])),
                    ('ccsspectrumrequeststatus', (YLeaf(YType.enumeration, 'ccsSpectrumRequestStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccsspectrumrequestindex = None
                self.ccsspectrumrequestifindex = None
                self.ccsspectrumrequestmacaddr = None
                self.ccsspectrumrequestlowfreq = None
                self.ccsspectrumrequestupperfreq = None
                self.ccsspectrumrequestresolution = None
                self.ccsspectrumrequestoperation = None
                self.ccsspectrumrequestoperstate = None
                self.ccsspectrumrequeststarttime = None
                self.ccsspectrumrequeststoppedtime = None
                self.ccsspectrumrequeststatus = None
                self._segment_path = lambda: "ccsSpectrumRequestEntry" + "[ccsSpectrumRequestIndex='" + str(self.ccsspectrumrequestindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsSpectrumRequestTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable.CcsSpectrumRequestEntry, ['ccsspectrumrequestindex', 'ccsspectrumrequestifindex', 'ccsspectrumrequestmacaddr', 'ccsspectrumrequestlowfreq', 'ccsspectrumrequestupperfreq', 'ccsspectrumrequestresolution', 'ccsspectrumrequestoperation', 'ccsspectrumrequestoperstate', 'ccsspectrumrequeststarttime', 'ccsspectrumrequeststoppedtime', 'ccsspectrumrequeststatus'], name, value)


    class CcsSpectrumDataTable(Entity):
        """
        This table contains the receiving power or background
        noise measurement based on the criteria that is set in
        the ccsSpectrumRequestEntry.
        
        .. attribute:: ccsspectrumdataentry
        
        	Information about the receiving power or background noise measured at a particular frequency for the ccsSpectrumRequestEntry
        	**type**\: list of  		 :py:class:`CcsSpectrumDataEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable.CcsSpectrumDataEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable, self).__init__()

            self.yang_name = "ccsSpectrumDataTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsSpectrumDataEntry", ("ccsspectrumdataentry", CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable.CcsSpectrumDataEntry))])
            self._leafs = OrderedDict()

            self.ccsspectrumdataentry = YList(self)
            self._segment_path = lambda: "ccsSpectrumDataTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable, [], name, value)


        class CcsSpectrumDataEntry(Entity):
            """
            Information about the receiving power or background noise
            measured at a particular frequency for the
            ccsSpectrumRequestEntry.
            
            .. attribute:: ccsspectrumrequestindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..100
            
            	**refers to**\:  :py:class:`ccsspectrumrequestindex <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpectrumRequestTable.CcsSpectrumRequestEntry>`
            
            .. attribute:: ccsspectrumdatafreq  (key)
            
            	ccsSpectrumDataPower measurement frequency.  Due to the adjustment calculation the starting frequency range for the actual measured frequency if off comparing to the configured frequency.  Refer to ccsSpectrumRequestLowFreq DESCRIPTIONS for the adjustment calculation
            	**type**\: int
            
            	**range:** 4000..85000
            
            	**units**\: KHz
            
            .. attribute:: ccsspectrumdatapower
            
            	The receiving power measured at the ccsSpectrumDataFreq
            	**type**\: int
            
            	**range:** \-50..50
            
            	**units**\: dBmV
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable.CcsSpectrumDataEntry, self).__init__()

                self.yang_name = "ccsSpectrumDataEntry"
                self.yang_parent_name = "ccsSpectrumDataTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsspectrumrequestindex','ccsspectrumdatafreq']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsspectrumrequestindex', (YLeaf(YType.str, 'ccsSpectrumRequestIndex'), ['int'])),
                    ('ccsspectrumdatafreq', (YLeaf(YType.int32, 'ccsSpectrumDataFreq'), ['int'])),
                    ('ccsspectrumdatapower', (YLeaf(YType.int32, 'ccsSpectrumDataPower'), ['int'])),
                ])
                self.ccsspectrumrequestindex = None
                self.ccsspectrumdatafreq = None
                self.ccsspectrumdatapower = None
                self._segment_path = lambda: "ccsSpectrumDataEntry" + "[ccsSpectrumRequestIndex='" + str(self.ccsspectrumrequestindex) + "']" + "[ccsSpectrumDataFreq='" + str(self.ccsspectrumdatafreq) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsSpectrumDataTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpectrumDataTable.CcsSpectrumDataEntry, ['ccsspectrumrequestindex', 'ccsspectrumdatafreq', 'ccsspectrumdatapower'], name, value)


    class CcsSNRRequestTable(Entity):
        """
        A table of CNR requests.
        
        .. attribute:: ccssnrrequestentry
        
        	Information about an CNR request.  The management system uses ccsSNRRequestStatus to control entry modification, creation, and deletion
        	**type**\: list of  		 :py:class:`CcsSNRRequestEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSNRRequestTable.CcsSNRRequestEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsSNRRequestTable, self).__init__()

            self.yang_name = "ccsSNRRequestTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsSNRRequestEntry", ("ccssnrrequestentry", CISCOCABLESPECTRUMMIB.CcsSNRRequestTable.CcsSNRRequestEntry))])
            self._leafs = OrderedDict()

            self.ccssnrrequestentry = YList(self)
            self._segment_path = lambda: "ccsSNRRequestTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSNRRequestTable, [], name, value)


        class CcsSNRRequestEntry(Entity):
            """
            Information about an CNR request.  The management
            system uses ccsSNRRequestStatus to control entry
            modification, creation, and deletion.
            
            .. attribute:: ccssnrrequestindex  (key)
            
            	An arbitrary integer to uniquely identify this entry
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: ccssnrrequestmacaddr
            
            	A MAC address that identifies the remote online CM that the CNR measurement operation is being performed on
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: ccssnrrequestsnr
            
            	A snap shot of the CNR value that is measured over the in\-use band frequency.  The ccsSNRRequestSNR is set to 0 when ccsSNRRequestOperState is in the 'running' state
            	**type**\: int
            
            	**range:** \-100..100
            
            	**units**\: dB
            
            .. attribute:: ccssnrrequestoperation
            
            	The control that allows start or abort of the test.  Since there is only 1 FFT engine running on the CMTS, 'start' changes ccsSNRRequestOperState to 'pending' state if the FFT is busy; Otherwise, it changes ccsSNRRequestOperState to 'running'.  'abort' changes ccsSNRRequestOperState to 'aborted' state.  Only 'start' when request is to be started and 'abort' when request is to be aborted can be set by the user. It is set to 'none' only on completion of the request by the FFT engine
            	**type**\:  :py:class:`CCSRequestOperation <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CCSRequestOperation>`
            
            .. attribute:: ccssnrrequestoperstate
            
            	The operational state of the test.  ccsSNRRequestMacAddr, cannot be changed when the ccsSNRRequestOperState is in the 'running' state
            	**type**\:  :py:class:`CCSRequestOperState <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CCSRequestOperState>`
            
            .. attribute:: ccssnrrequeststarttime
            
            	The value of sysUpTime when the CNR measurement operation starts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccssnrrequeststoppedtime
            
            	The value of sysUpTime when the CNR measurement operation stops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccssnrrequeststatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the ccsSpectrumRequestEntry DESCRIPTION
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsSNRRequestTable.CcsSNRRequestEntry, self).__init__()

                self.yang_name = "ccsSNRRequestEntry"
                self.yang_parent_name = "ccsSNRRequestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccssnrrequestindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccssnrrequestindex', (YLeaf(YType.int32, 'ccsSNRRequestIndex'), ['int'])),
                    ('ccssnrrequestmacaddr', (YLeaf(YType.str, 'ccsSNRRequestMacAddr'), ['str'])),
                    ('ccssnrrequestsnr', (YLeaf(YType.int32, 'ccsSNRRequestSNR'), ['int'])),
                    ('ccssnrrequestoperation', (YLeaf(YType.enumeration, 'ccsSNRRequestOperation'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CCSRequestOperation', '')])),
                    ('ccssnrrequestoperstate', (YLeaf(YType.enumeration, 'ccsSNRRequestOperState'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CCSRequestOperState', '')])),
                    ('ccssnrrequeststarttime', (YLeaf(YType.uint32, 'ccsSNRRequestStartTime'), ['int'])),
                    ('ccssnrrequeststoppedtime', (YLeaf(YType.uint32, 'ccsSNRRequestStoppedTime'), ['int'])),
                    ('ccssnrrequeststatus', (YLeaf(YType.enumeration, 'ccsSNRRequestStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccssnrrequestindex = None
                self.ccssnrrequestmacaddr = None
                self.ccssnrrequestsnr = None
                self.ccssnrrequestoperation = None
                self.ccssnrrequestoperstate = None
                self.ccssnrrequeststarttime = None
                self.ccssnrrequeststoppedtime = None
                self.ccssnrrequeststatus = None
                self._segment_path = lambda: "ccsSNRRequestEntry" + "[ccsSNRRequestIndex='" + str(self.ccssnrrequestindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsSNRRequestTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSNRRequestTable.CcsSNRRequestEntry, ['ccssnrrequestindex', 'ccssnrrequestmacaddr', 'ccssnrrequestsnr', 'ccssnrrequestoperation', 'ccssnrrequestoperstate', 'ccssnrrequeststarttime', 'ccssnrrequeststoppedtime', 'ccssnrrequeststatus'], name, value)


    class CcsUpInSpecGroupTable(Entity):
        """
        This table contains the cable upstream interfaces assigned to
        a spectrum group. A spectrum group contains one or more fixed
        frequencies or frequency bands which can be assigned to cable
        upstream interfaces in the spectrum group.
        
        .. attribute:: ccsupinspecgroupentry
        
        	An entry in ccsUpInSpecGroupTable table. Each entry represents a cable upstream interface assigned to a spectrum group
        	**type**\: list of  		 :py:class:`CcsUpInSpecGroupEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable.CcsUpInSpecGroupEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable, self).__init__()

            self.yang_name = "ccsUpInSpecGroupTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsUpInSpecGroupEntry", ("ccsupinspecgroupentry", CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable.CcsUpInSpecGroupEntry))])
            self._leafs = OrderedDict()

            self.ccsupinspecgroupentry = YList(self)
            self._segment_path = lambda: "ccsUpInSpecGroupTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable, [], name, value)


        class CcsUpInSpecGroupEntry(Entity):
            """
            An entry in ccsUpInSpecGroupTable table. Each entry represents
            a cable upstream interface assigned to a spectrum group.
            
            .. attribute:: ccsspecgroupnumber  (key)
            
            	The spectrum group number. The value of the object is same as the value of ccsUpSpecMgmtSpecGroup object except value 0
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccsspecgroupupstreamifindex  (key)
            
            	The ifIndex of the Cable upstream interface belonging to this Spectrum Group. The value of the corresponding instance of ifType is 'docsCableUpstream(129)'
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccsspecgroupupstreamstorage
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccsspecgroupupstreamrowstatus
            
            	The status for this conceptual row. This object is used for creating/deleting entries in ccsUpInSpecGroupTable
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable.CcsUpInSpecGroupEntry, self).__init__()

                self.yang_name = "ccsUpInSpecGroupEntry"
                self.yang_parent_name = "ccsUpInSpecGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsspecgroupnumber','ccsspecgroupupstreamifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsspecgroupnumber', (YLeaf(YType.uint32, 'ccsSpecGroupNumber'), ['int'])),
                    ('ccsspecgroupupstreamifindex', (YLeaf(YType.int32, 'ccsSpecGroupUpstreamIfIndex'), ['int'])),
                    ('ccsspecgroupupstreamstorage', (YLeaf(YType.enumeration, 'ccsSpecGroupUpstreamStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccsspecgroupupstreamrowstatus', (YLeaf(YType.enumeration, 'ccsSpecGroupUpstreamRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccsspecgroupnumber = None
                self.ccsspecgroupupstreamifindex = None
                self.ccsspecgroupupstreamstorage = None
                self.ccsspecgroupupstreamrowstatus = None
                self._segment_path = lambda: "ccsUpInSpecGroupEntry" + "[ccsSpecGroupNumber='" + str(self.ccsspecgroupnumber) + "']" + "[ccsSpecGroupUpstreamIfIndex='" + str(self.ccsspecgroupupstreamifindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsUpInSpecGroupTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable.CcsUpInSpecGroupEntry, ['ccsspecgroupnumber', 'ccsspecgroupupstreamifindex', 'ccsspecgroupupstreamstorage', 'ccsspecgroupupstreamrowstatus'], name, value)


    class CcsUpInFiberNodeTable(Entity):
        """
        This table contains the cable upstream interfaces in a
        fiber\-node.Each fiber\-node uniquely represents an RF
        domain.Cable upstream interfaces in the same fiber\-node
        are physically combined together into the same RF domain.
        
        .. attribute:: ccsupinfibernodeentry
        
        	An entry in ccsUpInFiberNodeTable. Each entry represents a cable upstream interface assigned to a fiber\-node
        	**type**\: list of  		 :py:class:`CcsUpInFiberNodeEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable.CcsUpInFiberNodeEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable, self).__init__()

            self.yang_name = "ccsUpInFiberNodeTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsUpInFiberNodeEntry", ("ccsupinfibernodeentry", CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable.CcsUpInFiberNodeEntry))])
            self._leafs = OrderedDict()

            self.ccsupinfibernodeentry = YList(self)
            self._segment_path = lambda: "ccsUpInFiberNodeTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable, [], name, value)


        class CcsUpInFiberNodeEntry(Entity):
            """
            An entry in ccsUpInFiberNodeTable. Each entry represents a
            cable upstream interface assigned to a fiber\-node.
            
            .. attribute:: ccsfibernodenumber  (key)
            
            	The fiber\-node number. The value of the object is same as the value of ccsUpSpecMgmtSharedSpectrum except value 0
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccsfibernodeupstreamifindex  (key)
            
            	The ifIndex of the Cable upstream interface belonging to this Spectrum Group. The value of the corresponding instance of ifType is 'docsCableUpstream(129)'
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccsfibernodeupstreamstorage
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccsfibernodeupstreamrowstatus
            
            	The status for this conceptual row. This object is used for creating/deleting entries in ccsUpInFiberNodeTable
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable.CcsUpInFiberNodeEntry, self).__init__()

                self.yang_name = "ccsUpInFiberNodeEntry"
                self.yang_parent_name = "ccsUpInFiberNodeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsfibernodenumber','ccsfibernodeupstreamifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsfibernodenumber', (YLeaf(YType.uint32, 'ccsFiberNodeNumber'), ['int'])),
                    ('ccsfibernodeupstreamifindex', (YLeaf(YType.int32, 'ccsFiberNodeUpstreamIfIndex'), ['int'])),
                    ('ccsfibernodeupstreamstorage', (YLeaf(YType.enumeration, 'ccsFiberNodeUpstreamStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccsfibernodeupstreamrowstatus', (YLeaf(YType.enumeration, 'ccsFiberNodeUpstreamRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccsfibernodenumber = None
                self.ccsfibernodeupstreamifindex = None
                self.ccsfibernodeupstreamstorage = None
                self.ccsfibernodeupstreamrowstatus = None
                self._segment_path = lambda: "ccsUpInFiberNodeEntry" + "[ccsFiberNodeNumber='" + str(self.ccsfibernodenumber) + "']" + "[ccsFiberNodeUpstreamIfIndex='" + str(self.ccsfibernodeupstreamifindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsUpInFiberNodeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpInFiberNodeTable.CcsUpInFiberNodeEntry, ['ccsfibernodenumber', 'ccsfibernodeupstreamifindex', 'ccsfibernodeupstreamstorage', 'ccsfibernodeupstreamrowstatus'], name, value)


    class CcsUpSpecMgmtTable(Entity):
        """
        This table contains the attributes of the cable
        upstream interfaces, ifType of docsCableUpstream(129),
        to be used for improving performance and proactive
        hopping.
        
        Proactive hopping is achieved by setting the SNR 
        polling period over the in\-use band without CM
        signals.
        
        .. attribute:: ccsupspecmgmtentry
        
        	Upstream interface's spectrum management information
        	**type**\: list of  		 :py:class:`CcsUpSpecMgmtEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable, self).__init__()

            self.yang_name = "ccsUpSpecMgmtTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsUpSpecMgmtEntry", ("ccsupspecmgmtentry", CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry))])
            self._leafs = OrderedDict()

            self.ccsupspecmgmtentry = YList(self)
            self._segment_path = lambda: "ccsUpSpecMgmtTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable, [], name, value)


        class CcsUpSpecMgmtEntry(Entity):
            """
            Upstream interface's spectrum management information.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: ccsupspecmgmthoppriority
            
            	A preference priority for changing the frequency, modulation, or channel width supporting the automatic switching of the modulation scheme when the channel becomes noisy.  The default priority is frequency, modulation, and channel width.  With the default preference, the frequency is changed if there is a clean band available.  If there's no clean band available, the modulation is changed.  And if the clean band is still not available, the bandwidth is reduced until an acceptable band is found or a minimum bandwidth of 200KHz
            	**type**\:  :py:class:`CcsUpSpecMgmtHopPriority <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry.CcsUpSpecMgmtHopPriority>`
            
            .. attribute:: ccsupspecmgmtsnrthres1
            
            	The Signal to Noise (SNR) threshold.  This object is applicable for modulation profile 1.  When the CMTS detects that the SNR goes lower than ccsUpSpecMgmtSnrThres1, it switches to profile 2. Therefore, ccsUpSpecMgmtSnrThres1 should be larger than ccsUpSpecMgmtSnrThres2.  A value 0 indicates to bypass the threshold check
            	**type**\: int
            
            	**range:** 0..None \| 5..35
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtsnrthres2
            
            	The Signal to Noise (SNR) threshold.  This object is applicable for modulation profile 2.  Refer to ccsUpSpecMgmtCriteria on how  ccsUpSpecMgmtSnrThres2 can trigger a change  in frequency, modulation or channel width.  A value 0 indicates to bypass the threshold check.  Note\: The SNMP SET is rejected if both  ccsUpSpecMgmtSnrThres1, ccsUpSpecMgmtSnrThres2 are non\-zero and ccsUpSpecMgmtSnrThres2 is higher than ccsUpSpecMgmtSnrThres1
            	**type**\: int
            
            	**range:** 0..None \| 5..35
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtfeccorrectthres1
            
            	The Forward Error Correction (FEC) correctable count threshold.  This object is applicable for profile 1.  A value 0 indicates to bypass the threshold check.  When CMTS detects that FEC correctable count goes higher than ccsUpSpecMgmtFecCorrectThres1, it switch to Profile 2.  Therefore, ccsUpSpecMgmtFecCorrectThres1 should be smaller than ccsUpSpecMgmtFecCorrectThres2
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ccsupspecmgmtfeccorrectthres2
            
            	The FEC correctable count threshold.  This object is applicable for profile 2.  When CMTS detects that FEC correctable count goes higher than ccsUpSpecMgmtFecCorrectThres2, modulation change can occur, depending on the type of ccsUpSpecMgmtHopPriority.  Note\: SNMP SET will be rejected if  ccsUpSpecMgmtFecCorrectThres2 is lower than  ccsUpSpecMgmtFecCorrectThres1
            	**type**\: int
            
            	**range:** 1..20
            
            	**status**\: deprecated
            
            .. attribute:: ccsupspecmgmtfecuncorrectthres1
            
            	The FEC uncorrectable count threshold.  This object is applicable for modulation profile 1.  A value 0 indicates to bypass the threshold check.  When CMTS detects that FEC uncorrectable count goes higher than ccsUpSpecMgmtFecUnCorrectThres1, it switches to Profile 2. Therefore, ccsUpSpecMgmtFecUnCorrectThres1 should be smaller than ccsUpSpecMgmtFecUnCorrectThres2
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ccsupspecmgmtfecuncorrectthres2
            
            	The FEC uncorrectable count threshold.  This object is applicable for modulation profile 2.  A value 0 indicates to bypass the threshold check.  Refer to ccsUpSpecMgmtCriteria on how  ccsUpSpecMgmtFecUnCorrectThres2 can trigger a change  in frequency, modulation or channel width.  Note\: SNMP SET is rejected if ccsUpSpecMgmtFecUnCorrectThres2 is lower than ccsUpSpecMgmtFecUnCorrectThres1
            	**type**\: int
            
            	**range:** 0..30
            
            .. attribute:: ccsupspecmgmtsnrpollperiod
            
            	A period between SNR pollings.  The SNR is collected from the Fast Fourier Transform (FFT) measurement over the in\-use band when there is no CM signals. When the CMTS detects that SNR doesn't meet ccsUpSpecMgmtSnrThres1 or ccsUpSpecMgmtSnrThres2, a possible hopping occurs, depending on the type of ccsUpSpecMgmtHopPriority
            	**type**\: int
            
            	**range:** 0..None \| 500..25000
            
            	**units**\: msec
            
            	**status**\: deprecated
            
            .. attribute:: ccsupspecmgmthopcondition
            
            	A condition that triggers hopping.  The SNR condition occurs when SNR does not meet the ccsUpSpecMgmtSnrThres1 or ccsUpSpecMgmtSnrThres2.  The stationMaintainenceMiss condition occurs when the  percentage of offline CMs is reached
            	**type**\:  :py:class:`CcsUpSpecMgmtHopCondition <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry.CcsUpSpecMgmtHopCondition>`
            
            	**status**\: deprecated
            
            .. attribute:: ccsupspecmgmtfromcenterfreq
            
            	Center frequency before hopping occurs.  A value 0 indicates that the interface has no frequency assigned
            	**type**\: int
            
            	**range:** 0..None \| 5000..65000
            
            	**units**\: KHz
            
            .. attribute:: ccsupspecmgmttocenterfreq
            
            	Current center frequency.  A value 0 indicates that the interface has no frequency assigned
            	**type**\: int
            
            	**range:** 0..None \| 5000..65000
            
            	**units**\: KHz
            
            .. attribute:: ccsupspecmgmtfrombandwidth
            
            	Bandwidth before hopping occurs
            	**type**\: int
            
            	**range:** 200..None \| 400..None \| 800..None \| 1600..None \| 3200..None \| 6400..None
            
            	**units**\: KHz
            
            .. attribute:: ccsupspecmgmttobandwidth
            
            	Current bandwidth
            	**type**\: int
            
            	**range:** 200..None \| 400..None \| 800..None \| 1600..None \| 3200..None \| 6400..None
            
            	**units**\: KHz
            
            .. attribute:: ccsupspecmgmtfrommodprofile
            
            	Modulation profile index before hopping occurs. It is the index identical to the docsIfModIndex in the docsIfCmtsModulationTable.  For the detailed descriptions, see the docsIfCmtsModulationTable and docsIfCmtsModIndex DESCRIPTIONS
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccsupspecmgmttomodprofile
            
            	The current modulation profile index. It is the index identical to the docsIfModIndex in the docsIfCmtsModulationTable.  For the detailed descriptions, see the docsIfCmtsModulationTable and docsIfCmtsModIndex DESCRIPTIONS
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccsupspecmgmtsnr
            
            	Current SNR. A value \-99 indicates the system detected no  modem on line, and a value of \-100 indicates the  system was unable to retrieve the SNR value
            	**type**\: int
            
            	**range:** \-100..100
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtupperboundfreq
            
            	Upper bound frequency that the upstream supports
            	**type**\: int
            
            	**range:** 5000..85000
            
            	**units**\: KHz
            
            .. attribute:: ccsupspecmgmtcnrthres1
            
            	The Carrier to Noise (CNR) threshold.  This object is applicable for modulation profile 1.   When the CMTS detects that the CNR goes lower than ccsUpSpecMgmtCnrThres1, it switches to profile 2. Therefore, ccsUpSpecMgmtCnrThres1 should be larger  than ccsUpSpecMgmtCnrThres2.  A value 0 indicates to bypass the threshold check
            	**type**\: int
            
            	**range:** 0..None \| 5..35
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtcnrthres2
            
            	The Carrier to Noise (CNR) threshold.  This object is applicable for modulation profile 2.  Refer to ccsUpSpecMgmtCriteria on how  ccsUpSpecMgmtCnrThres2 can trigger a change  in frequency, modulation or channel width.  A value 0 indicates to bypass the threshold check.  Note\: The SNMP SET is rejected if both  ccsUpSpecMgmtCnrThres1, ccsUpSpecMgmtCnrThres2 are non\-zero and ccsUpSpecMgmtCnrThres2 is higher than ccsUpSpecMgmtCnrThres1
            	**type**\: int
            
            	**range:** 0..None \| 5..35
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtcnr
            
            	Current CNR. A value \-99 indicates the system detected no  modem on line, and a value of \-100 indicates the  system was unable to retrieve the CNR value
            	**type**\: int
            
            	**range:** \-100..100
            
            	**units**\: dB
            
            .. attribute:: ccsupspecmgmtmissedmaintmsgthres
            
            	The missed maintenance message threshold in percentage.  A value 0 indicates that the interface has no spectrum  group assigned. i.e. ccsUpSpecMgmtSpecGroup equals 0
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ccsupspecmgmthopperiod
            
            	The minimum time between frequency hops in seconds.  A value 0 indicates that the interface has no spectrum group assigned. i.e. ccsUpSpecMgmtSpecGroup equals to 0
            	**type**\: int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: ccsupspecmgmtcriteria
            
            	Defines the criteria that trigger a change in frequency hopping, modulation or channel width.    Depending on the type of linecards, the criteria  are slightly different\:  For the linecards that have no Hardware  Based Spectrum Management capability like  the uBR\-MC1xC, change in modulation or frequency occurs in the following criteria\:  1) Change from modulation profile 1 to     modulation profile 2 would occur when CMTS     detects the SNR that goes below the     threshold and either corr FEC or uncorr FEC     is above the threshold.  In this case,     snrBelowThres and either corrFecAboveThres or     uncorrFecAboveThres bits will get set.   2) Change from modulation profile 2 to     modulation profile 1 would occur when CMTS     detects the SNR goes above the threshold+3    and both corr FEC and uncorr FEC are     below the threshold.  In this case,     snrAboveThres and corrFecBelowThres    and uncorrFecBelowThres bits will get set.   3) Change in frequency or frequency hopping would    occur when CMTS detects no active modem on the link.      In this case, noActiveModem bit will get    set accordingly.   For the linecards that have the Hardware Based  Spectrum Management capability, change in  frequency, modulation or channel width occurs  in the following criteria\:  1) when CMTS detects the SNR or CNR goes below the     threshold and either corr FEC or uncorr FEC is     above the threshold.  In this case,     either snrBelowThres or cnrBelowThres and     either corrFecAboveThres or uncorrFecAboveThres     bits will get set.   2) when CMTS detects the SNR or CNR goes above the     threshold + 3 and both corr FEC and uncorr FEC are     below the threshold.  In this case,     either snrAboveThres or cnrAboveThres and both     corrFecBelowThres and uncorrFecBelowThres bits     will get set.   3) when CMTS detects no active modem on the link or     uncorr FEC is above ccsUpSpecMgmtFecUnCorrectThres2.     In this case noActiveModem or     uncorrFecAboveSecondThres bit will get set     accordingly.  Note\: The order of frequency, modulation or channel  width changes for the advanced spectrum management linecards will be determined based on the selection of  the ccsUpSpecMgmtHopPriority
            	**type**\:  :py:class:`CcsUpSpecMgmtCriteria <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry.CcsUpSpecMgmtCriteria>`
            
            .. attribute:: ccsupspecmgmtspecgroup
            
            	The spectrum group assigned to the upstream. The value of 0 for the object indicates that the upstream has no spectrum group assigned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccsupspecmgmtsharedspectrum
            
            	The fiber\-node assigned to the upstreams. Upstreams having same fiber\-node number indicates that they physically combine together into same RF domain and must have unique frequency assigned. The value of 0 for the object indicates that the upstream is not physically combine with any others
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry, self).__init__()

                self.yang_name = "ccsUpSpecMgmtEntry"
                self.yang_parent_name = "ccsUpSpecMgmtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ccsupspecmgmthoppriority', (YLeaf(YType.enumeration, 'ccsUpSpecMgmtHopPriority'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CISCOCABLESPECTRUMMIB', 'CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry.CcsUpSpecMgmtHopPriority')])),
                    ('ccsupspecmgmtsnrthres1', (YLeaf(YType.int32, 'ccsUpSpecMgmtSnrThres1'), ['int'])),
                    ('ccsupspecmgmtsnrthres2', (YLeaf(YType.int32, 'ccsUpSpecMgmtSnrThres2'), ['int'])),
                    ('ccsupspecmgmtfeccorrectthres1', (YLeaf(YType.int32, 'ccsUpSpecMgmtFecCorrectThres1'), ['int'])),
                    ('ccsupspecmgmtfeccorrectthres2', (YLeaf(YType.int32, 'ccsUpSpecMgmtFecCorrectThres2'), ['int'])),
                    ('ccsupspecmgmtfecuncorrectthres1', (YLeaf(YType.int32, 'ccsUpSpecMgmtFecUnCorrectThres1'), ['int'])),
                    ('ccsupspecmgmtfecuncorrectthres2', (YLeaf(YType.int32, 'ccsUpSpecMgmtFecUnCorrectThres2'), ['int'])),
                    ('ccsupspecmgmtsnrpollperiod', (YLeaf(YType.int32, 'ccsUpSpecMgmtSnrPollPeriod'), ['int'])),
                    ('ccsupspecmgmthopcondition', (YLeaf(YType.enumeration, 'ccsUpSpecMgmtHopCondition'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CISCOCABLESPECTRUMMIB', 'CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry.CcsUpSpecMgmtHopCondition')])),
                    ('ccsupspecmgmtfromcenterfreq', (YLeaf(YType.uint32, 'ccsUpSpecMgmtFromCenterFreq'), ['int'])),
                    ('ccsupspecmgmttocenterfreq', (YLeaf(YType.uint32, 'ccsUpSpecMgmtToCenterFreq'), ['int'])),
                    ('ccsupspecmgmtfrombandwidth', (YLeaf(YType.uint32, 'ccsUpSpecMgmtFromBandWidth'), ['int'])),
                    ('ccsupspecmgmttobandwidth', (YLeaf(YType.uint32, 'ccsUpSpecMgmtToBandWidth'), ['int'])),
                    ('ccsupspecmgmtfrommodprofile', (YLeaf(YType.int32, 'ccsUpSpecMgmtFromModProfile'), ['int'])),
                    ('ccsupspecmgmttomodprofile', (YLeaf(YType.int32, 'ccsUpSpecMgmtToModProfile'), ['int'])),
                    ('ccsupspecmgmtsnr', (YLeaf(YType.int32, 'ccsUpSpecMgmtSNR'), ['int'])),
                    ('ccsupspecmgmtupperboundfreq', (YLeaf(YType.int32, 'ccsUpSpecMgmtUpperBoundFreq'), ['int'])),
                    ('ccsupspecmgmtcnrthres1', (YLeaf(YType.int32, 'ccsUpSpecMgmtCnrThres1'), ['int'])),
                    ('ccsupspecmgmtcnrthres2', (YLeaf(YType.int32, 'ccsUpSpecMgmtCnrThres2'), ['int'])),
                    ('ccsupspecmgmtcnr', (YLeaf(YType.int32, 'ccsUpSpecMgmtCNR'), ['int'])),
                    ('ccsupspecmgmtmissedmaintmsgthres', (YLeaf(YType.int32, 'ccsUpSpecMgmtMissedMaintMsgThres'), ['int'])),
                    ('ccsupspecmgmthopperiod', (YLeaf(YType.int32, 'ccsUpSpecMgmtHopPeriod'), ['int'])),
                    ('ccsupspecmgmtcriteria', (YLeaf(YType.bits, 'ccsUpSpecMgmtCriteria'), ['Bits'])),
                    ('ccsupspecmgmtspecgroup', (YLeaf(YType.uint32, 'ccsUpSpecMgmtSpecGroup'), ['int'])),
                    ('ccsupspecmgmtsharedspectrum', (YLeaf(YType.uint32, 'ccsUpSpecMgmtSharedSpectrum'), ['int'])),
                ])
                self.ifindex = None
                self.ccsupspecmgmthoppriority = None
                self.ccsupspecmgmtsnrthres1 = None
                self.ccsupspecmgmtsnrthres2 = None
                self.ccsupspecmgmtfeccorrectthres1 = None
                self.ccsupspecmgmtfeccorrectthres2 = None
                self.ccsupspecmgmtfecuncorrectthres1 = None
                self.ccsupspecmgmtfecuncorrectthres2 = None
                self.ccsupspecmgmtsnrpollperiod = None
                self.ccsupspecmgmthopcondition = None
                self.ccsupspecmgmtfromcenterfreq = None
                self.ccsupspecmgmttocenterfreq = None
                self.ccsupspecmgmtfrombandwidth = None
                self.ccsupspecmgmttobandwidth = None
                self.ccsupspecmgmtfrommodprofile = None
                self.ccsupspecmgmttomodprofile = None
                self.ccsupspecmgmtsnr = None
                self.ccsupspecmgmtupperboundfreq = None
                self.ccsupspecmgmtcnrthres1 = None
                self.ccsupspecmgmtcnrthres2 = None
                self.ccsupspecmgmtcnr = None
                self.ccsupspecmgmtmissedmaintmsgthres = None
                self.ccsupspecmgmthopperiod = None
                self.ccsupspecmgmtcriteria = Bits()
                self.ccsupspecmgmtspecgroup = None
                self.ccsupspecmgmtsharedspectrum = None
                self._segment_path = lambda: "ccsUpSpecMgmtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsUpSpecMgmtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsUpSpecMgmtTable.CcsUpSpecMgmtEntry, ['ifindex', 'ccsupspecmgmthoppriority', 'ccsupspecmgmtsnrthres1', 'ccsupspecmgmtsnrthres2', 'ccsupspecmgmtfeccorrectthres1', 'ccsupspecmgmtfeccorrectthres2', 'ccsupspecmgmtfecuncorrectthres1', 'ccsupspecmgmtfecuncorrectthres2', 'ccsupspecmgmtsnrpollperiod', 'ccsupspecmgmthopcondition', 'ccsupspecmgmtfromcenterfreq', 'ccsupspecmgmttocenterfreq', 'ccsupspecmgmtfrombandwidth', 'ccsupspecmgmttobandwidth', 'ccsupspecmgmtfrommodprofile', 'ccsupspecmgmttomodprofile', 'ccsupspecmgmtsnr', 'ccsupspecmgmtupperboundfreq', 'ccsupspecmgmtcnrthres1', 'ccsupspecmgmtcnrthres2', 'ccsupspecmgmtcnr', 'ccsupspecmgmtmissedmaintmsgthres', 'ccsupspecmgmthopperiod', 'ccsupspecmgmtcriteria', 'ccsupspecmgmtspecgroup', 'ccsupspecmgmtsharedspectrum'], name, value)

            class CcsUpSpecMgmtHopCondition(Enum):
                """
                CcsUpSpecMgmtHopCondition (Enum Class)

                A condition that triggers hopping.

                The SNR condition occurs when SNR does not meet

                the ccsUpSpecMgmtSnrThres1 or ccsUpSpecMgmtSnrThres2.

                The stationMaintainenceMiss condition occurs when the 

                percentage of offline CMs is reached.

                .. data:: snr = 0

                .. data:: stationMaintainenceMiss = 1

                .. data:: others = 2

                """

                snr = Enum.YLeaf(0, "snr")

                stationMaintainenceMiss = Enum.YLeaf(1, "stationMaintainenceMiss")

                others = Enum.YLeaf(2, "others")


            class CcsUpSpecMgmtHopPriority(Enum):
                """
                CcsUpSpecMgmtHopPriority (Enum Class)

                A preference priority for changing the frequency,

                modulation, or channel width supporting the automatic

                switching of the modulation scheme when the channel

                becomes noisy.

                The default priority is frequency, modulation, and

                channel width.  With the default preference, the

                frequency is changed if there is a clean band

                available.  If there's no clean band available,

                the modulation is changed.  And if the

                clean band is still not available, the bandwidth is

                reduced until an acceptable band is found or a minimum

                bandwidth of 200KHz.

                .. data:: frqModChannel = 0

                .. data:: frqChannelMod = 1

                .. data:: modFrqChannel = 2

                .. data:: modChannelFrq = 3

                .. data:: channelFrqMod = 4

                .. data:: channelModFrq = 5

                """

                frqModChannel = Enum.YLeaf(0, "frqModChannel")

                frqChannelMod = Enum.YLeaf(1, "frqChannelMod")

                modFrqChannel = Enum.YLeaf(2, "modFrqChannel")

                modChannelFrq = Enum.YLeaf(3, "modChannelFrq")

                channelFrqMod = Enum.YLeaf(4, "channelFrqMod")

                channelModFrq = Enum.YLeaf(5, "channelModFrq")



    class CcsSpecGroupFreqTable(Entity):
        """
        This table contains the frequency and band configuration
        of the spectrum group.
        
        .. attribute:: ccsspecgroupfreqentry
        
        	An entry in ccsSpecGroupFreqTable. Each entry represents a center frequency or a frequency band configured for the spectrum group
        	**type**\: list of  		 :py:class:`CcsSpecGroupFreqEntry <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry>`
        
        

        """

        _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
        _revision = '2011-04-08'

        def __init__(self):
            super(CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable, self).__init__()

            self.yang_name = "ccsSpecGroupFreqTable"
            self.yang_parent_name = "CISCO-CABLE-SPECTRUM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccsSpecGroupFreqEntry", ("ccsspecgroupfreqentry", CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry))])
            self._leafs = OrderedDict()

            self.ccsspecgroupfreqentry = YList(self)
            self._segment_path = lambda: "ccsSpecGroupFreqTable"
            self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable, [], name, value)


        class CcsSpecGroupFreqEntry(Entity):
            """
            An entry in ccsSpecGroupFreqTable. Each entry represents a
            center frequency or a frequency band configured for the
            spectrum group.
            
            .. attribute:: ccsspecgroupnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccsspecgroupnumber <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsUpInSpecGroupTable.CcsUpInSpecGroupEntry>`
            
            .. attribute:: ccsspecgroupfreqindex  (key)
            
            	An arbitrary index to uniquely identify frequencies or bands configured in spectrum group
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccsspecgroupfreqtype
            
            	The type of the frequency configured in spectrum group. This is a mandatory object and can be modified when the row is active. If the value of centerFreq(1) is specified, the values of the corresponding instance of ccsSpecGroupFreqLower and csSpecGroupFreqUpper object must be identical. If the value of bandFreq(2) is specified, the values of the corresponding instance of ccsSpecGroupFreqLower and csSpecGroupFreqUpper must be unique
            	**type**\:  :py:class:`CcsSpecGroupFreqType <ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB.CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry.CcsSpecGroupFreqType>`
            
            .. attribute:: ccsspecgroupfreqlower
            
            	The lower frequency configured in spectrum group. This is a mandatory object and can be modified when the row is active. To configure a band frequency in the spectrum group, the value of this object must be lower than the value of the corresponding instance of ccsSpecGroupFreqUpper. To configure a fixed center frequency in the spectrum group, the value of this object must be equal to the value of the corresponding instance of ccsSpecGroupFreqUpper
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**units**\: Hz
            
            .. attribute:: ccsspecgroupfrequpper
            
            	The upper frequency configured in spectrum group. This is a mandatory object and can be modified when the row is active. To configure a band frequency in the spectrum group, the value of this object must be greater than the value of the corresponding instance of ccsSpecGroupFreqLower. To configure a fixed center frequency in the spectrum group, the value of this object must be equal to the value of the corresponding instance of ccsSpecGroupFreqLower
            	**type**\: int
            
            	**range:** 0..1000000000
            
            	**units**\: Hz
            
            .. attribute:: ccsspecgroupstorage
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ccsspecgrouprowstatus
            
            	The status of this conceptual row. This object is used for creating/deleting entries in ccsSpecGroupFreqTable.  A conceptual row may not be created via SNMP without explicitly setting the value of ccsSpecGroupRowStatus to createAndGo(4).  A conceptual row can not have the status of active(1) until proper values have been assigned to the mandatory objects ccsSpecGroupFreqType, ccsSpecGroupFreqLower, and ccsSpecGroupFreqUpper.  A conceptual row may be modified or deleted any time. If the frequency represents by the row has been assigned to a cable upstream interface, modifying or deleting such row would cause the cable upstream interface frequency reassignment
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CABLE-SPECTRUM-MIB'
            _revision = '2011-04-08'

            def __init__(self):
                super(CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry, self).__init__()

                self.yang_name = "ccsSpecGroupFreqEntry"
                self.yang_parent_name = "ccsSpecGroupFreqTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccsspecgroupnumber','ccsspecgroupfreqindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccsspecgroupnumber', (YLeaf(YType.str, 'ccsSpecGroupNumber'), ['int'])),
                    ('ccsspecgroupfreqindex', (YLeaf(YType.uint32, 'ccsSpecGroupFreqIndex'), ['int'])),
                    ('ccsspecgroupfreqtype', (YLeaf(YType.enumeration, 'ccsSpecGroupFreqType'), [('ydk.models.cisco_ios_xe.CISCO_CABLE_SPECTRUM_MIB', 'CISCOCABLESPECTRUMMIB', 'CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry.CcsSpecGroupFreqType')])),
                    ('ccsspecgroupfreqlower', (YLeaf(YType.int32, 'ccsSpecGroupFreqLower'), ['int'])),
                    ('ccsspecgroupfrequpper', (YLeaf(YType.int32, 'ccsSpecGroupFreqUpper'), ['int'])),
                    ('ccsspecgroupstorage', (YLeaf(YType.enumeration, 'ccsSpecGroupStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccsspecgrouprowstatus', (YLeaf(YType.enumeration, 'ccsSpecGroupRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ccsspecgroupnumber = None
                self.ccsspecgroupfreqindex = None
                self.ccsspecgroupfreqtype = None
                self.ccsspecgroupfreqlower = None
                self.ccsspecgroupfrequpper = None
                self.ccsspecgroupstorage = None
                self.ccsspecgrouprowstatus = None
                self._segment_path = lambda: "ccsSpecGroupFreqEntry" + "[ccsSpecGroupNumber='" + str(self.ccsspecgroupnumber) + "']" + "[ccsSpecGroupFreqIndex='" + str(self.ccsspecgroupfreqindex) + "']"
                self._absolute_path = lambda: "CISCO-CABLE-SPECTRUM-MIB:CISCO-CABLE-SPECTRUM-MIB/ccsSpecGroupFreqTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCABLESPECTRUMMIB.CcsSpecGroupFreqTable.CcsSpecGroupFreqEntry, ['ccsspecgroupnumber', 'ccsspecgroupfreqindex', 'ccsspecgroupfreqtype', 'ccsspecgroupfreqlower', 'ccsspecgroupfrequpper', 'ccsspecgroupstorage', 'ccsspecgrouprowstatus'], name, value)

            class CcsSpecGroupFreqType(Enum):
                """
                CcsSpecGroupFreqType (Enum Class)

                The type of the frequency configured in spectrum group. This is

                a mandatory object and can be modified when the row is active.

                If the value of centerFreq(1) is specified, the values of the

                corresponding instance of ccsSpecGroupFreqLower and

                csSpecGroupFreqUpper object must be identical. If the value of

                bandFreq(2) is specified, the values of the corresponding

                instance of ccsSpecGroupFreqLower and csSpecGroupFreqUpper

                must be unique.

                .. data:: centerFreq = 1

                .. data:: bandFreq = 2

                """

                centerFreq = Enum.YLeaf(1, "centerFreq")

                bandFreq = Enum.YLeaf(2, "bandFreq")


    def clone_ptr(self):
        self._top_entity = CISCOCABLESPECTRUMMIB()
        return self._top_entity

