import re
import tempfile

import subprocess
from django.db import models

from core.models import Dated, Titled


class CodeCheckList(Dated, Titled):

    def check_all_attr(self, ucode):
        for one_check in self.code_check_set.all():
            if not one_check.check(ucode):
                return False
        return True

    def __str__(self):
        return '{1}-{0}'.format(self.pk, self.title)


class CodeCheck(Titled):
    codechecklist = models.ForeignKey(CodeCheckList, related_name='checks')
    attribute = models.CharField(max_length=256)
    ttl = models.IntegerField(default=15)
    check_regex = models.BinaryField(default=b'(.*)')

    def check_attr(self, ucode):
        regex = re.compile(self.check_regex)
        try:
            with tempfile.NamedTemporaryFile() as temp:
                temp.write(ucode.strip().encode())
                command = ['python', temp.name]
                command.extend(self.attribute.split())
                output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=self.ttl)
                if regex.match(output.stdout):
                    return True
        except IOError:
            return False
        return False

    def __str__(self):
        return '{3}-{1}-{2}-{0}'.format(self.title, self.codechecklist_id, self.pk, self.codechecklist.title)


class Code(Dated):
    codechecklist = models.ForeignKey(CodeCheckList, related_name='codes')
    code = models.TextField(default='print("test")', blank=True)
    error = models.BooleanField(default=True)

    def check_code(self):
        if self.codechecklist.check_all_attr(self.code):
            self.error = False
            return self.error
        self.error = True
        return self.error

    def __str__(self):
        return 'Code-{0}-{1}'.format(self.pk, self.codechecklist.title)
