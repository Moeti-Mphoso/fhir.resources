# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Medication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Medication(domainresource.DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """

    resource_type = "Medication"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Amount of drug in package.
        Type `Ratio` (represented as `dict` in JSON). """

        self.batch = None
        """ Details about packaged medications.
        Type `MedicationBatch` (represented as `dict` in JSON). """

        self.code = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.form = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier for this medication.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationIngredient` items (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """

        super(Medication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", ratio.Ratio, "Ratio", False, None, False),
                (
                    "batch",
                    "batch",
                    MedicationBatch,
                    "MedicationBatch",
                    False,
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
                    "form",
                    "form",
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
                (
                    "ingredient",
                    "ingredient",
                    MedicationIngredient,
                    "MedicationIngredient",
                    True,
                    None,
                    False,
                ),
                (
                    "manufacturer",
                    "manufacturer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
            ]
        )
        return js


class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """

    resource_type = "MedicationBatch"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.expirationDate = None
        """ When batch will expire.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lotNumber = None
        """ Identifier assigned to batch.
        Type `str`. """

        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend(
            [
                (
                    "expirationDate",
                    "expirationDate",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                ("lotNumber", "lotNumber", str, "string", False, None, False),
            ]
        )
        return js


class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """

    resource_type = "MedicationIngredient"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.isActive = None
        """ Active ingredient indicator.
        Type `bool`. """

        self.itemCodeableConcept = None
        """ The actual ingredient or content.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.itemReference = None
        """ The actual ingredient or content.
        Type `FHIRReference` referencing `['Substance', 'Medication']` (represented as `dict` in JSON). """

        self.strength = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """

        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend(
            [
                ("isActive", "isActive", bool, "boolean", False, None, False),
                (
                    "itemCodeableConcept",
                    "itemCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "item",
                    True,
                ),
                (
                    "itemReference",
                    "itemReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "item",
                    True,
                ),
                ("strength", "strength", ratio.Ratio, "Ratio", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
