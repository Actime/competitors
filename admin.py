from django.contrib import admin
from .forms import RegisterForm, TimeRegForm, CompetitorForm
from .models import Register, TimeReg, Competitor

# Register your models here.

class CompetitorAdmin( admin.ModelAdmin ) :
    form = CompetitorForm
    list_display = [
        'id',
        'name',
        'second_name',
    ]
# End of competiror admin class

class TimeRegAdmin( admin.ModelAdmin ):
    form = TimeRegForm
    list_display = [
        'id',
        'register',
        'time',
    ]
    
# End of time reg admin class

class RegisterAdmin( admin.ModelAdmin ) :
    form = RegisterForm
    list_display = [
        'id',
        'competitor_num',
        'competition',
        'competitor',
    ]
# End of register admin class

admin.site.register( Competitor, CompetitorAdmin )
admin.site.register( Register, RegisterAdmin )
admin.site.register( TimeReg, TimeRegAdmin )