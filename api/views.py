from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CapstoneProjectSerializer, CourseMaterialSerializer, TrackSerializer, UserSerializer, CourseSerializer, VoucherSerializer
from lms.models import CapstoneProject, Track, Course, CourseMaterial, Voucher

# Create your views here.




class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseMaterialView(viewsets.ModelViewSet):
    serializer_class = CourseMaterialSerializer
    queryset = CourseMaterial.objects.all()

class TrackView(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TrackDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class CapstoneProjectView(viewsets.ModelViewSet):
    serializer_class = CapstoneProjectSerializer
    queryset = CapstoneProject.objects.all()


class CapstoneDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CapstoneProjectSerializer
    queryset = CapstoneProject.objects.all()


class VoucherListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def perform_create(self, serializer):
        code = serializer.validated_data.get('code')
        percentage = serializer.validated_data.get('percentage')
        serializer.save(
            code=code,
            percentage=percentage
        )
    

class VoucherDetailAPIView(generics.RetrieveAPIView):
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()    

# class VoucherCreateView(generics.CreateAPIView):
#     serializer_class = VoucherSerializer
#     queryset = Voucher.objects.all()

# trying out function based views

@api_view(['GET', 'POST'])
def voucher_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # details
            obj = get_object_or_404(Voucher, pk=pk)
            return Response()
        # list all items
        qs = Voucher.objects.all()
        data = VoucherSerializer(qs, many=True).data
        return Response(data)

    if method == 'POST':
        # create and item
        serializer = VoucherSerializer
        if serializer.is_valid(raise_exception=True):
            # code = serializer.validated_data.get('code')
            # percentage = serializer.validated_data.get('percentage')
            # serializer.save(
            #     code=code,
            #     percentage=percentage
            # )
            
            return Response(serializer.data)
        return Response({'invalid': 'not good data'}, status=400)