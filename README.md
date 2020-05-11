基于Docker+Python对git项目自动提交
### 使用场景
#### 第一个使用场景
自己本地有几个私有库，如`hexo`、`资料记载`等...这些个私有库有事没事就需要`push`更改，所以需要自动提交
#### 第二个使用场景
`home-assistant`安装在树莓派上，但是对于`home-assistant`的配置文件希望用`git`管理起来

### 使用
以上两个使用场景其实都是需要外挂盘符来操作的，接下来编写`docker-compose.yml`文件
```
version: '2'
services:
  git-auto-push:
    image: jakehu/git-auto-push:latest
    container_name: git-auto-push
    restart: always
    volumes:
      - /Web/项目1:/opt/Web/项目1
      - /Web/项目2:/opt/Web/项目2
      - /Web/项目3:/opt/Web/项目3
      - /you_dir/.ssh/:/root/.ssh/
```
`/opt/Web/`勿修改，程序会自动读取`/opt/Web/`下一级目录作为需要监听的项目，`.ssh`挂载进去主要是不用单独去配置`ssh key`

启动：`docker-compose up -d`