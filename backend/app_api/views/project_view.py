from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from app_api.serializer.project import ProjectValidator, ProjectSerializer
from app_api.models.project_model import Project
from app_common.utils.pagination import Pagination
from app_common.utils.response import response, Error

# Create your views here.
class ProjectView(APIView):

    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pk')
        if pid is not None:  # 查询单条
            try:
                project = Project.objects.get(pk=pid, is_delete=False)
                ser = ProjectSerializer(instance=project, many=False)
            except Project.DoesNotExist:
                return JsonResponse({'msg': 'project object is null'})
            return JsonResponse({'msg': '查询成功', 'data': ser.data})
        else:  # 查询多条数据
            project = Project.objects.filter(is_delete=False).all()
            pg = Pagination()
            page_data = pg.paginate_queryset(queryset=project, request=request, view=self)
            ser = ProjectSerializer(instance=page_data, many=True)
            return JsonResponse({'msg': '查询成功', 'data': ser.data})

    def post(self, request, *args, **kwargs):
        """
        添加项目 request.data
        """
        val = ProjectValidator(data=request.data)
        if val.is_valid():  # 字段验证通过
            val.save()
        else:
            return JsonResponse({'msg': '添加', 'error': val.errors})
        return JsonResponse({'msg': '添加成功'})

    def put(self, request, *args, **kwargs):
        """
        id写在url中 更新：使用kwargs，id通过写在请求参数中更新使用request.data.get
        """
        pid = kwargs.get('pk')  # url 中 获取
        # pid = request.data.get('id')  # 请求参数中获取
        if pid is None:
            return JsonResponse({'msg': "project id is null"})
        try:
            project = Project.objects.get(pk=pid, is_delete=False)
        except Project.DoesNotExist:
            return JsonResponse({"msg": "Project object is null"})

        # 更新
        val = ProjectValidator(instance=project, data=request.data)
        if val.is_valid():
            val.save()
        else:
            return JsonResponse({'msg': '更新失败', 'error': val.errors})

        return JsonResponse({'msg': '更新'})

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        pid = kwargs.get('pk')
        if pid is not None:
            project = Project.objects.filter(pk=pid, is_delete=False).update(is_delete=True)
            print(project)
            if project == 0:
                return JsonResponse({'msg': '删除失败'})
            return JsonResponse({'msg': '删除成功'})
