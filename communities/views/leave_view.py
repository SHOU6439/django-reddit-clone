from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from communities.usecases.leave_community_action import leave_community_action



@login_required
def leave(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    leave_community_action(request.user, pk)
    return redirect('communities:detail', pk=pk)