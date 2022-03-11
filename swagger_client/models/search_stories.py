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

class SearchStories(object):
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
        'archived': 'bool',
        'owner_id': 'str',
        'story_type': 'str',
        'epic_ids': 'list[int]',
        'project_ids': 'list[int]',
        'updated_at_end': 'datetime',
        'completed_at_end': 'datetime',
        'workflow_state_types': 'list[str]',
        'deadline_end': 'datetime',
        'created_at_start': 'datetime',
        'epic_id': 'int',
        'label_name': 'str',
        'requested_by_id': 'str',
        'iteration_id': 'int',
        'label_ids': 'list[int]',
        'group_id': 'str',
        'workflow_state_id': 'int',
        'iteration_ids': 'list[int]',
        'created_at_end': 'datetime',
        'deadline_start': 'datetime',
        'group_ids': 'list[str]',
        'owner_ids': 'list[str]',
        'external_id': 'str',
        'includes_description': 'bool',
        'estimate': 'int',
        'project_id': 'int',
        'completed_at_start': 'datetime',
        'updated_at_start': 'datetime'
    }

    attribute_map = {
        'archived': 'archived',
        'owner_id': 'owner_id',
        'story_type': 'story_type',
        'epic_ids': 'epic_ids',
        'project_ids': 'project_ids',
        'updated_at_end': 'updated_at_end',
        'completed_at_end': 'completed_at_end',
        'workflow_state_types': 'workflow_state_types',
        'deadline_end': 'deadline_end',
        'created_at_start': 'created_at_start',
        'epic_id': 'epic_id',
        'label_name': 'label_name',
        'requested_by_id': 'requested_by_id',
        'iteration_id': 'iteration_id',
        'label_ids': 'label_ids',
        'group_id': 'group_id',
        'workflow_state_id': 'workflow_state_id',
        'iteration_ids': 'iteration_ids',
        'created_at_end': 'created_at_end',
        'deadline_start': 'deadline_start',
        'group_ids': 'group_ids',
        'owner_ids': 'owner_ids',
        'external_id': 'external_id',
        'includes_description': 'includes_description',
        'estimate': 'estimate',
        'project_id': 'project_id',
        'completed_at_start': 'completed_at_start',
        'updated_at_start': 'updated_at_start'
    }

    def __init__(self, archived=None, owner_id=None, story_type=None, epic_ids=None, project_ids=None, updated_at_end=None, completed_at_end=None, workflow_state_types=None, deadline_end=None, created_at_start=None, epic_id=None, label_name=None, requested_by_id=None, iteration_id=None, label_ids=None, group_id=None, workflow_state_id=None, iteration_ids=None, created_at_end=None, deadline_start=None, group_ids=None, owner_ids=None, external_id=None, includes_description=None, estimate=None, project_id=None, completed_at_start=None, updated_at_start=None):  # noqa: E501
        """SearchStories - a model defined in Swagger"""  # noqa: E501
        self._archived = None
        self._owner_id = None
        self._story_type = None
        self._epic_ids = None
        self._project_ids = None
        self._updated_at_end = None
        self._completed_at_end = None
        self._workflow_state_types = None
        self._deadline_end = None
        self._created_at_start = None
        self._epic_id = None
        self._label_name = None
        self._requested_by_id = None
        self._iteration_id = None
        self._label_ids = None
        self._group_id = None
        self._workflow_state_id = None
        self._iteration_ids = None
        self._created_at_end = None
        self._deadline_start = None
        self._group_ids = None
        self._owner_ids = None
        self._external_id = None
        self._includes_description = None
        self._estimate = None
        self._project_id = None
        self._completed_at_start = None
        self._updated_at_start = None
        self.discriminator = None
        if archived is not None:
            self.archived = archived
        if owner_id is not None:
            self.owner_id = owner_id
        if story_type is not None:
            self.story_type = story_type
        if epic_ids is not None:
            self.epic_ids = epic_ids
        if project_ids is not None:
            self.project_ids = project_ids
        if updated_at_end is not None:
            self.updated_at_end = updated_at_end
        if completed_at_end is not None:
            self.completed_at_end = completed_at_end
        if workflow_state_types is not None:
            self.workflow_state_types = workflow_state_types
        if deadline_end is not None:
            self.deadline_end = deadline_end
        if created_at_start is not None:
            self.created_at_start = created_at_start
        if epic_id is not None:
            self.epic_id = epic_id
        if label_name is not None:
            self.label_name = label_name
        if requested_by_id is not None:
            self.requested_by_id = requested_by_id
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if label_ids is not None:
            self.label_ids = label_ids
        if group_id is not None:
            self.group_id = group_id
        if workflow_state_id is not None:
            self.workflow_state_id = workflow_state_id
        if iteration_ids is not None:
            self.iteration_ids = iteration_ids
        if created_at_end is not None:
            self.created_at_end = created_at_end
        if deadline_start is not None:
            self.deadline_start = deadline_start
        if group_ids is not None:
            self.group_ids = group_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if external_id is not None:
            self.external_id = external_id
        if includes_description is not None:
            self.includes_description = includes_description
        if estimate is not None:
            self.estimate = estimate
        if project_id is not None:
            self.project_id = project_id
        if completed_at_start is not None:
            self.completed_at_start = completed_at_start
        if updated_at_start is not None:
            self.updated_at_start = updated_at_start

    @property
    def archived(self):
        """Gets the archived of this SearchStories.  # noqa: E501

        A true/false boolean indicating whether the Story is in archived state.  # noqa: E501

        :return: The archived of this SearchStories.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SearchStories.

        A true/false boolean indicating whether the Story is in archived state.  # noqa: E501

        :param archived: The archived of this SearchStories.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def owner_id(self):
        """Gets the owner_id of this SearchStories.  # noqa: E501

        An array of UUIDs for any Users who may be Owners of the Stories.  # noqa: E501

        :return: The owner_id of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this SearchStories.

        An array of UUIDs for any Users who may be Owners of the Stories.  # noqa: E501

        :param owner_id: The owner_id of this SearchStories.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def story_type(self):
        """Gets the story_type of this SearchStories.  # noqa: E501

        The type of Stories that you want returned.  # noqa: E501

        :return: The story_type of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._story_type

    @story_type.setter
    def story_type(self, story_type):
        """Sets the story_type of this SearchStories.

        The type of Stories that you want returned.  # noqa: E501

        :param story_type: The story_type of this SearchStories.  # noqa: E501
        :type: str
        """
        allowed_values = ["feature", "chore", "bug"]  # noqa: E501
        if story_type not in allowed_values:
            raise ValueError(
                "Invalid value for `story_type` ({0}), must be one of {1}"  # noqa: E501
                .format(story_type, allowed_values)
            )

        self._story_type = story_type

    @property
    def epic_ids(self):
        """Gets the epic_ids of this SearchStories.  # noqa: E501

        The Epic IDs that may be associated with the Stories.  # noqa: E501

        :return: The epic_ids of this SearchStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._epic_ids

    @epic_ids.setter
    def epic_ids(self, epic_ids):
        """Sets the epic_ids of this SearchStories.

        The Epic IDs that may be associated with the Stories.  # noqa: E501

        :param epic_ids: The epic_ids of this SearchStories.  # noqa: E501
        :type: list[int]
        """

        self._epic_ids = epic_ids

    @property
    def project_ids(self):
        """Gets the project_ids of this SearchStories.  # noqa: E501

        The IDs for the Projects the Stories may be assigned to.  # noqa: E501

        :return: The project_ids of this SearchStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this SearchStories.

        The IDs for the Projects the Stories may be assigned to.  # noqa: E501

        :param project_ids: The project_ids of this SearchStories.  # noqa: E501
        :type: list[int]
        """

        self._project_ids = project_ids

    @property
    def updated_at_end(self):
        """Gets the updated_at_end of this SearchStories.  # noqa: E501

        Stories should have been updated before this date.  # noqa: E501

        :return: The updated_at_end of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_end

    @updated_at_end.setter
    def updated_at_end(self, updated_at_end):
        """Sets the updated_at_end of this SearchStories.

        Stories should have been updated before this date.  # noqa: E501

        :param updated_at_end: The updated_at_end of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._updated_at_end = updated_at_end

    @property
    def completed_at_end(self):
        """Gets the completed_at_end of this SearchStories.  # noqa: E501

        Stories should have been completed before this date.  # noqa: E501

        :return: The completed_at_end of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at_end

    @completed_at_end.setter
    def completed_at_end(self, completed_at_end):
        """Sets the completed_at_end of this SearchStories.

        Stories should have been completed before this date.  # noqa: E501

        :param completed_at_end: The completed_at_end of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._completed_at_end = completed_at_end

    @property
    def workflow_state_types(self):
        """Gets the workflow_state_types of this SearchStories.  # noqa: E501

        The type of Workflow State the Stories may be in.  # noqa: E501

        :return: The workflow_state_types of this SearchStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._workflow_state_types

    @workflow_state_types.setter
    def workflow_state_types(self, workflow_state_types):
        """Sets the workflow_state_types of this SearchStories.

        The type of Workflow State the Stories may be in.  # noqa: E501

        :param workflow_state_types: The workflow_state_types of this SearchStories.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["started", "unstarted", "done"]  # noqa: E501
        if not set(workflow_state_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `workflow_state_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(workflow_state_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._workflow_state_types = workflow_state_types

    @property
    def deadline_end(self):
        """Gets the deadline_end of this SearchStories.  # noqa: E501

        Stories should have a deadline before this date.  # noqa: E501

        :return: The deadline_end of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline_end

    @deadline_end.setter
    def deadline_end(self, deadline_end):
        """Sets the deadline_end of this SearchStories.

        Stories should have a deadline before this date.  # noqa: E501

        :param deadline_end: The deadline_end of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._deadline_end = deadline_end

    @property
    def created_at_start(self):
        """Gets the created_at_start of this SearchStories.  # noqa: E501

        Stories should have been created after this date.  # noqa: E501

        :return: The created_at_start of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_start

    @created_at_start.setter
    def created_at_start(self, created_at_start):
        """Sets the created_at_start of this SearchStories.

        Stories should have been created after this date.  # noqa: E501

        :param created_at_start: The created_at_start of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._created_at_start = created_at_start

    @property
    def epic_id(self):
        """Gets the epic_id of this SearchStories.  # noqa: E501

        The Epic IDs that may be associated with the Stories.  # noqa: E501

        :return: The epic_id of this SearchStories.  # noqa: E501
        :rtype: int
        """
        return self._epic_id

    @epic_id.setter
    def epic_id(self, epic_id):
        """Sets the epic_id of this SearchStories.

        The Epic IDs that may be associated with the Stories.  # noqa: E501

        :param epic_id: The epic_id of this SearchStories.  # noqa: E501
        :type: int
        """

        self._epic_id = epic_id

    @property
    def label_name(self):
        """Gets the label_name of this SearchStories.  # noqa: E501

        The name of any associated Labels.  # noqa: E501

        :return: The label_name of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this SearchStories.

        The name of any associated Labels.  # noqa: E501

        :param label_name: The label_name of this SearchStories.  # noqa: E501
        :type: str
        """

        self._label_name = label_name

    @property
    def requested_by_id(self):
        """Gets the requested_by_id of this SearchStories.  # noqa: E501

        The UUID of any Users who may have requested the Stories.  # noqa: E501

        :return: The requested_by_id of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._requested_by_id

    @requested_by_id.setter
    def requested_by_id(self, requested_by_id):
        """Sets the requested_by_id of this SearchStories.

        The UUID of any Users who may have requested the Stories.  # noqa: E501

        :param requested_by_id: The requested_by_id of this SearchStories.  # noqa: E501
        :type: str
        """

        self._requested_by_id = requested_by_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this SearchStories.  # noqa: E501

        The Iteration ID that may be associated with the Stories.  # noqa: E501

        :return: The iteration_id of this SearchStories.  # noqa: E501
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this SearchStories.

        The Iteration ID that may be associated with the Stories.  # noqa: E501

        :param iteration_id: The iteration_id of this SearchStories.  # noqa: E501
        :type: int
        """

        self._iteration_id = iteration_id

    @property
    def label_ids(self):
        """Gets the label_ids of this SearchStories.  # noqa: E501

        The Label IDs that may be associated with the Stories.  # noqa: E501

        :return: The label_ids of this SearchStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this SearchStories.

        The Label IDs that may be associated with the Stories.  # noqa: E501

        :param label_ids: The label_ids of this SearchStories.  # noqa: E501
        :type: list[int]
        """

        self._label_ids = label_ids

    @property
    def group_id(self):
        """Gets the group_id of this SearchStories.  # noqa: E501

        The Group ID that is associated with the Stories  # noqa: E501

        :return: The group_id of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this SearchStories.

        The Group ID that is associated with the Stories  # noqa: E501

        :param group_id: The group_id of this SearchStories.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def workflow_state_id(self):
        """Gets the workflow_state_id of this SearchStories.  # noqa: E501

        The unique IDs of the specific Workflow States that the Stories should be in.  # noqa: E501

        :return: The workflow_state_id of this SearchStories.  # noqa: E501
        :rtype: int
        """
        return self._workflow_state_id

    @workflow_state_id.setter
    def workflow_state_id(self, workflow_state_id):
        """Sets the workflow_state_id of this SearchStories.

        The unique IDs of the specific Workflow States that the Stories should be in.  # noqa: E501

        :param workflow_state_id: The workflow_state_id of this SearchStories.  # noqa: E501
        :type: int
        """

        self._workflow_state_id = workflow_state_id

    @property
    def iteration_ids(self):
        """Gets the iteration_ids of this SearchStories.  # noqa: E501

        The Iteration IDs that may be associated with the Stories.  # noqa: E501

        :return: The iteration_ids of this SearchStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._iteration_ids

    @iteration_ids.setter
    def iteration_ids(self, iteration_ids):
        """Sets the iteration_ids of this SearchStories.

        The Iteration IDs that may be associated with the Stories.  # noqa: E501

        :param iteration_ids: The iteration_ids of this SearchStories.  # noqa: E501
        :type: list[int]
        """

        self._iteration_ids = iteration_ids

    @property
    def created_at_end(self):
        """Gets the created_at_end of this SearchStories.  # noqa: E501

        Stories should have been created before this date.  # noqa: E501

        :return: The created_at_end of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_end

    @created_at_end.setter
    def created_at_end(self, created_at_end):
        """Sets the created_at_end of this SearchStories.

        Stories should have been created before this date.  # noqa: E501

        :param created_at_end: The created_at_end of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._created_at_end = created_at_end

    @property
    def deadline_start(self):
        """Gets the deadline_start of this SearchStories.  # noqa: E501

        Stories should have a deadline after this date.  # noqa: E501

        :return: The deadline_start of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline_start

    @deadline_start.setter
    def deadline_start(self, deadline_start):
        """Sets the deadline_start of this SearchStories.

        Stories should have a deadline after this date.  # noqa: E501

        :param deadline_start: The deadline_start of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._deadline_start = deadline_start

    @property
    def group_ids(self):
        """Gets the group_ids of this SearchStories.  # noqa: E501

        The Group IDs that are associated with the Stories  # noqa: E501

        :return: The group_ids of this SearchStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this SearchStories.

        The Group IDs that are associated with the Stories  # noqa: E501

        :param group_ids: The group_ids of this SearchStories.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this SearchStories.  # noqa: E501

        An array of UUIDs for any Users who may be Owners of the Stories.  # noqa: E501

        :return: The owner_ids of this SearchStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this SearchStories.

        An array of UUIDs for any Users who may be Owners of the Stories.  # noqa: E501

        :param owner_ids: The owner_ids of this SearchStories.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

    @property
    def external_id(self):
        """Gets the external_id of this SearchStories.  # noqa: E501

        An ID or URL that references an external resource. Useful during imports.  # noqa: E501

        :return: The external_id of this SearchStories.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SearchStories.

        An ID or URL that references an external resource. Useful during imports.  # noqa: E501

        :param external_id: The external_id of this SearchStories.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def includes_description(self):
        """Gets the includes_description of this SearchStories.  # noqa: E501

        Whether to include the story description in the response.  # noqa: E501

        :return: The includes_description of this SearchStories.  # noqa: E501
        :rtype: bool
        """
        return self._includes_description

    @includes_description.setter
    def includes_description(self, includes_description):
        """Sets the includes_description of this SearchStories.

        Whether to include the story description in the response.  # noqa: E501

        :param includes_description: The includes_description of this SearchStories.  # noqa: E501
        :type: bool
        """

        self._includes_description = includes_description

    @property
    def estimate(self):
        """Gets the estimate of this SearchStories.  # noqa: E501

        The number of estimate points associate with the Stories.  # noqa: E501

        :return: The estimate of this SearchStories.  # noqa: E501
        :rtype: int
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this SearchStories.

        The number of estimate points associate with the Stories.  # noqa: E501

        :param estimate: The estimate of this SearchStories.  # noqa: E501
        :type: int
        """

        self._estimate = estimate

    @property
    def project_id(self):
        """Gets the project_id of this SearchStories.  # noqa: E501

        The IDs for the Projects the Stories may be assigned to.  # noqa: E501

        :return: The project_id of this SearchStories.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchStories.

        The IDs for the Projects the Stories may be assigned to.  # noqa: E501

        :param project_id: The project_id of this SearchStories.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def completed_at_start(self):
        """Gets the completed_at_start of this SearchStories.  # noqa: E501

        Stories should have been completed after this date.  # noqa: E501

        :return: The completed_at_start of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at_start

    @completed_at_start.setter
    def completed_at_start(self, completed_at_start):
        """Sets the completed_at_start of this SearchStories.

        Stories should have been completed after this date.  # noqa: E501

        :param completed_at_start: The completed_at_start of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._completed_at_start = completed_at_start

    @property
    def updated_at_start(self):
        """Gets the updated_at_start of this SearchStories.  # noqa: E501

        Stories should have been updated after this date.  # noqa: E501

        :return: The updated_at_start of this SearchStories.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_start

    @updated_at_start.setter
    def updated_at_start(self, updated_at_start):
        """Sets the updated_at_start of this SearchStories.

        Stories should have been updated after this date.  # noqa: E501

        :param updated_at_start: The updated_at_start of this SearchStories.  # noqa: E501
        :type: datetime
        """

        self._updated_at_start = updated_at_start

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
        if issubclass(SearchStories, dict):
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
        if not isinstance(other, SearchStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
