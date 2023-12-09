# from is_anagram_v1 import is_anagram
# from is_anagram_v2 import is_anagram
# from is_anagram_v3 import is_anagram
# from is_anagram_v4 import is_anagram
# from is_anagram_v5 import is_anagram
from is_anagram_v6 import is_anagram

import  unittest

class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertEqual(is_anagram("lol", "bol"), False)
        self.assertEqual(is_anagram("bol", "lob"), True)
        self.assertEqual(is_anagram('sur', "rus"), True)

if __name__ == "__main__":
    unittest.main()

    
    SELECT patient_id 
FROM home_patientvisit
GROUP BY patient_id;