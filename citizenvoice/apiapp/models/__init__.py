"""
Allows to import everything from survey.models without knowing the details.
"""

from .answer import Answer
from .question import Question
from .response import Response
from .survey import Survey
from .location import PointFeature, PolygonFeature, LineFeature, LocationCollection
from .mapview import MapView
from .dashboard_topic import DashboardTopic

__all__ = ["Answer", 
           "Response", 
           "Survey", 
           "Question", 
           "LocationCollection", 
           "PointFeature", 
           "PolygonFeature", 
           "LineFeature", 
           "MapView",
           "DashboardTopic"]
