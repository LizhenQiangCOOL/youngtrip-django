import os
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.file.models import File
from apps.file.serializers import FileSerializer

from youngtrip.settings import MEDIA_ROOT
from apps.util.tf import handle_img

class FileViewSet(viewsets.ViewSet):
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = self.request.data.get('file', None)
        filetype = None
        if not file:
            return Response({
                'msg':'上传失败'
            }, status=400)
        
        img_content_type = ['image/png', 'image/jpeg', 'image/jpg']
        if file.content_type in img_content_type:
            filetype = 'img'
        file.name = str(file.name).lower()
        if file.name.endswith('.mp4'):
            filetype = 'video'
        
        if not filetype:
            return Response({
                'msg':'文件格式错误'
            }, status=300)
        
        f = File.objects.create(
            file=file,
            type=filetype
        ) 
        if f.type == 'img':
            imgpath = os.path.join(MEDIA_ROOT ,str(f.file))
            res = handle_img(imgpath)
            print(res)
            if res['classes'] == 'porn':
                f.delete()
                return Response({
                    'msg':'请不要上传不雅图片',
                }, status=400)

        host = self.request.get_host()
        fileurl = ''.join(('http://', host, '/media/', str(f.file)))
        return Response({
            'msg':'上传成功',
            'data':fileurl
        }, status=200)