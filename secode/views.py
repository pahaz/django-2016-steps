from django.http import JsonResponse
from django.middleware.csrf import get_token

from secode.models import CodeCheckList, CodeCheck, Code


class JsonView:
    def __init__(self, methods=('GET', 'POST')):
        if type(methods) in (list, tuple):
            self.methods = tuple(methods)
        else:
            self.methods = (methods,)

    def __call__(self, request, *args, **kwargs):
        answer = {}
        try:
            if request.method not in self.methods:
                raise Exception('No support method')
            ans = self.handler(request, *args, **kwargs)
            if ans:
                answer['answer'] = ans
                answer['status'] = 'OK'
            else:
                raise Exception('No answer')
        except NotImplementedError:
            raise
        except Exception:
            answer['status'] = 'FAIL'
        return JsonResponse(answer)

    def handler(self, request):
        raise NotImplementedError('Not implemented')


class GetCsrfToken(JsonView):
    def handler(self, request):
        return {'csrfmiddlewaretoken': get_token(request),
                'tips:': 'csrfmiddlewaretoken - key for data; csrftoken - key for cookies'}


class CreateList(JsonView):
    def handler(self, request):
        ccl = CodeCheckList(title=request.POST['title'])
        ccl.save()
        return {'title': ccl.title, 'id': ccl.id, 'date': ccl.created}


class DeleteList(JsonView):
    def handler(self, request):
        ccl = CodeCheckList.objects.get(pk=request.POST['id'])
        title = ccl.title
        ccl.delete()
        return {'title': title, 'delete': 'OK'}


class CreateCheckToList(JsonView):
    def handler(self, request):
        ccl = CodeCheckList.objects.get(pk=request.POST['id'])
        cc = CodeCheck(
            codechecklist=ccl,
            title=request.POST['title'],
            ttl=request.POST['ttl'],
            attribute=request.POST['attributes'],
            check_regex=request.POST['regex'].encode()
        )
        cc.save()
        return dict(list_id=request.POST['id'], check_id=cc.id, title=cc.title, ttl=cc.ttl, attributes=cc.attribute,
                    regex=cc.check_regex.decode())


class DeleteCheckFromList(JsonView):
    def handler(self, request):
        cc = CodeCheckList.objects.get(pk=request.POST['list_id']).checks.get(pk=request.POST['check_id'])
        title = cc.title
        cc.delete()
        return {'title': title, 'delete': 'OK'}


class CreateCodeAndCheck(JsonView):
    def handler(self, request):
        c = Code(codechecklist=CodeCheckList.objects.get(pk=request.POST['id']), code=request.POST['code'])
        c.save()
        return {'list_id': request.POST['id'], 'code_id': c.id, 'error': c.error, 'check': c.check_code()}
