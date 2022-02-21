from rest_framework import serializers
from app_api.models.project_model import Project


# aatype = [1, 2, 3]
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']


class ProjectValidator(serializers.Serializer):
    """
    项目验证器
    """
    name = serializers.CharField(required=True, max_length=50, error_messages={'required': 'name不能为空！',
                                                                               'invalid': '类型不对',
                                                                               'max_length': '长度不能大于50'
                                                                               })
    describe = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)

    # aatype = serializers.ChoiceField(choices=aatype)

    def create(self, validated_data):
        """
        创建  -- 特有写法
        """
        project = Project.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        """
        更新任务
        params: instace, 待更新对象（数据库）， validated_data 更新的数据（request）
        """
        instance.name = validated_data.get('name')
        instance.describe = validated_data.get('describe')
        instance.status = validated_data.get('status')
        instance.save()
        return instance
