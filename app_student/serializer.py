import sys
import traceback
import json
from pytz import timezone
import datetime

from rest_framework.response import Response
from rest_framework import serializers

from app_student.models import *


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields ="__all__"


class StudentSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    def get_teacher_name(self,obj):
        return obj.teacher.name

    class Meta:
        model = Student
        fields =['id','name','age','gender','teacher','teacher_name']
        read_only_fields = ['teacher_name']


class MarkListSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    student_id = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()

    def get_student_name(self,obj):
        return obj.student.name

    def get_student_id(self,obj):
        return obj.student.id

    def get_created_date(self,obj):
        date_format = '%b %-d %Y,%I:%M %p'
        now_asia = obj.created_date.astimezone(timezone('Asia/Kolkata'))
        date = datetime.datetime.strftime(now_asia,date_format)
        return date

    class Meta:
        model = Mark
        fields =['id','student_id','student_name','maths','science','history','term','total','created_date']
        read_only_fields = ['student_id','student_name','created_date','total']


class MarkUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields =['student','maths','science','history','term','created_date']

    def create(self, validated_data):
        try:
            student=validated_data['student']
            term=validated_data['term']
            maths=validated_data['maths']
            science=validated_data['science']
            history=validated_data['history']
            total = maths + science + history

            mark = Mark(student = student,maths=maths,science = science,history = history,total=total,term = term)
            mark.full_clean()
            mark.save()
            return mark
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)

class MarkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields =['student','maths','science','history','term']

    def update(self,instance, validated_data):
        instance.term=validated_data['term']
        instance.maths=validated_data['maths']
        instance.science=validated_data['science']
        instance.history=validated_data['history']
        instance.total = validated_data['maths'] + validated_data['science'] + validated_data['history']
        instance.full_clean()
        instance.save()
        return instance