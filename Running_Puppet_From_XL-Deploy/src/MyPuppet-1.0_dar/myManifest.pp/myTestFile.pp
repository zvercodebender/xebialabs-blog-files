# /root/examples/file-1.pp

file {'testfile':
   path    => '/tmp/testfile',
   ensure  => present,
   mode    => 0640,
   content => "hello, {{petName}}.  How are you?",
}

