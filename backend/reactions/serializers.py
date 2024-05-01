from rest_framework import serializers
from .models import Category, Reaction

class ReactionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = (
            "id",
            "name",
            "conversion",
            "slug",
            "get_absolute_url",
            "reactants",
            "products",
            "catalysts",
            "temperature",
            "extra",
            "date_added"
        )