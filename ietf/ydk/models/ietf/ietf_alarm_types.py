""" ietf_alarm_types 

This module contains Alarm data type definitions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EventTypeIdentity(object):
    """
    Base identity from which specific alarm types are
        derived.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EventTypeIdentity']['meta_info']


class ProbableCauseTypeIdentity(object):
    """
    Base identity from which specific probable cause types
        are derived.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProbableCauseTypeIdentity']['meta_info']


class TimeoutexpiredIdentity(ProbableCauseTypeIdentity):
    """
    timeoutExpired
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TimeoutexpiredIdentity']['meta_info']


class ExternalpointfailureIdentity(ProbableCauseTypeIdentity):
    """
    externalPointFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExternalpointfailureIdentity']['meta_info']


class SynchronizationsourcemismatchIdentity(ProbableCauseTypeIdentity):
    """
    synchronizationSourceMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SynchronizationsourcemismatchIdentity']['meta_info']


class NeidentifierduplicationIdentity(ProbableCauseTypeIdentity):
    """
    nEIdentifierDuplication
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['NeidentifierduplicationIdentity']['meta_info']


class Timingproblemx733Identity(ProbableCauseTypeIdentity):
    """
    timingProblemX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Timingproblemx733Identity']['meta_info']


class Receiverfailurex733Identity(ProbableCauseTypeIdentity):
    """
    receiverFailureX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Receiverfailurex733Identity']['meta_info']


class ExternalifdeviceproblemIdentity(ProbableCauseTypeIdentity):
    """
    externalIFDeviceProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExternalifdeviceproblemIdentity']['meta_info']


class PowersupplyfailureIdentity(ProbableCauseTypeIdentity):
    """
    powerSupplyFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PowersupplyfailureIdentity']['meta_info']


class GeneratorfailureIdentity(ProbableCauseTypeIdentity):
    """
    generatorFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['GeneratorfailureIdentity']['meta_info']


class DemodulationfailureIdentity(ProbableCauseTypeIdentity):
    """
    demodulationFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DemodulationfailureIdentity']['meta_info']


class CommunicationEventTypeIdentity(EventTypeIdentity):
    """
    Alarm of this type is principally associated with the
        procedures and/or processes required to convey
        information from one point to another.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CommunicationEventTypeIdentity']['meta_info']


class TimingproblemIdentity(ProbableCauseTypeIdentity):
    """
    timingProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TimingproblemIdentity']['meta_info']


class TransmissionerrorIdentity(ProbableCauseTypeIdentity):
    """
    transmissionError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TransmissionerrorIdentity']['meta_info']


class UnderlayingresourceunavailableIdentity(ProbableCauseTypeIdentity):
    """
    underlayingResourceUnavailable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['UnderlayingresourceunavailableIdentity']['meta_info']


class LossofrealtimelIdentity(ProbableCauseTypeIdentity):
    """
    lossOfRealTimel
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofrealtimelIdentity']['meta_info']


class MemorymismatchIdentity(ProbableCauseTypeIdentity):
    """
    memoryMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['MemorymismatchIdentity']['meta_info']


class ModulationfailureIdentity(ProbableCauseTypeIdentity):
    """
    modulationFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ModulationfailureIdentity']['meta_info']


class BandwidthreducedIdentity(ProbableCauseTypeIdentity):
    """
    bandwidthReduced
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BandwidthreducedIdentity']['meta_info']


class ResponsetimeexecessiveIdentity(ProbableCauseTypeIdentity):
    """
    responseTimeExecessive
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ResponsetimeexecessiveIdentity']['meta_info']


class RemotealarminterfaceIdentity(ProbableCauseTypeIdentity):
    """
    remoteAlarmInterface
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RemotealarminterfaceIdentity']['meta_info']


class EnginefailureIdentity(ProbableCauseTypeIdentity):
    """
    engineFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EnginefailureIdentity']['meta_info']


class AuthenticationfailureIdentity(ProbableCauseTypeIdentity):
    """
    authenticationFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AuthenticationfailureIdentity']['meta_info']


class ReplaceableunitmissingIdentity(ProbableCauseTypeIdentity):
    """
    replaceableUnitMissing
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReplaceableunitmissingIdentity']['meta_info']


class LanerrorIdentity(ProbableCauseTypeIdentity):
    """
    lanError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LanerrorIdentity']['meta_info']


class CabletamperIdentity(ProbableCauseTypeIdentity):
    """
    cableTamper
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CabletamperIdentity']['meta_info']


class Transmitfailurex733Identity(ProbableCauseTypeIdentity):
    """
    transmitFailureX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Transmitfailurex733Identity']['meta_info']


class MultiplexerproblemIdentity(ProbableCauseTypeIdentity):
    """
    multiplexerProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['MultiplexerproblemIdentity']['meta_info']


class PumpfailureIdentity(ProbableCauseTypeIdentity):
    """
    pumpFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PumpfailureIdentity']['meta_info']


class RoutingfailureIdentity(ProbableCauseTypeIdentity):
    """
    routingFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RoutingfailureIdentity']['meta_info']


class Lossofframex733Identity(ProbableCauseTypeIdentity):
    """
    lossOfFrameX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Lossofframex733Identity']['meta_info']


class VentilationssystemfailureIdentity(ProbableCauseTypeIdentity):
    """
    ventilationsSystemFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['VentilationssystemfailureIdentity']['meta_info']


class OutofmemoryIdentity(ProbableCauseTypeIdentity):
    """
    outOfMemory
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OutofmemoryIdentity']['meta_info']


class Outofmemoryx733Identity(ProbableCauseTypeIdentity):
    """
    outOfMemoryX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Outofmemoryx733Identity']['meta_info']


class TransmitfailureIdentity(ProbableCauseTypeIdentity):
    """
    transmitFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TransmitfailureIdentity']['meta_info']


class Congestionx733Identity(ProbableCauseTypeIdentity):
    """
    congestionX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Congestionx733Identity']['meta_info']


class RectifierlowfvoltageIdentity(ProbableCauseTypeIdentity):
    """
    rectifierLowFVoltage
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RectifierlowfvoltageIdentity']['meta_info']


class DatasetormodemerrorIdentity(ProbableCauseTypeIdentity):
    """
    dataSetOrModemError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DatasetormodemerrorIdentity']['meta_info']


class SignalqualityevaluationfailureIdentity(ProbableCauseTypeIdentity):
    """
    signalQualityEvaluationFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SignalqualityevaluationfailureIdentity']['meta_info']


class EnvironmentalEventTypeIdentity(EventTypeIdentity):
    """
    Alarm of this type is principally associated with a
        condition relating to an enclosure in which the
        equipment resides.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EnvironmentalEventTypeIdentity']['meta_info']


class LowwaterIdentity(ProbableCauseTypeIdentity):
    """
    lowWater
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowwaterIdentity']['meta_info']


class Enclosuredooropenx733Identity(ProbableCauseTypeIdentity):
    """
    enclosureDoorOpenX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Enclosuredooropenx733Identity']['meta_info']


class LowcablepressureIdentity(ProbableCauseTypeIdentity):
    """
    lowCablePressure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowcablepressureIdentity']['meta_info']


class FramingerrorIdentity(ProbableCauseTypeIdentity):
    """
    framingError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FramingerrorIdentity']['meta_info']


class BatterychargingfailureIdentity(ProbableCauseTypeIdentity):
    """
    batteryChargingFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BatterychargingfailureIdentity']['meta_info']


class AntennafailureIdentity(ProbableCauseTypeIdentity):
    """
    antennaFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AntennafailureIdentity']['meta_info']


class LowfuelIdentity(ProbableCauseTypeIdentity):
    """
    lowFuel
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowfuelIdentity']['meta_info']


class LowhumidityIdentity(ProbableCauseTypeIdentity):
    """
    lowHumidity
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowhumidityIdentity']['meta_info']


class ResourceatornearingcapacityIdentity(ProbableCauseTypeIdentity):
    """
    resourceAtOrNearingCapacity
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ResourceatornearingcapacityIdentity']['meta_info']


class Storagecapacityproblemx733Identity(ProbableCauseTypeIdentity):
    """
    storageCapacityProblemX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Storagecapacityproblemx733Identity']['meta_info']


class HighwindIdentity(ProbableCauseTypeIdentity):
    """
    highWind
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['HighwindIdentity']['meta_info']


class DuplicateinformationIdentity(ProbableCauseTypeIdentity):
    """
    duplicateInformation
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DuplicateinformationIdentity']['meta_info']


class LowbatterythresholdIdentity(ProbableCauseTypeIdentity):
    """
    lowBatteryThreshold
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowbatterythresholdIdentity']['meta_info']


class ExcessiveresponsetimeIdentity(ProbableCauseTypeIdentity):
    """
    excessiveResponseTime
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExcessiveresponsetimeIdentity']['meta_info']


class HeatingventcoolingsystemproblemIdentity(ProbableCauseTypeIdentity):
    """
    heatingVentCoolingSystemProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['HeatingventcoolingsystemproblemIdentity']['meta_info']


class RectifierhighvoltageIdentity(ProbableCauseTypeIdentity):
    """
    rectifierHighVoltage
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RectifierhighvoltageIdentity']['meta_info']


class BatterydischargingIdentity(ProbableCauseTypeIdentity):
    """
    batteryDischarging
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BatterydischargingIdentity']['meta_info']


class ToxicleakdetectedIdentity(ProbableCauseTypeIdentity):
    """
    toxicLeakDetected
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ToxicleakdetectedIdentity']['meta_info']


class OtherEventTypeIdentity(EventTypeIdentity):
    """
    Alarm type other than the 
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OtherEventTypeIdentity']['meta_info']


class ReducedloggingcapabilityIdentity(ProbableCauseTypeIdentity):
    """
    reducedLoggingCapability
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReducedloggingcapabilityIdentity']['meta_info']


class ConfigurationorcustomisationerrorIdentity(ProbableCauseTypeIdentity):
    """
    configurationOrCustomisationError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ConfigurationorcustomisationerrorIdentity']['meta_info']


class DenialofserviceIdentity(ProbableCauseTypeIdentity):
    """
    denialOfService
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DenialofserviceIdentity']['meta_info']


class DiskfailureIdentity(ProbableCauseTypeIdentity):
    """
    diskFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DiskfailureIdentity']['meta_info']


class LinecardproblemIdentity(ProbableCauseTypeIdentity):
    """
    lineCardProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LinecardproblemIdentity']['meta_info']


class HumidityunacceptableIdentity(ProbableCauseTypeIdentity):
    """
    humidityUnacceptable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['HumidityunacceptableIdentity']['meta_info']


class CommercialpowerfailureIdentity(ProbableCauseTypeIdentity):
    """
    commercialPowerFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CommercialpowerfailureIdentity']['meta_info']


class Versionmismatchx733Identity(ProbableCauseTypeIdentity):
    """
    versionMismatchX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Versionmismatchx733Identity']['meta_info']


class OutofcpucyclesIdentity(ProbableCauseTypeIdentity):
    """
    outOfCPUCycles
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OutofcpucyclesIdentity']['meta_info']


class UnavailableIdentity(ProbableCauseTypeIdentity):
    """
    unavailable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['UnavailableIdentity']['meta_info']


class NonrepudiationfailureIdentity(ProbableCauseTypeIdentity):
    """
    nonRepudiationFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['NonrepudiationfailureIdentity']['meta_info']


class Softwareerrorx733Identity(ProbableCauseTypeIdentity):
    """
    softwareErrorX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Softwareerrorx733Identity']['meta_info']


class BatteryfailureIdentity(ProbableCauseTypeIdentity):
    """
    batteryFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BatteryfailureIdentity']['meta_info']


class FusefailureIdentity(ProbableCauseTypeIdentity):
    """
    fuseFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FusefailureIdentity']['meta_info']


class Pumpfailurex733Identity(ProbableCauseTypeIdentity):
    """
    pumpFailureX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Pumpfailurex733Identity']['meta_info']


class DegradedsignalIdentity(ProbableCauseTypeIdentity):
    """
    degradedSignal
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DegradedsignalIdentity']['meta_info']


class ProcessingEventTypeIdentity(EventTypeIdentity):
    """
    Alarm of this type is principally associated with a
        software or processing alarm.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProcessingEventTypeIdentity']['meta_info']


class AirconditioningfailureIdentity(ProbableCauseTypeIdentity):
    """
    airConditioningFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AirconditioningfailureIdentity']['meta_info']


class ReceiverfailureIdentity(ProbableCauseTypeIdentity):
    """
    receiverFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReceiverfailureIdentity']['meta_info']


class UnexpectedinformationIdentity(ProbableCauseTypeIdentity):
    """
    unexpectedInformation
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['UnexpectedinformationIdentity']['meta_info']


class ExcessivevibrationIdentity(ProbableCauseTypeIdentity):
    """
    excessiveVibration
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExcessivevibrationIdentity']['meta_info']


class PowerproblemsIdentity(ProbableCauseTypeIdentity):
    """
    powerProblems
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PowerproblemsIdentity']['meta_info']


class Localnodetransmissionerrorx733Identity(ProbableCauseTypeIdentity):
    """
    localNodeTransmissionErrorX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Localnodetransmissionerrorx733Identity']['meta_info']


class IodeviceerrorIdentity(ProbableCauseTypeIdentity):
    """
    iODeviceError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['IodeviceerrorIdentity']['meta_info']


class ReceivefailureIdentity(ProbableCauseTypeIdentity):
    """
    receiveFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReceivefailureIdentity']['meta_info']


class InputdeviceerrorIdentity(ProbableCauseTypeIdentity):
    """
    inputDeviceError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InputdeviceerrorIdentity']['meta_info']


class BackplanefailureIdentity(ProbableCauseTypeIdentity):
    """
    backplaneFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BackplanefailureIdentity']['meta_info']


class LossofsynchronisationIdentity(ProbableCauseTypeIdentity):
    """
    lossOfSynchronisation
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofsynchronisationIdentity']['meta_info']


class CongestionIdentity(ProbableCauseTypeIdentity):
    """
    congestion
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CongestionIdentity']['meta_info']


class TerminalproblemIdentity(ProbableCauseTypeIdentity):
    """
    terminalProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TerminalproblemIdentity']['meta_info']


class LossofredundancyIdentity(ProbableCauseTypeIdentity):
    """
    lossOfRedundancy
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofredundancyIdentity']['meta_info']


class HightemperatureIdentity(ProbableCauseTypeIdentity):
    """
    highTemperature
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['HightemperatureIdentity']['meta_info']


class IntrusiondetectionIdentity(ProbableCauseTypeIdentity):
    """
    intrusionDetection
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['IntrusiondetectionIdentity']['meta_info']


class TrunkcardproblemIdentity(ProbableCauseTypeIdentity):
    """
    trunkCardProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TrunkcardproblemIdentity']['meta_info']


class AirdryerfailureIdentity(ProbableCauseTypeIdentity):
    """
    airDryerFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AirdryerfailureIdentity']['meta_info']


class PowerproblemIdentity(ProbableCauseTypeIdentity):
    """
    powerProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PowerproblemIdentity']['meta_info']


class EquipmentmalfunctionIdentity(ProbableCauseTypeIdentity):
    """
    equipmentMalfunction
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EquipmentmalfunctionIdentity']['meta_info']


class ApplicationsubsystemfailtureIdentity(ProbableCauseTypeIdentity):
    """
    applicationSubsystemFailture
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ApplicationsubsystemfailtureIdentity']['meta_info']


class FrequencyhoppingfailureIdentity(ProbableCauseTypeIdentity):
    """
    frequencyHoppingFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FrequencyhoppingfailureIdentity']['meta_info']


class ConfigurationorcustomizationerrorIdentity(ProbableCauseTypeIdentity):
    """
    configurationOrCustomizationError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ConfigurationorcustomizationerrorIdentity']['meta_info']


class EquipmentidentifierduplicationIdentity(ProbableCauseTypeIdentity):
    """
    equipmentIdentifierDuplication
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EquipmentidentifierduplicationIdentity']['meta_info']


class SmokeIdentity(ProbableCauseTypeIdentity):
    """
    smoke
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SmokeIdentity']['meta_info']


class Framingerrorx733Identity(ProbableCauseTypeIdentity):
    """
    framingErrorX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Framingerrorx733Identity']['meta_info']


class InputoutputdeviceerrorIdentity(ProbableCauseTypeIdentity):
    """
    inputOutputDeviceError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InputoutputdeviceerrorIdentity']['meta_info']


class Remotenodetransmissionerrorx733Identity(ProbableCauseTypeIdentity):
    """
    remoteNodeTransmissionErrorX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Remotenodetransmissionerrorx733Identity']['meta_info']


class PressureunacceptableIdentity(ProbableCauseTypeIdentity):
    """
    pressureUnacceptable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PressureunacceptableIdentity']['meta_info']


class CommunicationssubsystemfailureIdentity(ProbableCauseTypeIdentity):
    """
    communicationsSubsystemFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CommunicationssubsystemfailureIdentity']['meta_info']


class Degradedsignalx733Identity(ProbableCauseTypeIdentity):
    """
    degradedSignalX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Degradedsignalx733Identity']['meta_info']


class ProtectingresourcefailureIdentity(ProbableCauseTypeIdentity):
    """
    protectingResourceFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProtectingresourcefailureIdentity']['meta_info']


class MaterialsupplyexhaustedIdentity(ProbableCauseTypeIdentity):
    """
    materialSupplyExhausted
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['MaterialsupplyexhaustedIdentity']['meta_info']


class ExcessiveerrorrateIdentity(ProbableCauseTypeIdentity):
    """
    excessiveErrorRate
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExcessiveerrorrateIdentity']['meta_info']


class ReplaceableunitproblemIdentity(ProbableCauseTypeIdentity):
    """
    replaceableUnitProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReplaceableunitproblemIdentity']['meta_info']


class SoftwareerrorIdentity(ProbableCauseTypeIdentity):
    """
    softwareError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SoftwareerrorIdentity']['meta_info']


class PhysicalViolationEventTypeIdentity(EventTypeIdentity):
    """
    Physical Violation Event Type
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PhysicalViolationEventTypeIdentity']['meta_info']


class ProtectionmechanismfailureIdentity(ProbableCauseTypeIdentity):
    """
    protectionMechanismFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProtectionmechanismfailureIdentity']['meta_info']


class InformationoutofsequenceIdentity(ProbableCauseTypeIdentity):
    """
    informationOutOfSequence
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InformationoutofsequenceIdentity']['meta_info']


class CoruptdataIdentity(ProbableCauseTypeIdentity):
    """
    coruptData
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CoruptdataIdentity']['meta_info']


class LeakdetectedIdentity(ProbableCauseTypeIdentity):
    """
    leakDetected
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LeakdetectedIdentity']['meta_info']


class ConnectionestablishmenterrorIdentity(ProbableCauseTypeIdentity):
    """
    connectionEstablishmentError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ConnectionestablishmenterrorIdentity']['meta_info']


class InformationmodificationdetectedIdentity(ProbableCauseTypeIdentity):
    """
    informationModificationDetected
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InformationmodificationdetectedIdentity']['meta_info']


class SfwrenvironmentproblemIdentity(ProbableCauseTypeIdentity):
    """
    sfwrEnvironmentProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SfwrenvironmentproblemIdentity']['meta_info']


class TransmitterfailureIdentity(ProbableCauseTypeIdentity):
    """
    transmitterFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TransmitterfailureIdentity']['meta_info']


class InformationmissingIdentity(ProbableCauseTypeIdentity):
    """
    informationMissing
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InformationmissingIdentity']['meta_info']


class SystemresourcesoverloadIdentity(ProbableCauseTypeIdentity):
    """
    systemResourcesOverload
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SystemresourcesoverloadIdentity']['meta_info']


class BreachofconfidentialityIdentity(ProbableCauseTypeIdentity):
    """
    breachOfConfidentiality
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BreachofconfidentialityIdentity']['meta_info']


class FiredetectorfailureIdentity(ProbableCauseTypeIdentity):
    """
    fireDetectorFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FiredetectorfailureIdentity']['meta_info']


class EnclosuredooropenIdentity(ProbableCauseTypeIdentity):
    """
    enclosureDoorOpen
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EnclosuredooropenIdentity']['meta_info']


class AisIdentity(ProbableCauseTypeIdentity):
    """
    aIS
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AisIdentity']['meta_info']


class Multiplexerproblemx733Identity(ProbableCauseTypeIdentity):
    """
    multiplexerProblemX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Multiplexerproblemx733Identity']['meta_info']


class QueuesizeexceededIdentity(ProbableCauseTypeIdentity):
    """
    queueSizeExceeded
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['QueuesizeexceededIdentity']['meta_info']


class LowtemperatueIdentity(ProbableCauseTypeIdentity):
    """
    lowTemperatue
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LowtemperatueIdentity']['meta_info']


class CoolingfanfailureIdentity(ProbableCauseTypeIdentity):
    """
    coolingFanFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CoolingfanfailureIdentity']['meta_info']


class ThresholdcrossedIdentity(ProbableCauseTypeIdentity):
    """
    thresholdCrossed
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ThresholdcrossedIdentity']['meta_info']


class LossofframeIdentity(ProbableCauseTypeIdentity):
    """
    lossOfFrame
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofframeIdentity']['meta_info']


class Bandwidthreducedx733Identity(ProbableCauseTypeIdentity):
    """
    bandwidthReducedX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Bandwidthreducedx733Identity']['meta_info']


class OutofhoursactivityIdentity(ProbableCauseTypeIdentity):
    """
    outOfHoursActivity
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OutofhoursactivityIdentity']['meta_info']


class FireIdentity(ProbableCauseTypeIdentity):
    """
    fire
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FireIdentity']['meta_info']


class ProceduralerrorIdentity(ProbableCauseTypeIdentity):
    """
    proceduralError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProceduralerrorIdentity']['meta_info']


class QosEventTypeIdentity(EventTypeIdentity):
    """
    Alarm of this type is principally associated with a
        degradation in the quality of a service.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['QosEventTypeIdentity']['meta_info']


class TimeDomainViolationEventTypeIdentity(EventTypeIdentity):
    """
    Time domain Violation Event Type
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TimeDomainViolationEventTypeIdentity']['meta_info']


class PerformancedegradedIdentity(ProbableCauseTypeIdentity):
    """
    performanceDegraded
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PerformancedegradedIdentity']['meta_info']


class DatabaseinconsistencyIdentity(ProbableCauseTypeIdentity):
    """
    databaseInconsistency
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DatabaseinconsistencyIdentity']['meta_info']


class CoolingsystemfailureIdentity(ProbableCauseTypeIdentity):
    """
    coolingSystemFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CoolingsystemfailureIdentity']['meta_info']


class SignallabelmismatchIdentity(ProbableCauseTypeIdentity):
    """
    signalLabelMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SignallabelmismatchIdentity']['meta_info']


class ExcessiveretransmissionrateIdentity(ProbableCauseTypeIdentity):
    """
    excessiveRetransmissionRate
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExcessiveretransmissionrateIdentity']['meta_info']


class Receivefailurex733Identity(ProbableCauseTypeIdentity):
    """
    receiveFailureX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Receivefailurex733Identity']['meta_info']


class ExcessiveberIdentity(ProbableCauseTypeIdentity):
    """
    excessiveBER
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExcessiveberIdentity']['meta_info']


class ToxicgasIdentity(ProbableCauseTypeIdentity):
    """
    toxicGas
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ToxicgasIdentity']['meta_info']


class PathtracemismatchIdentity(ProbableCauseTypeIdentity):
    """
    pathTraceMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PathtracemismatchIdentity']['meta_info']


class DtedceinterfaceerrorIdentity(ProbableCauseTypeIdentity):
    """
    dteDceInterfaceError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DtedceinterfaceerrorIdentity']['meta_info']


class UnderlyingresourceunavailableIdentity(ProbableCauseTypeIdentity):
    """
    underlyingResourceUnavailable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['UnderlyingresourceunavailableIdentity']['meta_info']


class IcebuildupIdentity(ProbableCauseTypeIdentity):
    """
    iceBuildUp
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['IcebuildupIdentity']['meta_info']


class FiredetectedIdentity(ProbableCauseTypeIdentity):
    """
    fireDetected
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FiredetectedIdentity']['meta_info']


class IntegrityViolationEventTypeIdentity(EventTypeIdentity):
    """
    Integrity Violation Event Type
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['IntegrityViolationEventTypeIdentity']['meta_info']


class LocalnodetransmissionerrorIdentity(ProbableCauseTypeIdentity):
    """
    localNodeTransmissionError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LocalnodetransmissionerrorIdentity']['meta_info']


class EquipmentEventTypeIdentity(EventTypeIdentity):
    """
    Alarm of this type is principally associated with an
        equipment alarm.
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['EquipmentEventTypeIdentity']['meta_info']


class ApplicationsubsystemfailureIdentity(ProbableCauseTypeIdentity):
    """
    applicationSubsystemFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ApplicationsubsystemfailureIdentity']['meta_info']


class OperationViolationEventTypeIdentity(EventTypeIdentity):
    """
    Operation Violation Event Type
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OperationViolationEventTypeIdentity']['meta_info']


class SecurityServiceOrMechanismViolationEventTypeIdentity(EventTypeIdentity):
    """
    Security Service or Mechanism Violation Event Type
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        EventTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SecurityServiceOrMechanismViolationEventTypeIdentity']['meta_info']


class ProtectionpathfailureIdentity(ProbableCauseTypeIdentity):
    """
    protectionPathFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProtectionpathfailureIdentity']['meta_info']


class LossofsignalIdentity(ProbableCauseTypeIdentity):
    """
    lossOfSignal
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofsignalIdentity']['meta_info']


class RealtimeclockfailureIdentity(ProbableCauseTypeIdentity):
    """
    realTimeClockFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RealtimeclockfailureIdentity']['meta_info']


class TemperatureunacceptableIdentity(ProbableCauseTypeIdentity):
    """
    temperatureUnacceptable
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TemperatureunacceptableIdentity']['meta_info']


class SoftwareprogramerrorIdentity(ProbableCauseTypeIdentity):
    """
    softwareProgramError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SoftwareprogramerrorIdentity']['meta_info']


class ProcessorproblemsIdentity(ProbableCauseTypeIdentity):
    """
    processorProblems
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProcessorproblemsIdentity']['meta_info']


class CommunicationsprotocolerrorIdentity(ProbableCauseTypeIdentity):
    """
    communicationsProtocolError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CommunicationsprotocolerrorIdentity']['meta_info']


class FileerrorIdentity(ProbableCauseTypeIdentity):
    """
    fileError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FileerrorIdentity']['meta_info']


class DelayedinformationIdentity(ProbableCauseTypeIdentity):
    """
    delayedInformation
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DelayedinformationIdentity']['meta_info']


class CallsetupfailureIdentity(ProbableCauseTypeIdentity):
    """
    callSetUpFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CallsetupfailureIdentity']['meta_info']


class Fileerrorx733Identity(ProbableCauseTypeIdentity):
    """
    fileErrorX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Fileerrorx733Identity']['meta_info']


class PayloadtypemismatchIdentity(ProbableCauseTypeIdentity):
    """
    payloadTypeMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['PayloadtypemismatchIdentity']['meta_info']


class ExternalequipmentfailureIdentity(ProbableCauseTypeIdentity):
    """
    externalEquipmentFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExternalequipmentfailureIdentity']['meta_info']


class DatasetproblemIdentity(ProbableCauseTypeIdentity):
    """
    dataSetProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['DatasetproblemIdentity']['meta_info']


class RemotenodetransmissionerrorIdentity(ProbableCauseTypeIdentity):
    """
    remoteNodeTransmissionError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RemotenodetransmissionerrorIdentity']['meta_info']


class SoftwareprogramabnormallyterminatedIdentity(ProbableCauseTypeIdentity):
    """
    softwareProgramAbnormallyTerminated
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SoftwareprogramabnormallyterminatedIdentity']['meta_info']


class FloodIdentity(ProbableCauseTypeIdentity):
    """
    flood
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FloodIdentity']['meta_info']


class OtherIdentity(ProbableCauseTypeIdentity):
    """
    other
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OtherIdentity']['meta_info']


class KeyexpiredIdentity(ProbableCauseTypeIdentity):
    """
    keyExpired
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['KeyexpiredIdentity']['meta_info']


class CorruptdataIdentity(ProbableCauseTypeIdentity):
    """
    corruptData
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CorruptdataIdentity']['meta_info']


class OuputdeviceerrorIdentity(ProbableCauseTypeIdentity):
    """
    ouputDeviceError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OuputdeviceerrorIdentity']['meta_info']


class VersionmismatchIdentity(ProbableCauseTypeIdentity):
    """
    versionMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['VersionmismatchIdentity']['meta_info']


class SfwrdownloadfailureIdentity(ProbableCauseTypeIdentity):
    """
    sfwrDownloadFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['SfwrdownloadfailureIdentity']['meta_info']


class TransmiterfailureIdentity(ProbableCauseTypeIdentity):
    """
    transmiterFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TransmiterfailureIdentity']['meta_info']


class HighhumidityIdentity(ProbableCauseTypeIdentity):
    """
    highHumidity
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['HighhumidityIdentity']['meta_info']


class LossofmultiframeIdentity(ProbableCauseTypeIdentity):
    """
    lossOfMultiFrame
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofmultiframeIdentity']['meta_info']


class LossofpointerIdentity(ProbableCauseTypeIdentity):
    """
    lossOfPointer
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['LossofpointerIdentity']['meta_info']


class ReplaceableunittypemismatchIdentity(ProbableCauseTypeIdentity):
    """
    replaceableUnitTypeMismatch
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ReplaceableunittypemismatchIdentity']['meta_info']


class CallestablishmenterrorIdentity(ProbableCauseTypeIdentity):
    """
    callEstablishmentError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CallestablishmenterrorIdentity']['meta_info']


class AdaptererrorIdentity(ProbableCauseTypeIdentity):
    """
    adapterError
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['AdaptererrorIdentity']['meta_info']


class TranceiverfailureIdentity(ProbableCauseTypeIdentity):
    """
    tranceiverFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['TranceiverfailureIdentity']['meta_info']


class BroadcastchannelfailureIdentity(ProbableCauseTypeIdentity):
    """
    broadcastChannelFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['BroadcastchannelfailureIdentity']['meta_info']


class UnauthorizedaccessattemptIdentity(ProbableCauseTypeIdentity):
    """
    unauthorizedAccessAttempt
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['UnauthorizedaccessattemptIdentity']['meta_info']


class InvalidmessagereceivedIdentity(ProbableCauseTypeIdentity):
    """
    invalidMessageReceived
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['InvalidmessagereceivedIdentity']['meta_info']


class OutofserviceIdentity(ProbableCauseTypeIdentity):
    """
    outOfService
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['OutofserviceIdentity']['meta_info']


class CpucycleslimitexceededIdentity(ProbableCauseTypeIdentity):
    """
    cpuCyclesLimitExceeded
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['CpucycleslimitexceededIdentity']['meta_info']


class Lossofsignalx733Identity(ProbableCauseTypeIdentity):
    """
    lossOfSignalX733
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['Lossofsignalx733Identity']['meta_info']


class RectifierfailureIdentity(ProbableCauseTypeIdentity):
    """
    rectifierFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RectifierfailureIdentity']['meta_info']


class StoragecapacityproblemIdentity(ProbableCauseTypeIdentity):
    """
    storageCapacityProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['StoragecapacityproblemIdentity']['meta_info']


class RetransmissionrateexcessiveIdentity(ProbableCauseTypeIdentity):
    """
    retransmissionRateExcessive
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['RetransmissionrateexcessiveIdentity']['meta_info']


class FarendreceiverfailureIdentity(ProbableCauseTypeIdentity):
    """
    farEndReceiverFailure
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['FarendreceiverfailureIdentity']['meta_info']


class ProcessorproblemIdentity(ProbableCauseTypeIdentity):
    """
    processorProblem
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ProcessorproblemIdentity']['meta_info']


class ExplosivegasIdentity(ProbableCauseTypeIdentity):
    """
    explosiveGas
    
    

    """

    _prefix = 'flt-types'
    _revision = '2016-09-26'

    def __init__(self):
        ProbableCauseTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm_types as meta
        return meta._meta_table['ExplosivegasIdentity']['meta_info']


