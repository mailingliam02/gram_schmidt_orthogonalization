# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:47:09 2021

@author: Percy
"""
import unittest 
from src.graham_schmidtt_basic import vector, tensor, main
class TestDataset(unittest.TestCase):
    def setUp(self):
        path = ".\\test\\fake_data.csv"
        save_path = ".\\test\\clean_fake_data.csv"
        self.dataset_cleaner = Dataset(path, save_path)
    
    def tearDown(self):
        #https://careerkarma.com/blog/python-check-if-file-exists/
        file_exist = os.path.isfile(".\\test\\clean_fake_data.csv")
        if file_exist:
            os.remove(".\\test\\clean_fake_data.csv")
        
    def test_remove_no_outcome_success(self):
        test_case = {"age": ["10", "15", "20"], 
                     "sex": ["male", "male", "female"], 
                     "latitude": [1.1, 2.2, 3.3], 
                     "longitude": [1.3, 2.6, 1.3],
                     "date_onset_symptoms": ["11.01.20", "24.03.20", "25.02.20"], 
                     "date_admission_hospital": ["11.01.20", "24.03.20", "25.02.20"], 
                     "symptoms": ["cough, respiratory distress", "headache", "fever"], 
                     "chronic_disease": ["diabetes", "COPD", "hypertension"],        
                     "date_death_or_discharge": ["11.01.20", "24.03.20", "25.02.20"], 
                     "outcome": ["death",np.nan,"discharged"], 
                     "admin1": ["True","False","False"]}
        preclean_data = pd.DataFrame(data = test_case, columns = ["age", "sex", "latitude", 
                              "longitude", "date_onset_symptoms", 
                              "date_admission_hospital", "symptoms", "chronic_disease", 
                              "date_death_or_discharge", "outcome", "admin1"])
        actual = self.dataset_cleaner._Dataset__remove_no_outcome(preclean_data).reset_index(drop = True)
        test_case_clean = {"age": ["10", "20"], 
                     "sex": ["male", "female"], 
                     "latitude": [1.1, 3.3], 
                     "longitude": [1.3, 1.3],
                     "date_onset_symptoms": ["11.01.20", "25.02.20"], 
                     "date_admission_hospital": ["11.01.20", "25.02.20"], 
                     "symptoms": ["cough, respiratory distress","fever"], 
                     "chronic_disease": ["diabetes", "hypertension"],        
                     "date_death_or_discharge": ["11.01.20","25.02.20"], 
                     "outcome": ["death","discharged"], 
                     "admin1": ["True","False"]}
        preclean_data1 = pd.DataFrame(data = test_case_clean, columns = ["age", "sex", "latitude", 
                              "longitude", "date_onset_symptoms", 
                              "date_admission_hospital", "symptoms", "chronic_disease", 
                              "date_death_or_discharge", "outcome", "admin1"])
        expected = preclean_data1.reset_index(drop = True)
        #Should raise error
        pd.testing.assert_frame_equal(actual, expected)
        #If above does not raise error, means they are equivalent. Hence Assert True
        self.assertEqual(1,1)