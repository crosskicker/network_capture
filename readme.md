# Network Capture

## Overview

Network supervision project for our own machine to visualize the transport protocol used.

### Requirements

`pip3 install -r requirements.txt`

OR

`pip3 install pandas`

`pip3 install scapy`

`pip3 install matplotlib`

`pip3 install pyspark`

### Virtual environnement

Create

`python3 -m venv myvenv`

Activate

`source <myvenv>/bin/activate`

Desactivate

`deactivate`

## RUN

Run the main.py to create the csv file (to collect data) to finish => ^C

`python3 main.py`  to finish => ^C

Run spark_graph.py visualize which type of packets are circulating each secondto visualize which kind of packets are traveling for each second.

`python3 spark_graph.py`

Run the graph.py to visualize the numbers of packet since the beginning

`python3 graph.py`
