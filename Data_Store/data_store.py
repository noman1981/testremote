import json
import os
from dicttoxml import dicttoxml


class DataStore:
    def __init__(self, out_format='json', output_location='static/'):

        """
        Constructor of Class Datastore

        :param out_format: file format of output file
        :param output_location: location to save output file
        """

        self._file_location = output_location
        self._output_format = out_format
        self._store = {}

    def get_values(self):
        """ Returns Storage values"""
        if not self.is_empty():
            return self._store
        else:
            raise Exception('Store is Empty')

    def insert(self, key_values):

        """ Insert data to storage
            only take tuple or list of tuples as Input
        """

        if key_values:
            if isinstance(key_values, list):
                for key_value in key_values:
                    if len(key_value) == 2:
                        if not isinstance(key_value[1], list) and key_values[0]:
                            self._store[key_value[0]] = key_value[1]
                        else:
                            raise TypeError('list type for value and NoneType for Key not allowed')
                    else:
                        raise TypeError('There should only be key value pair')
                return True
            elif isinstance(key_values, tuple):
                if len(key_values) == 2:
                    if not isinstance(key_values[1], list) and key_values[0]:
                        self._store[key_values[0]] = key_values[1]
                        return True
                    else:
                        raise TypeError("lists not allowed as value")
                else:
                    raise TypeError('Except only key value pair')
        else:
            raise TypeError('NoneType cannot be inserted')

    def update(self, key, value):

        """ Take key value pair to update value in storage"""

        if key in self._store.keys():
            if key and value:
                self.insert(key_values=(key, value))
                return True
            else:
                raise TypeError('NoneType')
        else:
            raise KeyError('Key Does Not Exist')

    def pull(self, key):

        """ Pull value against provided Key """

        if not self.is_empty():
            if key in self._store.keys():
                return self._store[key]
            else:
                raise KeyError('Key Not Found')
        else:
            raise TypeError('Store is Empty')

    def delete(self, key):
        """Delete a Value against Key"""
        if key in self._store.keys():
            del self._store[key]
            return True
        else:
            raise KeyError('Key Does Not Exist')

    @staticmethod
    def open_file(__file_location, __output_format):

        """
        Static method to open file on file location and with provided output format extension
        """

        if os.path.exists(__file_location):
            _output = open(f"{__file_location}output.{__output_format.lower()}", 'w')
            return _output
        else:
            os.makedirs(__file_location)
            _output = open(f"{__file_location}output.{__output_format.lower()}", 'w')
            return _output

    def save(self):
        """ Saves storage file default or configured location"""
        if not self.is_empty():
            _output = self.open_file(self._file_location, self._output_format)
            if self._output_format.lower() == 'json':
                json.dump(self._store, _output)
            elif self._output_format.lower() == 'xml':
                xml_decode = dicttoxml(self._store).decode()
                _output.write(xml_decode)
            _output.close()
        else:
            raise TypeError('NoneType Cannot be write to file')

    def filter(self, filter_string, limit=1, offset=0):

        """ Filter values on key basis"""

        if filter_string:
            _dict = {k: v for (k, v) in self._store.items() if filter_string in k}
            filtered_dict = _dict.copy()
            for ind, k in enumerate(_dict):
                if ind < offset:
                    filtered_dict.pop(k)
                else:
                    break
            while len(filtered_dict) > limit:
                filtered_dict.popitem()
            return filtered_dict
        else:
            raise TypeError('NoneType cannot be Filtered')

    def is_empty(self):

        """ Returns Boolean value for storage to be full or not"""

        if self._store.__len__():
            return False
        else:
            return True

