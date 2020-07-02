from rest_framework import serializers


class Enums:
    LIST_STATUS = ['ACTIVO', 'INACTIVO']
    ACTIVO = 'ACTIVO'
    INACTIVO = 'INACTIVO'


class DynamicFieldsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        notfields = kwargs.pop('notfields', None)

        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            existing = set(self.fields.keys())
            if not isinstance(fields, str):
                allowed = set(fields)
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
            else:
                for field_name in existing:
                    if field_name != fields:
                        self.fields.pop(field_name)

        elif notfields is not None:
            existing = set(self.fields.keys())
            if not isinstance(notfields, str):
                disallowed = set(notfields)
                for field_name in disallowed:
                    if field_name in existing:
                        self.fields.pop(field_name)
            else:
                self.fields.pop(notfields)