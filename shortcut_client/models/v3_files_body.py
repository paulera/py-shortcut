# coding: utf-8

"""
    Shortcut API

    Shortcut API  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V3FilesBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'story_id': 'int',
        'file0': 'str',
        'file1': 'str',
        'file2': 'str',
        'file3': 'str'
    }

    attribute_map = {
        'story_id': 'story_id',
        'file0': 'file0',
        'file1': 'file1',
        'file2': 'file2',
        'file3': 'file3'
    }

    def __init__(self, story_id=None, file0=None, file1=None, file2=None, file3=None):  # noqa: E501
        """V3FilesBody - a model defined in Swagger"""  # noqa: E501
        self._story_id = None
        self._file0 = None
        self._file1 = None
        self._file2 = None
        self._file3 = None
        self.discriminator = None
        if story_id is not None:
            self.story_id = story_id
        self.file0 = file0
        if file1 is not None:
            self.file1 = file1
        if file2 is not None:
            self.file2 = file2
        if file3 is not None:
            self.file3 = file3

    @property
    def story_id(self):
        """Gets the story_id of this V3FilesBody.  # noqa: E501

        The story ID that these files will be associated with.  # noqa: E501

        :return: The story_id of this V3FilesBody.  # noqa: E501
        :rtype: int
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id):
        """Sets the story_id of this V3FilesBody.

        The story ID that these files will be associated with.  # noqa: E501

        :param story_id: The story_id of this V3FilesBody.  # noqa: E501
        :type: int
        """

        self._story_id = story_id

    @property
    def file0(self):
        """Gets the file0 of this V3FilesBody.  # noqa: E501

        A file upload. At least one is required.  # noqa: E501

        :return: The file0 of this V3FilesBody.  # noqa: E501
        :rtype: str
        """
        return self._file0

    @file0.setter
    def file0(self, file0):
        """Sets the file0 of this V3FilesBody.

        A file upload. At least one is required.  # noqa: E501

        :param file0: The file0 of this V3FilesBody.  # noqa: E501
        :type: str
        """
        if file0 is None:
            raise ValueError("Invalid value for `file0`, must not be `None`")  # noqa: E501

        self._file0 = file0

    @property
    def file1(self):
        """Gets the file1 of this V3FilesBody.  # noqa: E501

        Optional additional files.  # noqa: E501

        :return: The file1 of this V3FilesBody.  # noqa: E501
        :rtype: str
        """
        return self._file1

    @file1.setter
    def file1(self, file1):
        """Sets the file1 of this V3FilesBody.

        Optional additional files.  # noqa: E501

        :param file1: The file1 of this V3FilesBody.  # noqa: E501
        :type: str
        """

        self._file1 = file1

    @property
    def file2(self):
        """Gets the file2 of this V3FilesBody.  # noqa: E501

        Optional additional files.  # noqa: E501

        :return: The file2 of this V3FilesBody.  # noqa: E501
        :rtype: str
        """
        return self._file2

    @file2.setter
    def file2(self, file2):
        """Sets the file2 of this V3FilesBody.

        Optional additional files.  # noqa: E501

        :param file2: The file2 of this V3FilesBody.  # noqa: E501
        :type: str
        """

        self._file2 = file2

    @property
    def file3(self):
        """Gets the file3 of this V3FilesBody.  # noqa: E501

        Optional additional files.  # noqa: E501

        :return: The file3 of this V3FilesBody.  # noqa: E501
        :rtype: str
        """
        return self._file3

    @file3.setter
    def file3(self, file3):
        """Sets the file3 of this V3FilesBody.

        Optional additional files.  # noqa: E501

        :param file3: The file3 of this V3FilesBody.  # noqa: E501
        :type: str
        """

        self._file3 = file3

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V3FilesBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3FilesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
