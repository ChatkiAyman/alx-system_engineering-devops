# File: /etc/puppetlabs/code/environments/production/manifests/site.pp

node default {
  class { 'nginx':
    manage_repo  => true,
    package_name => 'nginx',
    service_name => 'nginx',
    config_file  => '/etc/nginx/nginx.conf',
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx/nginx.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/nginx.conf'],
  }
}

# File: /etc/puppetlabs/code/environments/production/modules/nginx/templates/nginx.conf.erb

worker_processes auto;
events {
    worker_connections 1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
