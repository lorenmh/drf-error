from rest_framework.serializers import Serializer, CharField

class Foo(Serializer):
    foo = CharField()
    def __init__(self, some_param, *args, **kwargs):
        self.some_param = some_param
        super(Foo, self).__init__(*args, **kwargs)

bar = [{'foo':1}, {'foo':2}, {'foo':3}]

serializer = Foo('some_param', bar, many=True)
print serializer.data
