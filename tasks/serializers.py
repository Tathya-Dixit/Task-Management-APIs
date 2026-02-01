from rest_framework import serializers

from tasks.models import Category, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['created_at']

class TaskSerializer(serializers.ModelSerializer):
    category_details = CategorySerializer(source='category', read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        write_only = True,
        required = False
    )

    class Meta:
        model = Task
        fields = ['id','title','description','category','category_details','priority','status','due_date','done_date','created_at']
        read_only_fields = ['created_at']

    def validate_category(self, value):
        if value and (value.user != self.context['request'].user):
            raise serializers.ValidationError("Invalid category")
        return value
