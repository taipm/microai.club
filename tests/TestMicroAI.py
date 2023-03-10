from configparser import ConfigParser
import unittest
from ai.MicroAI import MicroAI

config = ConfigParser()
config.read('/Users/taipm/Documents/GitHub/microai.club/config.ini')


class TestMicroAI(unittest.TestCase):
    def setUp(self):
        self.micro_ai = MicroAI(api_key=config.get('openai', 'api_key'))
    
    def test_generate_answer(self):
        question = "What is the capital of France?"
        result = self.micro_ai.generate_answer(question)
        self.assertIn('answer', result)
        self.assertIsInstance(result['answer'], str)
    
    def tearDown(self):
        del self.micro_ai

if __name__ == '__main__':
    unittest.main()
