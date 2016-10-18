from django.http import HttpResponse
from app.models import Version
import json

def verify(request, app, version):
    data = None
    critical = False
    status = 200
    try:
        versions = Version.objects.filter(app=app, version_code__gt=version).order_by("-version_code")
        if not versions:
            return HttpResponse(json.dumps(data), status=status, content_type="application/json")
        else:
            for v in versions:
                if v.type == 2:
                    critical = True
            data = {}
            data['version_code'] = versions.first().version_code
            data['message'] = versions.first().message
            data['app_package'] = versions.first().app.package
            data['critical'] = critical

            return HttpResponse(json.dumps(data), status=status, content_type="application/json")

    except Exception, e:
        data = {"message": e.message}
        return HttpResponse(json.dumps(data), status=500, content_type="application/json")