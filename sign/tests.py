from django.test import TestCase
from sign.models import Event, Guest
from django.utils import timezone
from django.contrib.auth.models import User


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


class IndexPageTest(TestCase):
    '''Test Index page'''

    def test_index_page_renders_index_template(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    """ Test login Action"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_author_email(self):
        """ Test add new user """
        user = User.objects.get(username="admin")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@mail.com")

    def test_login_action_username_password_null(self):
        """ User and Password is null """
        response = self.client.post(
            '/login_action/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password null", response.content)

    def test_login_action_username_password_error(self):
        """ Wrong User and Password """
        response = self.client.post(
            '/login_action/', {'username': 'abc', 'password': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error", response.content)

    def test_login_action_success(self):
        """ Login success """
        response = self.client.post(
            '/login_action/', data={'username': 'admin', 'password': 'admin123456'})
        self.assertEqual(response.status_code, 302)


class EventMangeTest(TestCase):
    """ EventMangeTest """

    def setUp(self):
        """Add new event"""
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name="xiaomi5", limit=2000, address='beijing',
                             status=1, start_time=timezone.now())
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # 预先登录

    def test_add_event_data(self):
        """ Test added event """
        event = Event.objects.get(name="xiaomi5")
        self.assertEqual(event.address, "beijing")

    def test_event_mange_success(self):
        """ Test event:xiaomi5 """
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_event_mange_search_success(self):
        """ Test event search """
        response = self.client.post('/search_name/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)


class GuestManageTest(TestCase):
    """ Guest management """

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000,
                             address='beijing', status=1, start_time=timezone.now())
        Guest.objects.create(realname="alen", phone="18611001100",
                             email='alen@mail.com', sign=0, event_id=1)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # Pre login

    def test_add_guest_data(self):
        """ Test add guest """
        guest = Guest.objects.get(realname="alen")
        self.assertEqual(guest.phone, "18611001100")
        self.assertEqual(guest.email, "alen@mail.com")
        self.assertFalse(guest.sign)

    def test_event_mange_success(self):
        """ Test Guest Info: alen """
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)

    def test_guest_mange_search_success(self):
        """ Test Guest search """
        response = self.client.post('/search_phone/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)


class SignIndexActionTest(TestCase):
    """ Event sign """

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000,
                             address='beijing', status=1, start_time=timezone.now())
        Event.objects.create(id=2, name="oneplus4", limit=2000,
                             address='shenzhen', status=1, start_time=timezone.now())
        Guest.objects.create(realname="alen", phone="18611001100",
                             email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone="18611001101",
                             email='una@mail.com', sign=1, event_id=2)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)

    def test_sign_index_action_phone_null(self):
        """ phone is null """
        response = self.client.post('/sign_index_action/1/', {"phone": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        """ phone or event id is null """
        response = self.client.post(
            '/sign_index_action/2/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_sign_index_action_user_sign_has(self):
        """ User is null """
        response = self.client.post(
            '/sign_index_action/2/', {"phone": "18611001101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_sign_index_action_sign_success(self):
        """ Sign succeed """
        response = self.client.post(
            '/sign_index_action/1/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)
