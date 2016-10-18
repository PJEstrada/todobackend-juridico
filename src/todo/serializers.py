from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.ReadOnlyField()
	# comment
	class Meta:
		model = TodoItem
		fields = ('url', 'title', 'completed', 'order')
		