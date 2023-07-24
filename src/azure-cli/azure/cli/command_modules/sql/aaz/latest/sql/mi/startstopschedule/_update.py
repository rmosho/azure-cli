# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sql mi startstopschedule update",
)
class Update(AAZCommand):
    """Update the managed instance's Start/Stop schedule.

    :example: Update (override) the managed instance's start stop schedule.
        az sql mi startstopschedule update --ids resourceId --schedule-list "[{'startDay':'Monday','startTime':'10:00 AM','stopDay':'Monday','stopTime':'12:00 AM'}]"
        az sql mi startstopschedule update --mi miName -g resourceGroup --subscription subscriptionId --schedule-list "[{'startDay':'Monday','startTime':'10:00 AM','stopDay':'Monday','stopTime':'12:00 AM'}]"
    :example: Add schedule items to the managed instance's start stop schedule.
        az sql mi startstopschedule update --ids resourceId --add schedule_list "{'startDay':'Monday','startTime':'10:00 AM','stopDay':'Monday','stopTime':'12:00 AM'}"
    :example: Remove schedule items from the managed instance's start stop schedule.
        az sql mi startstopschedule update --ids resourceId --remove schedule_list index(0 based)
    """

    _aaz_info = {
        "version": "2022-11-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/startstopschedules/{}", "2022-11-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.managed_instance = AAZStrArg(
            options=["--mi", "--managed-instance"],
            help="The name of the managed instance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="The description of the schedule.",
            nullable=True,
        )
        _args_schema.schedule_list = AAZListArg(
            options=["--schedule-list"],
            arg_group="Properties",
            help="Schedule list.",
        )
        _args_schema.timezone_id = AAZStrArg(
            options=["--timezone-id"],
            arg_group="Properties",
            help="The time zone of the schedule.",
            nullable=True,
        )

        schedule_list = cls._args_schema.schedule_list
        schedule_list.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.schedule_list.Element
        _element.start_day = AAZStrArg(
            options=["start-day"],
            help="Start day.",
            enum={"Friday": "Friday", "Monday": "Monday", "Saturday": "Saturday", "Sunday": "Sunday", "Thursday": "Thursday", "Tuesday": "Tuesday", "Wednesday": "Wednesday"},
        )
        _element.start_time = AAZStrArg(
            options=["start-time"],
            help="Start time.",
        )
        _element.stop_day = AAZStrArg(
            options=["stop-day"],
            help="Stop day.",
            enum={"Friday": "Friday", "Monday": "Monday", "Saturday": "Saturday", "Sunday": "Sunday", "Thursday": "Thursday", "Tuesday": "Tuesday", "Wednesday": "Wednesday"},
        )
        _element.stop_time = AAZStrArg(
            options=["stop-time"],
            help="Stop time.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.StartStopManagedInstanceSchedulesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.StartStopManagedInstanceSchedulesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class StartStopManagedInstanceSchedulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/startStopSchedules/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_start_stop_managed_instance_schedule_read(cls._schema_on_200)

            return cls._schema_on_200

    class StartStopManagedInstanceSchedulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/startStopSchedules/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_start_stop_managed_instance_schedule_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("scheduleList", AAZListType, ".schedule_list", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("timeZoneId", AAZStrType, ".timezone_id")

            schedule_list = _builder.get(".properties.scheduleList")
            if schedule_list is not None:
                schedule_list.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.scheduleList[]")
            if _elements is not None:
                _elements.set_prop("startDay", AAZStrType, ".start_day", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("startTime", AAZStrType, ".start_time", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("stopDay", AAZStrType, ".stop_day", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("stopTime", AAZStrType, ".stop_time", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_start_stop_managed_instance_schedule_read = None

    @classmethod
    def _build_schema_start_stop_managed_instance_schedule_read(cls, _schema):
        if cls._schema_start_stop_managed_instance_schedule_read is not None:
            _schema.id = cls._schema_start_stop_managed_instance_schedule_read.id
            _schema.name = cls._schema_start_stop_managed_instance_schedule_read.name
            _schema.properties = cls._schema_start_stop_managed_instance_schedule_read.properties
            _schema.system_data = cls._schema_start_stop_managed_instance_schedule_read.system_data
            _schema.type = cls._schema_start_stop_managed_instance_schedule_read.type
            return

        cls._schema_start_stop_managed_instance_schedule_read = _schema_start_stop_managed_instance_schedule_read = AAZObjectType()

        start_stop_managed_instance_schedule_read = _schema_start_stop_managed_instance_schedule_read
        start_stop_managed_instance_schedule_read.id = AAZStrType(
            flags={"read_only": True},
        )
        start_stop_managed_instance_schedule_read.name = AAZStrType(
            flags={"read_only": True},
        )
        start_stop_managed_instance_schedule_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        start_stop_managed_instance_schedule_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        start_stop_managed_instance_schedule_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_start_stop_managed_instance_schedule_read.properties
        properties.description = AAZStrType()
        properties.next_execution_time = AAZStrType(
            serialized_name="nextExecutionTime",
            flags={"read_only": True},
        )
        properties.next_run_action = AAZStrType(
            serialized_name="nextRunAction",
            flags={"read_only": True},
        )
        properties.schedule_list = AAZListType(
            serialized_name="scheduleList",
            flags={"required": True},
        )
        properties.time_zone_id = AAZStrType(
            serialized_name="timeZoneId",
        )

        schedule_list = _schema_start_stop_managed_instance_schedule_read.properties.schedule_list
        schedule_list.Element = AAZObjectType()

        _element = _schema_start_stop_managed_instance_schedule_read.properties.schedule_list.Element
        _element.start_day = AAZStrType(
            serialized_name="startDay",
            flags={"required": True},
        )
        _element.start_time = AAZStrType(
            serialized_name="startTime",
            flags={"required": True},
        )
        _element.stop_day = AAZStrType(
            serialized_name="stopDay",
            flags={"required": True},
        )
        _element.stop_time = AAZStrType(
            serialized_name="stopTime",
            flags={"required": True},
        )

        system_data = _schema_start_stop_managed_instance_schedule_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_start_stop_managed_instance_schedule_read.id
        _schema.name = cls._schema_start_stop_managed_instance_schedule_read.name
        _schema.properties = cls._schema_start_stop_managed_instance_schedule_read.properties
        _schema.system_data = cls._schema_start_stop_managed_instance_schedule_read.system_data
        _schema.type = cls._schema_start_stop_managed_instance_schedule_read.type


__all__ = ["Update"]
