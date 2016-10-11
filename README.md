# avinetworks.avisdk
[![Build Status](https://travis-ci.org/avinetworks/ansible-role-avisdk.svg?branch=master)](https://travis-ci.org/avinetworks/ansible-role-avisdk)

Using this role, you will be able to use the latest version, and version specific Avi Ansible Modules.

## Requirements

This role requires Ansible 2.0 or higher. Requirements are listed in the metadata file.

## Role Variables

Available variables listed below, for default values (see `defaults/main.yml`)

    version: 16.3b5 # default is 'latest'


## Example Playbook

The following example is generic, applies to any module.

```
    ---
    - hosts: localhost
      connection: local
      roles:
        - role: avinetworks.avisdk
          version: 16.3b5
      tasks:
        - avi_<module_name>:
          controller: 10.10.27.90
          username: admin
          password: AviNetworks123!
          ......
```

This example shows usage of the avi_healthmonitor module included in this role.

```
    ---
    - hosts: localhost
      connection: local
      roles:
        - role: avinetworks.avisdk
      tasks:
        - avi_healthmonitor:
            controller: 10.10.27.90
            username: admin
            password: AviNetworks123!
            https_monitor:
              http_request: HEAD / HTTP/1.0
              http_response_code:
                - HTTP_2XX
                - HTTP_3XX
            receive_timeout: 4
            failed_checks: 3
            send_interval: 10
            successful_checks: 3
            type: HEALTH_MONITOR_HTTPS
            name: MyWebsite-HTTPS
```

There are many more examples located at [https://github.com/avinetworks/avi-ansible-samples](https://github.com/avinetworks/avi-ansible-samples) and also available in the "EXAMPLES" within each module.

## License

BSD

## Author Information

Eric Anderson
[Avi Networks](http://avinetworks.com)
