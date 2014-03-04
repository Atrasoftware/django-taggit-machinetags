from __future__ import unicode_literals

from django.contrib import admin

from taggit_machinetags.models import MachineTag, MachineTaggedItem


class MachineTaggedItemInline(admin.StackedInline):
    model = MachineTaggedItem


class MachineTagAdmin(admin.ModelAdmin):
    #inlines = [
    #    MachineTaggedItemInline
    #]
    list_display = ["slug", "namespace", "name"]

    ordering = ["namespace", "name"]
    #search_fields = ["name"]
    #prepopulated_fields = {"slug": ["name"]}
    fieldsets = (
        (None, {'fields': ('namespace', 'name')}),
        ('Advanced options', {
                'classes': (),
                'fields':(),
                        }),
                )


admin.site.register(MachineTag, MachineTagAdmin)
