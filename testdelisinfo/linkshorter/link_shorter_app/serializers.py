from rest_framework import serializers
import pyshorteners

from .models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('id','short_url')

    def create(self, validated_data):
        short = pyshorteners.Shortener(api_key = '######################################')
        validated_data['short_url'] = short.bitly.short(validated_data['full_url'])
        return super(LinkSerializer, self).create(validated_data)
