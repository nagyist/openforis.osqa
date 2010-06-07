import os.path
from base import Setting, SettingSet

from django.forms.widgets import Textarea
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as djsettings
from django.utils.version import get_svn_revision

OSQA_VERSION = "Development Build"
SVN_REVISION = get_svn_revision(djsettings.SITE_SRC_ROOT)

MAINTAINANCE_MODE = Setting('MAINTAINANCE_MODE', None)

SETTINGS_PACK = Setting('SETTINGS_PACK', "default")
DJSTYLE_ADMIN_INTERFACE = Setting('DJSTYLE_ADMIN_INTERFACE', True)

APP_URL = djsettings.APP_URL
FORUM_SCRIPT_ALIAS = djsettings.FORUM_SCRIPT_ALIAS

STATIC_PAGE_REGISTRY = Setting('STATIC_PAGE_REGISTRY', {})


from basic import *
from sidebar import *
from email import *
from extkeys import *
from minrep import *
from repgain import *
from voting import *
from upload import *
from about import *
from faq import *
from form import *
from moderation import *
from users import *

BADGES_SET = SettingSet('badges', _('Badges config'), _("Configure badges on your OSQA site."), 500)

#__all__ = locals().keys()

