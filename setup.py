import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="japantokyocovidage", # 設定する名前
    version="0.0.2", # バージョン設定
    author="taiki shirato", # 名前
    author_email="taikishirato4869@gmail.com", # メアド変更
    description='A package for visualization of aggregate data of players in "tokyocovidage"', # 説明文書書き換え
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s2022071/japantokyocovidage", # GitHubURL
    project_urls={
        "Bug Tracker": "https://github.com/s2022071/japantokyocovidage", #GitHubURL
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['Tokyocovidage'], # 設定するモジュール名
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'japantokyocovidage = japantokyocovidage:main' # srcの中にある.pyの手前の文字
        ]
    },
)
