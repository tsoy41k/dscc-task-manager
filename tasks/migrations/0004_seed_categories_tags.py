from django.db import migrations

def seed_data(apps, schema_editor):
    Category = apps.get_model('tasks', 'Category')
    Tag = apps.get_model('tasks', 'Tag')

    categories = ["Work", "Study", "Personal"]
    tags = ["urgent", "important", "later"]

    for name in categories:
        Category.objects.get_or_create(name=name)

    for name in tags:
        Tag.objects.get_or_create(name=name)

def unseed_data(apps, schema_editor):
    Category = apps.get_model('tasks', 'Category')
    Tag = apps.get_model('tasks', 'Tag')

    Category.objects.filter(name__in=["Work", "Study", "Personal"]).delete()
    Tag.objects.filter(name__in=["urgent", "important", "later"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_category'),  # оставь то, что там уже стоит
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]