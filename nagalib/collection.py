#! /usr/bin/env python
# -*- coding:utf-8 -*-
# by Xuyuan Pang 2016-08-10 11:06:56


def flatten(iterable):
    for ele in iterable:
        if hasattr(ele, '__iter__'):
            for e in flatten(ele):
                yield e
        else:
            yield ele


def take(iterable, n):
    if n > 0:
        for ele in iterable:
            yield ele
            n -= 1
            if n == 0:
                break


def takeWhile(iterable, fn):
    for ele in iterable:
        if fn(ele):
            yield ele
        else:
            break


def drop(iterable, n):
    for ele in iterable:
        if n == 0:
            yield ele
        else:
            n -= 1


def dropWhile(iterable, fn):
    d = False
    for ele in iterable:
        if not d:
            if not fn(ele):
                yield ele
                d = True
            continue
        yield ele

