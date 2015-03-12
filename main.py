#!/usr/bin/python
#coding:utf8
#author shengaofeng@gmail.com

#import xml.etree.ElementTree as ET
import copy
from lxml import etree
import os
import lxml.html.soupparser as soupparser

NCX_OUTPUT = 'out.ncx'
OPF_OUTPUT = 'out.opf'

tree = etree.parse('lxb.opf')
root = tree.getroot()

book_info = {
    "title":"none",
    "author":"none",
    "date":"none",
    "type":"none",
    "language":"zh-cn",
    }

book = root.find("./main:metadata/main:dc-metadata",
                    namespaces = dict(main = "http://www.idpf.org/2007/opf"))
for x in book:
    if x.text:
        x.text = etree.CDATA(x.text.format(**book_info))

items = root.find("./main:manifest",
                  namespaces = dict(main = "http://www.idpf.org/2007/opf"))

files = [ x for x in os.listdir(".") if x.endswith(".html") and  x.startswith("chap") ]
files.sort()
ids = []
for f in files:
    zz = etree.SubElement(items,'{%s}item' % ("http://www.idpf.org/2007/opf"), 
                          nsmap={None: "http://www.idpf.org/2007/opf"})
    zz.set("id",f.split(".")[0])
    ids.append(f.split(".")[0])
    zz.set("href",f)
    zz.set("media-type","application/xhtml+xml")

spine = root.find("./main:spine", 
                  namespaces = dict(main = "http://www.idpf.org/2007/opf"))

for i in ids:
    zz = etree.SubElement(spine,'{%s}itemref' % ("http://www.idpf.org/2007/opf"), nsmap={None: "http://www.idpf.org/2007/opf"})
    zz.set("idref", i)

tree.write(OPF_OUTPUT)

tree = etree.parse('toc.ncx')
root = tree.getroot()
titles = []
files.insert(0 , "preface.html")
items = root.find("./ns:navMap", namespaces = dict(ns = "http://www.daisy.org/z3986/2005/ncx/"))
for f in files:
    mytree = soupparser.parse(f)
    try:
        titles.append(mytree.xpath('.//h4/text()')[0])
    except:
        titles.append("null")

count = 1
for title in titles:
#    print title[:20]
    zz = etree.SubElement(items,'{%s}navPoint' % ("http://www.daisy.org/z3986/2005/ncx/"), nsmap={None: "http://www.daisy.org/z3986/2005/ncx/"})
    zz.set("id","navPoint-" + str(count))
    zz.set("playOrder",str(count))
    ff = etree.SubElement(zz,'{%s}navLabel' % ("http://www.daisy.org/z3986/2005/ncx/"), nsmap={None: "http://www.daisy.org/z3986/2005/ncx/"})
    text = etree.SubElement(ff,'{%s}text' % ("http://www.daisy.org/z3986/2005/ncx/"), nsmap={None: "http://www.daisy.org/z3986/2005/ncx/"})
    text.text = etree.CDATA(title)
    content = etree.SubElement(ff,'{%s}content' % ("http://www.daisy.org/z3986/2005/ncx/"), nsmap={None: "http://www.daisy.org/z3986/2005/ncx/"})
    content.set("src",files[count - 1])
    count += 1

tree.write(NCX_OUTPUT,  encoding='utf-8')
