## tower-playbook
Development tool to help with Ansible -> Tower transition.

### Features
* Sync directory to tower project
* Launch Job Template
* Stream Ansible output to console
* Ctrl+C support

### TODO
* `-e` support
* command-line playbook specification
* 'Smart' creation of Manual Project & Job Template

### Maybe TODO
* Import inventory Ansible -> Tower

## Configure
`tower-playbook` expects a inventory group named `tower` with one host and 3 variables. Below is an example to be placed in `/etc/ansible/hosts`

### Expected variables
```
tower_url
tower_user
tower_pass
```

### Example tower group
```
[tower]
tower.example.com ansible_ssh_user=user_with_root_or_awx tower_url="https://tower.example.com" tower_user="admin" tower_pass="password"
```
