# ansible2
New repository for my Ansible roles

*WARNING* I run Centos7 on all my servers, and my roles reflect this for simplicity.
Running a different OS likely means you'll run into problems. ex - The repos role
pulls down the "el7" repos for Enterprise Linux

I've gotten better with Ansible, and scripting, and wanted to redo a lot of functionality. A lot of previous roles didn't consistently abstract the data through templates, making them pretty useless.
Rather then fix my git repo (lukepafford-ansible), I'm just pushing everything to this new one. 

Feel free to use any roles in here if they look like something you need. I'm going to try and make sure each role has a *readme* specifying what variables need to be provided
