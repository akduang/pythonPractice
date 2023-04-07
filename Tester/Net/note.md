# 存储工具

This is a file with a top-level heading
session和cookie的区别
前后端交互

http协议如何保证数据在传输过程中不丢失
七层，握手挥手机制

请求头  accept、accept
验证身份

cookie和session

b/s架构

cookie 客户端，可以伪造，存储在本地，用户看不见
session 服务器 数据库-->一般redis
session 过期时间  redis自动管理过期时间

服务器生成cookie，发给客户端。验证

cookie在客户端的头信息中
seesion在服务端存储

session验证需要cookie带一个字段，禁用cookie就没法用

osi网络分层
应用层 为应用程序提供服务
表示层 数据格式化及加密操作
会话层 建立，管理和维护会话
传输层 建立，管理和维护端到端的连接   tcp、udp
网络层 ip地址及路由选择              ip、icmp
数据链路层 提供介质访问和链路管理      arp、rarp
物理层 物理层，即物理设备             mlt-3，pam5

eg
老张向老王提供了一份货物清单及价格清单
怕别的竞争对手公司看到给清单做了加密
市场部整理后将报价清单放到收发室
收发室将报价清单送到快递公司
快递公司分发到不同的集散中心
运输路线的规划及各集散中心访问方式
通过汽车火车飞机等设备进行运输

五层就是应用层包含三层
应用层 协议 http、https，ftp、smtp
  应用层
  表示层
  会话层
