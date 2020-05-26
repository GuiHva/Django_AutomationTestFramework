from django.test import TestCase
from sign.models import Event,Guest
from django.utils import timezone

# Create your tests here.
class ModuleTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="Apple macbookpro event", status=True,
                            limit=2000,
                            address="hangzhou", 
                            start_time=timezone.now())
        Guest.objects.create(id=1, event_id=1, realname="Gui",
                            phone="12345678912",
                            email="123@123.com",
                            sign=False)
    
    def test_event_models(self):
        result = Event.objects.get(name="Apple macbookpro event")
        self.assertEqual(result.address, "hangzhou")
        self.assertTrue(result.status)
    
    def test_guest_models(self):
        result = Guest.objects.get(phone="12345678912")
        self.assertEqual(result.realname, "Gui")
        self.assertFalse(result.sign)

    def tearDown(self):
        pass