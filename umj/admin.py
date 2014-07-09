from django.contrib import admin
from .models import Term, Definition

class DefInline(admin.TabularInline):
	model = Definition
	extra = 3


class TermAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,               {'fields': ['phrase']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	
	inlines = [DefInline]


admin.site.register(Term, TermAdmin)
