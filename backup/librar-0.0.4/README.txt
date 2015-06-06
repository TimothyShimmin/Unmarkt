This package asissts using the command line version of rar on linux



Install this module like this:


    sudo pip install librar-0.0.x.tar.gz 


(replace x with your version)




You also need rar


On ubuntu:


    sudo aptitude install rar



Usage example


  #!/usr/bin/python

  from librar import archive

  a = archive.Archive("/home/me/testarchive1.rar") # this will be created

  a.add_file("/home/me/testfile") # testfile will be added to archive
  


  # create archive:

  a.run() 
  




You can also add directories:


  a.add_dir("/home/me/dir1") # directory and everythin below it will be added to archive



You can use add_dir and add_file multiple times and also combine them.  
