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

class CreateProject(object):
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
        'description': 'str',
        'color': 'str',
        'name': 'str',
        'start_time': 'datetime',
        'updated_at': 'datetime',
        'follower_ids': 'list[str]',
        'external_id': 'str',
        'team_id': 'int',
        'iteration_length': 'int',
        'abbreviation': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'color': 'color',
        'name': 'name',
        'start_time': 'start_time',
        'updated_at': 'updated_at',
        'follower_ids': 'follower_ids',
        'external_id': 'external_id',
        'team_id': 'team_id',
        'iteration_length': 'iteration_length',
        'abbreviation': 'abbreviation',
        'created_at': 'created_at'
    }

    def __init__(self, description=None, color=None, name=None, start_time=None, updated_at=None, follower_ids=None, external_id=None, team_id=None, iteration_length=None, abbreviation=None, created_at=None):  # noqa: E501
        """CreateProject - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._color = None
        self._name = None
        self._start_time = None
        self._updated_at = None
        self._follower_ids = None
        self._external_id = None
        self._team_id = None
        self._iteration_length = None
        self._abbreviation = None
        self._created_at = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if color is not None:
            self.color = color
        self.name = name
        if start_time is not None:
            self.start_time = start_time
        if updated_at is not None:
            self.updated_at = updated_at
        if follower_ids is not None:
            self.follower_ids = follower_ids
        if external_id is not None:
            self.external_id = external_id
        self.team_id = team_id
        if iteration_length is not None:
            self.iteration_length = iteration_length
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if created_at is not None:
            self.created_at = created_at

    @property
    def description(self):
        """Gets the description of this CreateProject.  # noqa: E501

        The Project description.  # noqa: E501

        :return: The description of this CreateProject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProject.

        The Project description.  # noqa: E501

        :param description: The description of this CreateProject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def color(self):
        """Gets the color of this CreateProject.  # noqa: E501

        The color you wish to use for the Project in the system.  # noqa: E501

        :return: The color of this CreateProject.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CreateProject.

        The color you wish to use for the Project in the system.  # noqa: E501

        :param color: The color of this CreateProject.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def name(self):
        """Gets the name of this CreateProject.  # noqa: E501

        The name of the Project.  # noqa: E501

        :return: The name of this CreateProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProject.

        The name of the Project.  # noqa: E501

        :param name: The name of this CreateProject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this CreateProject.  # noqa: E501

        The date at which the Project was started.  # noqa: E501

        :return: The start_time of this CreateProject.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateProject.

        The date at which the Project was started.  # noqa: E501

        :param start_time: The start_time of this CreateProject.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateProject.  # noqa: E501

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :return: The updated_at of this CreateProject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateProject.

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :param updated_at: The updated_at of this CreateProject.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def follower_ids(self):
        """Gets the follower_ids of this CreateProject.  # noqa: E501

        An array of UUIDs for any members you want to add as Owners on this new Epic.  # noqa: E501

        :return: The follower_ids of this CreateProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this CreateProject.

        An array of UUIDs for any members you want to add as Owners on this new Epic.  # noqa: E501

        :param follower_ids: The follower_ids of this CreateProject.  # noqa: E501
        :type: list[str]
        """

        self._follower_ids = follower_ids

    @property
    def external_id(self):
        """Gets the external_id of this CreateProject.  # noqa: E501

        This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this CreateProject.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateProject.

        This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this CreateProject.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def team_id(self):
        """Gets the team_id of this CreateProject.  # noqa: E501

        The ID of the team the project belongs to.  # noqa: E501

        :return: The team_id of this CreateProject.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this CreateProject.

        The ID of the team the project belongs to.  # noqa: E501

        :param team_id: The team_id of this CreateProject.  # noqa: E501
        :type: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def iteration_length(self):
        """Gets the iteration_length of this CreateProject.  # noqa: E501

        The number of weeks per iteration in this Project.  # noqa: E501

        :return: The iteration_length of this CreateProject.  # noqa: E501
        :rtype: int
        """
        return self._iteration_length

    @iteration_length.setter
    def iteration_length(self, iteration_length):
        """Sets the iteration_length of this CreateProject.

        The number of weeks per iteration in this Project.  # noqa: E501

        :param iteration_length: The iteration_length of this CreateProject.  # noqa: E501
        :type: int
        """

        self._iteration_length = iteration_length

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CreateProject.  # noqa: E501

        The Project abbreviation used in Story summaries. Should be kept to 3 characters at most.  # noqa: E501

        :return: The abbreviation of this CreateProject.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CreateProject.

        The Project abbreviation used in Story summaries. Should be kept to 3 characters at most.  # noqa: E501

        :param abbreviation: The abbreviation of this CreateProject.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def created_at(self):
        """Gets the created_at of this CreateProject.  # noqa: E501

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :return: The created_at of this CreateProject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateProject.

        Defaults to the time/date it is created but can be set to reflect another date.  # noqa: E501

        :param created_at: The created_at of this CreateProject.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(CreateProject, dict):
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
        if not isinstance(other, CreateProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
