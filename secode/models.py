import re
import tempfile

import subprocess
from django.db import models

from core.models import Dated, Titled


class CodeCheckList(Dated, Titled):

    def check_all_attr(self, ucode):
        if self.checks.all():
            for one_check in self.checks.all():
                if not one_check.check_attr(ucode):
                    return False
            return True
        return False

    def __str__(self):
        return '{1}-{0}'.format(self.pk, self.title)


class CodeCheck(Titled):
    codechecklist = models.ForeignKey(CodeCheckList, related_name='checks')
    attribute = models.CharField(max_length=256, default='')
    ttl = models.IntegerField(default=15)
    check_regex = models.BinaryField(default=b'(.*)')

    def check_attr(self, ucode):
        regex = re.compile(self.check_regex, re.M)
        try:
            with tempfile.NamedTemporaryFile() as temp:
                temp.write(ucode.strip().encode())
                temp.flush()
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
            return True
        self.error = True
        return False

    def __str__(self):
        return 'Code-{0}-{1}'.format(self.pk, self.codechecklist.title)
