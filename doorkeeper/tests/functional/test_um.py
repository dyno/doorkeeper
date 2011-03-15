from doorkeeper.tests import *

class TestUmController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='um', action='index'))
        # Test response...
