# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class NutritionOrder(domainresource.DomainResource):
    """ Diet, formula or nutritional supplement request.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    resource_type = "NutritionOrder"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allergyIntolerance = None
        """ List of the patient's food and nutrition-related allergies and
        intolerances.
        List of `FHIRReference` items referencing `['AllergyIntolerance']` (represented as `dict` in JSON). """

        self.dateTime = None
        """ Date and time the nutrition order was requested.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.encounter = None
        """ The encounter associated with this nutrition order.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.enteralFormula = None
        """ Enteral formula components.
        Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON). """

        self.excludeFoodModifier = None
        """ Order-specific modifier about the type of food that should not be
        given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.foodPreferenceModifier = None
        """ Order-specific modifier about the type of food that should be given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `str` items. """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['ActivityDefinition', 'PlanDefinition']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """

        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.oralDiet = None
        """ Oral diet components.
        Type `NutritionOrderOralDiet` (represented as `dict` in JSON). """

        self.orderer = None
        """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.patient = None
        """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.supplement = None
        """ Supplement components.
        List of `NutritionOrderSupplement` items (represented as `dict` in JSON). """

        super(NutritionOrder, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend(
            [
                (
                    "allergyIntolerance",
                    "allergyIntolerance",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "dateTime",
                    "dateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    True,
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
                    "enteralFormula",
                    "enteralFormula",
                    NutritionOrderEnteralFormula,
                    "NutritionOrderEnteralFormula",
                    False,
                    None,
                    False,
                ),
                (
                    "excludeFoodModifier",
                    "excludeFoodModifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "foodPreferenceModifier",
                    "foodPreferenceModifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
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
                ("instantiates", "instantiates", str, "uri", True, None, False),
                (
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
                ("intent", "intent", str, "code", False, None, True),
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
                    "oralDiet",
                    "oralDiet",
                    NutritionOrderOralDiet,
                    "NutritionOrderOralDiet",
                    False,
                    None,
                    False,
                ),
                (
                    "orderer",
                    "orderer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "supplement",
                    "supplement",
                    NutritionOrderSupplement,
                    "NutritionOrderSupplement",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """

    resource_type = "NutritionOrderEnteralFormula"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additiveProductName = None
        """ Product or brand name of the modular additive.
        Type `str`. """

        self.additiveType = None
        """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.administration = None
        """ Formula feeding instruction as structured data.
        List of `NutritionOrderEnteralFormulaAdministration` items (represented as `dict` in JSON). """

        self.administrationInstruction = None
        """ Formula feeding instructions expressed as text.
        Type `str`. """

        self.baseFormulaProductName = None
        """ Product or brand name of the enteral or infant formula.
        Type `str`. """

        self.baseFormulaType = None
        """ Type of enteral or infant formula.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.caloricDensity = None
        """ Amount of energy per specified volume that is required.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxVolumeToDeliver = None
        """ Upper limit on formula volume per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """

        self.routeofAdministration = None
        """ How the formula should enter the patient's gastrointestinal tract.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(NutritionOrderEnteralFormula, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend(
            [
                (
                    "additiveProductName",
                    "additiveProductName",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "additiveType",
                    "additiveType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "administration",
                    "administration",
                    NutritionOrderEnteralFormulaAdministration,
                    "NutritionOrderEnteralFormulaAdministration",
                    True,
                    None,
                    False,
                ),
                (
                    "administrationInstruction",
                    "administrationInstruction",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "baseFormulaProductName",
                    "baseFormulaProductName",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "baseFormulaType",
                    "baseFormulaType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "caloricDensity",
                    "caloricDensity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "maxVolumeToDeliver",
                    "maxVolumeToDeliver",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "routeofAdministration",
                    "routeofAdministration",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """

    resource_type = "NutritionOrderEnteralFormulaAdministration"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.quantity = None
        """ The volume of formula to provide.
        Type `Quantity` (represented as `dict` in JSON). """

        self.rateQuantity = None
        """ Speed with which the formula is provided per period of time.
        Type `Quantity` (represented as `dict` in JSON). """

        self.rateRatio = None
        """ Speed with which the formula is provided per period of time.
        Type `Ratio` (represented as `dict` in JSON). """

        self.schedule = None
        """ Scheduled frequency of enteral feeding.
        Type `Timing` (represented as `dict` in JSON). """

        super(NutritionOrderEnteralFormulaAdministration, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend(
            [
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "rateQuantity",
                    "rateQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "rate",
                    False,
                ),
                ("rateRatio", "rateRatio", ratio.Ratio, "Ratio", False, "rate", False),
                ("schedule", "schedule", timing.Timing, "Timing", False, None, False),
            ]
        )
        return js


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """

    resource_type = "NutritionOrderOralDiet"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.fluidConsistencyType = None
        """ The required consistency of fluids and liquids provided to the
        patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.instruction = None
        """ Instructions or additional information about the oral diet.
        Type `str`. """

        self.nutrient = None
        """ Required  nutrient modifications.
        List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON). """

        self.schedule = None
        """ Scheduled frequency of diet.
        List of `Timing` items (represented as `dict` in JSON). """

        self.texture = None
        """ Required  texture modifications.
        List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(NutritionOrderOralDiet, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend(
            [
                (
                    "fluidConsistencyType",
                    "fluidConsistencyType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("instruction", "instruction", str, "string", False, None, False),
                (
                    "nutrient",
                    "nutrient",
                    NutritionOrderOralDietNutrient,
                    "NutritionOrderOralDietNutrient",
                    True,
                    None,
                    False,
                ),
                ("schedule", "schedule", timing.Timing, "Timing", True, None, False),
                (
                    "texture",
                    "texture",
                    NutritionOrderOralDietTexture,
                    "NutritionOrderOralDietTexture",
                    True,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """

    resource_type = "NutritionOrderOralDietNutrient"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Quantity of the specified nutrient.
        Type `Quantity` (represented as `dict` in JSON). """

        self.modifier = None
        """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(NutritionOrderOralDietNutrient, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", quantity.Quantity, "Quantity", False, None, False),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """

    resource_type = "NutritionOrderOralDietTexture"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.foodType = None
        """ Concepts that are used to identify an entity that is ingested for
        nutritional purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.modifier = None
        """ Code to indicate how to alter the texture of the foods, e.g. pureed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(NutritionOrderOralDietTexture, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend(
            [
                (
                    "foodType",
                    "foodType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "modifier",
                    "modifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """

    resource_type = "NutritionOrderSupplement"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.instruction = None
        """ Instructions or additional information about the oral supplement.
        Type `str`. """

        self.productName = None
        """ Product or brand name of the nutritional supplement.
        Type `str`. """

        self.quantity = None
        """ Amount of the nutritional supplement.
        Type `Quantity` (represented as `dict` in JSON). """

        self.schedule = None
        """ Scheduled frequency of supplement.
        List of `Timing` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(NutritionOrderSupplement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend(
            [
                ("instruction", "instruction", str, "string", False, None, False),
                ("productName", "productName", str, "string", False, None, False),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("schedule", "schedule", timing.Timing, "Timing", True, None, False),
                (
                    "type",
                    "type",
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
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
