from django_extensions.mongodb.fields import CreationDateTimeField, ModificationDateTimeField


class TimeStampedModel:
    """ TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        abstract = True
