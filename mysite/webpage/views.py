from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import restaurant, restaurant_menu
from django.contrib.auth.decorators import login_required
from myreview.models import Review
# Create your views here.
# @login_required(login_url='login')
def index(request):
    """ หน้าหลักแสดงร้านอาหารที่มีทั้งหมด """

    # เป็นตัวแปรเพื่อรับค่าค้นหานั้นมา (Frame)
    search_restaurant = request.GET.get('search_restaurant', '')
    # เป็นตัวแปรที่ดึงข้อมูลจาก models restaurant (Frame)
    restaurantfo = restaurant.objects.all()

    # ถ้ามีการค้นหาจะเรียกเงื่อนไขนี้มาทำแล้วแสดงข้อมูลตาม keyword ที่หาไป (Frame)
    if request.method == 'GET':
        if search_restaurant != '':
            restaurantfo = restaurant.objects.filter(restaurant_name__icontains=search_restaurant)
    
    # แปลงเพื่อไปใช้บนหน้า html (Frame)
    context = {
        'search_restaurant': search_restaurant,
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)

def index_type(request, type_id):
    """ แสดงตามประเภท """
    # เป็นตัวแปรเพื่อรับค่าค้นหานั้นมา (Frame)
    search_restaurant = request.GET.get('search_restaurant', '')
    # เป็นตัวแปรที่ดึงข้อมูล models restaurant ที่เอาข้อมูลแค่ประเภทของร้านอาหารนั้นๆ (Frame)
    restaurantfo = restaurant.objects.filter(restaurant_type_id_id=type_id)

    if request.method == 'GET':
        if search_restaurant != '':
            restaurantfo = restaurant.objects.filter(restaurant_name__icontains=search_restaurant)
    # แปลงเพื่อไปใช้บนหน้า html (Frame)
    context = {
        'search_restaurant': search_restaurant,
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)


# หน้ารายละเอียดนี่ยังไม่ได้ทำนะครับ (Frame)
def res_detail(request, restaurant_id):
    """ ดูรายละเอียดข้องร้านอาหาร และ มีปุ่มจองร้านอาหาร """
    if request.method == "POST":
        review = request.POST.get('review', '')
        print(review)
        if review != '':
            reviewjing = Review.objects.create(comment=review,user=request.user,restaurant_id=restaurant_id)

    
    review_list = Review.objects.filter(restaurant__id = restaurant_id)
    review_count = len(review_list)
    restaurantdt = restaurant.objects.get(pk=restaurant_id)
    menushow = restaurant_menu.objects.filter(restaurant_id_id=restaurant_id)
    context = {
        'restaurantdt': restaurantdt,
        'menushow': menushow,
        'review_list': review_list,
        'review_count': review_count,
    }
    return render(request, 'webpage/detail.html', context=context)