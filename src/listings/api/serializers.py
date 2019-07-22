from  rest_framework import serializers

from listings.models import Listing

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'realtor',
            'title',
            'address',
            'city',
            'state',
            'zipcode',
            'description',
            'price',
            'bedrooms',
            'bathrooms',
            'garage',
            'sqft',
            'lot_size',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
            'is_published',
            'list_date',
        ]

        # def validate_content(self, value):
        #     if len(value) > 10000:
        #         raise serializers.ValidationError("This is wayy too long.")
        #     return value

        def validate(self, data):
            content = data.get("content", None)
            if content == "":
                content = None
            image = data.get("image", None)
            if content is None and image is None:
                raise serializers.ValidationError("Content or image is required.")
            return data

