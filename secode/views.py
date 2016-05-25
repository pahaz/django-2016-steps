from django.http import JsonResponse
from django.middleware.csrf import get_token

from secode.models import CodeCheckList, CodeCheck, Code


def get_csrf_token(request):
    answer = {
        'status': 'OK',
        'csrftoken': get_token(request)
    }
    return JsonResponse(answer)


def create_list(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            ccl = CodeCheckList(title=title)
            ccl.save()
            answer = {
                'status': 'OK',
                'object': dict(title=ccl.title, id=ccl.id, date=ccl.created)
            }
            return JsonResponse(answer)
        except KeyError:
            pass
    answer = {
        'status': 'FAIL'
    }
    return JsonResponse(answer)


def delete_list(request):
    if request.method == 'POST':
        try:
            CodeCheckList.objects.filter(pk=request.POST['id']).delete()
            answer = {
                'status': 'OK'
            }
            return JsonResponse(answer)
        except KeyError:
            pass
    answer = {
        'status': 'FAIL'
    }
    return JsonResponse(answer)


def add_check_to_list(request):
    if request.method == 'POST':
        try:
            lista = CodeCheckList.objects.filter(pk=request.POST['id'])
            title = request.POST['title']
            ttl = request.POST['ttl']
            attribute = request.POST['attr']
            check_regex = request.POST['regex'].encode()
            cc = CodeCheck(codechecklist=lista, title=title, ttl=ttl, attribute=attribute, check_regex=check_regex)
            cc.save()
            answer = {
                'status': 'OK',
                'object': {'list_id': request.POST['id'], 'check_id': cc.id, 'title': title, 'ttl': ttl,
                           'attribute': attribute, 'regex': check_regex.decode()}
            }
        except KeyError:
            pass
    answer = {
        'status': 'FAIL'
    }
    return JsonResponse(answer)


def delete_check_from_list(request):
    if request.method == 'POST':
        try:
            CodeCheckList.objects.filter(pk=request.POST['list_id']).checks.filter(pk=request.POST['check_id']).delete()
            answer = {
                'status': 'OK'
            }
            return JsonResponse(answer)
        except KeyError:
            pass
    answer = {
        'status': 'FAIL'
    }
    return JsonResponse(answer)


def add_and_check_code(request):
    if request.method == 'POST':
        try:
            ids = request.POST['id']
            code = request.POST['code']
            c = Code(codechecklist=CodeCheckList.objects.filter(pk=ids), code=code)
            c.save()
            answer = {
                'status': 'OK',
                'object': {'list_id': request.POST['id'], 'code_id': c.id, 'error': c.error, 'check': c.check_code()}
            }
            return JsonResponse(answer)
        except KeyError:
            pass
    answer = {
        'status': 'FAIL'
    }
    return JsonResponse(answer)
