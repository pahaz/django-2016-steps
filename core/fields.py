import json

from django.db import models
from django.utils.translation import ugettext_lazy as _


class JSONField(models.TextField):
    description = _("Simple JSON filed (store only, without filtration)")

    def db_type(self, connection):
        if connection.vendor == 'postgresql':
            # Only do jsonb if in pg 9.4+
            if connection.pg_version >= 90400:
                return 'jsonb'
            return 'text'
        if connection.vendor == 'mysql':
            return 'longtext'
        return 'text'

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return json.loads(value)

    def to_python(self, value):
        return json.dumps(value)
