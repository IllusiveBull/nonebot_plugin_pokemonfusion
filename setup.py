import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
  long_description = fh.read()

setuptools.setup(
  name="nonebot_plugin_pokemonfusion",
  version="1.0.0",
  author="IllusiveBull",
  author_email="xjn233@gmail.com",
  description="Nonebot2的Pokemon Infinite Fusion中文版融合计算器插件",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/IllusiveBull/nonebot_plugin_pokemonfusion",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)