# from .models import 

# # utils.py


from django.contrib.sessions.models import Session
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()

def get_active_users():
    active_sessions = Session.objects.filter(expire_date__gte=now())  # Get non-expired sessions
    user_ids = []
    
    for session in active_sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id')
        if user_id:
            user_ids.append(user_id)
    
    return User.objects.filter(id__in=user_ids)  # Return the active users

def dashboard_callback(request, context):
    context.update({
        "variable": "Hello world"
    })

    return context