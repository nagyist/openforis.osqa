from django import forms
from lib import captcha
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode, smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
import settings

class ReCaptchaField(forms.Field):

	def __init__(self, *args, **kwargs):
		super(ReCaptchaField, self).__init__(widget=ReCaptchaWidget)

	def get_client_ip(request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip
		
	def clean(self, values):
		super(ReCaptchaField, self).clean(values)
		recaptcha_response_value = smart_unicode(values)
		check_captcha = captcha.submit(recaptcha_response_value, settings.RECAPTCHA_PRIV_KEY, "0.0.0.0")

		if not check_captcha.is_valid:
			raise forms.util.ValidationError(_('Invalid captcha ' + check_captcha.error_code))
            
		return values


class ReCaptchaWidget(forms.Widget):
	def render(self, name, value, attrs=None):
		return mark_safe(force_unicode(captcha.displayhtml(settings.RECAPTCHA_PUB_KEY)))

	def value_from_datadict(self, data, files, name):

		return data.get('g-recaptcha-response', None)
        

