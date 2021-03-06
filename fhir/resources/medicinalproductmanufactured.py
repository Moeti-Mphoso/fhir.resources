# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class MedicinalProductManufactured(domainresource.DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """

    resource_type = "MedicinalProductManufactured"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.ingredient = None
        """ Ingredient.
        List of `FHIRReference` items referencing `['MedicinalProductIngredient']` (represented as `dict` in JSON). """

        self.manufacturedDoseForm = None
        """ Dose form as manufactured and before any transformation into the
        pharmaceutical product.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of the item (Note that this should be named
        "manufacturer" but it currently causes technical issues).
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """

        self.quantity = None
        """ The quantity or "count number" of the manufactured item.
        Type `Quantity` (represented as `dict` in JSON). """

        self.unitOfPresentation = None
        """ The “real world” units in which the quantity of the manufactured
        item is described.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductManufactured, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend(
            [
                (
                    "ingredient",
                    "ingredient",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "manufacturedDoseForm",
                    "manufacturedDoseForm",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "manufacturer",
                    "manufacturer",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "otherCharacteristics",
                    "otherCharacteristics",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "physicalCharacteristics",
                    "physicalCharacteristics",
                    prodcharacteristic.ProdCharacteristic,
                    "ProdCharacteristic",
                    False,
                    None,
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    True,
                ),
                (
                    "unitOfPresentation",
                    "unitOfPresentation",
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + ".prodcharacteristic"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
