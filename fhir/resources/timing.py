# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Timing
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import sys
if sys.version.startswith("2"):
    # Disclaimer: Timing is originally baseDefinition
    # from http://hl7.org/fhir/StructureDefinition/BackboneElement
    # But there is circular dependency problem in python2!
    # extension.Extension is used in BackboneElement.modifierExtension as value type.
    # and also timing.Timing is used as Extension.valueTiming value type.
    # As a result we are using ``BackboneElement`` as base class of Timing,
    # faced import error (because od circular dependency).
    from .element import Element as BaseTiming
else:
    from .backboneelement import BackboneElement as BaseTiming
from . import element


class Timing(BaseTiming):
    """ A timing schedule that specifies an event that may occur multiple times.

    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """

    resource_type = "Timing"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ BID | TID | QID | AM | PM | QD | QOD | +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.event = None
        """ When the event occurs.
        List of `FHIRDate` items (represented as `str` in JSON). """

        self.repeat = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """

        super(Timing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("event", "event", fhirdate.FHIRDate, "dateTime", True, None, False),
                ("repeat", "repeat", TimingRepeat, "TimingRepeat", False, None, False),
            ]
        )
        return js


class TimingRepeat(element.Element):
    """ When the event is to occur.

    A set of rules that describe when the event is scheduled.
    """

    resource_type = "TimingRepeat"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.boundsDuration = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Duration` (represented as `dict` in JSON). """

        self.boundsPeriod = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """

        self.boundsRange = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """

        self.count = None
        """ Number of times to repeat.
        Type `int`. """

        self.countMax = None
        """ Maximum number of times to repeat.
        Type `int`. """

        self.dayOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """

        self.duration = None
        """ How long when it happens.
        Type `float`. """

        self.durationMax = None
        """ How long when it happens (Max).
        Type `float`. """

        self.durationUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """

        self.frequency = None
        """ Event occurs frequency times per period.
        Type `int`. """

        self.frequencyMax = None
        """ Event occurs up to frequencyMax times per period.
        Type `int`. """

        self.offset = None
        """ Minutes from event (before or after).
        Type `int`. """

        self.period = None
        """ Event occurs frequency times per period.
        Type `float`. """

        self.periodMax = None
        """ Upper limit of period (3-4 hours).
        Type `float`. """

        self.periodUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """

        self.timeOfDay = None
        """ Time of day for action.
        List of `FHIRDate` items (represented as `str` in JSON). """

        self.when = None
        """ Code for time period of occurrence.
        List of `str` items. """

        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend(
            [
                (
                    "boundsDuration",
                    "boundsDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "bounds",
                    False,
                ),
                (
                    "boundsPeriod",
                    "boundsPeriod",
                    period.Period,
                    "Period",
                    False,
                    "bounds",
                    False,
                ),
                (
                    "boundsRange",
                    "boundsRange",
                    range.Range,
                    "Range",
                    False,
                    "bounds",
                    False,
                ),
                ("count", "count", int, "positiveInt", False, None, False),
                ("countMax", "countMax", int, "positiveInt", False, None, False),
                ("dayOfWeek", "dayOfWeek", str, "code", True, None, False),
                ("duration", "duration", float, "decimal", False, None, False),
                ("durationMax", "durationMax", float, "decimal", False, None, False),
                ("durationUnit", "durationUnit", str, "code", False, None, False),
                ("frequency", "frequency", int, "positiveInt", False, None, False),
                (
                    "frequencyMax",
                    "frequencyMax",
                    int,
                    "positiveInt",
                    False,
                    None,
                    False,
                ),
                ("offset", "offset", int, "unsignedInt", False, None, False),
                ("period", "period", float, "decimal", False, None, False),
                ("periodMax", "periodMax", float, "decimal", False, None, False),
                ("periodUnit", "periodUnit", str, "code", False, None, False),
                (
                    "timeOfDay",
                    "timeOfDay",
                    fhirdate.FHIRDate,
                    "time",
                    True,
                    None,
                    False,
                ),
                ("when", "when", str, "code", True, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
