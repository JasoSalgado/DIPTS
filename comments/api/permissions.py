# blog/comments/api/permissions.py
# Rest framework modules
from rest_framework.permissions import BasePermission
# My modules
from comments.models import Comment

class IsOwnerOrReadAndCreate(BasePermission):
    """
    Is owner or can read and create
    """
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            #Obtaining the id to delete or edit
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            # Retrieving the user that is trying to execute the request
            id_user = request.user.pk
            # Obtain id user to try to do the comment
            id_user_comment = comment.user_id

            # It id_user = id_user_comment so, it is the same person
            if id_user == id_user_comment:
                return True
            return False
