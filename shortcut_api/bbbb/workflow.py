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

class Workflow(object):
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
        'entity_type': 'str',
        'project_ids': 'list[float]',
        'states': 'list[WorkflowState]',
        'name': 'str',
        'updated_at': 'datetime',
        'auto_assign_owner': 'bool',
        'id': 'int',
        'team_id': 'int',
        'created_at': 'datetime',
        'default_state_id': 'int'
    }

    attribute_map = {
        'description': 'description',
        'entity_type': 'entity_type',
        'project_ids': 'project_ids',
        'states': 'states',
        'name': 'name',
        'updated_at': 'updated_at',
        'auto_assign_owner': 'auto_assign_owner',
        'id': 'id',
        'team_id': 'team_id',
        'created_at': 'created_at',
        'default_state_id': 'default_state_id'
    }

    def __init__(self, description=None, entity_type=None, project_ids=None, states=None, name=None, updated_at=None, auto_assign_owner=None, id=None, team_id=None, created_at=None, default_state_id=None):  # noqa: E501
        """Workflow - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._entity_type = None
        self._project_ids = None
        self._states = None
        self._name = None
        self._updated_at = None
        self._auto_assign_owner = None
        self._id = None
        self._team_id = None
        self._created_at = None
        self._default_state_id = None
        self.discriminator = None
        self.description = description
        self.entity_type = entity_type
        self.project_ids = project_ids
        self.states = states
        self.name = name
        self.updated_at = updated_at
        self.auto_assign_owner = auto_assign_owner
        self.id = id
        self.team_id = team_id
        self.created_at = created_at
        self.default_state_id = default_state_id

    @property
    def description(self):
        """Gets the description of this Workflow.  # noqa: E501

        A description of the workflow.  # noqa: E501

        :return: The description of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workflow.

        A description of the workflow.  # noqa: E501

        :param description: The description of this Workflow.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this Workflow.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Workflow.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Workflow.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def project_ids(self):
        """Gets the project_ids of this Workflow.  # noqa: E501

        An array of IDs of projects within the Workflow.  # noqa: E501

        :return: The project_ids of this Workflow.  # noqa: E501
        :rtype: list[float]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this Workflow.

        An array of IDs of projects within the Workflow.  # noqa: E501

        :param project_ids: The project_ids of this Workflow.  # noqa: E501
        :type: list[float]
        """
        if project_ids is None:
            raise ValueError("Invalid value for `project_ids`, must not be `None`")  # noqa: E501

        self._project_ids = project_ids

    @property
    def states(self):
        """Gets the states of this Workflow.  # noqa: E501

        A map of the states in this Workflow.  # noqa: E501

        :return: The states of this Workflow.  # noqa: E501
        :rtype: list[WorkflowState]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this Workflow.

        A map of the states in this Workflow.  # noqa: E501

        :param states: The states of this Workflow.  # noqa: E501
        :type: list[WorkflowState]
        """
        if states is None:
            raise ValueError("Invalid value for `states`, must not be `None`")  # noqa: E501

        self._states = states

    @property
    def name(self):
        """Gets the name of this Workflow.  # noqa: E501

        The name of the workflow.  # noqa: E501

        :return: The name of this Workflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workflow.

        The name of the workflow.  # noqa: E501

        :param name: The name of this Workflow.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this Workflow.  # noqa: E501

        The date the Workflow was updated.  # noqa: E501

        :return: The updated_at of this Workflow.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Workflow.

        The date the Workflow was updated.  # noqa: E501

        :param updated_at: The updated_at of this Workflow.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def auto_assign_owner(self):
        """Gets the auto_assign_owner of this Workflow.  # noqa: E501

        Indicates if an owner is automatically assigned when an unowned story is started.  # noqa: E501

        :return: The auto_assign_owner of this Workflow.  # noqa: E501
        :rtype: bool
        """
        return self._auto_assign_owner

    @auto_assign_owner.setter
    def auto_assign_owner(self, auto_assign_owner):
        """Sets the auto_assign_owner of this Workflow.

        Indicates if an owner is automatically assigned when an unowned story is started.  # noqa: E501

        :param auto_assign_owner: The auto_assign_owner of this Workflow.  # noqa: E501
        :type: bool
        """
        if auto_assign_owner is None:
            raise ValueError("Invalid value for `auto_assign_owner`, must not be `None`")  # noqa: E501

        self._auto_assign_owner = auto_assign_owner

    @property
    def id(self):
        """Gets the id of this Workflow.  # noqa: E501

        The unique ID of the Workflow.  # noqa: E501

        :return: The id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workflow.

        The unique ID of the Workflow.  # noqa: E501

        :param id: The id of this Workflow.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def team_id(self):
        """Gets the team_id of this Workflow.  # noqa: E501

        The ID of the team the workflow belongs to.  # noqa: E501

        :return: The team_id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Workflow.

        The ID of the team the workflow belongs to.  # noqa: E501

        :param team_id: The team_id of this Workflow.  # noqa: E501
        :type: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def created_at(self):
        """Gets the created_at of this Workflow.  # noqa: E501

        The date the Workflow was created.  # noqa: E501

        :return: The created_at of this Workflow.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Workflow.

        The date the Workflow was created.  # noqa: E501

        :param created_at: The created_at of this Workflow.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def default_state_id(self):
        """Gets the default_state_id of this Workflow.  # noqa: E501

        The unique ID of the default state that new Stories are entered into.  # noqa: E501

        :return: The default_state_id of this Workflow.  # noqa: E501
        :rtype: int
        """
        return self._default_state_id

    @default_state_id.setter
    def default_state_id(self, default_state_id):
        """Sets the default_state_id of this Workflow.

        The unique ID of the default state that new Stories are entered into.  # noqa: E501

        :param default_state_id: The default_state_id of this Workflow.  # noqa: E501
        :type: int
        """
        if default_state_id is None:
            raise ValueError("Invalid value for `default_state_id`, must not be `None`")  # noqa: E501

        self._default_state_id = default_state_id

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
        if issubclass(Workflow, dict):
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
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other