#!/bin/bash

my_dir=$(cd $(dirname $0) && pwd)

# ==========================================================================================
# bootadmin
# ==========================================================================================

mkdir -p $my_dir/{{cookiecutter.package_name}}/apps/common/static/bootadmin/{css,js,webfonts}

cd $my_dir/{{cookiecutter.package_name}}/apps/common/static/bootadmin/css
ln -s ../../../../../../vendor/bootadmin/css/bootadmin.min.css
ln -s ../../../../../../vendor/bootadmin/css/bootstrap.min.css
ln -s ../../../../../../vendor/bootadmin/css/fontawesome-all.min.css

cd $my_dir/{{cookiecutter.package_name}}/apps/common/static/bootadmin/js
ln -s ../../../../../../vendor/bootadmin/js/bootadmin.min.js
ln -s ../../../../../../vendor/bootadmin/js/bootstrap.bundle.min.js
ln -s ../../../../../../vendor/bootadmin/js/jquery.min.js

cd $my_dir/{{cookiecutter.package_name}}/apps/common/static/bootadmin/webfonts
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-brands-400.eot
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-brands-400.svg
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-brands-400.ttf
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-brands-400.woff
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-brands-400.woff2
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-regular-400.eot
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-regular-400.svg
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-regular-400.ttf
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-regular-400.woff
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-regular-400.woff2
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-solid-900.eot
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-solid-900.svg
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-solid-900.ttf
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-solid-900.woff
ln -s ../../../../../../vendor/bootadmin/webfonts/fa-solid-900.woff2
