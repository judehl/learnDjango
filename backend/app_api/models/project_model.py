from django.db import models


# Create your models here.
class Project(models.Model):
    """
    项目表： 包含项目名称，描述，状态，是否可删除，创建时间和更新时间
    """
    name = models.CharField('名称', max_length=50, null=False)
    describe = models.TextField('描述', null=True, default='')
    status = models.BooleanField('状态', null=True, default=True)
    is_delete = models.BooleanField('是否删除', null=True, default=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
