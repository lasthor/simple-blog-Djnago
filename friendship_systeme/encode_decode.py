from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode


def encode_id(obj):
    return urlsafe_base64_encode(str(obj).encode('utf-8'))


def decode_id(data):
    return int(urlsafe_base64_decode(data))