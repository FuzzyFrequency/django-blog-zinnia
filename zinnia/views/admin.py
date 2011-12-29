from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from oauth_access.models import UserAssociation

@staff_member_required
def facebook_callback(request, access, token):
    UserAssociation.objects.create(user=request.user,
                                   service='facebook',
                                   identifier='zinnia',
                                   token=token,
                                   expires=token.expires
                                   )


    messages.success(request,
                     _('Your Facebook account has been associated')
                     )

    return redirect('admin:zinnia_entry_changelist')


