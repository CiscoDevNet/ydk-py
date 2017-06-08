""" ietf_alarm 

Alarm YANG Data Model for Network Topology and Services.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Alarms(object):
    """
    Serves as top\-level container for list of alarms.
    
    .. attribute:: alarm
    
    	List of active alarms
    	**type**\: list of    :py:class:`Alarm <ydk.models.ietf.ietf_alarm.Alarms.Alarm>`
    
    

    """

    _prefix = 'flt'
    _revision = '2016-09-26'

    def __init__(self):
        self.alarm = YList()
        self.alarm.parent = self
        self.alarm.name = 'alarm'


    class Alarm(object):
        """
        List of active alarms.
        
        .. attribute:: alarm_id  <key>
        
        	Unique alarm id for the alarm. In most cases this will be a combination of entity\-type, entity\-id, probable\-cause and severity
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: additional_text
        
        	This parameter, when present, allows a free form text description to be reported
        	**type**\:  str
        
        .. attribute:: alarm_time
        
        	Time at which the alarm was raised / reported
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        	**mandatory**\: True
        
        .. attribute:: correlated_notifications
        
        	This parameter contains a set of Notification identifiers of the correlated alarms
        	**type**\:  str
        
        .. attribute:: direction
        
        	Direction for which alarm is reported
        	**type**\:   :py:class:`DirectionEnum <ydk.models.ietf.ietf_alarm.Alarms.Alarm.DirectionEnum>`
        
        .. attribute:: entity_id
        
        	An identifier for the entity on which the alarm is raised. This entity can be in the device, domain controllers, element management systems, or northbound orchestrators
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: entity_type
        
        	Type of the entity on which the alarm is raised
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: event_type
        
        	This parameter categorizes the alarm
        	**type**\:   :py:class:`EventTypeIdentity <ydk.models.ietf.ietf_alarm_types.EventTypeIdentity>`
        
        	**mandatory**\: True
        
        .. attribute:: location
        
        	Location where the alarm is reported
        	**type**\:   :py:class:`LocationEnum <ydk.models.ietf.ietf_alarm.Alarms.Alarm.LocationEnum>`
        
        .. attribute:: notification_identifier
        
        	This parameter provides an identifier for the notification, which may be carried in the correlated notifications parameter of future notifications. Notification identifiers must be chosen to be unique across all notifications of a particular managed object throughout the time that correlation is significant
        	**type**\:  str
        
        .. attribute:: perceived_severity
        
        	This parameter indicates the perceived severity level of the alarm
        	**type**\:   :py:class:`PerceivedSeverityEnum <ydk.models.ietf.ietf_alarm.Alarms.Alarm.PerceivedSeverityEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: probable_cause
        
        	This parameter defines further qualification as to the probable cause of the alarm
        	**type**\:   :py:class:`ProbableCauseTypeIdentity <ydk.models.ietf.ietf_alarm_types.ProbableCauseTypeIdentity>`
        
        	**mandatory**\: True
        
        .. attribute:: service_affecting
        
        	This parameter indicates if the alarm impacts an active service. If the alarm is service affecting then the value is true. If the alarm does not affect the service then the value is false
        	**type**\:  bool
        
        .. attribute:: trend_indication
        
        	This parameter, when present, specifies the current severity trend of the managed entity
        	**type**\:   :py:class:`TrendIndicationEnum <ydk.models.ietf.ietf_alarm.Alarms.Alarm.TrendIndicationEnum>`
        
        

        """

        _prefix = 'flt'
        _revision = '2016-09-26'

        def __init__(self):
            self.parent = None
            self.alarm_id = None
            self.additional_text = None
            self.alarm_time = None
            self.correlated_notifications = None
            self.direction = None
            self.entity_id = None
            self.entity_type = None
            self.event_type = None
            self.location = None
            self.notification_identifier = None
            self.perceived_severity = None
            self.probable_cause = None
            self.service_affecting = None
            self.trend_indication = None

        class DirectionEnum(Enum):
            """
            DirectionEnum

            Direction for which alarm is reported.

            .. data:: NA = 0

            .. data:: Rx = 1

            .. data:: Tx = 2

            """

            NA = 0

            Rx = 1

            Tx = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_alarm as meta
                return meta._meta_table['Alarms.Alarm.DirectionEnum']


        class LocationEnum(Enum):
            """
            LocationEnum

            Location where the alarm is reported.

            .. data:: NA = 0

            .. data:: nearEnd = 1

            .. data:: farEnd = 2

            """

            NA = 0

            nearEnd = 1

            farEnd = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_alarm as meta
                return meta._meta_table['Alarms.Alarm.LocationEnum']


        class PerceivedSeverityEnum(Enum):
            """
            PerceivedSeverityEnum

            This parameter indicates the perceived severity

            level of the alarm.

            .. data:: Critical = 0

            .. data:: Major = 1

            .. data:: Minor = 2

            .. data:: Warning = 3

            .. data:: Cleared = 4

            .. data:: Indeterminate = 5

            """

            Critical = 0

            Major = 1

            Minor = 2

            Warning = 3

            Cleared = 4

            Indeterminate = 5


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_alarm as meta
                return meta._meta_table['Alarms.Alarm.PerceivedSeverityEnum']


        class TrendIndicationEnum(Enum):
            """
            TrendIndicationEnum

            This parameter, when present, specifies the current

            severity trend of the managed entity.

            .. data:: moreSevere = 0

            .. data:: noChange = 1

            .. data:: lessSevere = 2

            """

            moreSevere = 0

            noChange = 1

            lessSevere = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_alarm as meta
                return meta._meta_table['Alarms.Alarm.TrendIndicationEnum']


        @property
        def _common_path(self):
            if self.alarm_id is None:
                raise YPYModelError('Key property alarm_id is None')

            return '/ietf-alarm:alarms/ietf-alarm:alarm[ietf-alarm:alarm-id = ' + str(self.alarm_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.alarm_id is not None:
                return True

            if self.additional_text is not None:
                return True

            if self.alarm_time is not None:
                return True

            if self.correlated_notifications is not None:
                return True

            if self.direction is not None:
                return True

            if self.entity_id is not None:
                return True

            if self.entity_type is not None:
                return True

            if self.event_type is not None:
                return True

            if self.location is not None:
                return True

            if self.notification_identifier is not None:
                return True

            if self.perceived_severity is not None:
                return True

            if self.probable_cause is not None:
                return True

            if self.service_affecting is not None:
                return True

            if self.trend_indication is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_alarm as meta
            return meta._meta_table['Alarms.Alarm']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-alarm:alarms'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.alarm is not None:
            for child_ref in self.alarm:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_alarm as meta
        return meta._meta_table['Alarms']['meta_info']


