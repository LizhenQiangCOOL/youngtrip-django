# youngtrip　后端API

## 技术栈
Django + DRF + celery+ mysql + redis + rabbitmq

## 开发环境与部署
使用docker-compose进行单主机容器编排并部署

## 单机监控
1. docker stats [--no-stream]
2. cAdvisor  [https://github.com/google/cadvisor/tree/master/docs]

### 监控API接口
1. 主机信息　https://cadv.xn--m83a.top/api/v2.0/machine
```
可调度逻辑CPU内核数
内存容量（以字节为单位）
支持的最大CPU频率（kHz）
可用文件系统：主要，次要数字和容量（以字节为单位）
网络设备：mac地址，MTU和速度（如果有）
机器拓扑：节点，核心，线程，每节点内存和缓存
```
2. 所有容器　https://cadv.xn--m83a.top/api/v2.0/stats?type=docker&recursive=true
```
绝对容器名称
子容器列表
ContainerSpec，它描述了在容器中启用的资源隔离
最近N几秒钟的容器详细资源使用情况统计信息（N可在cAdvisor中全局配置）
创建容器后的资源使用情况直方图
```

3. 某个容器统计(约２分钟统计信息)　https://cadv.xn--m83a.top/api/v2.0/stats/2c4dee605d22?type=docker
```
stats　资源信息
2c4dee605d22 可为容器id 或容器名称
如　youngtrip-django_web_1
```

4. 某个容器统计摘要　https://cadv.xn--m83a.top/api/v2.0/summary/<container identifier>?type=docker
```
如　youngtrip-django_web_1
```