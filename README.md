# community_ms
# 题目:基于人脸识别的小区进出管理系统
    需求:
    基于人脸识别的小区进出管理系统，需要用python来完成数据分析，需要用网站web jsp技术来表现管理信息，
    基于人脸识别是因为目前疫情环境，进出小区经常要保存用户相关信息。
    识别人脸的基本信息并且保存，如果识别人脸这一块有困难的话， 
    可以只加上小区进出人的基本信息，体温信息进行管理。

    管理系统:包含登录模块，用户管理，进出人员管理，人员类别分析几个模块，
    其中进出人员管理包含小区住户和临时进出人员两个类别，进出人员需要进行 
    进出小区时间，人员身份(工作，职位)，体温，人员姓名信息等进行管理，
    然后数据分析就是主要对人员的身份信息，体温信息进行分析(占百分比这种)。

# 功能描述：
+ 登录、注册
+ 居民身份（识别、登记）
    + 业主：姓名、年龄、住址、登记时间、工作职位、体温、电话、性别
    + 临时用户：姓名、进出事宜、登记时间、电话、性别
+ 进出记录:人员姓名、体温、通行时间、用户类型、人员编号
+ 系统管理员
+ 数据分析部分

# 数据库设计

## 数据库名
### community_manage
### create database community_manage

## 数据表名
+ 管理员表(cms_admin)
  - auto-generated definition
    create table app_cms_admin
    (
        id          bigint auto_increment
            primary key,
        name        varchar(16) not null,
        password    varchar(16) not null,
        create_time datetime(6) not null
    );

+ 小区住宅用户(cms_residents)
    - auto-generated definition
    create table app_cms_checklog
    (
        id          bigint auto_increment
            primary key,
        name        varchar(32) not null,
        user_id     int         not null,
        user_type   varchar(16) not null,
        temperature double      not null,
        sign_time   datetime(6) not null,
        matter      varchar(64) not null,
        comment     longtext    not null
    );


+ 小区外来人员(cms_migrants)
  - auto-generated definition
    create table app_cms_migrants
    (
        id       bigint auto_increment
            primary key,
        name     varchar(32) not null,
        age      int         not null,
        sex      varchar(8)  not null,
        phone    varchar(16) not null,
        log_time datetime(6) not null
    );


+ 进出记录(cms_check_log)
  - auto-generated definition
    create table app_cms_residents
    (
        id       bigint auto_increment
            primary key,
        name     varchar(32) not null,
        age      int         not null,
        sex      varchar(10) not null,
        phone    varchar(16) not null,
        address  varchar(64) not null,
        job      varchar(32) not null,
        log_time datetime(6) not null
    );

+ 数据分析部分(暂定)

核心功能模块：
+ 用户的管理
  -
  增删改查等交互操作，日常记录的维护
+ 人脸识别功能
    -
  + 摄像头窗口形状,可设置
  + 启动摄像头按钮、保存图片、结果处理页面
  + (自动转录入...)
  + 人脸识别页面逻辑
    识别人脸，当识别到得人脸没有在数据库时，弹出人员身份记录页面,
    两个按钮，一个为添加临时人员信息、另一个为添加业主信息，
    将业主信息添加完成之后
    记录face_token和user_id
    确认是否添加进出记录    
        若是，那么将face_token和user_id自动填入字段中,
    剩下的信息自行填写
    完成后确认按钮提交
    
+ 统计分析部分
    -
    剩下用户信息的update操作,
    小区进出统计数据分析部分
    
数据分析部分（饼图）
    1.进出人员体温temperature
    2.临时人员职业job，来访事宜matter，来访时间time
    
# 登录、注册
    人脸库只增不减
    
app_cms中，一些模块上传github时init.py文件没有成功上传，需要自建
# 已完结，文件只记录了部分过程
