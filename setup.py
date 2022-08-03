#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    thepoy
# @Email:     thepoy@163.com
# @File Name: setup.py
# @Created:   2022-03-31 09:43:35
# @Modified:  2022-08-03 09:58:55

import codecs

from setuptools import setup


with codecs.open("README.md", "r", "utf-8") as fd:
    setup(
        name="types-jieba",
        version="0.0.4",
        description="""
        jieba 类型库
        """,
        long_description_content_type="text/markdown",
        long_description=fd.read(),
        author="thepoy",
        author_email="thepoy@163.com",
        url="https://github.com/thep0y/types-jieba",
        license="MIT",
        keywords="jieba 中文 分词 类型",
        packages=["jieba-stubs"],
        package_data={
            "jieba-stubs": [
                "__init__.pyi",
                "_compat.pyi",
                "analyse/__init__.pyi",
                "analyse/textrank.pyi",
                "analyse/tfidf.pyi",
                "posseg/__init__.pyi",
                "posseg/char_state_tab.pyi",
                "posseg/prob_emit.pyi",
                "posseg/prob_start.pyi",
                "posseg/prob_trans.pyi",
                "posseg/viterbi.pyi",
            ]
        },
    )
