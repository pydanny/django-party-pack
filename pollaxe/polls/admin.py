import datetime

from django.contrib import admin

from polls.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date']}),
        ]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'    

admin.site.register(Poll, PollAdmin)