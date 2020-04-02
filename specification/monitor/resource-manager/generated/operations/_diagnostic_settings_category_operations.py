# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DiagnosticSettingsCategoryOperations(object):
    """DiagnosticSettingsCategoryOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~monitor_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        resource_uri,  # type: str
        name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DiagnosticSettingsCategoryResource"
        """Gets the diagnostic settings category for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiagnosticSettingsCategoryResource or the result of cls(response)
        :rtype: ~monitor_client.models.DiagnosticSettingsCategoryResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DiagnosticSettingsCategoryResource"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DiagnosticSettingsCategoryResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories/{name}'}

    def list(
        self,
        resource_uri,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DiagnosticSettingsCategoryResourceCollection"
        """Lists the diagnostic settings categories for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiagnosticSettingsCategoryResourceCollection or the result of cls(response)
        :rtype: ~monitor_client.models.DiagnosticSettingsCategoryResourceCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DiagnosticSettingsCategoryResourceCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-01-preview"

        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DiagnosticSettingsCategoryResourceCollection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories'}