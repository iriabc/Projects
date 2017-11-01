# EARTHQUAKES

This project downloads seismic data from the earthquake.usgs.gov database for a certain period. The data is converted and stored into a MySQL database and it allows to query it.

It also plots the data for the locations, depths and magnitudes on a map.


## Getting Started

Please follow these instructions to have a copy of the project on your local machine.


### Prerequisites

Download the package manager Anaconda for Python2.7.

Download mySQL


## Some useful commands

Activate Anaconda environment

```
source activate <env_name>
```

Open mySQL database:

```
/usr/bin/mysql -u root -p
```

Create database:

```
CREATE DATABASE <DB_NAME>
```

List all tables:

```
SHOW TABLES;
```