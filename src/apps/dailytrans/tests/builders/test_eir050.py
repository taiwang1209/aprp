import datetime
from django.test import TestCase
from django.core.management import call_command
from apps.dailytrans.models import DailyTran
from apps.chickens.models import Chicken
from apps.dailytrans.builders.eir050 import Api


class BuilderTestCase(TestCase):

    def setUp(self):
        # load fixtures
        call_command('loaddata', 'configs.yaml', verbosity=0)
        call_command('loaddata', 'cog10.yaml', verbosity=0)

        self.start_date = datetime.date(year=2017, month=1, day=1)
        self.end_date = datetime.date(year=2017, month=1, day=1)

    def test_chicken(self):
        # test create
        obj = Chicken.objects.filter(code='黑羽土雞舍飼(南區)公').filter(track_item=True).first()

        api = Api(model=Chicken, config_code='COG10', type_id=None)

        response = api.request(start_date=self.start_date,
                               end_date=self.end_date)
        api.load(response)

        count_qs = DailyTran.objects.filter(date=self.start_date,
                                            product=obj)

        self.assertEquals(count_qs.count(), 1)

        # test update by load again
        api.load(response)

        self.assertEquals(count_qs.count(), 1)
