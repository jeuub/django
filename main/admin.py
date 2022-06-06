from django.contrib import admin
from .models import Quiz, Authors, Categoties
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Quiz)
class quizs(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Authors)
class author(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    

@admin.register(Categoties)
class categotie(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
