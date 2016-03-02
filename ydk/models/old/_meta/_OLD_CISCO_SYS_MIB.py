


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt1warn_Enum' : _MetaInfoEnum('EnvTestPt1warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt2warn_Enum' : _MetaInfoEnum('EnvTestPt2warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt3warn_Enum' : _MetaInfoEnum('EnvTestPt3warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt4warn_Enum' : _MetaInfoEnum('EnvTestPt4warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt5warn_Enum' : _MetaInfoEnum('EnvTestPt5warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem.EnvTestPt6warn_Enum' : _MetaInfoEnum('EnvTestPt6warn_Enum', 'ydk.models.old.OLD_CISCO_SYS_MIB',
        {
            'warning':'WARNING',
            'noWarning':'NOWARNING',
        }, 'OLD-CISCO-SYS-MIB', _yang_ns._namespaces['OLD-CISCO-SYS-MIB']),
    'OLDCISCOSYSMIB.Lsystem' : {
        'meta_info' : _MetaInfoClass('OLDCISCOSYSMIB.Lsystem',
            False, 
            [
            _MetaInfoClassMember('authAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This variable contains the last SNMP
                authorization failure IP address.
                ''',
                'authaddr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('avgBusy1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                1 minute exponentially-decayed moving
                average of the CPU busy percentage.
                ''',
                'avgbusy1',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('avgBusy5', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                5 minute exponentially-decayed moving
                average of the CPU busy percentage.
                ''',
                'avgbusy5',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bootHost', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Contains the IP address of the host that
                supplied the currently running software.
                ''',
                'boothost',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of big buffer creates.
                ''',
                'bufferbgcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free big buffers.
                ''',
                'bufferbgfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of big buffer hits.
                ''',
                'bufferbghit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of big buffers.
                ''',
                'bufferbgmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of big buffer misses.
                ''',
                'bufferbgmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the size of big buffers.
                ''',
                'bufferbgsize',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgTotal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the total number of big buffers.
                ''',
                'bufferbgtotal',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferBgTrim', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of big buffer trims.
                ''',
                'bufferbgtrim',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferElCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of buffer element
                creates.
                ''',
                'bufferelcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferElFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free buffer
                elements.
                ''',
                'bufferelfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferElHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of buffer element hits.
                ''',
                'bufferelhit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferElMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of buffer
                elements.
                ''',
                'bufferelmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferElMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of buffer element
                misses.
                ''',
                'bufferelmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferFail', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Count of the number of buffer allocation
                failures.
                ''',
                'bufferfail',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of huge buffer creates.
                ''',
                'bufferhgcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free huge buffers.
                ''',
                'bufferhgfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of huge buffer hits.
                ''',
                'bufferhghit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of huge
                buffers.
                ''',
                'bufferhgmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of huge buffer misses.
                ''',
                'bufferhgmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the size of huge buffers.
                ''',
                'bufferhgsize',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgTotal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the total number of huge buffers.
                ''',
                'bufferhgtotal',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferHgTrim', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of huge buffer trims.
                ''',
                'bufferhgtrim',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of large buffer
                creates.
                ''',
                'bufferlgcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free large buffers.
                ''',
                'bufferlgfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of large buffer hits.
                ''',
                'bufferlghit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of large
                buffers.
                ''',
                'bufferlgmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of large buffer misses.
                ''',
                'bufferlgmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the size of large buffers.
                ''',
                'bufferlgsize',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgTotal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the total number of large buffers.
                ''',
                'bufferlgtotal',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferLgTrim', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of large buffer trims.
                ''',
                'bufferlgtrim',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of medium buffer
                creates.
                ''',
                'buffermdcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free medium buffers.
                ''',
                'buffermdfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of medium buffer hits.
                ''',
                'buffermdhit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of medium
                buffers.
                ''',
                'buffermdmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of medium buffer
                misses.
                ''',
                'buffermdmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the size of medium buffers.
                ''',
                'buffermdsize',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdTotal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the total number of medium
                buffers.
                ''',
                'buffermdtotal',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferMdTrim', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of medium buffer trims.
                ''',
                'buffermdtrim',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferNoMem', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Count of the number of buffer create
                failures due to no free memory.
                ''',
                'buffernomem',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmCreate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of small buffer
                creates.
                ''',
                'buffersmcreate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmFree', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of free small buffers.
                ''',
                'buffersmfree',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmHit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of small buffer hits.
                ''',
                'buffersmhit',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the maximum number of small
                buffers.
                ''',
                'buffersmmax',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmMiss', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of small buffer misses.
                ''',
                'buffersmmiss',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the size of small buffers.
                ''',
                'buffersmsize',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmTotal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the total number of small buffers.
                ''',
                'buffersmtotal',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('bufferSmTrim', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Contains the number of small buffer trims.
                ''',
                'buffersmtrim',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('busyPer', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                CPU busy percentage in the last 5 second
                period. Not the last 5 realtime seconds but
                the last 5 second period in the scheduler.
                ''',
                'busyper',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('ciscoContactInfo', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                cisco's name and address
                ''',
                'ciscocontactinfo',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('domainName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This variable is the domain portion of the
                domain name of the host.
                ''',
                'domainname',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envBurnDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The calibration / burn in date
                ''',
                'envburndate',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envFirmVersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of Environmental Card firmware
                ''',
                'envfirmversion',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envPresent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Is there an environmental monitor card in
                this box?, 0 - No, 1-AGS card present, wrong
                firmware, 2-AGS CARD present, firmware ok,
                3-7000 support
                ''',
                'envpresent',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envSerialNumber', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Serial Number of environmental monitor card
                ''',
                'envserialnumber',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTechnicianID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Technician ID
                ''',
                'envtechnicianid',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt1Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 1. Typically
                ambient air or the temperature of air
                entering the router
                ''',
                'envtestpt1descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt1last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt1 when last shutdown
                occurred.
                ''',
                'envtestpt1last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt1MarginVal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value at which the router will shutdown.
                Typically the ambient air temperature that
                will shut the router down. (e.g. 43)
                ''',
                'envtestpt1marginval',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt1Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 1. Typically a
                temperature in centigrade.
                ''',
                'envtestpt1measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt1warn', REFERENCE_ENUM_CLASS, 'EnvTestPt1warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt1warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt1warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt2Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 2. Typically
                airflow or the temperature of air leaving the
                router
                ''',
                'envtestpt2descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt2last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt2 when last shutdown
                occurred.
                ''',
                'envtestpt2last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt2MarginVal', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value at which the router will shutdown.
                Typically the airflow air temperature that
                will shut the router down. (e.g. 58)
                ''',
                'envtestpt2marginval',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt2Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 2. Typically a
                temperature in centigrade.
                ''',
                'envtestpt2measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt2warn', REFERENCE_ENUM_CLASS, 'EnvTestPt2warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt2warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt2warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt3Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 3. Typically
                +5 volt
                ''',
                'envtestpt3descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt3last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt3 when last shutdown
                occurred.
                ''',
                'envtestpt3last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt3MarginPercent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                +/- Percentage that will shut the router
                down, (e.g. 10%) typically +5 volt
                ''',
                'envtestpt3marginpercent',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt3Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 3. Typically the
                value in millivolts of the +5v supply
                ''',
                'envtestpt3measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt3warn', REFERENCE_ENUM_CLASS, 'EnvTestPt3warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt3warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt3warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt4Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 4. Typically
                +12 volt
                ''',
                'envtestpt4descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt4last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt4 when last shutdown
                occurred.
                ''',
                'envtestpt4last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt4MarginPercent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                +/- Percentage that will shut the router
                down, (e.g. 15%) typically +12 volt
                ''',
                'envtestpt4marginpercent',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt4Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 4. Typically the
                value in millivolts of the +12v supply
                ''',
                'envtestpt4measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt4warn', REFERENCE_ENUM_CLASS, 'EnvTestPt4warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt4warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt4warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt5Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 5. Typically
                -12 volt
                ''',
                'envtestpt5descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt5last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt5 when last shutdown
                occurred.
                ''',
                'envtestpt5last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt5MarginPercent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                +/- Percentage that will shut the router
                down, (e.g. 15%) typically -12 volt
                ''',
                'envtestpt5marginpercent',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt5Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 5. Typically the
                value in millivolts of the -12v supply
                ''',
                'envtestpt5measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt5warn', REFERENCE_ENUM_CLASS, 'EnvTestPt5warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt5warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt5warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt6Descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the test point 6. Typically
                -5 volt
                ''',
                'envtestpt6descr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt6last', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Value of TestPt6 when last shutdown
                occurred.
                ''',
                'envtestpt6last',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt6MarginPercent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                +/- Percentage that will shut the router
                down, (e.g. 10%) typically -5 volt
                ''',
                'envtestpt6marginpercent',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt6Measure', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Current value of test point 6. Typically the
                value in millivolts of the -5v supply
                ''',
                'envtestpt6measure',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envTestPt6warn', REFERENCE_ENUM_CLASS, 'EnvTestPt6warn_Enum' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem.EnvTestPt6warn_Enum', 
                [], [], 
                '''                Is this test point at a warning level?
                ''',
                'envtestpt6warn',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('envType', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The type of environmental card
                ''',
                'envtype',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('freeMem', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The freeMem mib object is obsolete as of IOS 11.1
                It has been replaced with the cisco memory pool mib
                ''',
                'freemem',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('hostConfigAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Contains the address of the host that
                provided the host-config file.
                ''',
                'hostconfigaddr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('hostConfigName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contains the name of the last configured
                host-confg file.
                ''',
                'hostconfigname',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('hostConfigProto', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Holds the protocol that supplied the host-
                confg file.
                ''',
                'hostconfigproto',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('hostConfigSet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Cause the loading of a new host-confg file
                using TFTP.
                ''',
                'hostconfigset',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('hostName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This variable represents the name of the
                host in printable ascii characters.
                ''',
                'hostname',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('idleCount', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                cisco internal variable. not to be used
                ''',
                'idlecount',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('idleWired', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                cisco internal variable. not to be used
                ''',
                'idlewired',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('netConfigAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Holds the address of the host that supplied
                the network-confg file.
                ''',
                'netconfigaddr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('netConfigName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Holds the name of the network configuration
                file.
                ''',
                'netconfigname',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('netConfigProto', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Holds the protocol that supplied the
                network-confg file.
                ''',
                'netconfigproto',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('netConfigSet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Cause the loading of a new network-confg
                file using TFTP.
                ''',
                'netconfigset',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('ping', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The ping mib object is obsolete as of IOS 10.2
                It has been superseded by the Cisco Ping MIB
                ''',
                'ping',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('romId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This variable contains a printable octet
                string which contains the System Bootstrap
                description and version identification.
                ''',
                'romid',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('sysClearARP', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Perform a clearing of the entire ARP cache
                and invalidation of route caches.
                ''',
                'syscleararp',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('sysClearInt', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Clear interface given IfIndex as value.
                ''',
                'sysclearint',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('sysConfigAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Holds the address of the host that supplied
                the system boot image.
                ''',
                'sysconfigaddr',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('sysConfigName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Holds the name of the system boot image.
                ''',
                'sysconfigname',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('sysConfigProto', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Holds the protocol that supplied the system
                boot image.
                ''',
                'sysconfigproto',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('whyReload', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This variable contains a printable octet
                string which contains the reason why the
                system was last restarted.
                ''',
                'whyreload',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('writeMem', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Write configuration into non-volatile memory
                / erase config memory if 0.
                ''',
                'writemem',
                'OLD-CISCO-SYS-MIB', False),
            _MetaInfoClassMember('writeNet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Write configuration to host using TFTP.
                ''',
                'writenet',
                'OLD-CISCO-SYS-MIB', False),
            ],
            'OLD-CISCO-SYS-MIB',
            'lsystem',
            _yang_ns._namespaces['OLD-CISCO-SYS-MIB'],
        'ydk.models.old.OLD_CISCO_SYS_MIB'
        ),
    },
    'OLDCISCOSYSMIB' : {
        'meta_info' : _MetaInfoClass('OLDCISCOSYSMIB',
            False, 
            [
            _MetaInfoClassMember('lsystem', REFERENCE_CLASS, 'Lsystem' , 'ydk.models.old.OLD_CISCO_SYS_MIB', 'OLDCISCOSYSMIB.Lsystem', 
                [], [], 
                '''                ''',
                'lsystem',
                'OLD-CISCO-SYS-MIB', False),
            ],
            'OLD-CISCO-SYS-MIB',
            'OLD-CISCO-SYS-MIB',
            _yang_ns._namespaces['OLD-CISCO-SYS-MIB'],
        'ydk.models.old.OLD_CISCO_SYS_MIB'
        ),
    },
}
_meta_table['OLDCISCOSYSMIB.Lsystem']['meta_info'].parent =_meta_table['OLDCISCOSYSMIB']['meta_info']
