# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Population
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement


class Population(backboneelement.BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.

    A populatioof people with some set of grouping criteria.
    """

    resource_type = "Population"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.ageCodeableConcept = None
        """ The age of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.ageRange = None
        """ The age of the specific population.
        Type `Range` (represented as `dict` in JSON). """

        self.gender = None
        """ The gender of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.physiologicalCondition = None
        """ The existing physiological conditions of the specific population to
        which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.race = None
        """ Race of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Population, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Population, self).elementProperties()
        js.extend(
            [
                (
                    "ageCodeableConcept",
                    "ageCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "age",
                    False,
                ),
                ("ageRange", "ageRange", range.Range, "Range", False, "age", False),
                (
                    "gender",
                    "gender",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "physiologicalCondition",
                    "physiologicalCondition",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "race",
                    "race",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
