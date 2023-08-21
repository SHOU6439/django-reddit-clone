from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from communities.usecases.join_community_action import join_community_action
from django.contrib.auth.decorators import login_required

@login_required
def join(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    join_community_action(request.user, pk)
    return redirect('communities:detail', pk=pk)
