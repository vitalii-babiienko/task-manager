from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import (
    Worker,
    Task,
    TaskType,
    Position,
)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "position",
                        "bio",
                    )
                }
            ),
        )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "bio",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = (
        "is_completed",
        "priority",
        "task_type",
    )


admin.site.register(TaskType)
admin.site.register(Position)
