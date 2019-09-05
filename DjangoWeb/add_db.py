# -*- coding: utf-8 -*-

from django.http import HttpResponse

from Model.models import MyModel


# 数据库操作
def testdb(request):
    test1 = MyModel(name='xuguozhong')
    test1.save()

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = MyModel.objects.all()
    for l in list:
        print(l.name)

    print('filter相当于SQL中的WHERE，可设置条件过滤结果')
    res = MyModel.objects.filter(name='xuguozhong2')
    for r in res:
        print(r.name)

    print('获取单个对象')
    response3 = MyModel.objects.get(name='xugz')
    print(response3.name)

    return HttpResponse("<p>数据操作成功！</p>")
