from django.shortcuts import render
from django.http import JsonResponse
from app_api.serializer.project import ProjectValidator, ProjectSerializer
from app_api.models.project_model import Project
from app_common.utils.pagination import Pagination
from app_common.utils.response import response, Error
from app_common.utils.base_view import BaseAPIView


# Create your views here.
class ProjectView(BaseAPIView):

    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pk')
        page = request.query_params.get('page', 1)  # 分页查询获取页码数
        size = request.query_params.get('size', 5)  # 分页查询获取每页条数
        if pid is not None:  # 查询单条
            try:
                project = Project.objects.get(pk=pid, is_delete=False)
                ser = ProjectSerializer(instance=project, many=False)
            except Project.DoesNotExist:
                return self.response_fail(error=self.PROJECT_ID_NULL)
            return self.response(data=ser.data)
        else:  # 查询多条数据
            project = Project.objects.filter(is_delete=False).all()
            pg = Pagination()
            page_data = pg.paginate_queryset(queryset=project, request=request, view=self)
            ser = ProjectSerializer(instance=page_data, many=True)
            data = {
                'total': len(project),
                'page': int(page),  # 分页信息不输默认第一页，每页5条
                'size': int(size),
                'projectList': ser.data
            }
            return self.response(data=data)

    def post(self, request, *args, **kwargs):
        """
        添加项目 request.data
        """
        val = ProjectValidator(data=request.data)
        if val.is_valid():  # 字段验证通过
            val.save()
        else:
            return self.response_fail(error=val.errors)
        return self.response()

    def put(self, request, *args, **kwargs):
        """
        id写在url中更新：使用kwargs
        id通过请求参数更新使用request.data.get
        """
        pid = kwargs.get('pk')  # url 中 获取
        # pid = request.data.get('id')  # 请求参数中获取
        if pid is None:
            return self.response(error=self.PROJECT_ID_NULL)
        try:
            project = Project.objects.get(pk=pid, is_delete=False)
        except Project.DoesNotExist:
            return self.response(error=self.PROJECT_OBJECT_NULL)

        # 更新
        val = ProjectValidator(instance=project, data=request.data)
        if val.is_valid():
            val.save()
        else:
            return self.response(error=val.errors)
        return self.response()

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        pid = kwargs.get('pk')
        if pid is not None:
            project = Project.objects.filter(pk=pid, is_delete=False).update(is_delete=True)
            print(project)
            if project == 0:
                return self.response(error=self.PROJECT_DELETE_ERROR)
            return self.response()
