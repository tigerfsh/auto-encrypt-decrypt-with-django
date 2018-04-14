from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def api_lists(request, format=None):
    data = {1: {"name": "添加个人信息",
                "url": reverse("add-personal-data", request=request, format=format)},
            2: {"name": "查询个人信息",
                "url": reverse("retrieve-personal-data", request=request, format=format)}
            }

    return Response(data=data)
