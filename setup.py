import setuptools

setuptools.setup(
  name="nonebot_plugin_pokemonfusion",
  version="1.1.0",
  author="IllusiveBull",
  author_email="xjn233@gmail.com",
  description="Nonebot2的Pokemon Infinite Fusion中文版融合计算器插件",
  url="https://github.com/IllusiveBull/nonebot_plugin_pokemonfusion",
  include_package_data = True,
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=["httpx","nonebot2>=2.0.0rc2","Pillow","nonebot-adapter-onebot"],
  package_data = {"nonebot_plugin_pokemonfusion":["nonebot_plugin_pokemonfusion/resources/pokemons.json"]},
)