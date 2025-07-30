import unittest
import assignment2_student as student_assignment
import csv

marks = 0
passed = []

def read_data(path, file_encoding='utf-8'):
    with open(path, 'r', encoding=file_encoding) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

class Tester(unittest.TestCase):

    def test_check_list_bounds(self):

        original = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15']
        ]

        data = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15']
        ]

        self.assertListEqual(original, data)
        self.assertFalse(student_assignment.check_list_bounds(data, 0, 0))
        self.assertFalse(student_assignment.check_list_bounds(data, 0, 4))
        self.assertFalse(student_assignment.check_list_bounds(data, 2, 0))
        self.assertFalse(student_assignment.check_list_bounds(data, 2, 4))
        self.assertFalse(student_assignment.check_list_bounds(data, 0, -1))
        self.assertFalse(student_assignment.check_list_bounds(data, 0, 5))
        self.assertFalse(student_assignment.check_list_bounds(data, 3, 0))
        self.assertFalse(student_assignment.check_list_bounds(data, 2, 5))
        self.assertTrue(student_assignment.check_list_bounds(data, 3, 5))

        data = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9'],
            ['11', '12', '13', '14', '15']
        ]

        self.assertFalse(student_assignment.check_list_bounds(data, 3, 5))

        data = [
            ['1', '2', '3', '4'],
            ['6', '7', '8', '9'],
            ['11', '12', '13', '14']
        ]

        self.assertFalse(student_assignment.check_list_bounds(data, 3, 5))
        self.assertTrue(student_assignment.check_list_bounds(data, 3, 4))

        data = [
            ['1', '2', '3',],
            ['6', '7', '8', '9'],
            ['11', '12', '13']
        ]

        self.assertFalse(student_assignment.check_list_bounds(data, 3, 3))
        self.assertFalse(student_assignment.check_list_bounds(data, 3, 4))
        

        global marks, passed
        passed += ["check_list_bounds"]
        marks += 12.5


    def test_convert_string_to_list(self):
        input = "1, 2, 3, 4, 5"
        expected_result = ['1', '2', '3', '4', '5']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = "1,2,3, 4, 5"
        expected_result = ['1', '2', '3', '4', '5']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = "1,2,3,4, 5"
        expected_result = ['1', '2', '3', '4', '5']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = "1,2,3,4,5"
        expected_result = ['1', '2', '3', '4', '5']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = "1,  2,     3, 4, 5"
        expected_result = ['1', ' 2', '    3', '4', '5']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = "this, will, become,  a, list,of,    things"
        expected_result = ['this', 'will', 'become', ' a', 'list', 'of', '   things']
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        input = ""
        expected_result = []
        actual_result = student_assignment.convert_string_to_list(input)
        self.assertListEqual(expected_result, actual_result)

        global marks, passed
        passed += ["convert_string_to_list"]
        marks += 12.5


    def test_replace_values_transposed(self):
        # TODO Finish me
        data = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15']
        ]

        new_values = ['a', 'b', 'c']

        expected_result = [
            ['1', '2', '3', 'a', '5'],
            ['6', '7', '8', 'b', '10'],
            ['11', '12', '13', 'c', '15']
        ]

        student_assignment.replace_values_transposed(data, new_values, 3)

        self.assertEqual(len(expected_result), len(data))
        for i in range(len(expected_result)):
            self.assertListEqual(expected_result[i], data[i])

        data = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
            ['19', '20', '21', '22', '23', '24', '25', '26', '27'],
            ['28', '29', '30', '31', '32', '33', '34', '35', '36'],
            ['37', '38', '39', '40', '41', '42', '43', '44', '45'],
            ['46', '47', '48', '49', '50', '51', '52', '53', '54'],
            ['55', '56', '57', '58', '59', '60', '61', '62', '63'],
            ['64', '65', '66', '67', '68', '69', '70', '71', '72'],
            ['73', '74', '75', '76', '77', '78', '79', '80', '81']
        ]

        new_values = ['this', 'is', 'a', 'test', 'for', 'the', 'replace', 'values', 'function']

        expected_result = [
            ['1', '2', '3', 'this', '5', '6', '7', '8', '9'],
            ['10', '11', '12', 'is', '14', '15', '16', '17', '18'],
            ['19', '20', '21', 'a', '23', '24', '25', '26', '27'],
            ['28', '29', '30', 'test', '32', '33', '34', '35', '36'],
            ['37', '38', '39', 'for', '41', '42', '43', '44', '45'],
            ['46', '47', '48', 'the', '50', '51', '52', '53', '54'],
            ['55', '56', '57', 'replace', '59', '60', '61', '62', '63'],
            ['64', '65', '66', 'values', '68', '69', '70', '71', '72'],
            ['73', '74', '75', 'function', '77', '78', '79', '80', '81']
        ]

        student_assignment.replace_values_transposed(data, new_values, 3)

        self.assertEqual(len(expected_result), len(data))
        for i in range(len(expected_result)):
            self.assertListEqual(expected_result[i], data[i])


        data = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
            ['19', '20', '21', '22', '23', '24', '25', '26', '27'],
            ['28', '29', '30', '31', '32', '33', '34', '35', '36'],
            ['37', '38', '39', '40', '41', '42', '43', '44', '45'],
            ['46', '47', '48', '49', '50', '51', '52', '53', '54'],
            ['55', '56', '57', '58', '59', '60', '61', '62', '63'],
            ['64', '65', '66', '67', '68', '69', '70', '71', '72'],
            ['73', '74', '75', '76', '77', '78', '79', '80', '81']
        ]

        new_values = ['this', 'is', 'a', 'test', 'for', 'the', 'replace', 'values', 'function']

        expected_result = [
            ['1', '2', '3', '4', '5', '6', 'this', '8', '9'],
            ['10', '11', '12', '13', '14', '15', 'is', '17', '18'],
            ['19', '20', '21', '22', '23', '24', 'a', '26', '27'],
            ['28', '29', '30', '31', '32', '33', 'test', '35', '36'],
            ['37', '38', '39', '40', '41', '42', 'for', '44', '45'],
            ['46', '47', '48', '49', '50', '51', 'the', '53', '54'],
            ['55', '56', '57', '58', '59', '60', 'replace', '62', '63'],
            ['64', '65', '66', '67', '68', '69', 'values', '71', '72'],
            ['73', '74', '75', '76', '77', '78', 'function', '80', '81']

        ]

        student_assignment.replace_values_transposed(data, new_values, 6)

        self.assertEqual(len(expected_result), len(data))
        for i in range(len(expected_result)):
            self.assertListEqual(expected_result[i], data[i])

        global marks, passed
        passed += ["replace_values_transposed"]
        marks += 12.5


    def test_remove_from_end(self):

        original = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15']
        ]

        data = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15']
        ]

        expected_result = [
            ['1', '2', '3'],
            ['6', '7', '8'],
            ['11', '12', '13']
        ]

        actual_result = student_assignment.remove_from_end(data, 2)

        self.assertListEqual(original, data) # Check data has not been modified
        for i in range(len(expected_result)):
            self.assertListEqual(expected_result[i], actual_result[i])


        original = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15'],
            ['16', '17', '18', '19', '20'],
            ['21', '22', '23', '24', '25'],
            ['26', '27', '28', '29', '30'],
            ['31', '32', '33', '34', '35'],
            ['36', '37', '38', '39', '40'],
            ['41', '42', '43', '44', '45'],
            ['46', '47', '48', '49', '50']
        ]

        data = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '10'],
            ['11', '12', '13', '14', '15'],
            ['16', '17', '18', '19', '20'],
            ['21', '22', '23', '24', '25'],
            ['26', '27', '28', '29', '30'],
            ['31', '32', '33', '34', '35'],
            ['36', '37', '38', '39', '40'],
            ['41', '42', '43', '44', '45'],
            ['46', '47', '48', '49', '50']
        ]

        expected_result = [
            ['1'],
            ['6'],
            ['11'],
            ['16'],
            ['21'],
            ['26'],
            ['31'],
            ['36'],
            ['41'],
            ['46']
        ]

        actual_result = student_assignment.remove_from_end(data, 4)

        self.assertListEqual(original, data) # Check data has not been modified
        for i in range(len(expected_result)):
            self.assertListEqual(expected_result[i], actual_result[i])

        original = read_data('netflix.csv')
        data = read_data('netflix.csv')
        actual_result = student_assignment.remove_from_end(data, 14)
        self.assertEqual(len(original), len(data))
        self.assertEqual(len(original), len(actual_result))
        for row in actual_result:
            self.assertEqual(12, len(row))
        for i in range(len(original)):
            for j in range(12):
                self.assertEqual(original[i][j], actual_result[i][j])

        global marks, passed
        passed += ["remove_from_end"]
        marks += 12.5


    def test_count_number_of_movies(self):
        
        original = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', 'Movie', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', 'TV Show', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        ]

        data = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', 'Movie', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', 'TV Show', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
        ]

        actual_result = student_assignment.count_number_of_movies(data)
        self.assertEqual(1, actual_result)
        self.assertEqual(len(original), len(data))
        for i in range(len(original)):
            self.assertListEqual(original[i], data[i])

        original = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', 'Movie', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', 'TV Show', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
            ['25', 'Movie', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
            ['37', 'Movie', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
            ['49', 'Movie', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'],
            ['61', 'TV Show', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72'],
            ['73', 'TV Show', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84'],
            ['85', 'Movie', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96'],
            ['97', 'Movie', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108'],
            ['109', 'Movie', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120'],
        ]

        data = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', 'Movie', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', 'TV Show', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
            ['25', 'Movie', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
            ['37', 'Movie', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48'],
            ['49', 'Movie', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'],
            ['61', 'TV Show', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72'],
            ['73', 'TV Show', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84'],
            ['85', 'Movie', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96'],
            ['97', 'Movie', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108'],
            ['109', 'Movie', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120'],
        ]

        actual_result = student_assignment.count_number_of_movies(data)
        self.assertEqual(7, actual_result)
        self.assertEqual(len(original), len(data))
        for i in range(len(original)):
            self.assertListEqual(original[i], data[i])


        original = read_data('netflix.csv')
        original = student_assignment.remove_from_end(original, 14)

        data = read_data('netflix.csv')
        data = student_assignment.remove_from_end(data, 14)


        actual_result = student_assignment.count_number_of_movies(data)
        self.assertEqual(6132, actual_result)
        self.assertEqual(len(original), len(data))
        for i in range(len(original)):
            self.assertListEqual(original[i], data[i])

        global marks, passed
        passed += ["count_number_of_movies"]
        marks += 12.5



    def test_list_to_dictionary(self):
        original = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
        ]

        data = [
            ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
        ]

        actual_result = student_assignment.list_to_dictionary(data)
        self.assertEqual(len(original), len(data))
        self.assertListEqual(original, data)
        self.assertEqual(len(original) - 1, len(actual_result))
        for row in original[1:]:
            self.assertTrue(row[0] in actual_result)
            for i in range(0, len(row)):
                self.assertEqual(row[i], actual_result[row[0]][original[0][i]])

        self.assertEqual(3, len(data))
        for sub in data:
            self.assertEqual(12, len(sub))

        original = read_data('netflix.csv')
        original = student_assignment.remove_from_end(original, 14)

        data = read_data('netflix.csv')
        data = student_assignment.remove_from_end(data, 14)

        actual_result = student_assignment.list_to_dictionary(data)
        self.assertEqual(len(original), len(data))
        self.assertListEqual(original, data)
        self.assertEqual(len(original) - 1, len(actual_result))
        for row in original[1:]:
            self.assertTrue(row[0] in actual_result)
            for i in range(0, len(row)):
                self.assertEqual(row[i], actual_result[row[0]][original[0][i]])
        
        global marks, passed
        passed += ["list_to_dictionary"]
        marks += 12.5


    def test_transform_dictionary(self):

        original = {
            's1' : {'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': ' September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her fat'},
        }

        data = {
            's1' : {'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': ' September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her fat'},
        }

        expected_result = {
            1: {
                'cast': [],
                'country': ['United States'],
                'date_added': {'day': 25, 'month': 9, 'year': 2021},
                'description': 'As her fat',
                'director': ['Kirsten Johnson'],
                'duration': '90 min',
                'listed_in': ['Documentaries'],
                'rating': 'PG-13',
                'release_year': 2020,
                'title': 'Dick Johnson Is Dead',
                'type': 'Movie'
            }
        }

        actual_result = student_assignment.transform_dictionary(data)
        self.assertDictEqual(original, data)
        self.assertDictEqual(expected_result, actual_result)

        original = {
            's1' : {'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': 'September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her fat'},
            's2' : {'show_id': 's2', 'type': 'TV Show', 'title': 'Blood & Water', 'director': '', 'cast': 'Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng', 'country': 'South Africa', 'date_added': 'September 24, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '2 Seasons', 'listed_in': 'International TV Shows, TV Dramas, TV Mysteries', 'description': 'After cros'},
            's100' : {'show_id': 's100', 'type': 'TV Show', 'title': 'On the Verge', 'director': '', 'cast': 'Julie Delpy, Elisabeth Shue, Sarah Jones, Alexia Landeau, Mathieu Demy, Troy Garity, Timm Sharp, Giovanni Ribisi', 'country': 'France, United States', 'date_added': 'September 7, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '1 Season', 'listed_in': 'TV Comedies, TV Dramas', 'description': 'Four women'},
        }

        data = {
            's1' : {'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': 'September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her fat'},
            's2' : {'show_id': 's2', 'type': 'TV Show', 'title': 'Blood & Water', 'director': '', 'cast': 'Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng', 'country': 'South Africa', 'date_added': 'September 24, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '2 Seasons', 'listed_in': 'International TV Shows, TV Dramas, TV Mysteries', 'description': 'After cros'},
            's100' : {'show_id': 's100', 'type': 'TV Show', 'title': 'On the Verge', 'director': '', 'cast': 'Julie Delpy, Elisabeth Shue, Sarah Jones, Alexia Landeau, Mathieu Demy, Troy Garity, Timm Sharp, Giovanni Ribisi', 'country': 'France, United States', 'date_added': 'September 7, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '1 Season', 'listed_in': 'TV Comedies, TV Dramas', 'description': 'Four women'},
        }

        expected_result = {
            1: {
                'cast': [],
                'country': ['United States'],
                'date_added': {'day': 25, 'month': 9, 'year': 2021},
                'description': 'As her fat',
                'director': ['Kirsten Johnson'],
                'duration': '90 min',
                'listed_in': ['Documentaries'],
                'rating': 'PG-13',
                'release_year': 2020,
                'title': 'Dick Johnson Is Dead',
                'type': 'Movie'
            },
            100: {
                'cast': ['Julie Delpy',
                        'Elisabeth Shue',
                        'Sarah Jones',
                        'Alexia Landeau',
                        'Mathieu Demy',
                        'Troy Garity',
                        'Timm Sharp',
                        'Giovanni Ribisi'],
                'country': ['France', 'United States'],
                'date_added': {'day': 7, 'month': 9, 'year': 2021},
                'description': 'Four women',
                'director': [],
                'duration': '1 Season',
                'listed_in': ['TV Comedies', 'TV Dramas'],
                'rating': 'TV-MA',
                'release_year': 2021,
                'title': 'On the Verge',
                'type': 'TV Show'
            },
            2: {
                'cast': ['Ama Qamata',
                            'Khosi Ngema',
                            'Gail Mabalane',
                            'Thabang Molaba',
                            'Dillon Windvogel',
                            'Natasha Thahane',
                            'Arno Greeff',
                            'Xolile Tshabalala',
                            'Getmore Sithole',
                            'Cindy Mahlangu',
                            'Ryle De Morny',
                            'Greteli Fincham',
                            'Sello Maake Ka-Ncube',
                            'Odwa Gwanya',
                            'Mekaila Mathys',
                            'Sandi Schultz',
                            'Duane Williams',
                            'Shamilla Miller',
                            'Patrick Mofokeng'],
                'country': ['South Africa'],
                'date_added': {'day': 24, 'month': 9, 'year': 2021},
                'description': 'After cros',
                'director': [],
                'duration': '2 Seasons',
                'listed_in': ['International TV Shows', 'TV Dramas', 'TV Mysteries'],
                'rating': 'TV-MA',
                'release_year': 2021,
                'title': 'Blood & Water',
                'type': 'TV Show'
            }
        }

        actual_result = student_assignment.transform_dictionary(data)
        self.assertDictEqual(original, data)
        self.assertDictEqual(expected_result, actual_result)

        original = {
            's1' : {'show_id': 's6067', 'type': 'TV Show', 'title': "A Young Doctor's Notebook and Other Stories", 'director': '', 'cast': 'Daniel Radcliffe, Jon Hamm, Adam Godley, Christopher Godwin, Rosie Cavaliero, Vicki Pepperdine, Margaret Clunie, Tim Steed, Shaun Pye', 'country': 'United Kingdom', 'date_added': '', 'release_year': '2013', 'rating': 'TV-MA', 'duration': '2 Seasons', 'listed_in': 'British TV Shows, TV Comedies, TV Dramas', 'description': "Set during the Russian Revolution, this comic miniseries is based on a doctor's memories of his early career working in an out-of-the-way village."}
        }

        data = {
            's1' : {'show_id': 's6067', 'type': 'TV Show', 'title': "A Young Doctor's Notebook and Other Stories", 'director': '', 'cast': 'Daniel Radcliffe, Jon Hamm, Adam Godley, Christopher Godwin, Rosie Cavaliero, Vicki Pepperdine, Margaret Clunie, Tim Steed, Shaun Pye', 'country': 'United Kingdom', 'date_added': '', 'release_year': '2013', 'rating': 'TV-MA', 'duration': '2 Seasons', 'listed_in': 'British TV Shows, TV Comedies, TV Dramas', 'description': "Set during the Russian Revolution, this comic miniseries is based on a doctor's memories of his early career working in an out-of-the-way village."}
        }

        expected_result = {
            1: {
                'cast': [
                    'Daniel Radcliffe',
                    'Jon Hamm',
                    'Adam Godley',
                    'Christopher Godwin',
                    'Rosie Cavaliero',
                    'Vicki Pepperdine',
                    'Margaret Clunie',
                    'Tim Steed',
                    'Shaun Pye'
                ],
                'country': ['United Kingdom'],
                'date_added': {'day': None, 'month': None, 'year': None},
                'description': 'Set during the Russian Revolution, this comic '
                                "miniseries is based on a doctor's memories of his early "
                                'career working in an out-of-the-way village.',
                'director': [],
                'duration': '2 Seasons',
                'listed_in': ['British TV Shows', 'TV Comedies', 'TV Dramas'],
                'rating': 'TV-MA',
                'release_year': 2013,
                'title': "A Young Doctor's Notebook and Other Stories",
                'type': 'TV Show'}
       }

        actual_result = student_assignment.transform_dictionary(data)
        self.assertDictEqual(original, data)
        self.assertDictEqual(expected_result, actual_result)

        global marks, passed
        passed += ["transform_dictionary"]
        marks += 12.5


    def test_get_titles_with_director_dict(self):

        original = read_data('netflix.csv')
        original = student_assignment.remove_from_end(original, 14)
        original = student_assignment.list_to_dictionary(original)
        original = student_assignment.transform_dictionary(original)

        
        data = read_data('netflix.csv')
        data = student_assignment.remove_from_end(data, 14)
        data = student_assignment.list_to_dictionary(data)
        data = student_assignment.transform_dictionary(data)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Christopher Nolan')
        expected_result = ['Inception']
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Martin Scorsese')
        expected_result = ['Shutter Island', 'No Direction Home: Bob Dylan', 'Hugo', 'The Irishman', 'Rolling Thunder Revue: A Bob Dylan Story by Martin Scorsese', "Alice Doesn't Live Here Anymore", 'Gangs of New York', 'GoodFellas', 'Mean Streets', 'Raging Bull', 'The Departed', "Who's That Knocking at My Door?"]
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Stephen Spielberg')
        expected_result = []
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Steven Spielberg')
        expected_result = ['Jaws', 'Catch Me If You Can', 'The BFG', 'Indiana Jones and the Kingdom of the Crystal Skull', 'Indiana Jones and the Last Crusade', 'Indiana Jones and the Raiders of the Lost Ark', 'Indiana Jones and the Temple of Doom', 'Lincoln', "Schindler's List", 'The Adventures of Tintin', 'War Horse']
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Quentin Tarintino')
        expected_result = []
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Quentin Tarantino')
        expected_result = ['Django Unchained', 'The Hateful Eight: Extended Version', 'The Hateful Eight', 'Inglourious Basterds', 'Jackie Brown', 'Kill Bill: Vol. 1', 'Kill Bill: Vol. 2', 'Pulp Fiction']
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Makoto Shinkai')
        expected_result = ['The Garden of Words']
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        actual_result = student_assignment.get_titles_with_director_dict(data, 'Tim Burton')
        expected_result = ['Mars Attacks!', 'Charlie and the Chocolate Factory', 'Sweeney Todd: The Demon Barber of Fleet Street']
        self.assertEqual(len(original), len(data))
        self.assertDictEqual(original, data)
        self.assertEqual(expected_result, actual_result)

        global marks, passed
        passed += ["get_titles_with_director_dict"]
        marks += 12.5
        

    @classmethod
    def tearDownClass(self):
        global marks, passed, final_output
        final_output = f'Final Mark: {marks}\nPassed: {passed}'

final_output = ""

if __name__ == "__main__":    
    unittest.main(exit=False)
    print("\n" * 5 + final_output)