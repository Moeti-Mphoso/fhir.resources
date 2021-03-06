# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import nutritionorder
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class NutritionOrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("NutritionOrder", js["resourceType"])
        return nutritionorder.NutritionOrder(js)

    def testNutritionOrder1(self):
        inst = self.instantiate_from("nutritionorder-example-diabeticsupplement.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder1(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder1(inst2)

    def implNutritionOrder1(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("kosher"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("diabeticsupplement"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.supplement[0].productName), force_bytes("Glucerna")
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].quantity.unit), force_bytes("8 oz bottle")
        )
        self.assertEqual(inst.supplement[0].quantity.value, 1)
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10T15:00:00Z").date,
        )
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.as_json(),
            "2015-02-10T15:00:00Z",
        )
        self.assertEqual(inst.supplement[0].schedule[0].repeat.frequency, 1)
        self.assertEqual(inst.supplement[0].schedule[0].repeat.period, 24)
        self.assertEqual(
            force_bytes(inst.supplement[0].schedule[0].repeat.periodUnit),
            force_bytes("h"),
        )
        self.assertEqual(inst.supplement[0].schedule[1].repeat.duration, 1)
        self.assertEqual(
            force_bytes(inst.supplement[0].schedule[1].repeat.durationUnit),
            force_bytes("h"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].schedule[1].repeat.when[0]),
            force_bytes("HS"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].code),
            force_bytes("443051000124104"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].display),
            force_bytes("Adult diabetes specialty formula"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].code), force_bytes("1010")
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].display),
            force_bytes("Adult diabetic formula"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].system),
            force_bytes("http://goodhealthhospital.org/supplement-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.text),
            force_bytes("Adult diabetic formula"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder2(self):
        inst = self.instantiate_from("nutritionorder-example-enteralbolus.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder2(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder2(inst2)

    def implNutritionOrder2(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveProductName),
            force_bytes("Acme Lipid Additive"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].code),
            force_bytes("lipid"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].display),
            force_bytes("Lipid"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].system),
            force_bytes("http://hl7.org/fhir/entformula-additive"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administrationInstruction),
            force_bytes("240 mls every 4hrs "),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.code),
            force_bytes("mL"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.unit),
            force_bytes("milliliters"),
        )
        self.assertEqual(inst.enteralFormula.administration[0].quantity.value, 240)
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17T16:00:00Z").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17T16:00:00Z",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.frequency, 1
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.period, 4
        )
        self.assertEqual(
            force_bytes(
                inst.enteralFormula.administration[0].schedule.repeat.periodUnit
            ),
            force_bytes("h"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaProductName),
            force_bytes("Acme High Protein Formula"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].code),
            force_bytes("659311000124118"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].display),
            force_bytes("Adult high protein formula"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].system),
            force_bytes("http://usextension/snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.code), force_bytes("cal/mL")
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.unit),
            force_bytes("calories per milliliter"),
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.value, 1.5)
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.code),
            force_bytes("mL/d"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.unit),
            force_bytes("milliliter/day"),
        )
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.value, 1440)
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].code),
            force_bytes("GT"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].display),
            force_bytes("Instillation, gastrostomy tube"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RouteOfAdministration"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("dairy-free"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("enteralbolus"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.acme.org/nutritionorders"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder3(self):
        inst = self.instantiate_from("nutritionorder-example-fiberrestricteddiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder3(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder3(inst2)

    def implNutritionOrder3(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("dairy-free"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("fiberrestricteddiet"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.code), force_bytes("g")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.unit), force_bytes("grams")
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 50)
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].code),
            force_bytes("256674009"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].display),
            force_bytes("Fat"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.oralDiet.schedule[0].repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code), force_bytes("15108003")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Restricted fiber diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1000")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("Fiber restricted"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text),
            force_bytes("Fiber restricted diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].code), force_bytes("16208003")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].display),
            force_bytes("Low fat diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].code), force_bytes("1100")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].display), force_bytes("Low Fat")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].text), force_bytes("Low fat diet")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder4(self):
        inst = self.instantiate_from("nutritionorder-example-texture-modified.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder4(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder4(inst2)

    def implNutritionOrder4(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(force_bytes(inst.id), force_bytes("texturemodified"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.oralDiet.schedule[0].repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].foodType.coding[0].code),
            force_bytes("28647000"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].foodType.coding[0].display),
            force_bytes("Meat"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].foodType.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].foodType.text),
            force_bytes("Regular, Chopped Meat"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].code),
            force_bytes("228049004"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].display),
            force_bytes("Chopped food"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.text),
            force_bytes("Regular, Chopped Meat"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code),
            force_bytes("435801000124108"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Texture modified diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1010")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("Texture modified diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text),
            force_bytes("Texture modified diet"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder5(self):
        inst = self.instantiate_from("nutritionorder-example-pureeddiet-simple.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder5(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder5(inst2)

    def implNutritionOrder5(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(force_bytes(inst.id), force_bytes("pureeddiet-simple"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].code),
            force_bytes("439021000124105"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].display),
            force_bytes("Dietary liquid consistency - nectar thick liquid"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].text),
            force_bytes("Nectar thick liquids"),
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.oralDiet.schedule[0].repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].code),
            force_bytes("228055009"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].display),
            force_bytes("Liquidized food"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.text), force_bytes("Pureed")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code), force_bytes("226211001")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Pureed diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1010")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("Pureed diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text), force_bytes("Pureed diet")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(
            force_bytes(inst.supplement[0].instruction),
            force_bytes("Ensure Pudding at breakfast, lunch, supper"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].productName),
            force_bytes("Ensure Pudding 4 oz container"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].code),
            force_bytes("442971000124100"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].display),
            force_bytes("Adult high energy formula"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].code), force_bytes("1040")
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].display),
            force_bytes("Adult high energy pudding"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.coding[1].system),
            force_bytes("http://goodhealthhospital.org/supplement-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.supplement[0].type.text),
            force_bytes("Adult high energy pudding"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder6(self):
        inst = self.instantiate_from("nutritionorder-example-infantenteral.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder6(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder6(inst2)

    def implNutritionOrder6(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveProductName),
            force_bytes("Acme High Carbohydrate Additive"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].code),
            force_bytes("carbohydrate"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].display),
            force_bytes("Carbohydrate"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.additiveType.coding[0].system),
            force_bytes("http://hl7.org/fhir/entformula-additive"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administrationInstruction),
            force_bytes(
                "Add high calorie high carbohydrate additive to increase cal/oz from 24 cal/oz to 27 cal/oz."
            ),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.code),
            force_bytes("[foz_us]"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].quantity.unit),
            force_bytes("ounces"),
        )
        self.assertEqual(inst.enteralFormula.administration[0].quantity.value, 4)
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.frequency, 1
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.period, 3
        )
        self.assertEqual(
            force_bytes(
                inst.enteralFormula.administration[0].schedule.repeat.periodUnit
            ),
            force_bytes("h"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaProductName),
            force_bytes("Acme Infant Formula + Iron"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].code),
            force_bytes("412414007"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].display),
            force_bytes("infant formula + iron"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.code),
            force_bytes("cal/[foz_us]"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.unit),
            force_bytes("calories per ounce"),
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.value, 20)
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.code),
            force_bytes("[foz_us]"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.unit),
            force_bytes("ounces"),
        )
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.value, 32)
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].code),
            force_bytes("PO"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].display),
            force_bytes("Swallow, oral"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RouteOfAdministration"),
        )
        self.assertTrue(
            inst.enteralFormula.routeofAdministration.coding[0].userSelected
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("infantenteral"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.acme.org/nutritionorders"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder7(self):
        inst = self.instantiate_from("nutritionorder-example-enteralcontinuous.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder7(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder7(inst2)

    def implNutritionOrder7(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.enteralFormula.administrationInstruction),
            force_bytes(
                "Hold feedings from 7 pm to 7 am. Add MCT oil to increase calories from 1.0 cal/mL to 1.5 cal/mL"
            ),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].rateQuantity.code),
            force_bytes("mL/h"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[0].rateQuantity.unit),
            force_bytes("ml/hr"),
        )
        self.assertEqual(inst.enteralFormula.administration[0].rateQuantity.value, 60)
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17T07:00:00Z").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17T07:00:00Z",
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[1].rateQuantity.code),
            force_bytes("mL/h"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[1].rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[1].rateQuantity.unit),
            force_bytes("ml/hr"),
        )
        self.assertEqual(inst.enteralFormula.administration[1].rateQuantity.value, 80)
        self.assertEqual(
            inst.enteralFormula.administration[
                1
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17T11:00:00Z").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                1
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17T11:00:00Z",
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[2].rateQuantity.code),
            force_bytes("mL/h"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[2].rateQuantity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.administration[2].rateQuantity.unit),
            force_bytes("ml/hr"),
        )
        self.assertEqual(inst.enteralFormula.administration[2].rateQuantity.value, 100)
        self.assertEqual(
            inst.enteralFormula.administration[
                2
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17T15:00:00Z").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                2
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17T15:00:00Z",
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaProductName),
            force_bytes(" Acme Diabetes Formula"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].code),
            force_bytes("6547210000124112"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].display),
            force_bytes("Diabetic specialty enteral formula"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.baseFormulaType.coding[0].system),
            force_bytes("http://snomed/sct"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.code), force_bytes("cal/mL")
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.caloricDensity.unit),
            force_bytes("calories per milliliter"),
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.value, 1)
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.code),
            force_bytes("mL/d"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.maxVolumeToDeliver.unit),
            force_bytes("milliliter/day"),
        )
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.value, 880)
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].code),
            force_bytes("NGT"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].display),
            force_bytes("Instillation, nasogastric tube"),
        )
        self.assertEqual(
            force_bytes(inst.enteralFormula.routeofAdministration.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RouteOfAdministration"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("enteralcontinuous"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://www.acme.org/nutritionorders"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder8(self):
        inst = self.instantiate_from("nutritionorder-example-cardiacdiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder8(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder8(inst2)

    def implNutritionOrder8(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("dairy-free"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("cardiacdiet"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            force_bytes(inst.oralDiet.instruction),
            force_bytes("Starting on 2/10 breakfast, maximum 400 ml fluids per meal"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.code), force_bytes("g")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.unit), force_bytes("grams")
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 2)
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].code),
            force_bytes("39972003"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].display),
            force_bytes("Sodium"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].amount.code), force_bytes("mL")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].amount.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].amount.unit),
            force_bytes("milliliter"),
        )
        self.assertEqual(inst.oralDiet.nutrient[1].amount.value, 1500)
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].modifier.coding[0].code),
            force_bytes("33463005"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].modifier.coding[0].display),
            force_bytes("Fluid"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[1].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code), force_bytes("386619000")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Low sodium diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1040")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("Low Sodium Diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text), force_bytes("Low sodium diet")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].code), force_bytes("226208002")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].display),
            force_bytes("Fluid restricted diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].code), force_bytes("1040")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].display),
            force_bytes("Fluid restricted diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[1].text),
            force_bytes("Fluid restricted diet"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder9(self):
        inst = self.instantiate_from("nutritionorder-example-pureeddiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder9(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder9(inst2)

    def implNutritionOrder9(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("dairy-free"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("pureeddiet"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].code),
            force_bytes("439021000124105"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].display),
            force_bytes("Dietary liquid consistency - nectar thick liquid"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.fluidConsistencyType[0].text),
            force_bytes("Nectar thick liquids"),
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.oralDiet.schedule[0].repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].code),
            force_bytes("228055009"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].display),
            force_bytes("Liquidized food"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.texture[0].modifier.text), force_bytes("Pureed")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code), force_bytes("226211001")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Pureed diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1010")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("Pureed diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text), force_bytes("Pureed diet")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testNutritionOrder10(self):
        inst = self.instantiate_from("nutritionorder-example-diabeticdiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder10(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder10(inst2)

    def implNutritionOrder10(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].code),
            force_bytes("227493005"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].display),
            force_bytes("Cashew Nut"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.excludeFoodModifier[0].coding[0].version),
            force_bytes("20140730"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].code),
            force_bytes("dairy-free"),
        )
        self.assertEqual(
            force_bytes(inst.foodPreferenceModifier[0].coding[0].system),
            force_bytes("http://hl7.org/fhir/diet"),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("diabeticdiet"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://goodhealthhospital.org/nutrition-requests"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123"))
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.code), force_bytes("g")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].amount.unit), force_bytes("grams")
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 75)
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].code),
            force_bytes("2331003"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].display),
            force_bytes("Carbohydrate"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.nutrient[0].modifier.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(
            force_bytes(inst.oralDiet.schedule[0].repeat.periodUnit), force_bytes("d")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].code), force_bytes("160670007")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].display),
            force_bytes("Diabetic diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].code), force_bytes("1030")
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].display),
            force_bytes("DD - Diabetic diet"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].coding[1].system),
            force_bytes("http://goodhealthhospital.org/diet-type-codes"),
        )
        self.assertEqual(
            force_bytes(inst.oralDiet.type[0].text), force_bytes("DD - Diabetic diet")
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
