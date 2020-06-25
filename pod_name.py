open_file=open('/var/lib/jenkins/workspace/JOB2_task3/pod.py','r')
read=open_file.read()
for a in read:
    if a.isupper() == True:
        pass
    else:
       print(a,end='')
