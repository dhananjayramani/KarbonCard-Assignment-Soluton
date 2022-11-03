#Q2
import json
import re

def correct_num_bedrooms(input_json):
    property_data = []
    property_data = json.loads(input_json)
    output_list = []
    for x in property_data:
        num_beds=0
        description = str(x['description'])
        num_beds_original = int(x['num_bedrooms'])
        desc_upper = description.upper()
        patterns_to_be_ignored = ['YOGA STUDIO','ART STUDIO','DANCE STUDIO','YOGA 1-BEDROOM','DANCE 1-BEDROOM','ART 1-BEDROOM' ]
        desc_upper_corrected = desc_upper
        for p in patterns_to_be_ignored:
            desc_upper_corrected = re.sub(p,'',desc_upper_corrected)
        bedroom_match = re.search('1-BEDROOM',desc_upper_corrected)
        studio_match = re.search('STUDIO',desc_upper_corrected)
        if len(bedroom_match) > 0 :
            num_beds = 1
        elif len(studio_match) > 0:
            num_beds=0
        else:
            num_beds = num_beds_original
        
        output_list.append(num_beds)
    return output_list

class test_output(unittest.TestCase):
    def test_output(self):
        input_data = json.dumps([{"id":"1", "agent":"Ralph", "unit":"#3", "description":"This luxurious studio apartment is in the heart of downtown.", "num_bedrooms":"1"},
                                {"id":"2", "agent":"Kelemen", "unit":"#36", "description":"We have a 1-bedroom available on the third floor.", "num_bedrooms":"1"},
                                {"id":"3", "agent":"Ton", "unit":"#12", "description":"Beautiful 1-bedroom apartment with nearby yoga studio.", "num_bedrooms":"1"},
                                {"id":"4", "agent":"Fishel", "unit":"#13", "description":"Beautiful studio with a nearby art studio.", "num_bedrooms":"1"}])
        actual_op = correct_num_bedrooms(input_data)
        expected_op = [0,1,1,0]
        self.assertEqual(actual_op,expected_op)

