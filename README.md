# metrics
Python script that show CPU and MEMORY metrics.

## Requirements
 
* python 2 or 3 version
* psutil

## Usage

python metrics.py `parameter`

### Parameter: 
 
cpu - prints CPU metrics

mem - prints Memory metrics

## Output

### python metrics.py cpu

```
system.cpu.idle 9799.67
system.cpu.user 1528.53
system.cpu.guest 0.0
system.cpu.iowait 48.78
system.cpu.stolen 0.0
system.cpu.system 646.64 
```


### python metrics.py mem

```
virtual total 8137957376
virtual used 4741726208
virtual free 199340032
virtual shared 734380032
swap total 2147479552
swap used 216006656
swap free 1931472896
```

## Usage Docker

To use script to show cpu info of host machine from docker container you need to run command:

`docker run --rm $(docker build -q .) cpu`

or for memory info

`docker run --rm $(docker build -q .) mem`

## Usage Docker-compose

If you already have installed docker-compose, you have to choose correct command inside docker-compose.yml like:

`command: cpu`

or

`command: mem`

and run container:

`docker-compose up`

* NOTE: For the first time, it takes a little bit times to build docker image
