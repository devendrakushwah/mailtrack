from django.http import HttpResponse
from PIL import Image
from datetime import datetime
from tracker.models import Email, TrackingInfo

def track(request):
        post_id = request.GET.get('post_id',None)
        ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        details = request.META.get('HTTP_USER_AGENT')
        date = str(datetime.now())
        obj = TrackingInfo.objects.create(ip=ip, date=date, details=details, email=Email.objects.get(id=post_id))
        obj.save()
        white = Image.new('RGB', (1,1), (255, 255, 255))
        response = HttpResponse(content_type="image/jpeg")
        white.save(response, "JPEG")
        return response

def new_tracking_link(request):
        subject = request.GET.get('subject', '')
        obj = Email.objects.create(subject = subject, created_at = str(datetime.now()))
        obj.save()
        post_id = str(obj.id)
        text = 'http://www.mymailtracker.pythonanywhere.com/track?post_id='+post_id
        return HttpResponse(text)
