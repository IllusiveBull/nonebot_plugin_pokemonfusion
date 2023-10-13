+ 10/13/2023 去discord找到了新的[融合计算器](https://fusioncalc.com/)
+ 10/12/2023 作者[库](https://github.com/Aegide/custom-fusion-sprites)被Github删了
+ 8/19/2023 原作者删除了raw.githubusercontent.com下所有自动生成的融合精灵导致大部分融合目前不可用
# 简介
[Pokemon Infinite Fusion](https://www.pokecommunity.com/showthread.php?t=347883) 是 Schrroms 制作的宝可梦同人游戏，游戏中你可以融合任意两只宝可梦，目前共有 $420^2=176,400$ 种组合，其中150,444种由 [Japeal](https://japeal.com/pkm/) 生成，其余45,956种由作者和超过180k官方Discord和Reddit成员设计且不断更新。本仓库基于 [Nonebot2](http://v2.nonebot.dev/) 实现了由 [SDM0](https://twitter.com/SDM_0_) 创建，[Aegide](https://github.com/Aegide) 维护的 [融合计算器](https://fusioncalc.com/) 的中文版插件。
# 安装
```pip install nonebot_plugin_pokemonfusion```
或
```nb plugin install nonebot_plugin_pokemonfusion```
# 配置
在.env中添加

```
enable_transparent = True
```

可以使机器人发送透明png（由于QQ的透明通道有bug所以不建议）
# 使用
```融合 [宝可梦A] [宝可梦B]```
参数留空则随机融合

![](/doc/1.png)
# 相关链接
作者及粉丝的原创精灵仓库 https://github.com/Aegide/custom-fusion-sprites

[Japeal](https://japeal.com/pkm/) 生成的精灵仓库 https://github.com/Aegide/autogen-fusion-sprites
