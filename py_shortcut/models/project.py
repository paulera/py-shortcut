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

class Project(object):
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
        'app_url': 'str',
        'description': 'str',
        'archived': 'bool',
        'entity_type': 'str',
        'days_to_thermometer': 'int',
        'color': 'str',
        'workflow_id': 'int',
        'name': 'str',
        'start_time': 'datetime',
        'updated_at': 'datetime',
        'follower_ids': 'list[str]',
        'external_id': 'str',
        'id': 'int',
        'show_thermometer': 'bool',
        'team_id': 'int',
        'iteration_length': 'int',
        'abbreviation': 'str',
        'stats': 'ProjectStats',
        'created_at': 'datetime'
    }

    attribute_map = {
        'app_url': 'app_url',
        'description': 'description',
        'archived': 'archived',
        'entity_type': 'entity_type',
        'days_to_thermometer': 'days_to_thermometer',
        'color': 'color',
        'workflow_id': 'workflow_id',
        'name': 'name',
        'start_time': 'start_time',
        'updated_at': 'updated_at',
        'follower_ids': 'follower_ids',
        'external_id': 'external_id',
        'id': 'id',
        'show_thermometer': 'show_thermometer',
        'team_id': 'team_id',
        'iteration_length': 'iteration_length',
        'abbreviation': 'abbreviation',
        'stats': 'stats',
        'created_at': 'created_at'
    }

    def __init__(self, app_url=None, description=None, archived=None, entity_type=None, days_to_thermometer=None, color=None, workflow_id=None, name=None, start_time=None, updated_at=None, follower_ids=None, external_id=None, id=None, show_thermometer=None, team_id=None, iteration_length=None, abbreviation=None, stats=None, created_at=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._description = None
        self._archived = None
        self._entity_type = None
        self._days_to_thermometer = None
        self._color = None
        self._workflow_id = None
        self._name = None
        self._start_time = None
        self._updated_at = None
        self._follower_ids = None
        self._external_id = None
        self._id = None
        self._show_thermometer = None
        self._team_id = None
        self._iteration_length = None
        self._abbreviation = None
        self._stats = None
        self._created_at = None
        self.discriminator = None
        self.app_url = app_url
        self.description = description
        self.archived = archived
        self.entity_type = entity_type
        self.days_to_thermometer = days_to_thermometer
        self.color = color
        self.workflow_id = workflow_id
        self.name = name
        self.start_time = start_time
        self.updated_at = updated_at
        self.follower_ids = follower_ids
        self.external_id = external_id
        self.id = id
        self.show_thermometer = show_thermometer
        self.team_id = team_id
        self.iteration_length = iteration_length
        self.abbreviation = abbreviation
        self.stats = stats
        self.created_at = created_at

    @property
    def app_url(self):
        """Gets the app_url of this Project.  # noqa: E501

        The Shortcut application url for the Project.  # noqa: E501

        :return: The app_url of this Project.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this Project.

        The Shortcut application url for the Project.  # noqa: E501

        :param app_url: The app_url of this Project.  # noqa: E501
        :type: str
        """
        if app_url is None:
            raise ValueError("Invalid value for `app_url`, must not be `None`")  # noqa: E501

        self._app_url = app_url

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        The description of the Project.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        The description of the Project.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def archived(self):
        """Gets the archived of this Project.  # noqa: E501

        True/false boolean indicating whether the Project is in an Archived state.  # noqa: E501

        :return: The archived of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Project.

        True/false boolean indicating whether the Project is in an Archived state.  # noqa: E501

        :param archived: The archived of this Project.  # noqa: E501
        :type: bool
        """
        if archived is None:
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def entity_type(self):
        """Gets the entity_type of this Project.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Project.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Project.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Project.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def days_to_thermometer(self):
        """Gets the days_to_thermometer of this Project.  # noqa: E501

        The number of days before the thermometer appears in the Story summary.  # noqa: E501

        :return: The days_to_thermometer of this Project.  # noqa: E501
        :rtype: int
        """
        return self._days_to_thermometer

    @days_to_thermometer.setter
    def days_to_thermometer(self, days_to_thermometer):
        """Sets the days_to_thermometer of this Project.

        The number of days before the thermometer appears in the Story summary.  # noqa: E501

        :param days_to_thermometer: The days_to_thermometer of this Project.  # noqa: E501
        :type: int
        """
        if days_to_thermometer is None:
            raise ValueError("Invalid value for `days_to_thermometer`, must not be `None`")  # noqa: E501

        self._days_to_thermometer = days_to_thermometer

    @property
    def color(self):
        """Gets the color of this Project.  # noqa: E501

        The color associated with the Project in the Shortcut member interface.  # noqa: E501

        :return: The color of this Project.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Project.

        The color associated with the Project in the Shortcut member interface.  # noqa: E501

        :param color: The color of this Project.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def workflow_id(self):
        """Gets the workflow_id of this Project.  # noqa: E501

        The ID of the workflow the project belongs to.  # noqa: E501

        :return: The workflow_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this Project.

        The ID of the workflow the project belongs to.  # noqa: E501

        :param workflow_id: The workflow_id of this Project.  # noqa: E501
        :type: int
        """
        if workflow_id is None:
            raise ValueError("Invalid value for `workflow_id`, must not be `None`")  # noqa: E501

        self._workflow_id = workflow_id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The name of the Project  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The name of the Project  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this Project.  # noqa: E501

        The date at which the Project was started.  # noqa: E501

        :return: The start_time of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Project.

        The date at which the Project was started.  # noqa: E501

        :param start_time: The start_time of this Project.  # noqa: E501
        :type: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def updated_at(self):
        """Gets the updated_at of this Project.  # noqa: E501

        The time/date that the Project was last updated.  # noqa: E501

        :return: The updated_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Project.

        The time/date that the Project was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Project.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def follower_ids(self):
        """Gets the follower_ids of this Project.  # noqa: E501

        An array of UUIDs for any Members listed as Followers.  # noqa: E501

        :return: The follower_ids of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this Project.

        An array of UUIDs for any Members listed as Followers.  # noqa: E501

        :param follower_ids: The follower_ids of this Project.  # noqa: E501
        :type: list[str]
        """
        if follower_ids is None:
            raise ValueError("Invalid value for `follower_ids`, must not be `None`")  # noqa: E501

        self._follower_ids = follower_ids

    @property
    def external_id(self):
        """Gets the external_id of this Project.  # noqa: E501

        This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Project.

        This field can be set to another unique ID. In the case that the Project has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this Project.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        The unique ID of the Project.  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        The unique ID of the Project.  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def show_thermometer(self):
        """Gets the show_thermometer of this Project.  # noqa: E501

        Configuration to enable or disable thermometers in the Story summary.  # noqa: E501

        :return: The show_thermometer of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._show_thermometer

    @show_thermometer.setter
    def show_thermometer(self, show_thermometer):
        """Sets the show_thermometer of this Project.

        Configuration to enable or disable thermometers in the Story summary.  # noqa: E501

        :param show_thermometer: The show_thermometer of this Project.  # noqa: E501
        :type: bool
        """
        if show_thermometer is None:
            raise ValueError("Invalid value for `show_thermometer`, must not be `None`")  # noqa: E501

        self._show_thermometer = show_thermometer

    @property
    def team_id(self):
        """Gets the team_id of this Project.  # noqa: E501

        The ID of the team the project belongs to.  # noqa: E501

        :return: The team_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Project.

        The ID of the team the project belongs to.  # noqa: E501

        :param team_id: The team_id of this Project.  # noqa: E501
        :type: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def iteration_length(self):
        """Gets the iteration_length of this Project.  # noqa: E501

        The number of weeks per iteration in this Project.  # noqa: E501

        :return: The iteration_length of this Project.  # noqa: E501
        :rtype: int
        """
        return self._iteration_length

    @iteration_length.setter
    def iteration_length(self, iteration_length):
        """Sets the iteration_length of this Project.

        The number of weeks per iteration in this Project.  # noqa: E501

        :param iteration_length: The iteration_length of this Project.  # noqa: E501
        :type: int
        """
        if iteration_length is None:
            raise ValueError("Invalid value for `iteration_length`, must not be `None`")  # noqa: E501

        self._iteration_length = iteration_length

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Project.  # noqa: E501

        The Project abbreviation used in Story summaries. Should be kept to 3 characters at most.  # noqa: E501

        :return: The abbreviation of this Project.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Project.

        The Project abbreviation used in Story summaries. Should be kept to 3 characters at most.  # noqa: E501

        :param abbreviation: The abbreviation of this Project.  # noqa: E501
        :type: str
        """
        if abbreviation is None:
            raise ValueError("Invalid value for `abbreviation`, must not be `None`")  # noqa: E501

        self._abbreviation = abbreviation

    @property
    def stats(self):
        """Gets the stats of this Project.  # noqa: E501


        :return: The stats of this Project.  # noqa: E501
        :rtype: ProjectStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Project.


        :param stats: The stats of this Project.  # noqa: E501
        :type: ProjectStats
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501

        The time/date that the Project was created.  # noqa: E501

        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.

        The time/date that the Project was created.  # noqa: E501

        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

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
        if issubclass(Project, dict):
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
