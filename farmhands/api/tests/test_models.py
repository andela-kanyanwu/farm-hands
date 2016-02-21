from django.test import TestCase
from api.models import Plan, Schedule, User
from datetime import datetime
from pytz import timezone


def save(modelDAO):
    """
    This function saves a model Data Access Object.

    :params: modelDAO
    :returns: modelDAO
    """
    modelDAO.save()
    return modelDAO


class PlanTestCase (TestCase):
    """This class is a test suite for the Plan model. """

    @classmethod
    def setUpClass(cls):
        plan = dict(
            name="Farm name", farm_size="S", weather="Fine",
            crop_type="Cash", budget="15000", duration="20")
        cls.planDAO = save(Plan(**plan))
        assert cls.planDAO.id is not None  # test can create plan

        super(PlanTestCase, cls).setUpClass()

    def test_01__can_read_plan(self):
        """Test that plans can be read. """
        queryset = Plan.objects.filter(id=self.planDAO.id)
        self.assertIsNotNone(queryset)

    def test_02__can_update_plan(self):
        """Test that plan can be updated. """
        queryset = Plan.objects.filter(id=self.planDAO.id)[0]
        old_name = queryset.name
        queryset.name = "Another farm name"
        queryset.save()
        self.assertNotEqual(queryset.name, old_name)

    def test_03__can_delete_plan(self):
        """Test that plan can be deleted. """
        queryset = Plan.objects.filter(id=self.planDAO.id)
        queryset[0].delete()
        queryset = Plan.objects.filter(id=self.planDAO.id)
        self.assertFalse(queryset)

    def tearDown(self):
        super(PlanTestCase, self).tearDown()


class ScheduleTestCase (TestCase):
    """This class is a test suite for the Schedule model. """

    tz = timezone('Africa/Lagos')

    @classmethod
    def _localize(cls, dt):
        """This method returns a localized datetime string. """
        return cls.tz.localize(dt)

    @classmethod
    def setUpClass(cls):
        plan = dict(
            name="Farm name", farm_size="S", weather="Fine",
            crop_type="Cash", budget="15000", duration="20")
        cls.planDAO = save(Plan(**plan))
        assert cls.planDAO.id is not None  # test can create plan

        schedule = dict(
                plan=cls.planDAO,
                start_time=cls._localize(datetime(2012, 3, 3, 1, 30)),
                end_time=cls._localize(datetime(2013, 3, 3, 1, 30)),
                cycle_type="DAILY",
                desc="Some description"
            )
        cls.scheduleDAO = save(Schedule(**schedule))
        assert cls.scheduleDAO.id is not None  # test can create schedule
        super(ScheduleTestCase, cls).setUpClass()

    def test_02__can_read_schedule(self):
        """Test that schedule can be read. """
        queryset = Schedule.objects.filter(id=self.scheduleDAO.id)
        self.assertNotEqual([], queryset)

    def test_03__can_update_schedule(self):
        """Test that schedule can be updated. """
        queryset = Schedule.objects.filter(id=self.scheduleDAO.id)[0]
        old_desc = queryset.desc
        queryset.desc = "Another long description"
        queryset.save()
        self.assertNotEqual(queryset.desc, old_desc)

    def test_04__can_delete_schedule(self):
        queryset = Schedule.objects.filter(id=self.scheduleDAO.id)[0]
        queryset.delete()
        queryset = Schedule.objects.filter(id=self.scheduleDAO.id)
        self.assertFalse(queryset)

    def tearDown(self):
        super(ScheduleTestCase, self).tearDown()


class UserTestCase (TestCase):
    """This class is a test suite for the User model. """

    @classmethod
    def setUpClass(cls):
        user = dict(
            username="testuser", email="testuser@domain.com",
            password="secret")
        cls.userDAO = save(User(**user))
        assert cls.userDAO.id is not None  # test can create user

        super(cls, UserTestCase).setUpClass()

    def test_01__can_read_user(self):
        """Test that user can be read. """
        queryset = User.objects.filter(id=self.userDAO.id)
        self.assertFalse([])

    def test_02__can_update_user(self):
        """Test that user can be updated. """
        queryset = User.objects.filter(id=self.userDAO.id)[0]
        old_username = queryset.username
        queryset.username = 'newtestuser'
        queryset.save()
        self.assertNotEqual(queryset.username, old_username)

    def test_03__can_delete_user(self):
        """Test that user can be deleted. """
        queryset = User.objects.filter(id=self.userDAO.id)[0]
        queryset.delete()
        queryset = User.objects.filter(id=self.userDAO.id)
        self.assertFalse(queryset)

    def tearDown(self):
        super(UserTestCase, self).tearDown()
