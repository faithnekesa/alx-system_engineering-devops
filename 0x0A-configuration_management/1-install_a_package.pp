#!/usr/bin/pup
# install flask 2.1.0 from pip3 with Werkzeug 2.1.1
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
