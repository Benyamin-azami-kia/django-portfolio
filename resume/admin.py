from django.contrib import admin
from .models import Profile, Skill, Contact, Project, Tag, ProjectImages, Certificate


class SkillInline(admin.TabularInline):
    model=Skill
    autocomplete_fields=['owner']
    extra=1


class CertificateInline(admin.StackedInline):
    model=Certificate
    extra=1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines=[SkillInline, CertificateInline]
    autocomplete_fields=['user']
    search_fields=['user__first_name__istartswith','user__last_name__istartswith','user__username']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ProjectImagesInline(admin.TabularInline):
    model=ProjectImages
    extra=1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields=['owner']
    inlines=[ProjectImagesInline]