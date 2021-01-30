from unittest.test.test_result import __init__

from django.test import TestCase
from curriculum.models import *
import datetime


# Create your tests here.
class IdentityTestCase(TestCase):
    def setUp(self):
        # skill = Skill.objects.create(
        #     sector="Informatica",
        #     skill="Jenkins",
        #     level=9
        # )
        # summary = Summary.objects.create(
        #     summary="un texto largo para ver si la cosa fgunciona correctamente .............",
        #     skills=skill.id
        # )
        Identity.objects.create(
            dni="76649586Q",
            name="Daniel",
            last_name="Ramón Gallardo",
            birthdate = datetime.date.today(),
            email="danielramongallardo@gmail.com",
            # address="Carrer sobrerroca 5-7, 1/3",
            phone=601367201,
            modification_date=datetime.date.today(),
            creation_date=datetime.date.today(),
            motto="No tomo cafe programar es lo que me despierta"
        )

    def test_curriculum(self):
        """Basic curriculum is working correctly"""
        curriculum = Identity.objects.get(dni="76649586Q")
        self.assertEqual(curriculum, curriculum)
