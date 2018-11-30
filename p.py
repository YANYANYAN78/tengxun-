# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # with open('../yuguang.ttl', 'r+') as f:
# #     content = f.readlines()
# #     print(content[22592])
# #     content[22592]='<http://dsc.nlp-bigdatalab.org:8086/一代宗师止痛透骨膏周期装>	<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>	<http://dsc.nlp-bigdatalab.org:8086/药品> .\n'
# #
# # ff=open('../yuguang.ttl','w+')
# # ff.writelines(content)
#
#
# from py2neo import Node, Relationship, Graph
# from pandas import DataFrame
# import json
#
# # a = Node('Person', name='Alice')
# #
# # b = Node('Person', name='Bob')
# #
# # r = Relationship(a, 'KNOWS', b)
# #
# # s = a | b | r
#
# graph = Graph(password='123')
# with open('category.json', 'r',encoding='utf-8') as f:
#     content = f.readline()
#     # print(content)
#     l=json.loads(content)
#     # print(len(l))
#     diseases=[]
#     discategorys=[]
#     rels_category = []
#     for i in l:
#         if 'diseases' in i:
#             dis_l = i['diseases']
#             for j in dis_l:
#                 if 'name' in j:
#                     disease = j['name']
#                     diseases.append(disease)
#                 if "discategorys" in j:
#                     discategorys += j['discategorys']
#                     for n in j['discategorys']:
#                         rels_category.append([disease,n])
#
# #创建疾病的节点
# for d in set(diseases):
#     node_d = Node('疾病', name=d)
#     graph.merge(node_d)
#
# #创建分类的节点
# for c in set(discategorys):
#     node_c = Node('分类', name=c)
#     graph.merge(node_c)
#
# #创建疾病和分类的关系
# set_edges = []
# for rel in rels_category:
#     set_edges.append('###'.join(rel))
# for edge in set(set_edges):
#     edge = edge.split('###')
#     p = edge[0]
#     q = edge[1]
#     query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
#         '疾病', '分类', p, q, '所属分类')
#     try:
#         graph.run(query)
#     except Exception as e:
#         print(e)

# [ {"name":"12","op_icon_focus":"","op_icon_unfocus":"","diseases":[{"name":"1型糖尿病","type":1,"released":1,"discategorys":["慢性病","内分泌科","全身"],"source":0},
#             {"name":"2型糖尿病","type":1,"released":1,"discategorys":["慢性病","内分泌科","老年科","全身"],"source":0}],"released":0},
#   {"name":"A","op_icon_focus":"","op_icon_unfocus":"",
#       "diseases":[{"name":"阿尔茨海默病","type":1,"released":1,"discategorys":["慢性病","神经内科","精神心理科","老年科","头部"],"source":0},
#                  {"name":"埃博拉病毒感染","type":0,"released":1,"discategorys":["传染病","感染科","全身"],"source":1},
#                {"name":"爱迪生氏病","type":0,"released":0,"discategorys":["慢性病","内分泌科","全身"],"source":1},
#                {"name":"矮小症","type":0,"released":0,"discategorys":["慢性病","儿科","内分泌科","全身"],"source":0},
#                {"name":"癌性疼痛","type":0,"released":1,"discategorys":["肿瘤","肿瘤科","全身"],"source":1},
#                {"name":"癌症","type":5,"released":1,"discategorys":["肿瘤","肿瘤科","全身"],"source":1},
#                {"name":"艾滋病","type":1,"released":1,"discategorys":["慢性病","皮肤性病科","全身"],"source":0},
#                {"name":"阿斯伯格综合征","type":0,"released":1,"discategorys":["其它种类","精神心理科","精神"],"source":1}],"released":0},
#  {"name":"B","op_icon_focus":"","op_icon_unfocus":"",
#         "diseases":[{"name":"白癜风","type":1,"released":1,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"白喉","type":1,"released":1,"discategorys":["传染病","儿科","感染科","颈部"],"source":0},
#                     {"name":"白化病","type":1,"released":1,"discategorys":["先天疾病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"白内障","type":1,"released":1,"discategorys":["慢性病","眼科","头部"],"source":0},
#                     {"name":"百日咳","type":1,"released":1,"discategorys":["传染病","呼吸内科","胸部"],"source":0},
#                     {"name":"白塞氏病","type":0,"released":0,"discategorys":["慢性病","风湿免疫科","全身"],"source":0},
#                     {"name":"白塞综合征","type":1,"released":1,"discategorys":["慢性病","风湿免疫科","全身"],"source":0},
#                      {"name":"白血病","type":0,"released":1,"discategorys":["肿瘤","肿瘤科","血液科","血液"],"source":1},
#                     {"name":"瘢痕疙瘩","type":0,"released":0,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"斑秃","type":0,"released":1,"discategorys":["慢性病","皮肤性病科","头部"],"source":1},
#                     {"name":"半月板撕裂","type":0,"released":1,"discategorys":["其它种类","运动医学科","四肢"],"source":1},
#                     {"name":"半月板损伤","type":0,"released":1,"discategorys":["其它种类","骨科","骨骼"],"source":1},
#                     {"name":"暴发型肝炎","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"包茎","type":0,"released":1,"discategorys":["其它种类","泌尿外科","会阴部"],"source":0},
#                     {"name":"包皮龟头炎","type":1,"released":1,"discategorys":["其它种类","泌尿外科","会阴部"],"source":0},
#                     {"name":"包皮过长","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"暴食症","type":0,"released":1,"discategorys":["其它种类","精神心理科","精神"],"source":0},
#                     {"name":"巴氏腺囊肿","type":0,"released":1,"discategorys":["慢性病","妇科","会阴部"],"source":1},
#                     {"name":"背部问题和损伤","type":3,"released":1,"discategorys":[],"source":1},
#                     {"name":"贝尔麻痹","type":0,"released":1,"discategorys":["慢性病","神经内科","头部"],"source":0},
#                     {"name":"贝克囊肿","type":0,"released":1,"discategorys":["慢性病","骨科","四肢"],"source":1},
#                     {"name":"苯丙酮尿症","type":0,"released":0,"discategorys":["先天疾病","儿科","营养科","全身"],"source":0},
#                     {"name":"便秘","type":1,"released":1,"discategorys":["慢性病","消化内科","肛肠外科","腹部"],"source":0},
#                     {"name":"扁平足","type":0,"released":0,"discategorys":["慢性病","普外科","四肢"],"source":0},
#                     {"name":"扁桃体炎","type":0,"released":1,"discategorys":["急性病","耳鼻喉科","颈部"],"source":0},
#                     {"name":"扁桃体周围脓肿","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"边缘型人格障碍","type":0,"released":1,"discategorys":["慢性病","精神心理科","精神"],"source":1},
#                     {"name":"鼻出血","type":0,"released":1,"discategorys":["急性病","耳鼻喉科","头部"],"source":1},
#                     {"name":"臂丛神经损伤","type":0,"released":0,"discategorys":["急性病","神经外科","四肢"],"source":0},
#                     {"name":"鼻窦炎","type":1,"released":1,"discategorys":["慢性病","耳鼻喉科","头部"],"source":0},
#                     {"name":"鼻骨折","type":0,"released":1,"discategorys":["急性病","骨科","头部"],"source":1},
#                     {"name":"贲门失弛缓症","type":0,"released":0,"discategorys":["慢性病","消化内科","腹部"],"source":0},
#                     {"name":"鼻内异物","type":0,"released":1,"discategorys":["急性病","耳鼻喉科","头部"],"source":1},
#                     {"name":"病态窦房结综合征","type":0,"released":1,"discategorys":["急性病","心血管内科","胸部"],"source":1},
#                     {"name":"髌骨骨折","type":0,"released":0,"discategorys":["急性病","骨科","骨骼"],"source":0},
#                     {"name":"丙型肝炎","type":1,"released":1,"discategorys":["传染病","感染科","消化内科","腹部"],"source":0},
#                     {"name":"鼻前庭炎","type":0,"released":0,"discategorys":["慢性病","耳鼻喉科","头部"],"source":0},
#                     {"name":"鼻外伤","type":3,"released":1,"discategorys":[],"source":1},
#                     {"name":"鼻息肉","type":1,"released":1,"discategorys":["慢性病","耳鼻喉科","头部"],"source":0},
#                     {"name":"避孕","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"鼻中隔偏曲","type":0,"released":1,"discategorys":["慢性病","耳鼻喉科","头部"],"source":0},
#                     {"name":"玻璃体混浊","type":0,"released":1,"discategorys":["慢性病","眼科","头部"],"source":0},
#                     {"name":"玻璃体积血","type":0,"released":1,"discategorys":["慢性病","眼科","头部"],"source":0},
#                     {"name":"勃起功能障碍","type":1,"released":1,"discategorys":["慢性病","男科","会阴部"],"source":0},
#                     {"name":"不宁腿综合征","type":0,"released":1,"discategorys":["慢性病","神经内科","头部"],"source":0},
#                     {"name":"布氏杆菌病","type":1,"released":1,"discategorys":["传染病","感染科","全身"],"source":0},
#                     {"name":"不孕不育","type":1,"released":1,"discategorys":["其它种类","妇科","男科","会阴部"],"source":0}],"released":0},
# {"name":"C","op_icon_focus":"","op_icon_unfocus":"",
#         "diseases":[{"name":"餐后血糖","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"擦伤","type":3,"released":1,"discategorys":[],"source":1},
#                     {"name":"肠梗阻","type":0,"released":1,"discategorys":["急性病","普外科","腹部"],"source":1},
#                     {"name":"肠痉挛","type":0,"released":0,"discategorys":["急性病","消化内科","急诊科","腹部"],"source":0},
#                     {"name":"肠套叠","type":0,"released":0,"discategorys":["急性病","儿科","急诊科","肛肠外科","腹部"],"source":0},
#                     {"name":"肠易激综合征","type":0,"released":1,"discategorys":["慢性病","消化内科","腹部"],"source":0},
#                     {"name":"产后甲状腺炎","type":1,"released":1,"discategorys":["慢性病","内分泌科","颈部"],"source":0},
#                     {"name":"产后抑郁症","type":0,"released":1,"discategorys":["慢性病","产科","妇科","精神心理科","精神"],"source":0},
#                     {"name":"尘肺病","type":0,"released":1,"discategorys":["慢性病","呼吸内科","胸部"],"source":0},
#                     {"name":"成人腹泻","type":0,"released":1,"discategorys":["其它种类","消化内科","腹部"],"source":0},
#                     {"name":"痴呆","type":0,"released":1,"discategorys":["慢性病","神经内科","头部"],"source":0},
#                     {"name":"尺神经损伤","type":0,"released":0,"discategorys":["其它种类","骨科","神经外科","四肢"],"source":0},
#                     {"name":"抽动症","type":0,"released":1,"discategorys":["慢性病","儿科","精神心理科","头部"],"source":0},
#                     {"name":"臭汗症","type":0,"released":1,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"创伤后应激障碍","type":0,"released":1,"discategorys":["慢性病","精神心理科","头部"],"source":0},
#                     {"name":"创伤性关节炎","type":1,"released":1,"discategorys":["其它种类","骨科","四肢"],"source":0},
#                     {"name":"川崎病","type":0,"released":1,"discategorys":["急性病","儿科","全身"],"source":0},
#                     {"name":"传染性单核细胞增多症","type":1,"released":1,"discategorys":["传染病","感染科","全身"],"source":0},
#                     {"name":"传染性红斑","type":0,"released":1,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"垂体瘤","type":0,"released":1,"discategorys":["肿瘤","神经外科","头部"],"source":0},
#                     {"name":"唇腭裂","type":0,"released":1,"discategorys":["先天疾病","儿科","口腔科","头部"],"source":0},
#                     {"name":"唇裂","type":0,"released":1,"discategorys":["先天疾病","口腔科","头部"],"source":0},
#                     {"name":"唇疱疹","type":0,"released":1,"discategorys":["传染病","皮肤性病科","头部"],"source":1},
#                     {"name":"出血热","type":1,"released":1,"discategorys":["传染病","感染科","全身"],"source":0},
#                     {"name":"刺伤","type":0,"released":1,"discategorys":["急性病","普外科","全身"],"source":1},
#                     {"name":"丛集性头痛","type":0,"released":1,"discategorys":["慢性病","神经内科","头部"],"source":0},
#                     {"name":"痤疮","type":1,"released":1,"discategorys":["慢性病","头部"],"source":0},
#                     {"name":"错牙合","type":1,"released":1,"discategorys":["慢性病","口腔科","头部"],"source":0},
#                     {"name":"卒中","type":1,"released":1,"discategorys":["急性病","康复科","急诊科","神经内科","神经外科","头部"],"source":0}],"released":0},
# {"name":"D","op_icon_focus":"","op_icon_unfocus":"",
#         "diseases":[{"name":"大肠杆菌感染","type":0,"released":1,"discategorys":["传染病","感染科","全身"],"source":1},
#                     {"name":"打鼾","type":0,"released":1,"discategorys":["慢性病","呼吸内科","头部"],"source":0},
#                     {"name":"带状疱疹","type":0,"released":1,"discategorys":["传染病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"单纯疱疹","type":0,"released":1,"discategorys":["传染病","皮肤性病科","全身"],"source":0},
#                     {"name":"单纯性甲状腺肿","type":0,"released":1,"discategorys":["慢性病","内分泌科","颈部"],"source":0},
#                     {"name":"胆道闭锁","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"丹毒","type":0,"released":1,"discategorys":["急性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"胆固醇","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"单核细胞增多症","type":0,"released":1,"discategorys":["传染病","儿科","感染科","头部"],"source":0},
#                     {"name":"胆结石","type":1,"released":1,"discategorys":["慢性病","普外科","消化内科","肝胆外科","腹部"],"source":0},
#                     {"name":"胆囊息肉","type":1,"released":1,"discategorys":["慢性病","普外科","消化内科","肝胆外科","腹部"],"source":0},
#                     {"name":"胆囊炎","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"大疱性类天疱疮","type":0,"released":1,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"登革热","type":0,"released":1,"discategorys":["传染病","感染科","全身"],"source":0},
#                     {"name":"电风暴","type":0,"released":1,"discategorys":["慢性病","心脏外科","胸部"],"source":1},
#                     {"name":"癫痫","type":1,"released":1,"discategorys":["慢性病","急诊科","神经内科","神经外科","头部"],"source":0},
#                     {"name":"癫痫发作","type":0,"released":1,"discategorys":["急性病","神经内科","精神"],"source":1},
#                     {"name":"滴虫病","type":0,"released":1,"discategorys":["传染病","妇科","会阴部"],"source":1},
#                     {"name":"地图样舌","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"低温暴露","type":3,"released":1,"discategorys":[],"source":1},
#                     {"name":"低血糖","type":0,"released":1,"discategorys":["急性病","内分泌科","全身"],"source":0},
#                     {"name":"低血压","type":0,"released":1,"discategorys":["急性病","心血管内科","全身"],"source":0},
#                     {"name":"地中海贫血","type":0,"released":1,"discategorys":["慢性病","血液科","血液"],"source":0},
#                     {"name":"doctor","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"动脉粥样硬化","type":0,"released":1,"discategorys":["慢性病","心血管内科","全身"],"source":0},
#                     {"name":"动物或人咬伤","type":3,"released":1,"discategorys":[],"source":1},
#                     {"name":"窦性静止","type":0,"released":1,"discategorys":["慢性病","心脏外科","胸部"],"source":1},
#                     {"name":"窦性心动过缓","type":0,"released":1,"discategorys":["慢性病","心血管内科","胸部"],"source":0},
#                     {"name":"窦性心动过速","type":0,"released":1,"discategorys":["急性病","心血管内科","胸部"],"source":1},
#                     {"name":"短暂性脑缺血发作","type":0,"released":1,"discategorys":["急性病","急诊科","神经内科","头部"],"source":0},
#                     {"name":"多动症","type":0,"released":1,"discategorys":["慢性病","儿科","精神心理科","精神"],"source":0},
#                     {"name":"多发性骨髓瘤","type":1,"released":1,"discategorys":["慢性病","血液科","血液"],"source":0},
#                     {"name":"多发性肌炎","type":1,"released":1,"discategorys":["慢性病","神经内科","全身"],"source":0},
#                     {"name":"多发性硬化","type":0,"released":1,"discategorys":["慢性病","神经内科","全身"],"source":0},
#                     {"name":"多汗症","type":0,"released":1,"discategorys":["慢性病","皮肤性病科","皮肤"],"source":0},
#                     {"name":"多毛症","type":0,"released":0,"discategorys":[],"source":0},
#                     {"name":"多囊卵巢综合征","type":1,"released":1,"discategorys":["慢性病","内分泌科","妇科","会阴部"],"source":0},
#                     {"name":"多囊肾","type":1,"released":1,"discategorys":["其它种类","肾内科","腹部"],"source":0},
#
# graph.create(s)

# data = graph.data('MATCH (p:Person) return p')

# print(data)

# df = DataFrame(data)

# print(df)

# coding: utf-8

from py2neo import Node, Relationship, Graph
from pandas import DataFrame
import json
import codecs


graph = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="123")

with codecs.open('json39_tq.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    # content = ''.join()
    # print(contents[0:2])
    # c=''
    # for line in contents:
    #     # line = line.strip()
    #     c+=line

    # print(type(c))
    # print(c[0:10])
    l = json.loads(contents)
    # print(type(l))
    # print(l[0])
    # print('++++++++++++++++++++++')
    print(len(l))
    print(l[1995])

