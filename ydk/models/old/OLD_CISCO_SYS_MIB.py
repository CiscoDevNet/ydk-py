""" OLD_CISCO_SYS_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class OLDCISCOSYSMIB(object):
    """
    
    
    .. attribute:: lsystem
    
    	
    	**type**\: :py:class:`Lsystem <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem>`
    
    

    """

    _prefix = 'old-cisco'

    def __init__(self):
        self.lsystem = OLDCISCOSYSMIB.Lsystem()
        self.lsystem.parent = self


    class Lsystem(object):
        """
        
        
        .. attribute:: authaddr
        
        	This variable contains the last SNMP authorization failure IP address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: avgbusy1
        
        	1 minute exponentially\-decayed moving average of the CPU busy percentage
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: avgbusy5
        
        	5 minute exponentially\-decayed moving average of the CPU busy percentage
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: boothost
        
        	Contains the IP address of the host that supplied the currently running software
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: bufferbgcreate
        
        	Contains the number of big buffer creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgfree
        
        	Contains the number of free big buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbghit
        
        	Contains the number of big buffer hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgmax
        
        	Contains the maximum number of big buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgmiss
        
        	Contains the number of big buffer misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgsize
        
        	Contains the size of big buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgtotal
        
        	Contains the total number of big buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferbgtrim
        
        	Contains the number of big buffer trims
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferelcreate
        
        	Contains the number of buffer element creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferelfree
        
        	Contains the number of free buffer elements
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferelhit
        
        	Contains the number of buffer element hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferelmax
        
        	Contains the maximum number of buffer elements
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferelmiss
        
        	Contains the number of buffer element misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferfail
        
        	Count of the number of buffer allocation failures
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgcreate
        
        	Contains the number of huge buffer creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgfree
        
        	Contains the number of free huge buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhghit
        
        	Contains the number of huge buffer hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgmax
        
        	Contains the maximum number of huge buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgmiss
        
        	Contains the number of huge buffer misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgsize
        
        	Contains the size of huge buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgtotal
        
        	Contains the total number of huge buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferhgtrim
        
        	Contains the number of huge buffer trims
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgcreate
        
        	Contains the number of large buffer creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgfree
        
        	Contains the number of free large buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlghit
        
        	Contains the number of large buffer hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgmax
        
        	Contains the maximum number of large buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgmiss
        
        	Contains the number of large buffer misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgsize
        
        	Contains the size of large buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgtotal
        
        	Contains the total number of large buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: bufferlgtrim
        
        	Contains the number of large buffer trims
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdcreate
        
        	Contains the number of medium buffer creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdfree
        
        	Contains the number of free medium buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdhit
        
        	Contains the number of medium buffer hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdmax
        
        	Contains the maximum number of medium buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdmiss
        
        	Contains the number of medium buffer misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdsize
        
        	Contains the size of medium buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdtotal
        
        	Contains the total number of medium buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffermdtrim
        
        	Contains the number of medium buffer trims
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffernomem
        
        	Count of the number of buffer create failures due to no free memory
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmcreate
        
        	Contains the number of small buffer creates
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmfree
        
        	Contains the number of free small buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmhit
        
        	Contains the number of small buffer hits
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmmax
        
        	Contains the maximum number of small buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmmiss
        
        	Contains the number of small buffer misses
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmsize
        
        	Contains the size of small buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmtotal
        
        	Contains the total number of small buffers
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: buffersmtrim
        
        	Contains the number of small buffer trims
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: busyper
        
        	CPU busy percentage in the last 5 second period. Not the last 5 realtime seconds but the last 5 second period in the scheduler
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ciscocontactinfo
        
        	cisco's name and address
        	**type**\: str
        
        .. attribute:: domainname
        
        	This variable is the domain portion of the domain name of the host
        	**type**\: str
        
        .. attribute:: envburndate
        
        	The calibration / burn in date
        	**type**\: str
        
        .. attribute:: envfirmversion
        
        	Description of Environmental Card firmware
        	**type**\: str
        
        .. attribute:: envpresent
        
        	Is there an environmental monitor card in this box?, 0 \- No, 1\-AGS card present, wrong firmware, 2\-AGS CARD present, firmware ok, 3\-7000 support
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envserialnumber
        
        	Serial Number of environmental monitor card
        	**type**\: str
        
        .. attribute:: envtechnicianid
        
        	Technician ID
        	**type**\: str
        
        .. attribute:: envtestpt1descr
        
        	Description of the test point 1. Typically ambient air or the temperature of air entering the router
        	**type**\: str
        
        .. attribute:: envtestpt1last
        
        	Value of TestPt1 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt1marginval
        
        	Value at which the router will shutdown. Typically the ambient air temperature that will shut the router down. (e.g. 43)
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt1measure
        
        	Current value of test point 1. Typically a temperature in centigrade
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt1warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt1warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt1warn_Enum>`
        
        .. attribute:: envtestpt2descr
        
        	Description of the test point 2. Typically airflow or the temperature of air leaving the router
        	**type**\: str
        
        .. attribute:: envtestpt2last
        
        	Value of TestPt2 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt2marginval
        
        	Value at which the router will shutdown. Typically the airflow air temperature that will shut the router down. (e.g. 58)
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt2measure
        
        	Current value of test point 2. Typically a temperature in centigrade
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt2warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt2warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt2warn_Enum>`
        
        .. attribute:: envtestpt3descr
        
        	Description of the test point 3. Typically +5 volt
        	**type**\: str
        
        .. attribute:: envtestpt3last
        
        	Value of TestPt3 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt3marginpercent
        
        	+/\- Percentage that will shut the router down, (e.g. 10%) typically +5 volt
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt3measure
        
        	Current value of test point 3. Typically the value in millivolts of the +5v supply
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt3warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt3warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt3warn_Enum>`
        
        .. attribute:: envtestpt4descr
        
        	Description of the test point 4. Typically +12 volt
        	**type**\: str
        
        .. attribute:: envtestpt4last
        
        	Value of TestPt4 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt4marginpercent
        
        	+/\- Percentage that will shut the router down, (e.g. 15%) typically +12 volt
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt4measure
        
        	Current value of test point 4. Typically the value in millivolts of the +12v supply
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt4warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt4warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt4warn_Enum>`
        
        .. attribute:: envtestpt5descr
        
        	Description of the test point 5. Typically \-12 volt
        	**type**\: str
        
        .. attribute:: envtestpt5last
        
        	Value of TestPt5 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt5marginpercent
        
        	+/\- Percentage that will shut the router down, (e.g. 15%) typically \-12 volt
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt5measure
        
        	Current value of test point 5. Typically the value in millivolts of the \-12v supply
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt5warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt5warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt5warn_Enum>`
        
        .. attribute:: envtestpt6descr
        
        	Description of the test point 6. Typically \-5 volt
        	**type**\: str
        
        .. attribute:: envtestpt6last
        
        	Value of TestPt6 when last shutdown occurred
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt6marginpercent
        
        	+/\- Percentage that will shut the router down, (e.g. 10%) typically \-5 volt
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt6measure
        
        	Current value of test point 6. Typically the value in millivolts of the \-5v supply
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: envtestpt6warn
        
        	Is this test point at a warning level?
        	**type**\: :py:class:`EnvTestPt6warn_Enum <ydk.models.old.OLD_CISCO_SYS_MIB.OLDCISCOSYSMIB.Lsystem.EnvTestPt6warn_Enum>`
        
        .. attribute:: envtype
        
        	The type of environmental card
        	**type**\: str
        
        .. attribute:: freemem
        
        	The freeMem mib object is obsolete as of IOS 11.1 It has been replaced with the cisco memory pool mib
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: hostconfigaddr
        
        	Contains the address of the host that provided the host\-config file
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: hostconfigname
        
        	Contains the name of the last configured host\-confg file
        	**type**\: str
        
        .. attribute:: hostconfigproto
        
        	Holds the protocol that supplied the host\- confg file
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: hostconfigset
        
        	Cause the loading of a new host\-confg file using TFTP
        	**type**\: str
        
        .. attribute:: hostname
        
        	This variable represents the name of the host in printable ascii characters
        	**type**\: str
        
        .. attribute:: idlecount
        
        	cisco internal variable. not to be used
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: idlewired
        
        	cisco internal variable. not to be used
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: netconfigaddr
        
        	Holds the address of the host that supplied the network\-confg file
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: netconfigname
        
        	Holds the name of the network configuration file
        	**type**\: str
        
        .. attribute:: netconfigproto
        
        	Holds the protocol that supplied the network\-confg file
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: netconfigset
        
        	Cause the loading of a new network\-confg file using TFTP
        	**type**\: str
        
        .. attribute:: ping
        
        	The ping mib object is obsolete as of IOS 10.2 It has been superseded by the Cisco Ping MIB
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: romid
        
        	This variable contains a printable octet string which contains the System Bootstrap description and version identification
        	**type**\: str
        
        .. attribute:: syscleararp
        
        	Perform a clearing of the entire ARP cache and invalidation of route caches
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: sysclearint
        
        	Clear interface given IfIndex as value
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: sysconfigaddr
        
        	Holds the address of the host that supplied the system boot image
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: sysconfigname
        
        	Holds the name of the system boot image
        	**type**\: str
        
        .. attribute:: sysconfigproto
        
        	Holds the protocol that supplied the system boot image
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: whyreload
        
        	This variable contains a printable octet string which contains the reason why the system was last restarted
        	**type**\: str
        
        .. attribute:: writemem
        
        	Write configuration into non\-volatile memory / erase config memory if 0
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: writenet
        
        	Write configuration to host using TFTP
        	**type**\: str
        
        

        """

        _prefix = 'old-cisco'

        def __init__(self):
            self.parent = None
            self.authaddr = None
            self.avgbusy1 = None
            self.avgbusy5 = None
            self.boothost = None
            self.bufferbgcreate = None
            self.bufferbgfree = None
            self.bufferbghit = None
            self.bufferbgmax = None
            self.bufferbgmiss = None
            self.bufferbgsize = None
            self.bufferbgtotal = None
            self.bufferbgtrim = None
            self.bufferelcreate = None
            self.bufferelfree = None
            self.bufferelhit = None
            self.bufferelmax = None
            self.bufferelmiss = None
            self.bufferfail = None
            self.bufferhgcreate = None
            self.bufferhgfree = None
            self.bufferhghit = None
            self.bufferhgmax = None
            self.bufferhgmiss = None
            self.bufferhgsize = None
            self.bufferhgtotal = None
            self.bufferhgtrim = None
            self.bufferlgcreate = None
            self.bufferlgfree = None
            self.bufferlghit = None
            self.bufferlgmax = None
            self.bufferlgmiss = None
            self.bufferlgsize = None
            self.bufferlgtotal = None
            self.bufferlgtrim = None
            self.buffermdcreate = None
            self.buffermdfree = None
            self.buffermdhit = None
            self.buffermdmax = None
            self.buffermdmiss = None
            self.buffermdsize = None
            self.buffermdtotal = None
            self.buffermdtrim = None
            self.buffernomem = None
            self.buffersmcreate = None
            self.buffersmfree = None
            self.buffersmhit = None
            self.buffersmmax = None
            self.buffersmmiss = None
            self.buffersmsize = None
            self.buffersmtotal = None
            self.buffersmtrim = None
            self.busyper = None
            self.ciscocontactinfo = None
            self.domainname = None
            self.envburndate = None
            self.envfirmversion = None
            self.envpresent = None
            self.envserialnumber = None
            self.envtechnicianid = None
            self.envtestpt1descr = None
            self.envtestpt1last = None
            self.envtestpt1marginval = None
            self.envtestpt1measure = None
            self.envtestpt1warn = None
            self.envtestpt2descr = None
            self.envtestpt2last = None
            self.envtestpt2marginval = None
            self.envtestpt2measure = None
            self.envtestpt2warn = None
            self.envtestpt3descr = None
            self.envtestpt3last = None
            self.envtestpt3marginpercent = None
            self.envtestpt3measure = None
            self.envtestpt3warn = None
            self.envtestpt4descr = None
            self.envtestpt4last = None
            self.envtestpt4marginpercent = None
            self.envtestpt4measure = None
            self.envtestpt4warn = None
            self.envtestpt5descr = None
            self.envtestpt5last = None
            self.envtestpt5marginpercent = None
            self.envtestpt5measure = None
            self.envtestpt5warn = None
            self.envtestpt6descr = None
            self.envtestpt6last = None
            self.envtestpt6marginpercent = None
            self.envtestpt6measure = None
            self.envtestpt6warn = None
            self.envtype = None
            self.freemem = None
            self.hostconfigaddr = None
            self.hostconfigname = None
            self.hostconfigproto = None
            self.hostconfigset = None
            self.hostname = None
            self.idlecount = None
            self.idlewired = None
            self.netconfigaddr = None
            self.netconfigname = None
            self.netconfigproto = None
            self.netconfigset = None
            self.ping = None
            self.romid = None
            self.syscleararp = None
            self.sysclearint = None
            self.sysconfigaddr = None
            self.sysconfigname = None
            self.sysconfigproto = None
            self.whyreload = None
            self.writemem = None
            self.writenet = None

        class EnvTestPt1warn_Enum(Enum):
            """
            EnvTestPt1warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt1warn_Enum']


        class EnvTestPt2warn_Enum(Enum):
            """
            EnvTestPt2warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt2warn_Enum']


        class EnvTestPt3warn_Enum(Enum):
            """
            EnvTestPt3warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt3warn_Enum']


        class EnvTestPt4warn_Enum(Enum):
            """
            EnvTestPt4warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt4warn_Enum']


        class EnvTestPt5warn_Enum(Enum):
            """
            EnvTestPt5warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt5warn_Enum']


        class EnvTestPt6warn_Enum(Enum):
            """
            EnvTestPt6warn_Enum

            Is this test point at a warning level?

            """

            WARNING = 1

            NOWARNING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
                return meta._meta_table['OLDCISCOSYSMIB.Lsystem.EnvTestPt6warn_Enum']


        @property
        def _common_path(self):

            return '/OLD-CISCO-SYS-MIB:OLD-CISCO-SYS-MIB/OLD-CISCO-SYS-MIB:lsystem'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.authaddr is not None:
                return True

            if self.avgbusy1 is not None:
                return True

            if self.avgbusy5 is not None:
                return True

            if self.boothost is not None:
                return True

            if self.bufferbgcreate is not None:
                return True

            if self.bufferbgfree is not None:
                return True

            if self.bufferbghit is not None:
                return True

            if self.bufferbgmax is not None:
                return True

            if self.bufferbgmiss is not None:
                return True

            if self.bufferbgsize is not None:
                return True

            if self.bufferbgtotal is not None:
                return True

            if self.bufferbgtrim is not None:
                return True

            if self.bufferelcreate is not None:
                return True

            if self.bufferelfree is not None:
                return True

            if self.bufferelhit is not None:
                return True

            if self.bufferelmax is not None:
                return True

            if self.bufferelmiss is not None:
                return True

            if self.bufferfail is not None:
                return True

            if self.bufferhgcreate is not None:
                return True

            if self.bufferhgfree is not None:
                return True

            if self.bufferhghit is not None:
                return True

            if self.bufferhgmax is not None:
                return True

            if self.bufferhgmiss is not None:
                return True

            if self.bufferhgsize is not None:
                return True

            if self.bufferhgtotal is not None:
                return True

            if self.bufferhgtrim is not None:
                return True

            if self.bufferlgcreate is not None:
                return True

            if self.bufferlgfree is not None:
                return True

            if self.bufferlghit is not None:
                return True

            if self.bufferlgmax is not None:
                return True

            if self.bufferlgmiss is not None:
                return True

            if self.bufferlgsize is not None:
                return True

            if self.bufferlgtotal is not None:
                return True

            if self.bufferlgtrim is not None:
                return True

            if self.buffermdcreate is not None:
                return True

            if self.buffermdfree is not None:
                return True

            if self.buffermdhit is not None:
                return True

            if self.buffermdmax is not None:
                return True

            if self.buffermdmiss is not None:
                return True

            if self.buffermdsize is not None:
                return True

            if self.buffermdtotal is not None:
                return True

            if self.buffermdtrim is not None:
                return True

            if self.buffernomem is not None:
                return True

            if self.buffersmcreate is not None:
                return True

            if self.buffersmfree is not None:
                return True

            if self.buffersmhit is not None:
                return True

            if self.buffersmmax is not None:
                return True

            if self.buffersmmiss is not None:
                return True

            if self.buffersmsize is not None:
                return True

            if self.buffersmtotal is not None:
                return True

            if self.buffersmtrim is not None:
                return True

            if self.busyper is not None:
                return True

            if self.ciscocontactinfo is not None:
                return True

            if self.domainname is not None:
                return True

            if self.envburndate is not None:
                return True

            if self.envfirmversion is not None:
                return True

            if self.envpresent is not None:
                return True

            if self.envserialnumber is not None:
                return True

            if self.envtechnicianid is not None:
                return True

            if self.envtestpt1descr is not None:
                return True

            if self.envtestpt1last is not None:
                return True

            if self.envtestpt1marginval is not None:
                return True

            if self.envtestpt1measure is not None:
                return True

            if self.envtestpt1warn is not None:
                return True

            if self.envtestpt2descr is not None:
                return True

            if self.envtestpt2last is not None:
                return True

            if self.envtestpt2marginval is not None:
                return True

            if self.envtestpt2measure is not None:
                return True

            if self.envtestpt2warn is not None:
                return True

            if self.envtestpt3descr is not None:
                return True

            if self.envtestpt3last is not None:
                return True

            if self.envtestpt3marginpercent is not None:
                return True

            if self.envtestpt3measure is not None:
                return True

            if self.envtestpt3warn is not None:
                return True

            if self.envtestpt4descr is not None:
                return True

            if self.envtestpt4last is not None:
                return True

            if self.envtestpt4marginpercent is not None:
                return True

            if self.envtestpt4measure is not None:
                return True

            if self.envtestpt4warn is not None:
                return True

            if self.envtestpt5descr is not None:
                return True

            if self.envtestpt5last is not None:
                return True

            if self.envtestpt5marginpercent is not None:
                return True

            if self.envtestpt5measure is not None:
                return True

            if self.envtestpt5warn is not None:
                return True

            if self.envtestpt6descr is not None:
                return True

            if self.envtestpt6last is not None:
                return True

            if self.envtestpt6marginpercent is not None:
                return True

            if self.envtestpt6measure is not None:
                return True

            if self.envtestpt6warn is not None:
                return True

            if self.envtype is not None:
                return True

            if self.freemem is not None:
                return True

            if self.hostconfigaddr is not None:
                return True

            if self.hostconfigname is not None:
                return True

            if self.hostconfigproto is not None:
                return True

            if self.hostconfigset is not None:
                return True

            if self.hostname is not None:
                return True

            if self.idlecount is not None:
                return True

            if self.idlewired is not None:
                return True

            if self.netconfigaddr is not None:
                return True

            if self.netconfigname is not None:
                return True

            if self.netconfigproto is not None:
                return True

            if self.netconfigset is not None:
                return True

            if self.ping is not None:
                return True

            if self.romid is not None:
                return True

            if self.syscleararp is not None:
                return True

            if self.sysclearint is not None:
                return True

            if self.sysconfigaddr is not None:
                return True

            if self.sysconfigname is not None:
                return True

            if self.sysconfigproto is not None:
                return True

            if self.whyreload is not None:
                return True

            if self.writemem is not None:
                return True

            if self.writenet is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
            return meta._meta_table['OLDCISCOSYSMIB.Lsystem']['meta_info']

    @property
    def _common_path(self):

        return '/OLD-CISCO-SYS-MIB:OLD-CISCO-SYS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.lsystem is not None and self.lsystem._has_data():
            return True

        if self.lsystem is not None and self.lsystem.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.old._meta import _OLD_CISCO_SYS_MIB as meta
        return meta._meta_table['OLDCISCOSYSMIB']['meta_info']


