# youngtrip　后端API

## 前端项目地址
https://github.com/LizhenQiangCOOL/youngtrip

## 技术栈
Django + DRF + celery+ mysql + redis + rabbitmq

## 开发环境与部署
使用docker-compose进行单主机容器编排并部署

## 单机监控
1. docker stats [--no-stream]
2. cAdvisor  [https://github.com/google/cadvisor/tree/master/docs]

### 监控API接口
1. 主机信息　https://127.0.0.1/api/v2.0/machine
```
可调度逻辑CPU内核数
内存容量（以字节为单位）
支持的最大CPU频率（kHz）
可用文件系统：主要，次要数字和容量（以字节为单位）
网络设备：mac地址，MTU和速度（如果有）
机器拓扑：节点，核心，线程，每节点内存和缓存
```
2. 所有容器　https://127.0.0.1/api/v2.0/stats?type=docker&recursive=true
```
绝对容器名称
子容器列表
ContainerSpec，它描述了在容器中启用的资源隔离
最近N几秒钟的容器详细资源使用情况统计信息（N可在cAdvisor中全局配置）
创建容器后的资源使用情况直方图
```

3. 某个容器统计(约２分钟统计信息)　https://127.0.0.1/api/v2.0/stats/2c4dee605d22?type=docker
```
stats　资源信息
2c4dee605d22 可为容器id 或容器名称
如　youngtrip-django_web_1
```

4. 某个容器统计摘要　https://127.0.0.1/api/v2.0/summary/<container identifier>?type=docker
```
如　youngtrip-django_web_1
```

## Django安全漏洞

### CVE-2020-7471（moderate severity）
- 影响版本：>= 2.0.0, < 2.2.10
- 修复版本：2.2.10
- 描述：不受信任的数据用作StringAgg分隔符，进行SQL注入
- 代码模块：contrib.postgres.aggregates.StringAgg
```
```

###  CVE-2019-19844（moderate severity）
- 影响版本: <1.11.17, 2.0.0<= x <2.2.9, <3.0.1
- 修复版本：2.2.9
- 描述：Django密码重设表单，使用不区分大小的电子邮件名来检索重设密码用户
- 代码模块：　django.contrib.auth.forms.py 中　类PasswordResetForm　的方法get_users
```
  active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % UserModel.get_email_field_name(): email,
            'is_active': True,
        })
```
## 科普
#### 高危漏洞
1. 远程执行代码
2. SQL注入
#### 中度漏洞
1. 跨站点脚本(XSS)
2. 跨站点伪造请求(CSRF)
3. 拒接服务攻击(DDOS)
4. 身份验证缺陷
#### 低级漏洞
1. 敏感数据公开
2. 会话管理缺陷
3. 未验证的重定向/转发
4. 