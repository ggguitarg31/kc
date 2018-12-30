from django.shortcuts import render
from .models import Clothes, ClothesCategory
# from .filters import BtnFilter


def clothes(request):
    # btn_categories = ButtonCategory.objects.all()
    clothes = Clothes.objects.all()
    return render(request, 'clothes.html', {'clothes': clothes})
    # return render(request, 'main/button_info.html', {'btn_categories': btn_categories})
