# django-ktag
[![GitHub version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://pypi.org/project/django-ktag/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20V3-blue.svg)](https://github.com/gojuukaze/django-ktag/blob/master/LICENSE)


django tag input field

![alt tag](https://github.com/gojuukaze/django-ktag/blob/master/demo.gif?raw=true)

# 引用项目
* js,css 代码使用了 [tagify](https://github.com/yairEO/tagify/blob/master/README.md)

# 依赖

* python3+
* django 2.0+

# 文档
+ [安装](#安装)
+ [使用](#使用)
  - [快速开始](#快速开始)
  - [在Model与Admin使用](#在model与admin使用)
+ [参数表](#参数表)
+ [Example](#example)



# 安装
* 下载
```shell
pip install django-ktag
or
pip install --index-url https://pypi.org/simple/ django-ktag 
```

* 把 'ktag' 加到 `INSTALLED_APPS`中

```python
INSTALLED_APPS = [
    ...
    'ktag',
]
```
* 确定 TEMPLATES 中 `APP_DIRS` 为 True

```python
TEMPLATES = [
    ...
    'APP_DIRS': True,
    ...
]
```

# 使用
## 快速开始
**The form class**

编写form类:

```python
from django import forms
from ktag.fields import TagField

class TagForm(forms.Form):
    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=' ',
                          data_list=['apple', 'banana', 'watermelon', 'orange'], initial='grape coconut')
```

**The view**

编写view:

```python

from django.http import HttpResponse
from django.shortcuts import render

from example.forms import TagForm

def index(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
           if form.is_valid():
                print(form.cleaned_data['fruits'])
                return HttpResponse(str(form.cleaned_data['fruits']))

    else:
        form = TagForm()
    return render(request, 'index.html', {'form': form})
```

**The template**

编写html模板 :

```python
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <br>
    <input type="submit" value="OK" style="font-size: larger">
</form>
```

## 在Model与Admin使用
ktag 不支持外键（因为外键不好），所以你必须自己保存关联表的数据等
下面有个例子:

* 编写两个model
```python
from django.db import models


class People(models.Model):
    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'People'

    name = models.CharField(verbose_name='name', max_length=20)


class PeopleFruits(models.Model):
    class Meta:
        verbose_name = 'People-Fruits'
        verbose_name_plural = 'People-Fruits'

    people_id = models.IntegerField(verbose_name='people_id')
    fruit = models.CharField(verbose_name='fruit', max_length=30)

```
* 编写admin的form

```python
from django import forms

from example.models import People
from ktag.fields import TagField

class PeopleAdminForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=',',
                      data_list=['apple', 'banana', 'watermelon', 'orange'])


```
* 编写admin

在这里admin继承了 `ktag.admin.MultipleChoiceAdmin`

> `MultipleChoiceAdmin` 是我专门为tkag绑定数据写的
> 在`get_object()`中绑定数据
> 初始数据保存在`choice_field_value`中，他是一个dict，key是forms中field的名字，注意value是str不是list
> 在`save_model()`中保存数据

```python

from django.contrib import admin

from example.forms import PeopleAdminForm
from example.models import People
from ktag.admin import MultipleChoiceAdmin


@admin.register(People)
class PeopleAdmin(MultipleChoiceAdmin):

    form = PeopleAdminForm

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        """
        根据你的需要，从PeopleFruits中筛选数据
        PeopleFruits.objects.filter(people_id=object_id)
        ...
        """
        # bind value
        self.choice_field_value['fruits'] = "grape,coconut"

        return obj

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        fruits = form.cleaned_data['fruits']
        print(fruits)
        for f in fruits:
            """
            保存fruits
            ...
            if xxx:
                continue
            ...

            """
            PeopleFruits(people_id=obj.id,fruit=f).save()

```
# 参数表

Name                | Type       | Default     | Info
------------------- | ---------- | ----------- | --------------------------------------------------------------------------
place_holder        | string     | ""          | html input标签的展望符
delimiters          | string     | ","         | 标签的分隔符号
data_list           | list       | []          | 提示框的数据
black_list          | list       | []          | 黑名单
max_tags            | int        | None        | max number of tags
suggestions_chars   | int        | 1           | 输入多少字符后显示提示框


# Example
运行栗子
```shell
git clone git@github.com:gojuukaze/django-ktag.git  
cd django-ktag
pip install django
python manage.py makemigrations example 
python manage.py migrate   
python manage.py runserver 
```
