#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-17.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import binary
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class BinaryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Binary", js["resourceType"])
        return binary.Binary(js)
    
    def testBinary1(self):
        inst = self.instantiate_from("binary-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary1(inst)
        
        js = inst.as_json()
        self.assertEqual("Binary", js["resourceType"])
        inst2 = binary.Binary(js)
        self.implBinary1(inst2)
    
    def implBinary1(self, inst):
        self.assertEqual(force_bytes(inst.contentType), force_bytes("application/pdf"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))

