from django.test import TestCase
from apiapp.models import Question, Survey, Answer, Response, PointLocation, PolygonLocation, LineStringLocation
from django.contrib.auth.models import User
from datetime import date, timedelta
from apiapp import views


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

        # Create a new user
        user = User(username='testuser', password='testpass')
        user.save()

        # Create a new survey
        survey = Survey(name='Test Survey 1', description='This is used to test things',
                        publish_date=date.today(), expire_date=date.today() + timedelta(days=10), 
                        public_url='www.google.com', designer=user)
        survey.save()

        # Create a new (expired) survey
        survey = Survey(name='Test Survey 2', description='This is used to test some other things',
                        publish_date=date.today(), expire_date=date.today() - timedelta(days=10), 
                        public_url='www.bing.com', designer=user)
        survey.save()

        # Create a new question
        question = Question(text='Testing question', order=1, required=True,
                                question_type='text', choices='', survey=survey)
        question.save()

        # Create a new point location
        point_location = PointLocation(location='SRID=4326;POINT (0.0075149652548134 0.0322341867016535)', name='test location',
                                        question=question)
        point_location.save()

        pass

    def test_get_pointlocation_by_question(self):
        question = Question.objects.get(id=1)
        point_location = PointLocation.objects.get(question=question)
        location = point_location.location
        self.assertEqual(location, 'SRID=4326;POINT (0.0075149652548134 0.0322341867016535)')

    def test_get_non_expired_surveys(self):
        print('=================================')
        print(Survey.objects.all())
        available_surveys = views.SurveyViewSet.GetSurveyByAvailable()
        available_survey = available_surveys[0]
        print(available_surveys)
        print(available_survey)
        survey = Survey.objects.get(id=1)
        self.assertEqual(available_survey, survey)

