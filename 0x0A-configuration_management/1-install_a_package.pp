# install flask from pip3 using Puppet

package { 'python-pip': ensure=>present }

exec { 'install_flask':
    command=> '/usr/bin/pip3 install Flask==2.1.0',
    path=> ['/usr/bin']
    require=> package['python3-pip'],
}