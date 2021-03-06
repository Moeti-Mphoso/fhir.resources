# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Person
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class Person(domainresource.DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type = "Person"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ This person's record is in active use.
        Type `bool`. """

        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """

        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(Person, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                ("address", "address", address.Address, "Address", True, None, False),
                (
                    "birthDate",
                    "birthDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                ("gender", "gender", str, "code", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("link", "link", PersonLink, "PersonLink", True, None, False),
                (
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("name", "name", humanname.HumanName, "HumanName", True, None, False),
                (
                    "photo",
                    "photo",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    None,
                    False,
                ),
                (
                    "telecom",
                    "telecom",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    resource_type = "PersonLink"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """

        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `['Patient'], ['Practitioner'], ['RelatedPerson'], ['Person']` (represented as `dict` in JSON). """

        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend(
            [
                ("assurance", "assurance", str, "code", False, None, False),
                (
                    "target",
                    "target",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + ".address"]
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + ".humanname"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
