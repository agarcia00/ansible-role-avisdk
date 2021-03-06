#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_image
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of Image Avi RESTful Object
description:
    - This module is used to configure Image object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.7"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete"]
        type: str
    controller_info:
        description:
            - Controller package details.
            - Field introduced in 18.2.6.
        type: dict
    controller_patch_name:
        description:
            - Mandatory controller patch name that is applied along with this base image.
            - Field introduced in 18.2.10.
        type: str
    controller_patch_uuid:
        description:
            - It references the controller-patch associated with the uber image.
            - Field introduced in 18.2.8.
        type: str
    migrations:
        description:
            - This field describes the api migration related information.
            - Field introduced in 18.2.6.
        type: dict
    name:
        description:
            - Name of the image.
            - Field introduced in 18.2.6.
        required: true
        type: str
    se_info:
        description:
            - Se package details.
            - Field introduced in 18.2.6.
        type: dict
    se_patch_name:
        description:
            - Mandatory serviceengine patch name that is applied along with this base image.
            - Field introduced in 18.2.10.
        type: str
    se_patch_uuid:
        description:
            - It references the service engine patch associated with the uber image.
            - Field introduced in 18.2.8.
        type: str
    status:
        description:
            - Status to check if the image is present.
            - Enum options - SYSERR_SUCCESS, SYSERR_FAILURE, SYSERR_OUT_OF_MEMORY, SYSERR_NO_ENT, SYSERR_INVAL, SYSERR_ACCESS, SYSERR_FAULT, SYSERR_IO,
            - SYSERR_TIMEOUT, SYSERR_NOT_SUPPORTED, SYSERR_NOT_READY, SYSERR_UPGRADE_IN_PROGRESS, SYSERR_WARM_START_IN_PROGRESS, SYSERR_TRY_AGAIN,
            - SYSERR_NOT_UPGRADING, SYSERR_PENDING, SYSERR_EVENT_GEN_FAILURE, SYSERR_CONFIG_PARAM_MISSING, SYSERR_BAD_REQUEST, SYSERR_TEST1...
            - Field introduced in 18.2.6.
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
        type: str
    type:
        description:
            - Type of the image patch/system.
            - Enum options - IMAGE_TYPE_PATCH, IMAGE_TYPE_SYSTEM.
            - Field introduced in 18.2.6.
        type: str
    uber_bundle:
        description:
            - Status to check if the image is an uber bundle.
            - Field introduced in 18.2.8.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the image.
            - Field introduced in 18.2.6.
        type: str


extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create Image object
  avi_image:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_image
"""

RETURN = '''
obj:
    description: Image (api/image) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        controller_info=dict(type='dict',),
        controller_patch_name=dict(type='str',),
        controller_patch_uuid=dict(type='str',),
        migrations=dict(type='dict',),
        name=dict(type='str', required=True),
        se_info=dict(type='dict',),
        se_patch_name=dict(type='str',),
        se_patch_uuid=dict(type='str',),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        uber_bundle=dict(type='bool',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'image',
                           set([]))


if __name__ == '__main__':
    main()
