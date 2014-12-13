from setuptools import setup

setup(
    name = "translator",
    packages = ["translator"],
    version = "0.0.8",
    entry_points = {"console_scripts": ['gtranslate = translator.shellscript:main']},
    install_requires = ["beautifulsoup4>=4.0"],
    description = "Translate text using google translate",
    author = "Kaiyin Zhong",
    author_email = "kindlychung@gmail.com",
    url = "https://github.com/kindlychung/translator",
    keywords = ["gmail", "email"]
    )

