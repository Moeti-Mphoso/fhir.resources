# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Group
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class Group(domainresource.DomainResource):
    """ Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """

    resource_type = "Group"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this group's record is in active use.
        Type `bool`. """

        self.actual = None
        """ Descriptive or actual.
        Type `bool`. """

        self.characteristic = None
        """ Trait of group members.
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """

        self.code = None
        """ Kind of Group members.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique id.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.member = None
        """ Who or what is in group.
        List of `GroupMember` items (represented as `dict` in JSON). """

        self.name = None
        """ Label for Group.
        Type `str`. """

        self.quantity = None
        """ Number of members.
        Type `int`. """

        self.type = None
        """ person | animal | practitioner | device | medication | substance.
        Type `str`. """

        super(Group, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                ("actual", "actual", bool, "boolean", False, None, True),
                (
                    "characteristic",
                    "characteristic",
                    GroupCharacteristic,
                    "GroupCharacteristic",
                    True,
                    None,
                    False,
                ),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("member", "member", GroupMember, "GroupMember", True, None, False),
                ("name", "name", str, "string", False, None, False),
                ("quantity", "quantity", int, "unsignedInt", False, None, False),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class GroupCharacteristic(backboneelement.BackboneElement):
    """ Trait of group members.

    Identifies the traits shared by members of the group.
    """

    resource_type = "GroupCharacteristic"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Kind of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.exclude = None
        """ Group includes or excludes.
        Type `bool`. """

        self.period = None
        """ Period over which characteristic is tested.
        Type `Period` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ Value held by characteristic.
        Type `bool`. """

        self.valueCodeableConcept = None
        """ Value held by characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Value held by characteristic.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Value held by characteristic.
        Type `Range` (represented as `dict` in JSON). """

        super(GroupCharacteristic, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("exclude", "exclude", bool, "boolean", False, None, True),
                ("period", "period", period.Period, "Period", False, None, False),
                ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
                (
                    "valueCodeableConcept",
                    "valueCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueRange",
                    "valueRange",
                    range.Range,
                    "Range",
                    False,
                    "value",
                    True,
                ),
            ]
        )
        return js


class GroupMember(backboneelement.BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """

    resource_type = "GroupMember"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.entity = None
        """ Reference to the group member.
        Type `FHIRReference` referencing `['Patient'], ['Practitioner'], ['Device'], ['Medication'], ['Substance']` (represented as `dict` in JSON). """

        self.inactive = None
        """ If member is no longer in group.
        Type `bool`. """

        self.period = None
        """ Period member belonged to the group.
        Type `Period` (represented as `dict` in JSON). """

        super(GroupMember, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend(
            [
                (
                    "entity",
                    "entity",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("inactive", "inactive", bool, "boolean", False, None, False),
                ("period", "period", period.Period, "Period", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
