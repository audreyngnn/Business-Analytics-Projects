"""
# Student Declaration
# I [Nguyen Khuat Son Tra], student id: 48144134, declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit. 
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# I understand that i must read the entire assigment outline on iLearn before starting
# the assessment.
# [x] <== put an x in here to indicate you have read and agree to the above statements.
"""

def check_list_bounds(data, n : int, m : int):
    """(12.5 marks)
    Given a list of lists and an integer n and m. Return True if the list is a n by m list, False otherwise

    Example
    data = [
        ['1', '2', '3', '4', '5'],
        ['6', '7', '8', '9', '10'],
        ['11', '12', '13', '14', '15']
    ]
    check_list_bounds(data, 3, 5) should return True 
    check_list_bounds(data, 5, 3) should return False
    
    The original list should not be modfied
    """
    return len(data) == n and all(len(sublist) == m for sublist in data) 
            # check if the length of the outer list is equal to n
                                # check if the length of each inner sublist is equal to m


def convert_string_to_list(data: str):
    """(12.5 marks)
    Given a string of comma separated values, return a list of the values
    e.g. convert_string_to_list("1, 2, 3, 4, 5") should return ['1', '2', '3', '4', '5']
    """
    result = [] # Initialize an empty list to store the values
    current_value = '' # Initialize an empty string to store the current value being processed
    skip_next_space = False # Flag to keep track of whether to skip leading spaces after a comma
    
    for character in data:
        if character == ',': # Check if the character is a comma
            if current_value: 
                result.append(current_value) # If there is a non-empty current value, add it to the result list
                current_value = '' # Reset the current value
            skip_next_space = True # Set the flag to skip spaces after the comma

        elif character == ' ' and skip_next_space: # If the character is a space and skip_next_space is True, skip it
            skip_next_space = False # Reset the skip_space flag to False

        else:
            # If the character is not a comma or a space (or a space that should not be skipped)
            current_value += character # Append the character to the current value
            skip_next_space = False # Reset the skip_space flag to False

    # After processing all characters
    if current_value:
        result.append(current_value) # If there is a remaining non-empty current value, add it to the result list
    return result



def replace_values_transposed(data, new_values, column):
    """(12.5 marks)
    Given a list of lists and a list of new values, replace the values in the column specified by the column variable
    with the new values. The new values should be replaced in the same order as the original values.

    Example
    data = [
        ['1', '2', '3', '4', '5'],
        ['6', '7', '8', '9', '10'],
        ['11', '12', '13', '14', '15']
    ]
    new_values = ['a', 'b', 'c']
    column = 3

    replace_values_transposed(data, new_values, column) should return
    [
        ['1', '2', '3', 'a', '5'],
        ['6', '7', '8', 'b', '10'],
        ['11', '12', '13', 'c', '15']
    ]

    You may assume that the length of new_values is the same as the number of rows in data
    and that the data list is n by m where n is the number of rows and m is the number of columns
    
    You should modify the original list provided
    """
    # Iterate over the rows in the data list using enumerate to get the row index
    for index, row in enumerate(data):
        # Replace the value at the specified column index with the corresponding value from new_values
        row[column] = new_values[index]
    
    # Return the modified data list
    return data


def remove_from_end(list : list[list[str]], n : int):
    """(12.5 marks)
    Given a list of lists, remove the last n elements from each sublist
    e.g. data = [
        ['1', '2', '3', '4', '5'],
        ['6', '7', '8', '9', '10'],
        ['11', '12', '13', '14', '15']
    ]
    remove_from_end(data, 2) should return
    [
        ['1', '2', '3'],
        ['6', '7', '8'],
        ['11', '12', '13']
    ]

    You must not modify the original list provided
    """
    for sublist in list:
        # Check if the length of any sublist is smaller than the given number
        if n > len(sublist):
            return None
    
    # Create a new list of sublists with the last n elements removed
    return [x[:(len(x)-n)] for x in list]
        


def count_number_of_movies(data : list[list[str]]):
    """(12.5 marks)
    Given a list of lists where the first sublist contains column names for a dataset, return the number of movies
    in the dataset. A movie is defined as a row where the 'type' column is 'Movie'

    Example
    data = [
        ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
        ['1', 'Movie', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        ['13', 'TV Show', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    ]
    count_number_of_movies(data) should return 1

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
    count_number_of_movies(data) should return 7

    You must not modify the original list provided
    You may be required to complete the previous functions before the tests for this function can pass
    """
    col = data[0].index("type") # Find the index of the 'type' column
    count = 0
    for index, row in enumerate(data):
        if data[index][col] == "Movie": # Check if the 'type' value is 'Movie'
            count += 1
    return count


def list_to_dictionary(data : list[list[str]]):
    """(12.5 marks)
    Given a list of lists where the first sublist contains column names for a dataset, convert 
    the list of lists into a dictionary of dictionaries. Refer to the example below

    e.g.
    data = [
        ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    ]

    the function should return a dictionary of this form:
    {
        '1': {'show_id': '1', 'type': '2', 'title': '3', 'director': '4', 'cast': '5', 'country': '6', 'date_added': '7', 'release_year': '8', 'rating': '9', 'duration': '10', 'listed_in': '11', 'description': '12'},
        '13': {'show_id': '13', 'type': '14', 'title': '15', 'director': '16', 'cast': '17', 'country': '18', 'date_added': '19', 'release_year': '20', 'rating': '21', 'duration': '22', 'listed_in': '23', 'description': '24'}
    }

    You must not modify the original list provided
    You may be required to complete the previous functions before the tests for this function can pass
    """
    headers = data[0] # Get the column names from the first sublist
    result = {}

    for row in data[1:]: # Iterate over each row, excluding the first row (column names)
        key = row[0] # Use the first value of the row as the key for the dictionary
        row_dict = {headers[i]: row[i] for i in range(len(headers))} # Create a dictionary for the current row
        
        result[key] = row_dict # Add the row dictionary to the result dictionary using the key
    
    return result


def transform_dictionary(data : dict):
    """(12.5 marks)

    Given a dictionary of values which follow the given schema:
    {
        's1' : {'show_id': 's1', 'type': 'Movie', 'title': 'Dick Johnson Is Dead', 'director': 'Kirsten Johnson', 'cast': '', 'country': 'United States', 'date_added': ' September 25, 2021', 'release_year': '2020', 'rating': 'PG-13', 'duration': '90 min', 'listed_in': 'Documentaries', 'description': 'As her fat'},
        's2' : {'show_id': 's2', 'type': 'TV Show', 'title': 'Blood & Water', 'director': '', 'cast': 'Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng', 'country': 'South Africa', 'date_added': 'September 24, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '2 Seasons', 'listed_in': 'International TV Shows, TV Dramas, TV Mysteries', 'description': 'After cros'},
        's100' : {'show_id': 's100', 'type': 'TV Show', 'title': 'On the Verge', 'director': '', 'cast': 'Julie Delpy, Elisabeth Shue, Sarah Jones, Alexia Landeau, Mathieu Demy, Troy Garity, Timm Sharp, Giovanni Ribisi', 'country': 'France, United States', 'date_added': 'September 7, 2021', 'release_year': '2021', 'rating': 'TV-MA', 'duration': '1 Season', 'listed_in': 'TV Comedies, TV Dramas', 'description': 'Four women'},
    }

    Create a copy of the dictionary with the following operations performed:
    1. Remove the 'show_id' key from each dictionary
    2. Remove the 's' from the beginning of each key in the outter dictionary
    3. Convert each key in the outter dictionary to an int
    4. Convert the 'release_year' key to an integer
    5. Convert the director value to a list of directors
    6. Convert the country value to a list of countries
    7. Convert the cast value to a list of cast members
    8. Convert the listed_in value to a list of genres
    9. Convert date_added value to a dictionary containing the keys 'day', 'month', 'year' as integers with the corresponding values. If the date_value is empty, then None should be used for the value for all three keys

    Note: date_added may have an extra space at the front that you will need to remove

    When converting a string to a list of values, you should refer to the specifications outlined in the convert_string_to_list function

    You must not modify the original list provided
    You may be required to complete the previous functions before the tests for this function can pass
    """
    def date_transformed(date):
        # Check if the input date string is empty, if so return None for day, month, and year
        if not date:
            return {'day': None, 'month': None, 'year': None}

        # Create a new string 'result' without commas by iterating through 'date_str' and skipping commas
        result = ''
        for character in date:
            if character != ',':
                result += character

        # Find the index of the first non-space character in 'result'
        start = 0
        while start < len(result) and result[start] == ' ':
            start += 1

        # Find the index of the last non-space character in 'result'
        end = len(result) - 1
        while end >= start and result[end] == ' ':
            end -= 1

        # Create a trimmed string by slicing 'result' from 'start' to 'end+1'
        trim = result[start:end+1]

        # Define a dictionary 'month_map' to map month names to their corresponding integers
        month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                     'September': 9, 'October': 10, 'November': 11, 'December': 12}

        # Extract the month string from 'trim' by iterating until the first space is encountered
        month_str = ''
        i = 0
        while i < len(trim) and trim[i] != ' ':
            month_str += trim[i]
            i += 1

        # Get the integer value of the month from 'month_map' using the 'month_str' as the key
        month = month_map[month_str]

        # Extract the day and year part of the string by skipping the month part
        day_year_str = ''
        i += 1
        while i < len(trim):
            day_year_str += trim[i]
            i += 1

        # Find the index of the space separating the day and year in 'day_year_str'
        j = 0
        while j < len(day_year_str) and day_year_str[j] != ' ':
            j += 1

        # Convert the substring before the space to an integer to get the day
        day = int(day_year_str[:j])

        # Convert the substring after the space to an integer to get the year
        year = int(day_year_str[j+1:])

        # Return a dictionary with the extracted day, month, and year values
        return {'day': day, 'month': month, 'year': year}

    transformed_dictionary = {}
    for key, val in data.items():
        # Remove the 's' from the beginning of each key and convert it to an integer
        new_id = int(key[1:])

        # Create a new dictionary entry in 'transformed_dictionary' using 'new_id' as the key
        transformed_dictionary[new_id] = {
            'cast': convert_string_to_list(val.get('cast', '')),  # Convert the cast value to a list of cast members
            'country': convert_string_to_list(val.get('country', '')),  # Convert the country value to a list of countries
            'date_added': date_transformed(val.get('date_added', '')),  # Convert date_added value to the expected dictionary
            'description': val.get('description', ''),  # Add the description value as is
            'director': convert_string_to_list(val.get('director', '')),  # Convert the director value to a list of directors
            'duration': val.get('duration', ''),  # Add the duration value as is
            'listed_in': convert_string_to_list(val.get('listed_in', '')),  # Convert the listed_in value to a list of genres
            'rating': val.get('rating', ''),  # Add the rating value as is
            'release_year': int(val.get('release_year', '')),  # Convert the release_year value to an integer
            'title': val.get('title', ''),  # Add the title value as is
            'type': val.get('type', '')  # Add the type value as is
        }

    # Return the transformed dictionary
    return transformed_dictionary


def get_titles_with_director_dict(data : dict, director):
    """(12.5 marks)
    given a dictionary of dictionaries of the following schema:
    {
        '1': {
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
    Return a list of all titles of movies directed by the passed director

    You must not modify the original list provided
    You may be required to complete the previous functions before the tests for this function can pass
    """
    movies = [] # initialize an empty list to store the matching titles
    for movie_data in data.values(): # iterate over the values of the dictionary 
        if director in movie_data['director']: # check if the given director is in the 'director' list
            movies.append(movie_data['title']) # if the director is found, append the title to the list
    
    return movies # return the final result


