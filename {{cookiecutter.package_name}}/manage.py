#!/usr/bin/env python3
#
#
#

if __name__ == '__main__':
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.package_name}}.settings.development')

    from {{cookiecutter.package_name}}.cli import main
    main()
