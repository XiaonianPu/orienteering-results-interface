# orienteering-results-interface
定向运动成绩统计标准化接口
## 0 目的

- 创建易用、高效、轻量、稳定的成绩统计平台

## 1 声明
- 本开源项目仅通过读取主站CP2102 UART Bridge的原始数据(即D+/D-两个引脚)实现，不涉及任何软件反编译与硬件抄板。
- 仅在华瑞健三代产品测试成功，不保证其余版本之可用性

## 2 功能

### 2.1 赛事架构

- 位于Common包中，包含event、competition、class、entry、user、club、punch、course、control等赛事基本元素

### 2.1 成绩条打印

- 支持任意有线/无线串口打印机
- 不需要FTDI转接线，可以直接使用mini usb连接主站

### 2.2 成绩统计

- 实现了读取、解析IOF standarddata 3.0 格式xml赛事文件，该文件包括赛事的所有信息，包括检查点的图上坐标、路线分段长度、爬高量、地图比例尺等
- 实现了个人赛(Individual)的路线自动匹配，可用于训练中多条路线但未指定路线的情况
- 目前使用mysql进行成绩统计存储，可以自行修改并使用单文件的sqlite
- *[TODO]* 成绩数据导出

### 2.3 用户界面

- 偶溶解做完了 [@WaterFishJ](https://github.com/WaterFishJ)
- 有什么问题喷他就好

### 2.4 成绩分析

相对于2.2章节，成绩分析更多体现在对于竞赛数据的统计学处理，包括：

- *[TODO]* 分段计时数据分析，包括各种数据的pdf图、cdf图、直方图、散点图
- *[TODO]* 预计最佳完赛时间分析

### 2.5 网络功能

- *[TODO]* 实时成绩网络预览 - 数据库做好了，前端后端还没写

- *[TODO]* 接入微信公众号，实现成绩推送 - 有排做
- *[TODO]* 接入微信小程序，实现无PC成绩统计 - 有排做

## 3 联系方式

Xiaonian Pu：sserxiaonian@gmail.com

Rongjie Ou：1309908437@qq.com
