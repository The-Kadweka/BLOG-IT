import unittest
from app.models import User,Blog
class UserModelTest(unittest.TestCase):
   def setUp(self):
       self.new_user = User(password = 'banana')
   def test_password_setter(self):
       self.assertTrue(self.new_user.pass_secure is not None)
def test_no_access_password(self):
           with self.assertRaises(AttributeError):
               self.new_user.password
def test_password_verification(self):
   self.assertTrue(self.new_user.verify_password('banana'))
class TestBlog(unittest.TestCase):
   '''
   Test class that defines test cases for the contact class behaviours.
   Args:
       unittest.TestCase: TestCase class that helps in creating test cases
   '''
   def setUp(self):
       '''
       Set up method to run before each test cases.
       '''
       self.new_blog = Blog("1","be yourself","2","10")
        # create blog object
   def test_init(self):
       '''
       test_init test case to test if the object is initialized properly
       '''
       self.assertEqual(self.new_blog.id,"1")
       self.assertEqual(self.new_blog.content,"be yourself")
       self.assertEqual(self.new_blog.category_id,"2")
       self.assertEqual(self.new_blog.user_id,"10")
   def test_save_blog(self):
       '''
       test_save_contact test case to test if the contact object is saved into
        the contact list
       '''
       self.new_blog.save_blog() # saving the new contact
       self.assertEqual(len(Blog.blog_list),1)
if __name__ == '__main__':
   unittest.main()