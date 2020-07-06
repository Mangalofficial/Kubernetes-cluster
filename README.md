# <div align="center"> Under Guidence of </div>
# <div align="center"> ░V░i░m░a░l░ ░D░a░g░a░ </div><br>
### Automation-project using Kubernetes
#### Task Description task 3
 - Create container image that’s has Jenkins installed  using dockerfile  Or You can use the Jenkins Server on RHEL 8/7
 - When we launch this image, it should automatically starts Jenkins service in the container.
 - Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 
 - Job1 : Pull  the Github repo automatically when some developers push repo to Github.
 - Job2 : 
    1. By looking at the code or program file, Jenkins should automatically start the respective language interpreter installed image container to deploy code on top of Kubernetes 
    2.  Expose your pod so that testing team could perform the testing on the pod
    3. Make the data to remain persistent ( If server collects some data like logs, other user information )
 - Job3 : Test your app if it  is working or not.
 - Job4 : If app is not working , then send email to developer with error messages and redeploy the application after code is being edited by the developer

#### Task Description task 6

##### > Perform third task with the help of Jenkins coding file ( called as jenkinsfile approach ) and perform the with following phases:

  - Create container image that’s has Jenkins installed  using dockerfile  Or You can use the Jenkins Server on RHEL 8/7
  - When we launch this image, it should automatically starts Jenkins service in the container.
  - Create a job chain of job1, job2, job3 and  job4 using build pipeline plugin in Jenkins 
  - Job2 ( Seed Job ) : Pull  the Github repo automatically when some developers push repo to Github.
    - Further on jobs should be pipeline using written code  using Groovy language by the developer
  - Job1 :  
    1. By looking at the code or program file, Jenkins should automatically start the respective language interpreter installed image container to deploy code on top of Kubernetes ( eg. If code is of  PHP, then Jenkins should start the container that has PHP already installed )
    2.  Expose your pod so that testing team could perform the testing on the pod
    3. Make the data to remain persistent using PVC ( If server collects some data like logs, other user information )
  - Job3 : Test your app if it  is working or not.
  - Job4 : if app is not working , then send email to developer with error messages and redeploy the application after code is being edited by the developer
### Everything is same for the task 6, but the difference is that it is done using jenkinsfile approach.
#### >>> ` I have made a Build Pipeline for Monitoring (task 3) :` <br><br>
<img src="images/Build Pipeline.png"><br><br>
 
- Here I've used `POLL SCM` to perform the task.
- As the developer commits the codes, Jenkins automatically triggers the jobs and do certain tasks.<br><br>
### JOB_1 : 
#### >>>`Pull  the Github repo automatically when some developers push repo to Github`<br><br>
<img src="images/job1.1.png"><img src="images/job1.2.png"><br><br>
### JOB_2 : <br>
```
1. By looking at the code or program file, Jenkins should automatically start the respective language interpreter 
   installed image container to deploy code on top of Kubernetes.
2. Expose your pod so that testing team could perform the testing on the pod
3. Make the data to remain persistent ( If server collects some data like logs, other user information )
``` 
<br><br>
<img src="images/job2.1.png"><img src="images/job2.2.png"><br><br>
### JOB_3 : 
#### >>>`Test your app if it  is working or not`<br><br>
<img src="images/job3.1.png"><img src="images/job3.2.png"><br><br>
### JOB_4 : 
#### >>>`If app is not working, then send email to developer with error messages and redeploy the application` <br> `after code is being edited by the developer`<br><br>
<img src="images/job4.1.png"><img src="images/job4.2.png"><br><br>


##### Thank You Vimal Sir for this Intresting Task
