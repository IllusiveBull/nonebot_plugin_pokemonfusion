import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
  long_description = fh.read()
requirements = [r.strip() for r in open("requirements.txt", 'r', encoding='utf-8').readlines()]

setuptools.setup(
  name="nonebot_plugin_pokemonfusion",
  version="1.0.6",
  author="IllusiveBull",
  author_email="xjn233@gmail.com",
  description="Nonebot2的Pokemon Infinite Fusion中文版融合计算器插件",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/IllusiveBull/nonebot_plugin_pokemonfusion",
  include_package_data = True,
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=requirements,    
  package_data = {"nonebot_plugin_pokemonfusion":["nonebot_plugin_pokemonfusion/resources/pokemons.json"]},
)