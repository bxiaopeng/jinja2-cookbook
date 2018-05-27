# -*- coding:utf-8 -*-

"""
<Description> (test_set.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Created by bixiaofan <wirelessqa@163.com> on 2018/5/27 at 上午11:46
"""

from jinja2 import Template


def test_set_namespace():
    """
    问题描述：
    如何在 Jinja2 中通过 set 设置全局变量？

    解决方案：
    在 set 变量时，使用 namespace 可设置全局变量.

    举个例子：
    判断我的两个朋友是否有车，规则是：只要有一个人有车，就算我的朋友有车。

    参考资料：http://serverascode.com/2018/03/15/jinja2-namespaces.html
    """
    friends = []

    xiaoming = {
        "name": "小明",
        "car": False
    }
    lili = {
        "name": "丽丽",
        "car": True
    }

    friends.append(xiaoming)
    friends.append(lili)

    template_code_set_namespace = """
    {% set has_car = namespace(value=false) %} {# 设置全局变量 #}
    
    {% for f in friends %}
        {% if f.car %}
            我的朋友「{{ f.name }}」有车 
            {% set has_car.value = true %} {# 设置全局变量 #}
        {% else %}
            我的朋友「{{ f.name }}」没车             
        {% endif %}
    {% endfor %} {# for n in friends #}
    
    结论是：
    {% if has_car.value %}  {# 获取全局变量 #}
        我的朋友有车
    {% else %}
        我的朋友没车
    {% endif %}
    """

    # 跟局部变量对比一下
    template_code_set = """
        {% set has_car = false %} {# 设置变量 #}

        {% for f in friends %}
            {% if f.car %}
                我的朋友「{{ f.name }}」有车 
                {% set has_car = true %} {# 设置局部变量 #}
            {% else %}
                我的朋友「{{ f.name }}」没车             
            {% endif %}
        {% endfor %} {# for n in friends #}

        结论是：
        {% if has_car %}  {# 获取全局变量 #}
            我的朋友有车
        {% else %}
            我的朋友没车
        {% endif %}
        """

    render_set_namespace = Template(template_code_set_namespace, trim_blocks=True).render(friends=friends)
    render_set = Template(template_code_set, trim_blocks=True).render(friends=friends)

    print(render_set_namespace)
    print("-------------------------分隔线-------------------------")
    print(render_set)
