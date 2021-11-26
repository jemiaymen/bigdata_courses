# Module 6 HDFS 

## Install Hadoop in Windows OS

### Required tools

* (7zip) => to unzip hadoop binary package.
* (Java JDK) => JDK is required to run Hadoop as the framework is built using java 
* (Hadoop binary package) => we must download hadoop binary package from https://hadoop.apache.org/
* (Hadoop native IO binary) => Hadoop on linux includes optional Native IO support. However Native IO is mandatory on Windows and without it you will not be able to get installation working. Download all the files in the following location https://github.com/cdarlint/winutils/tree/master/hadoop-VERSION/bin
### Installation Steps
we try to install hadoop version '3.3.1'.
we use a sample paths like (C:\sdk) for java SDK and (C:\hadoop) for hadoop, we chould first create those folders.

1. Install java SDK with double click on jdk-8u311-windows-x64.exe chose a sample path like (C:\sdk) we use it for the next steps.
2. unzip hadoop-3.3.1.tar.gz to a sample path like (C:\hadoop) we use it for the next steps.
3. copy hadoop native IO binary to (C:\hadoop\bin).
4. copy all files from (etc) folder to (C:\hadoop\etc\hadoop).
5. configure environement variable [JAVA_HOME = C:\sdk], [HADOOP_HOME = C:\hadoop] and update PATH add [C:\jdk\bin;C:\hadoop\bin] we can use powershell commands
``` powershell
SETX JAVA_HOME "C:\jdk"
SETX HADOOP_HOME "C:\hadoop"
SETX PATH "$env:PATH;C:\jdk\bin;C:\hadoop\bin"
```
or manually just open Environment Variables.
6. initialise HDFS namenode with command
``` bash
hdfs namenode -format
```
7. start HDFS daemons open terminal and run
``` powershell
%HADOOP_HOME%\sbin\start-dfs.cmd
```
8. start YARN daemons open terminal and run
``` powershell
%HADOOP_HOME%\sbin\start-yarn.cmd
```
9. check namenode open your browser and open http://localhost:9870/dfshealth.html#tab-overview

## TP
If every thing allright so we can do some exercices.

We have two command 'hadoop fs \<arg>' and 'hdfs dfs \<arg>'.

The 'fs' term refers to a generic file system, which by the definition can point to ANY file system ( including HDFS), but dfs is very specific. On the other hand, 'DFS' refers precisely to Hadoop Distributed File System access. So when we use FS it can perform operation related to local or hadoop distributed file system and dfs can perform operation related to hadoop distributed file system only.

1. [hadoop fs \<args>] It is used when we are dealing with different file systems such as Local FS,  HDFS etc.
2. [hdfs dfs \<args>] It is used when we are dealing for operations related to HDFS.

### Exercice 1 
1. create hdfs /input/data folder
2. test if hdfs /input/data folder is created
3. create file.txt in hdfs folder /input/data
4. create file1.txt in hdfs folder /input/data
5. list all file in hdfs folder /input/data


### Exercice 2 (Local Storage to HDFS)
1. create local file firsthdfs.txt and copy to hdfs folder /input/data

2. copy firsthdfs.txt file to /input/data with other command
3. list all file in /input/data
4. delete /input/data/firsthdfs.txt
5. list all file in /input/data


### Exercice 3 (HDFS to Local Storage )

1. copy /input/data/file.txt to local storage and rename it to olddata.txt
2. move to local storage /input/data/file1.txt
3. check your local storage and hdfs folder /input/data
4. repeate exercice 1 with other command

### Exercice 4 
1. copy olddata.txt from hdfs /input/data/ to hdfs /input/ex2/data.txt
2. move /input/data/file1.txt to hdfs folder /input/ex2/data2.txt
3. show /input/ex2/data2.txt content

4. delete hdfs /input/data folder and /input/ex2
5. list all folder in /input


### Exercice 5

1. check the health of the files in hdfs /input/data folder
2. create empty file (empty) with size 0 byte in hdfs folder /input/data
3. check if the file is 0 byte or not
4. create file (test.txt) in /input/data if not exist
5. update hdfs file (/input/data/empty) with 'this is me'
6. show (/input/data/empty) content without -cat command
7. show stat about hdfs (/input/data/empty) 

``` bash
# formats stat command
%b –    file size in bytes
%g –    group name of owner
%n –    file name
%o –    block size
%r  –    replication
%u –    user name of owner
%y –    modification date
```

### Exercice 6
1. find hdfs file (empty) and print the result
2. count all files in hdfs (/input/data)
3. merge all files in hdfs (/input/data ) and copy to local storage alldata.txt
4. change mod for hdfs (/input/data/emtpy) file to read only
