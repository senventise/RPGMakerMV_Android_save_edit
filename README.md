# RPGMaker MV Android 存档修改

## Usage

### 获取文件
我个人采用的是直接从`/data/data/xxx`目录里拿（需要root），如果没有root的话可以试试能不能用`adb backup`提取出来文件，然后修改以后再复原回去，仅仅提供一下思路，没有具体试过。  
SQLite3文件位于`/data/data/YOUR_PACKAGE_NAME/app_xwalkcore/Default/Local\ Storage/file__0.localstorage`
### 导出
```shell
$ python export.py file__0.localstorage
```
导出后的存档文件将存放在`./data/`目录下，可以使用各种支持修改`xxx.rpgsave`存档的修改器进行修改。
### 还原
```shell
$ python restore.py
```
还原后的文件为`./data/file__0.localstorage`。

## More
详见[此处](https://www.senventise.com/2020/03/11/RPGMaker-Android-%E5%AD%98%E6%A1%A3%E4%BF%AE%E6%94%B9/)
