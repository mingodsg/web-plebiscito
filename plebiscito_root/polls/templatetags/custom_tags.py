from django import template
import json
import geocoder
from ..models import Vote

register = template.Library()


@register.filter
def json_parse(value):

    vote_data = Vote.objects.all()
    geo_list = []
    for item in vote_data:
        geo_list.append(geocoder.ip(item.geo_location).latlng)

    return geo_list
