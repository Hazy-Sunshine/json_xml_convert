#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import xmltodict
import json
import sys


def pythonConversionXml2Json(pa):
    """
        demo Python conversion between xml and json
    """
    # 1.Xml to Json

    f = open(pa)
    xml_str = f.read()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    converted_dict = xmltodict.parse(xml_str, encoding='utf-8')
    # print converted_dict
    # print (converted_dict)
    json_str = json.dumps(converted_dict, indent=1)  # indent设置输出格式
    out = open(pa+".json", 'w+')
    print type(json_str)
    print >>out, json_str.decode('utf-8')


def python_conversion_json_2_xml(pa):
    """Json to Xml"""
    f = open(pa)
    json_str = f.read()

    decode_json = json.loads(json_str)

    print len(decode_json)
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # print >>out2,json.dumps(decode_json, encoding="utf-8", ensure_ascii=False)

    converted_xml = xmltodict.unparse(decode_json)

    out = open(pa+".xml", 'w+')
    print >>out, converted_xml
    
# pythonConversionXml2Json('result.json.xml')
python_conversion_json_2_xml('xiaoyi.json')
