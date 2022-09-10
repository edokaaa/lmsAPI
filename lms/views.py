from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lms.serializers import  TrackSerializer, CourseSerializer
from lms.models import Track, Course

# auth
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # authentication_classes = []
    # permission_classes = []


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'pk'

    
class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # authentication_classes = []
    # permission_classes = []


class CourseDestroyAPIView(generics.DestroyAPIView
):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    # authentication_classes = []
    # permission_classes = []




class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = (IsAuthenticated,)

# class CourseMaterialView(viewsets.ModelViewSet):
#     serializer_class = CourseMaterialSerializer
#     queryset = CourseMaterial.objects.all()
#     # permission_classes = (IsAuthenticated,)


class TrackView(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    # permission_classes = (IsAuthenticated,)


# class CapstoneProjectView(viewsets.ModelViewSet):
#     serializer_class = CapstoneProjectSerializer
#     queryset = CapstoneProject.objects.all()


# class VoucherView(viewsets.ModelViewSet):
#     serializer_class = VoucherSerializer
#     queryset = Voucher.objects.all()

# # trying out function based views

# @api_view(['GET', 'POST'])
# def voucher_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':
#         if pk is not None:
#             # details
#             obj = get_object_or_404(Voucher, pk=pk)
#             return Response()
#         # list all items
#         qs = Voucher.objects.all()
#         data = VoucherSerializer(qs, many=True).data
#         return Response(data)

#     if method == 'POST':
#         # create and item
#         serializer = VoucherSerializer
#         if serializer.is_valid(raise_exception=True):
#             # code = serializer.validated_data.get('code')
#             # percentage = serializer.validated_data.get('percentage')
#             # serializer.save(
#             #     code=code,
#             #     percentage=percentage
#             # )
            
#             return Response(serializer.data)
#         return Response({'invalid': 'not good data'}, status=400)