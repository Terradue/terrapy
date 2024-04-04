# ResourceDeletionTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**background_job_id** | **str** |  | 

## Example

```python
from openapi_client.models.resource_deletion_task import ResourceDeletionTask

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDeletionTask from a JSON string
resource_deletion_task_instance = ResourceDeletionTask.from_json(json)
# print the JSON string representation of the object
print(ResourceDeletionTask.to_json())

# convert the object into a dict
resource_deletion_task_dict = resource_deletion_task_instance.to_dict()
# create an instance of ResourceDeletionTask from a dict
resource_deletion_task_form_dict = resource_deletion_task.from_dict(resource_deletion_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


