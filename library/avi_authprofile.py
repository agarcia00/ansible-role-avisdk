#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: not supported
# Avi Version: 16.3
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import (ansible_return, purge_optional_fields,
    avi_obj_cmp, cleanup_absent_fields, avi_ansible_api)


EXAMPLES = '''
  - avi_authprofile:
      controller: ''
      password: ''
      username: ''
      http:
        cache_expiration_time: 5
        group_member_is_full_dn: false
      ldap:
        base_dn: dc=avi,dc=local
        bind_as_administrator: true
        port: 389
        security_mode: AUTH_LDAP_SECURE_NONE
        server:
        - 10.10.0.100
        settings:
          admin_bind_dn: user@avi.local
          group_filter: (objectClass=*)
          group_member_attribute: member
          group_member_is_full_dn: true
          group_search_dn: dc=avi,dc=local
          group_search_scope: AUTH_LDAP_SCOPE_SUBTREE
          ignore_referrals: true
          password: password
          user_id_attribute: samAccountname
          user_search_dn: dc=avi,dc=local
          user_search_scope: AUTH_LDAP_SCOPE_ONE
      name: ProdAuth
      tenant_ref: admin
      type: AUTH_PROFILE_LDAP
'''
DOCUMENTATION = '''
---
module: avi_authprofile
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: AuthProfile Configuration
description:
    - This module is used to configure AuthProfile object
    - more examples at <https://github.com/avinetworks/avi-ansible-samples>
requirements: [ avisdk ]
version_added: 2.3
options:
    controller:
        description:
            - location of the controller. Environment variable AVI_CONTROLLER is default
    username:
        description:
            - username to access the Avi. Environment variable AVI_USERNAME is default
    password:
        description:
            - password of the Avi user. Environment variable AVI_PASSWORD is default
    tenant:
        description:
            - tenant for the operations
        default: admin
    tenant_uuid:
        description:
            - tenant uuid for the operations
        default: ''
    state:
        description:
            - The state that should be applied on the entity.
        required: false
        default: present
        choices: ["absent","present"]
    description:
        description:
            - Not present.
        type: string
    http:
        description:
            - HTTP user authentication params.
        type: AuthProfileHTTPClientParams
    ldap:
        description:
            - LDAP server and directory settings.
        type: LdapAuthSettings
    name:
        description:
            - Name of the Auth Profile.
        required: true
        type: string
    tacacs_plus:
        description:
            - TACACS+ settings
        type: TacacsPlusAuthSettings
    tenant_ref:
        description:
            - Not present. object ref Tenant.
        type: string
    type:
        description:
            - Type of the Auth Profile.
        required: true
        type: string
    url:
        description:
            - url
        required: true
        type: string
    uuid:
        description:
            - UUID of the Auth Profile.
        type: string
'''

RETURN = '''
obj:
    description: AuthProfile (api/authprofile) object
    returned: success, changed
    type: dict
'''

def main():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                controller=dict(default=os.environ.get('AVI_CONTROLLER', '')),
                username=dict(default=os.environ.get('AVI_USERNAME', '')),
                password=dict(default=os.environ.get('AVI_PASSWORD', '')),
                tenant=dict(default='admin'),
                tenant_uuid=dict(default=''),
                state=dict(default='present',
                           choices=['absent', 'present']),
                description=dict(
                    type='str',
                    ),
                http=dict(
                    type='dict',
                    ),
                ldap=dict(
                    type='dict',
                    ),
                name=dict(
                    type='str',
                    ),
                tacacs_plus=dict(
                    type='dict',
                    ),
                tenant_ref=dict(
                    type='str',
                    ),
                type=dict(
                    type='str',
                    ),
                url=dict(
                    type='str',
                    ),
                uuid=dict(
                    type='str',
                    ),
                ),
        )
        return avi_ansible_api(module, 'authprofile',
                               set([]))
    except:
        raise


if __name__ == '__main__':
    main()