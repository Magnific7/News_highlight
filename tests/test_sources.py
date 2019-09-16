import unittest
from app.models import Sources

class TestSource(unittest.TestCase):
	'''
	Test Case to test the behaviour of the Source Model
	Args:
		unittest.TestCase - helps in creating Test Cases
	'''
	def setUp(self):
		'''
		Inbuilt function that runs before each test is executed
		'''
		self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','general')

	def test_isSouceInstance(self):
		'''
		Function to test if the object created in the setup is indeed a Source Object
		'''
		self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
	unittest.main(verbosity=2)