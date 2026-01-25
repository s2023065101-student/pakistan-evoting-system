from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .logic import get_ai_response

@login_required
def ai_chat(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        reply = get_ai_response(user_message)
        return JsonResponse({"reply": reply})
