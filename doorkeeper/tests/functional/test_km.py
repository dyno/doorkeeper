from doorkeeper.tests import *

class TestKmController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='km', action='index'))
        # Test response...
