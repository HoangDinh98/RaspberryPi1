*Hot Key:
	+ F4: Open Terminal in Current Folder

* Set up proxy: 
	+ Open Terminal
	+ Type sudo chmod 777 ect/apt
	+ Create file name apt.conf
	+ Add Acquire::http::Proxy "http://192.168.101.253:3128"; in apt.conf
	+ Run sudo apt-get update
