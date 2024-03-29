from rest_framework import serializers
from ...models import Device, SaunaSession, Reading


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('user',)


class SaunaSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaunaSession
        fields = '__all__'
        read_only_fields = ('user',)


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'
        read_only_fields = ('user',)
