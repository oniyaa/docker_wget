# wget通过docker并行下载

将要下载的文件列表放到SPLIT/, list.txt 将被分割为100行一个文件并被放到INPUT/*

```
python3 1.split.py
```

```
python3 2.build_docker.py
```

```
python3 3.docker_wget.py
```
