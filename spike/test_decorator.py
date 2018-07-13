#!/usr/bin/env python
# -*- coding: utf-8 -*-
user = None


def login(func):
    def wrapper(*args, **kw):
        if user is not None:
            func(*args, **kw)
        else:
            print("登录之后再才能进入home页面")
            return False

    return wrapper


def go_to_home_page():
    print(user + "进入到了home页面")


if __name__ == "__main__":
    user = "LLr"
    go_to_home_page()
    user = None
    go_to_home_page()
