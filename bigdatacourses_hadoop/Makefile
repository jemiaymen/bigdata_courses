DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
current_branch = hadoop-3.2.2
build:
	docker build -t jemiaymen/hadoop:$(current_branch) ./base
	docker build -t jemiaymen/namenode:$(current_branch) ./namenode
	docker build -t jemiaymen/datanode:$(current_branch) ./datanode
	docker build -t jemiaymen/resourcemanager:$(current_branch) ./resourcemanager
	docker build -t jemiaymen/nodemanager:$(current_branch) ./nodemanager
	docker build -t jemiaymen/historyserver:$(current_branch) ./historyserver
