from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from misc.fields import ContentField
from misc.serializers import ContentCourseSerializer


from .fields import CategoryField
from .models import Resource, Chapter, Category, CourseAnswer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    parent_chapter = serializers.PrimaryKeyRelatedField(read_only=True)
    content = ContentField()

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'content', 'type', 'parent_chapter')


class ChapterCourseSerializer(ChapterSerializer):
    content = ContentCourseSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'content', 'type', 'parent_chapter')


class CourseAnswerSerializer(serializers.ModelSerializer):
    chapter = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CourseAnswer
        fields = '__all__'


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    search_type = serializers.CharField(default='resource', read_only=True)
    id = serializers.IntegerField(required=False)
    category = CategoryField(allow_null=True)

    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = ('id', 'name', 'category', 'course', 'search_type',
                  'on_day', 'tags', 'remove_on_complete', 'chapters')


class ResourceCourseSerializer(ResourceSerializer):
    chapters = ChapterCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = ('id', 'name', 'category', 'course',
                  'on_day', 'tags', 'remove_on_complete', 'chapters')


class ResourceSlimSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Resource
        fields = ('id', 'name')
