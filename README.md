# Bayou
A prototype for replicated, eventually consistent storage system design implemented using bi-directional streaming on gRPC, restful services using flask-restful and in-memory storage on redis



## Link to research paper on which the prototype is based
http://www.scs.stanford.edu/17au-cs244b/sched/readings/bayou.pdf


## Usage

#### Dependencies

参考`requirements.txt`

目前版本在我电脑上可以运行Server和Client

后端需要一个Redis数据库，默认端口6379

#### Configs
Check config.yaml to see/set configuration for clients and severs

#### Create proto files
 ```
 python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. a_e.proto
 ```
 
 #### Start server nodes (one terminal per server)
 
 ```shell
 python server.py one
 python server.py two
 python server.py three
 ```
 
 #### Start clients (one terminal per user)
 
 ```shell
 python client.py vish
 python client.py priyal
 ```
 
## Screenshots of usage
  ##### 1. Start server nodes
  
 
 ![](./output/1.%20Starting%20servers.png)



  ##### 2. Start client and book a room
 
 
 ![](./output/2.%20Sending%20request%20through%20client.png)
 
 
 
  ##### 3. Anti-entropy between server nodes:
  
  
   ![](./output/3.%20Anti%20entropy%20between%20servers.png)




