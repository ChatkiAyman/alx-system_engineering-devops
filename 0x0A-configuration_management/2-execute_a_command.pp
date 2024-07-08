#kill process

exec {'pkill':
command => 'pkill killmenow',
path    => ['bin','/usr/bin'],
}
