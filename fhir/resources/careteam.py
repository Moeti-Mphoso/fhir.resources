# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CareTeam
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class CareTeam(domainresource.DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.

    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    resource_type = "CareTeam"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.category = None
        """ Type of team.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this team.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ Organization responsible for the care team.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.name = None
        """ Name of the team, such as crisis assessment team.
        Type `str`. """

        self.note = None
        """ Comments made about the CareTeam.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.participant = None
        """ Members of the team.
        List of `CareTeamParticipant` items (represented as `dict` in JSON). """

        self.period = None
        """ Time period team covers.
        Type `Period` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why the care team exists.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why the care team exists.
        List of `FHIRReference` items referencing `['Condition']` (represented as `dict` in JSON). """

        self.status = None
        """ proposed | active | suspended | inactive | entered-in-error.
        Type `str`. """

        self.subject = None
        """ Who care team is for.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the care team (that applies to all members).
        List of `ContactPoint` items (represented as `dict` in JSON). """

        super(CareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend(
            [
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
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
                (
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "participant",
                    "participant",
                    CareTeamParticipant,
                    "CareTeamParticipant",
                    True,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "reasonCode",
                    "reasonCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
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


class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.

    Identifies all people and organizations who are expected to be involved in
    the care team.
    """

    resource_type = "CareTeamParticipant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'RelatedPerson', 'Patient', 'Organization', 'CareTeam']` (represented as `dict` in JSON). """

        self.onBehalfOf = None
        """ Organization of the practitioner.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ Time period of participant.
        Type `Period` (represented as `dict` in JSON). """

        self.role = None
        """ Type of involvement.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(CareTeamParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend(
            [
                (
                    "member",
                    "member",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "onBehalfOf",
                    "onBehalfOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
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
