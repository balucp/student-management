import sys
import traceback
import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from app_student.serializer import *
from app_student.models import *

# Create your views here.

class TeacherAPI(generics.ListCreateAPIView):

    """GET method will list all Teacher objects and POST method will create new Teacher object"""

    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all().order_by('name')

    def post(self,request):

        """This function will create teacher"""

        try:
            data = request.data
            serializer = TeacherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':0,'msg':'Teacher created successfully.'},status=200)
            else:
                return Response({'status':1,'msg':serializer.errors},status=400)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({'status':1, "msg": str(err)},status=400)


class StudentAPI(generics.ListCreateAPIView):

    """GET method will list all Student objects and POST method will create new Student object"""

    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('name')

    def post(self,request):

         """This function will create Student"""

        try:
            data = request.data
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':0,'msg':'Student created successfully.'},status=200)
            else:
                return Response({'status':1,'msg':serializer.errors},status=400)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({'status':1, "msg": str(err)},status=400)


class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    """API for fetch/update/delete student details"""

    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('name')

    def get(self,request,id):

        """This method will fetch student details"""

        try:
            try:
                student = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'status':1,'msg':'Student DoesNotExist'},status=400)

            serializer = StudentSerializer(student)
            return Response({'status':0,'data':serializer.data},status=200)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)

    def put(self,request,id):

        """This method will update existing student details"""

        try:
            try:
                student = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'status':1,'msg':'Student DoesNotExist'},status=400)

            serializer = StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':0,'msg':'Student details updated successfully.'},status=200)
            else:
                return Response({'status':1,'msg':serializer.errors},status=400)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)

    def delete(self,request,id):
        """This method will delete existing student details"""
        try:
            try:
                student = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'status':1,'msg':'Student DoesNotExist'},status=400)

            student.delete()
            return Response({'status':0,'msg':'Student deleted successfully.'},status=200)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)


class MarkAPI(generics.ListCreateAPIView):

    """API for entering student marks & for viewing marklist"""

    serializer_class = MarkUploadSerializer

    def post(self,request):

        """This method will save mark details of a student"""
        try:
            data = request.data
            serializer = MarkUploadSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':0,'msg':'Marks entered successfully.'},status=200)
            else:
                return Response({'msg':serializer.errors},status=400)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)

    def get(self,request):

        """This method will list  marks of all students"""

        queryset = Mark.objects.all()
        serializer = MarkListSerializer(queryset,many = True)
        return Response({'status':0,'data':serializer.data},status=200)


class MarkDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    """API for fetching/updating/deleting student marks"""

    serializer_class = MarkListSerializer

    def get(self,request,id):

        """This method will fetch marks of  student"""

        try:

            try:
                mark =Mark.objects.get(id=id)
            except Mark.DoesNotExist:
                return Response({'status':1,'msg':'Mark DoesNotExist.'},status=400)

            serializer = MarkListSerializer(mark)
            return Response({'status':0,'data':serializer.data},status=200)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)

    def put(self,request,id):

        """This method will update marks of a student"""

        try:
            data = request.data

            try:
                mark =Mark.objects.get(id=id)
            except Mark.DoesNotExist:
                return Response({'status':1,'msg':'Mark DoesNotExist.'},status=400)

            serializer = MarkUpdateSerializer(mark,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':0,'msg':'Marks updated successfully.'},status=200)
            else:
                return Response({'msg':serializer.errors},status=400)

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)

    def delete(self,request,id):

        """This method will delete marks of a student"""

        try:
            mark =Mark.objects.get(id=id)
            mark.delete()
            return Response({'status':0,'msg':'Marks deleted successfully.'},status=200)
            
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            return Response({"status": 1, "msg": str(err)},status=400)



