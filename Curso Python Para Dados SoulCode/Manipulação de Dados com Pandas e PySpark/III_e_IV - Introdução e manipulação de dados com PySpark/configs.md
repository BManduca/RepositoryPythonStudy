sudo apt update -y
sudo apt install default-jdk -y
wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz

tar -xvzf spark-*

sudo mv spark-3.5.1-bin-haddop3/ /opt/spark/

echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile

source ~/.profile

start-master.sh

start-worker.sh spark://NT0478:7077

spark-shell
