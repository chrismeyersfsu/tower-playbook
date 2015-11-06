#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(name='tower-playbook',
      version='0.0.1',
      description='Debug Ansible playbooks in Tower',
      author='Chris Meyers',
      author_email='cmeyers@ansible.com',
      install_requires=['PyYAML', 'requests'],
      url='https://ansible.com',
      scripts=[
          'bin/tower-playbook',
      ],
      data_files=[
          (os.path.join(sys.prefix, 'playbooks'), ['playbooks/*']),
      ],
)

