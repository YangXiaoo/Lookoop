# coding:utf-8
from django import forms

from ssh.models import Asset, AssetGroup


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "ip", "hostname", "port", "username", "password", "mac", "brand", "cpu", "memory", "disk", "system_type", "system_version",
            "status", "is_active", "comment"
        ]

class AssetGroupForm(forms.ModelForm):
	class Meta:
		model = AssetGroup
		fields = [
			"ip", "hostname", "user_id", "username", "password", "status", "is_active", "comment"
		]