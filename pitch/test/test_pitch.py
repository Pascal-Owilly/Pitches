import unittest
from pitch.models import Pitch
from . import db

def setUp(self):
    self.new_pitch = Pitch(1,'test pass','','',15,12)
    
def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.id,1)
    self.assertEquals(self.new_pitch.pitch,'test pass')
  
    self.assertEquals(self.new_pitch.like,15)
    self.assertEquals(self.new_pitch.dislike,12)
    
def test_save_pitch(self):
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)
    
def test_get_pitch_by_id(self):

    self.new_pitch.save_pitch()
    pitch = Pitch.get_pitch(1)
    self.assertTrue(len(pitch) == 1)
    

if __name__=='__main__':
    unittest.main()