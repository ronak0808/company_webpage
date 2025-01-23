from django.contrib import admin
from app.models import GenralInfo,Service,Testimonial,ContactFormLog,Blog,Author

@admin.register(GenralInfo)
class GenralInfoAdmin(admin.ModelAdmin):
    list_display=[
        'company_name',
        'location',
        'email',
        'phone',
    ]
    
    # #show to disable add permission
    # def has_add_permission(self, request, obj=None):
    #     return False
    # #show to disable update permission
    # def has_change_permission(self, request, obj =None):
    #     return False
    # #show to disable delete permission
    # def has_delete_permission(self, request, obj =None):
    #     return False
    #show you can set fiels to disable update
    # readonly_fields=[
    #     'email',
    #     'phone',
    # ]
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'description',
    ]
    
    search_fields=[
        'title',
        'description',
    ]
    


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=[
        'username',
        'user_job_title',
        'display_rating',
    ]
    
    
    def display_rating(self,obj):
        return "*"*obj.rating_count
    
    display_rating.short_description = "Rating"
    
@admin.register(ContactFormLog)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=[
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]
          # #show to disable add permission
    def has_add_permission(self, request, obj=None):
       return False
    # #show to disable update permission
    def has_change_permission(self, request, obj =None):
       return False
    # #show to disable delete permission
    def has_delete_permission(self, request, obj =None):
        return False
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'author',
        'created_at',
    ]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass