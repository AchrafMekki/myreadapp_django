reader = Reader.objects.get(username='achraf')

print()


from apps.reader.models import Reader

Reader.objects.get(username='achraf').delete()