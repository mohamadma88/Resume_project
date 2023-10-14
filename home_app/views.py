from django.shortcuts import render
from work_exp_app.models import Work
from award_app.models import Award
from skill_app.models import Skill
from header_app.models import Header


def home(request):
    work = Work.objects.all()
    award = Award.objects.all()
    skill = Skill.objects.all()
    header = Header.objects.all()
    return render(request, 'home_app/index.html', context={'work': work, 'award': award, 'skill': skill, 'header': header})
