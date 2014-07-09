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
	list_display = ('phrase', 'pub_date', 'was_published_recently')
	list_filter = ('pub_date',)
	search_field = 'phrase'
	date_hierarchy = 'pub_date'


admin.site.register(Term, TermAdmin)
