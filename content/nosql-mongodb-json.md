Title: mongo集群 导入导出json和csv
Date: 2015-10-22 11:17:19
Category: Nosql
Tags: Linux, nosql, mongodb
Slug: nosql-mongodb-json

#### 导出数据

```
# mongodump -d test -o bak
```
#### 导入数据

```
# mongorestore -h 127.0.0.1 --port 30000 -d test  bak/test/
```
#### 导出集合为csv

```
# mongoexport -h 127.0.0.1 --port 30000 -d test -c districts --type=csv -o districts.csv -f _id,district_code,province,city,district
```
#### 导出集合为json

```
# mongoexport -h 127.0.0.1 --port 30000 -d test -c districts  -o districts.json
```
#### 导入csv或者json

```
# mongoimport -d test -c districts  --type=json --file=districts.json --upsert
```

#### 备注：以上导出数据库 test  的集合 districts，并将数据以 csv 格式导出。

- -h 表示主机IP或主机名; 
- -d 表示数据库名; 
- -c 表示集合名; 
- -f 表示所选集合的字段; 
- -o 表示导出的文件名 
- --upsert 以新增的方式导入 
- --headerline   仅适用于导入csv,tsv格式的数据，表示文件中的第一行作为数据头