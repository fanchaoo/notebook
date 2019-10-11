
# mysql

docker pull mysql:5.7

docker run -p 3306:3306 --name mymysql -v /Users/icourt/software/dockermysql/conf:/etc/mysql/conf.d -v/Users/icourt/software/dockermysql/data:/var/lib/mysql -v /Users/icourt/software/dockermysql/logs:/logs -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7


# 安装man

yum install -y man