


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'EventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('EventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProbableCauseTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ProbableCauseTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'probable-cause-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TimeoutexpiredIdentity' : {
        'meta_info' : _MetaInfoClass('TimeoutexpiredIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'timeoutExpired',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExternalpointfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ExternalpointfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'externalPointFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SynchronizationsourcemismatchIdentity' : {
        'meta_info' : _MetaInfoClass('SynchronizationsourcemismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'synchronizationSourceMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'NeidentifierduplicationIdentity' : {
        'meta_info' : _MetaInfoClass('NeidentifierduplicationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'nEIdentifierDuplication',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Timingproblemx733Identity' : {
        'meta_info' : _MetaInfoClass('Timingproblemx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'timingProblemX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Receiverfailurex733Identity' : {
        'meta_info' : _MetaInfoClass('Receiverfailurex733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'receiverFailureX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExternalifdeviceproblemIdentity' : {
        'meta_info' : _MetaInfoClass('ExternalifdeviceproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'externalIFDeviceProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PowersupplyfailureIdentity' : {
        'meta_info' : _MetaInfoClass('PowersupplyfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'powerSupplyFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'GeneratorfailureIdentity' : {
        'meta_info' : _MetaInfoClass('GeneratorfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'generatorFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DemodulationfailureIdentity' : {
        'meta_info' : _MetaInfoClass('DemodulationfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'demodulationFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CommunicationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('CommunicationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'communication-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TimingproblemIdentity' : {
        'meta_info' : _MetaInfoClass('TimingproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'timingProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TransmissionerrorIdentity' : {
        'meta_info' : _MetaInfoClass('TransmissionerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'transmissionError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'UnderlayingresourceunavailableIdentity' : {
        'meta_info' : _MetaInfoClass('UnderlayingresourceunavailableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'underlayingResourceUnavailable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofrealtimelIdentity' : {
        'meta_info' : _MetaInfoClass('LossofrealtimelIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfRealTimel',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'MemorymismatchIdentity' : {
        'meta_info' : _MetaInfoClass('MemorymismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'memoryMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ModulationfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ModulationfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'modulationFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BandwidthreducedIdentity' : {
        'meta_info' : _MetaInfoClass('BandwidthreducedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'bandwidthReduced',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ResponsetimeexecessiveIdentity' : {
        'meta_info' : _MetaInfoClass('ResponsetimeexecessiveIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'responseTimeExecessive',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RemotealarminterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('RemotealarminterfaceIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'remoteAlarmInterface',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EnginefailureIdentity' : {
        'meta_info' : _MetaInfoClass('EnginefailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'engineFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AuthenticationfailureIdentity' : {
        'meta_info' : _MetaInfoClass('AuthenticationfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'authenticationFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReplaceableunitmissingIdentity' : {
        'meta_info' : _MetaInfoClass('ReplaceableunitmissingIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'replaceableUnitMissing',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LanerrorIdentity' : {
        'meta_info' : _MetaInfoClass('LanerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lanError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CabletamperIdentity' : {
        'meta_info' : _MetaInfoClass('CabletamperIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'cableTamper',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Transmitfailurex733Identity' : {
        'meta_info' : _MetaInfoClass('Transmitfailurex733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'transmitFailureX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'MultiplexerproblemIdentity' : {
        'meta_info' : _MetaInfoClass('MultiplexerproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'multiplexerProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PumpfailureIdentity' : {
        'meta_info' : _MetaInfoClass('PumpfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'pumpFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RoutingfailureIdentity' : {
        'meta_info' : _MetaInfoClass('RoutingfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'routingFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Lossofframex733Identity' : {
        'meta_info' : _MetaInfoClass('Lossofframex733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfFrameX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'VentilationssystemfailureIdentity' : {
        'meta_info' : _MetaInfoClass('VentilationssystemfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'ventilationsSystemFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OutofmemoryIdentity' : {
        'meta_info' : _MetaInfoClass('OutofmemoryIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'outOfMemory',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Outofmemoryx733Identity' : {
        'meta_info' : _MetaInfoClass('Outofmemoryx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'outOfMemoryX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TransmitfailureIdentity' : {
        'meta_info' : _MetaInfoClass('TransmitfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'transmitFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Congestionx733Identity' : {
        'meta_info' : _MetaInfoClass('Congestionx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'congestionX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RectifierlowfvoltageIdentity' : {
        'meta_info' : _MetaInfoClass('RectifierlowfvoltageIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'rectifierLowFVoltage',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DatasetormodemerrorIdentity' : {
        'meta_info' : _MetaInfoClass('DatasetormodemerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'dataSetOrModemError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SignalqualityevaluationfailureIdentity' : {
        'meta_info' : _MetaInfoClass('SignalqualityevaluationfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'signalQualityEvaluationFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EnvironmentalEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('EnvironmentalEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'environmental-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowwaterIdentity' : {
        'meta_info' : _MetaInfoClass('LowwaterIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowWater',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Enclosuredooropenx733Identity' : {
        'meta_info' : _MetaInfoClass('Enclosuredooropenx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'enclosureDoorOpenX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowcablepressureIdentity' : {
        'meta_info' : _MetaInfoClass('LowcablepressureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowCablePressure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FramingerrorIdentity' : {
        'meta_info' : _MetaInfoClass('FramingerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'framingError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BatterychargingfailureIdentity' : {
        'meta_info' : _MetaInfoClass('BatterychargingfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'batteryChargingFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AntennafailureIdentity' : {
        'meta_info' : _MetaInfoClass('AntennafailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'antennaFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowfuelIdentity' : {
        'meta_info' : _MetaInfoClass('LowfuelIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowFuel',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowhumidityIdentity' : {
        'meta_info' : _MetaInfoClass('LowhumidityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowHumidity',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ResourceatornearingcapacityIdentity' : {
        'meta_info' : _MetaInfoClass('ResourceatornearingcapacityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'resourceAtOrNearingCapacity',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Storagecapacityproblemx733Identity' : {
        'meta_info' : _MetaInfoClass('Storagecapacityproblemx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'storageCapacityProblemX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'HighwindIdentity' : {
        'meta_info' : _MetaInfoClass('HighwindIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'highWind',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DuplicateinformationIdentity' : {
        'meta_info' : _MetaInfoClass('DuplicateinformationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'duplicateInformation',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowbatterythresholdIdentity' : {
        'meta_info' : _MetaInfoClass('LowbatterythresholdIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowBatteryThreshold',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExcessiveresponsetimeIdentity' : {
        'meta_info' : _MetaInfoClass('ExcessiveresponsetimeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'excessiveResponseTime',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'HeatingventcoolingsystemproblemIdentity' : {
        'meta_info' : _MetaInfoClass('HeatingventcoolingsystemproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'heatingVentCoolingSystemProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RectifierhighvoltageIdentity' : {
        'meta_info' : _MetaInfoClass('RectifierhighvoltageIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'rectifierHighVoltage',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BatterydischargingIdentity' : {
        'meta_info' : _MetaInfoClass('BatterydischargingIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'batteryDischarging',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ToxicleakdetectedIdentity' : {
        'meta_info' : _MetaInfoClass('ToxicleakdetectedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'toxicLeakDetected',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OtherEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OtherEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'other-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReducedloggingcapabilityIdentity' : {
        'meta_info' : _MetaInfoClass('ReducedloggingcapabilityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'reducedLoggingCapability',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ConfigurationorcustomisationerrorIdentity' : {
        'meta_info' : _MetaInfoClass('ConfigurationorcustomisationerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'configurationOrCustomisationError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DenialofserviceIdentity' : {
        'meta_info' : _MetaInfoClass('DenialofserviceIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'denialOfService',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DiskfailureIdentity' : {
        'meta_info' : _MetaInfoClass('DiskfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'diskFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LinecardproblemIdentity' : {
        'meta_info' : _MetaInfoClass('LinecardproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lineCardProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'HumidityunacceptableIdentity' : {
        'meta_info' : _MetaInfoClass('HumidityunacceptableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'humidityUnacceptable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CommercialpowerfailureIdentity' : {
        'meta_info' : _MetaInfoClass('CommercialpowerfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'commercialPowerFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Versionmismatchx733Identity' : {
        'meta_info' : _MetaInfoClass('Versionmismatchx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'versionMismatchX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OutofcpucyclesIdentity' : {
        'meta_info' : _MetaInfoClass('OutofcpucyclesIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'outOfCPUCycles',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'UnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('UnavailableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'unavailable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'NonrepudiationfailureIdentity' : {
        'meta_info' : _MetaInfoClass('NonrepudiationfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'nonRepudiationFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Softwareerrorx733Identity' : {
        'meta_info' : _MetaInfoClass('Softwareerrorx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'softwareErrorX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BatteryfailureIdentity' : {
        'meta_info' : _MetaInfoClass('BatteryfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'batteryFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FusefailureIdentity' : {
        'meta_info' : _MetaInfoClass('FusefailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fuseFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Pumpfailurex733Identity' : {
        'meta_info' : _MetaInfoClass('Pumpfailurex733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'pumpFailureX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DegradedsignalIdentity' : {
        'meta_info' : _MetaInfoClass('DegradedsignalIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'degradedSignal',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProcessingEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ProcessingEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'processing-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AirconditioningfailureIdentity' : {
        'meta_info' : _MetaInfoClass('AirconditioningfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'airConditioningFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReceiverfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ReceiverfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'receiverFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'UnexpectedinformationIdentity' : {
        'meta_info' : _MetaInfoClass('UnexpectedinformationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'unexpectedInformation',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExcessivevibrationIdentity' : {
        'meta_info' : _MetaInfoClass('ExcessivevibrationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'excessiveVibration',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PowerproblemsIdentity' : {
        'meta_info' : _MetaInfoClass('PowerproblemsIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'powerProblems',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Localnodetransmissionerrorx733Identity' : {
        'meta_info' : _MetaInfoClass('Localnodetransmissionerrorx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'localNodeTransmissionErrorX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'IodeviceerrorIdentity' : {
        'meta_info' : _MetaInfoClass('IodeviceerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'iODeviceError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReceivefailureIdentity' : {
        'meta_info' : _MetaInfoClass('ReceivefailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'receiveFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InputdeviceerrorIdentity' : {
        'meta_info' : _MetaInfoClass('InputdeviceerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'inputDeviceError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BackplanefailureIdentity' : {
        'meta_info' : _MetaInfoClass('BackplanefailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'backplaneFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofsynchronisationIdentity' : {
        'meta_info' : _MetaInfoClass('LossofsynchronisationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfSynchronisation',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CongestionIdentity' : {
        'meta_info' : _MetaInfoClass('CongestionIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'congestion',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TerminalproblemIdentity' : {
        'meta_info' : _MetaInfoClass('TerminalproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'terminalProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofredundancyIdentity' : {
        'meta_info' : _MetaInfoClass('LossofredundancyIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfRedundancy',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'HightemperatureIdentity' : {
        'meta_info' : _MetaInfoClass('HightemperatureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'highTemperature',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'IntrusiondetectionIdentity' : {
        'meta_info' : _MetaInfoClass('IntrusiondetectionIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'intrusionDetection',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TrunkcardproblemIdentity' : {
        'meta_info' : _MetaInfoClass('TrunkcardproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'trunkCardProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AirdryerfailureIdentity' : {
        'meta_info' : _MetaInfoClass('AirdryerfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'airDryerFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PowerproblemIdentity' : {
        'meta_info' : _MetaInfoClass('PowerproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'powerProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EquipmentmalfunctionIdentity' : {
        'meta_info' : _MetaInfoClass('EquipmentmalfunctionIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'equipmentMalfunction',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ApplicationsubsystemfailtureIdentity' : {
        'meta_info' : _MetaInfoClass('ApplicationsubsystemfailtureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'applicationSubsystemFailture',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FrequencyhoppingfailureIdentity' : {
        'meta_info' : _MetaInfoClass('FrequencyhoppingfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'frequencyHoppingFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ConfigurationorcustomizationerrorIdentity' : {
        'meta_info' : _MetaInfoClass('ConfigurationorcustomizationerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'configurationOrCustomizationError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EquipmentidentifierduplicationIdentity' : {
        'meta_info' : _MetaInfoClass('EquipmentidentifierduplicationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'equipmentIdentifierDuplication',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SmokeIdentity' : {
        'meta_info' : _MetaInfoClass('SmokeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'smoke',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Framingerrorx733Identity' : {
        'meta_info' : _MetaInfoClass('Framingerrorx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'framingErrorX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InputoutputdeviceerrorIdentity' : {
        'meta_info' : _MetaInfoClass('InputoutputdeviceerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'inputOutputDeviceError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Remotenodetransmissionerrorx733Identity' : {
        'meta_info' : _MetaInfoClass('Remotenodetransmissionerrorx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'remoteNodeTransmissionErrorX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PressureunacceptableIdentity' : {
        'meta_info' : _MetaInfoClass('PressureunacceptableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'pressureUnacceptable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CommunicationssubsystemfailureIdentity' : {
        'meta_info' : _MetaInfoClass('CommunicationssubsystemfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'communicationsSubsystemFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Degradedsignalx733Identity' : {
        'meta_info' : _MetaInfoClass('Degradedsignalx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'degradedSignalX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProtectingresourcefailureIdentity' : {
        'meta_info' : _MetaInfoClass('ProtectingresourcefailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'protectingResourceFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'MaterialsupplyexhaustedIdentity' : {
        'meta_info' : _MetaInfoClass('MaterialsupplyexhaustedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'materialSupplyExhausted',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExcessiveerrorrateIdentity' : {
        'meta_info' : _MetaInfoClass('ExcessiveerrorrateIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'excessiveErrorRate',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReplaceableunitproblemIdentity' : {
        'meta_info' : _MetaInfoClass('ReplaceableunitproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'replaceableUnitProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SoftwareerrorIdentity' : {
        'meta_info' : _MetaInfoClass('SoftwareerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'softwareError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PhysicalViolationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PhysicalViolationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'physical-violation-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProtectionmechanismfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ProtectionmechanismfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'protectionMechanismFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InformationoutofsequenceIdentity' : {
        'meta_info' : _MetaInfoClass('InformationoutofsequenceIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'informationOutOfSequence',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CoruptdataIdentity' : {
        'meta_info' : _MetaInfoClass('CoruptdataIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'coruptData',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LeakdetectedIdentity' : {
        'meta_info' : _MetaInfoClass('LeakdetectedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'leakDetected',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ConnectionestablishmenterrorIdentity' : {
        'meta_info' : _MetaInfoClass('ConnectionestablishmenterrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'connectionEstablishmentError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InformationmodificationdetectedIdentity' : {
        'meta_info' : _MetaInfoClass('InformationmodificationdetectedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'informationModificationDetected',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SfwrenvironmentproblemIdentity' : {
        'meta_info' : _MetaInfoClass('SfwrenvironmentproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'sfwrEnvironmentProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TransmitterfailureIdentity' : {
        'meta_info' : _MetaInfoClass('TransmitterfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'transmitterFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InformationmissingIdentity' : {
        'meta_info' : _MetaInfoClass('InformationmissingIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'informationMissing',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SystemresourcesoverloadIdentity' : {
        'meta_info' : _MetaInfoClass('SystemresourcesoverloadIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'systemResourcesOverload',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BreachofconfidentialityIdentity' : {
        'meta_info' : _MetaInfoClass('BreachofconfidentialityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'breachOfConfidentiality',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FiredetectorfailureIdentity' : {
        'meta_info' : _MetaInfoClass('FiredetectorfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fireDetectorFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EnclosuredooropenIdentity' : {
        'meta_info' : _MetaInfoClass('EnclosuredooropenIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'enclosureDoorOpen',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AisIdentity' : {
        'meta_info' : _MetaInfoClass('AisIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'aIS',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Multiplexerproblemx733Identity' : {
        'meta_info' : _MetaInfoClass('Multiplexerproblemx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'multiplexerProblemX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'QueuesizeexceededIdentity' : {
        'meta_info' : _MetaInfoClass('QueuesizeexceededIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'queueSizeExceeded',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LowtemperatueIdentity' : {
        'meta_info' : _MetaInfoClass('LowtemperatueIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lowTemperatue',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CoolingfanfailureIdentity' : {
        'meta_info' : _MetaInfoClass('CoolingfanfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'coolingFanFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ThresholdcrossedIdentity' : {
        'meta_info' : _MetaInfoClass('ThresholdcrossedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'thresholdCrossed',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofframeIdentity' : {
        'meta_info' : _MetaInfoClass('LossofframeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfFrame',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Bandwidthreducedx733Identity' : {
        'meta_info' : _MetaInfoClass('Bandwidthreducedx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'bandwidthReducedX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OutofhoursactivityIdentity' : {
        'meta_info' : _MetaInfoClass('OutofhoursactivityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'outOfHoursActivity',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FireIdentity' : {
        'meta_info' : _MetaInfoClass('FireIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fire',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProceduralerrorIdentity' : {
        'meta_info' : _MetaInfoClass('ProceduralerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'proceduralError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'QosEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('QosEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'QoS-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TimeDomainViolationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TimeDomainViolationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'time-domain-violation-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PerformancedegradedIdentity' : {
        'meta_info' : _MetaInfoClass('PerformancedegradedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'performanceDegraded',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DatabaseinconsistencyIdentity' : {
        'meta_info' : _MetaInfoClass('DatabaseinconsistencyIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'databaseInconsistency',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CoolingsystemfailureIdentity' : {
        'meta_info' : _MetaInfoClass('CoolingsystemfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'coolingSystemFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SignallabelmismatchIdentity' : {
        'meta_info' : _MetaInfoClass('SignallabelmismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'signalLabelMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExcessiveretransmissionrateIdentity' : {
        'meta_info' : _MetaInfoClass('ExcessiveretransmissionrateIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'excessiveRetransmissionRate',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Receivefailurex733Identity' : {
        'meta_info' : _MetaInfoClass('Receivefailurex733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'receiveFailureX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExcessiveberIdentity' : {
        'meta_info' : _MetaInfoClass('ExcessiveberIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'excessiveBER',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ToxicgasIdentity' : {
        'meta_info' : _MetaInfoClass('ToxicgasIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'toxicGas',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PathtracemismatchIdentity' : {
        'meta_info' : _MetaInfoClass('PathtracemismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'pathTraceMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DtedceinterfaceerrorIdentity' : {
        'meta_info' : _MetaInfoClass('DtedceinterfaceerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'dteDceInterfaceError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'UnderlyingresourceunavailableIdentity' : {
        'meta_info' : _MetaInfoClass('UnderlyingresourceunavailableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'underlyingResourceUnavailable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'IcebuildupIdentity' : {
        'meta_info' : _MetaInfoClass('IcebuildupIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'iceBuildUp',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FiredetectedIdentity' : {
        'meta_info' : _MetaInfoClass('FiredetectedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fireDetected',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'IntegrityViolationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IntegrityViolationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'integrity-violation-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LocalnodetransmissionerrorIdentity' : {
        'meta_info' : _MetaInfoClass('LocalnodetransmissionerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'localNodeTransmissionError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'EquipmentEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('EquipmentEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'equipment-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ApplicationsubsystemfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ApplicationsubsystemfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'applicationSubsystemFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OperationViolationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OperationViolationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'operation-violation-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SecurityServiceOrMechanismViolationEventTypeIdentity' : {
        'meta_info' : _MetaInfoClass('SecurityServiceOrMechanismViolationEventTypeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'security-service-or-mechanism-violation-event-type',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProtectionpathfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ProtectionpathfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'protectionPathFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofsignalIdentity' : {
        'meta_info' : _MetaInfoClass('LossofsignalIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfSignal',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RealtimeclockfailureIdentity' : {
        'meta_info' : _MetaInfoClass('RealtimeclockfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'realTimeClockFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TemperatureunacceptableIdentity' : {
        'meta_info' : _MetaInfoClass('TemperatureunacceptableIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'temperatureUnacceptable',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SoftwareprogramerrorIdentity' : {
        'meta_info' : _MetaInfoClass('SoftwareprogramerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'softwareProgramError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProcessorproblemsIdentity' : {
        'meta_info' : _MetaInfoClass('ProcessorproblemsIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'processorProblems',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CommunicationsprotocolerrorIdentity' : {
        'meta_info' : _MetaInfoClass('CommunicationsprotocolerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'communicationsProtocolError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FileerrorIdentity' : {
        'meta_info' : _MetaInfoClass('FileerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fileError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DelayedinformationIdentity' : {
        'meta_info' : _MetaInfoClass('DelayedinformationIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'delayedInformation',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CallsetupfailureIdentity' : {
        'meta_info' : _MetaInfoClass('CallsetupfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'callSetUpFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Fileerrorx733Identity' : {
        'meta_info' : _MetaInfoClass('Fileerrorx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'fileErrorX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'PayloadtypemismatchIdentity' : {
        'meta_info' : _MetaInfoClass('PayloadtypemismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'payloadTypeMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExternalequipmentfailureIdentity' : {
        'meta_info' : _MetaInfoClass('ExternalequipmentfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'externalEquipmentFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'DatasetproblemIdentity' : {
        'meta_info' : _MetaInfoClass('DatasetproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'dataSetProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RemotenodetransmissionerrorIdentity' : {
        'meta_info' : _MetaInfoClass('RemotenodetransmissionerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'remoteNodeTransmissionError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SoftwareprogramabnormallyterminatedIdentity' : {
        'meta_info' : _MetaInfoClass('SoftwareprogramabnormallyterminatedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'softwareProgramAbnormallyTerminated',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FloodIdentity' : {
        'meta_info' : _MetaInfoClass('FloodIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'flood',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OtherIdentity' : {
        'meta_info' : _MetaInfoClass('OtherIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'other',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'KeyexpiredIdentity' : {
        'meta_info' : _MetaInfoClass('KeyexpiredIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'keyExpired',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CorruptdataIdentity' : {
        'meta_info' : _MetaInfoClass('CorruptdataIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'corruptData',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OuputdeviceerrorIdentity' : {
        'meta_info' : _MetaInfoClass('OuputdeviceerrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'ouputDeviceError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'VersionmismatchIdentity' : {
        'meta_info' : _MetaInfoClass('VersionmismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'versionMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'SfwrdownloadfailureIdentity' : {
        'meta_info' : _MetaInfoClass('SfwrdownloadfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'sfwrDownloadFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TransmiterfailureIdentity' : {
        'meta_info' : _MetaInfoClass('TransmiterfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'transmiterFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'HighhumidityIdentity' : {
        'meta_info' : _MetaInfoClass('HighhumidityIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'highHumidity',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofmultiframeIdentity' : {
        'meta_info' : _MetaInfoClass('LossofmultiframeIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfMultiFrame',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'LossofpointerIdentity' : {
        'meta_info' : _MetaInfoClass('LossofpointerIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfPointer',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ReplaceableunittypemismatchIdentity' : {
        'meta_info' : _MetaInfoClass('ReplaceableunittypemismatchIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'replaceableUnitTypeMismatch',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CallestablishmenterrorIdentity' : {
        'meta_info' : _MetaInfoClass('CallestablishmenterrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'callEstablishmentError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'AdaptererrorIdentity' : {
        'meta_info' : _MetaInfoClass('AdaptererrorIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'adapterError',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'TranceiverfailureIdentity' : {
        'meta_info' : _MetaInfoClass('TranceiverfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'tranceiverFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'BroadcastchannelfailureIdentity' : {
        'meta_info' : _MetaInfoClass('BroadcastchannelfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'broadcastChannelFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'UnauthorizedaccessattemptIdentity' : {
        'meta_info' : _MetaInfoClass('UnauthorizedaccessattemptIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'unauthorizedAccessAttempt',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'InvalidmessagereceivedIdentity' : {
        'meta_info' : _MetaInfoClass('InvalidmessagereceivedIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'invalidMessageReceived',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'OutofserviceIdentity' : {
        'meta_info' : _MetaInfoClass('OutofserviceIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'outOfService',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'CpucycleslimitexceededIdentity' : {
        'meta_info' : _MetaInfoClass('CpucycleslimitexceededIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'cpuCyclesLimitExceeded',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'Lossofsignalx733Identity' : {
        'meta_info' : _MetaInfoClass('Lossofsignalx733Identity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'lossOfSignalX733',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RectifierfailureIdentity' : {
        'meta_info' : _MetaInfoClass('RectifierfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'rectifierFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'StoragecapacityproblemIdentity' : {
        'meta_info' : _MetaInfoClass('StoragecapacityproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'storageCapacityProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'RetransmissionrateexcessiveIdentity' : {
        'meta_info' : _MetaInfoClass('RetransmissionrateexcessiveIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'retransmissionRateExcessive',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'FarendreceiverfailureIdentity' : {
        'meta_info' : _MetaInfoClass('FarendreceiverfailureIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'farEndReceiverFailure',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ProcessorproblemIdentity' : {
        'meta_info' : _MetaInfoClass('ProcessorproblemIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'processorProblem',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
    'ExplosivegasIdentity' : {
        'meta_info' : _MetaInfoClass('ExplosivegasIdentity',
            False, 
            [
            ],
            'ietf-alarm-types',
            'explosiveGas',
            _yang_ns._namespaces['ietf-alarm-types'],
        'ydk.models.ietf.ietf_alarm_types'
        ),
    },
}
