#!/bin/bash 

# # 检测有无docker 环境，没有则安装
# function docker_inst () {
#     echo "检查 docker ..."
#     docker -v 
#     if [ $? -eq 0 ];then 
#         echo "docker is installed"
#     else 
#         echo "is going to install docker..."
#         source ./docker_inst.sh 
#         echo "docker installed done"
#     fi
# }

get_distribution() {
	lsb_dist=""
	# Every system that we officially support has /etc/os-release
	if [ -r /etc/os-release ]; then
		lsb_dist="$(. /etc/os-release && echo "$ID")"
	fi
	# Returning an empty string here should be alright since the
	# case statements don't act unless you provide an actual value
	echo "$lsb_dist"
}
lsb_dist=$( get_distribution )
lsb_dist="$(echo "$lsb_dist" | tr '[:upper:]' '[:lower:]')"

case "$lsb_dist" in

    ubuntu)
        cd ./docker/ubuntu20
        sudo dpkg -i containerd.io_1.4.12-1_amd64.deb
        sudo dpkg -i docker-ce-cli_20.10.12~3-0~ubuntu-focal_amd64.deb
        sudo dpkg -i docker-ce_20.10.12~3-0~ubuntu-focal_amd64.deb
        \cp ../../docker-compose /usr/bin/
    ;;

    centos|rhel|sles)
        cd ./docker/centos7
        rpm -ivh *.rpm --force --nodeps &>/dev/null
        \cp ../../docker-compose /usr/bin/
        echo "已安装docker 版本为： " $(docker -v)
    ;;

    *)
        exit 1 
    ;;

esac

# 导入各服务部署所需要的镜像
cd ./images

DB=( emqx.tar fdfs.tar java8.tar mysql8.tar nginx.tar redis6.2.tar ubuntu20220602.tar)
for i in "${DB[@]}"
do
    echo ${i}
    docker load -i ${i}
done

# 将服务添加进 开机自动启动项
# shellDir=$(cd $(dirname $0); pwd)