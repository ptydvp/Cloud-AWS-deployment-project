from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from webpage.models import restaurant, restaurant_menu, restaurant_type

# from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
@permission_required('webpage.add_restaurant') 
def Add_Restaurant(request):
    """ หน้าเพิ่มร้านอาหารใหม่ """
    # ตั้งค่าข้อความเป็นว่างไว้ก่อน (Frame)
    msg = ''
    # ดึงข้อมูล models restaurant_type มาโดยเรียงตาม id
    res_type = restaurant_type.objects.all().order_by('id')

    # ถ้ามีการเรียกใช้ฟอรมหรือป้อนส่งข้อมูลลงไปในฟอรมนี้ เงื่อนไขนี้จะเริ่มทำงาน (Frame)
    # ถ้ามีการกระทำเป็น POST จะเริ่มรับค่าสร้างร้านอาหาร
    if request.method == 'POST': 
        restaurantnew = restaurant.objects.create(
            restaurant_name=request.POST.get('restaurant_name'),
            seller_phone=request.POST.get('seller_phone'),
            desc=request.POST.get('desc'),
            restaurant_type_id_id=request.POST.get('restaurant_type_id'),
            location_address=request.POST.get('location_address'),
            picture=request.FILES.get('picture'),
            restaurant_status=request.POST.get('restaurant_status'),
            own_by_id = request.user.id
        )
        print(restaurantnew.picture)
        msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurantnew.restaurant_name)

    else:
        restaurantnew = restaurant.objects.none()

    context = {
        'restaurantnew': restaurantnew,
        'res_type': res_type,
        'msg': msg
    }
    return render(request, 'management/add_restaurant.html', context=context)

# def is_store(user):
#     return user.groups.filter(name='store').exists()

# @user_passes_test(is_store, redirect_field_name='index')
@login_required
@permission_required('webpage.add_restaurant') 
def add_menu(request, restaurant_id):
    """ เพิ่มเมนูอาหารให้ร้านอาหาร """

    try:
        restauranted = restaurant.objects.get(pk=restaurant_id)
        msg = ''
    except restaurant.DoesNotExist:
        return redirect(to='Management')


    # ถ้ามีการเรียกใช้ฟอรมหรือป้อนส่งข้อมูลลงไปในฟอรมนี้ เงื่อนไขนี้จะเริ่มทำงาน (Frame)
    if request.method == 'POST':
        restaurantmnu = restaurant_menu.objects.create(
            menu_name=request.POST.get('menu_name'),
            picture=request.FILES.get('picture'),
            menu_price=request.POST.get('menu_price'),
            restaurant_id_id=restaurant_id
        )
        msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurantmnu.menu_name)
    else:
        restaurantmnu = restaurant_menu.objects.none()

    context = {
        'restaurantmnu': restaurantmnu,
        'restauranted': restauranted,
        'msg': msg
    }
    return render(request, 'management/add_menu.html', context=context)


@login_required
@permission_required('webpage.add_restaurant') 
def Management(request):
    """ หน้าจัดการร้านอาหาร ที่สามารถเพิ่ม ลบ แก้ ร้านอาหารหรือประเภทได้ """
    user = User.objects.get(id=request.user.id)
    restaurantfo = restaurant.objects.filter(own_by=user)
    context = {
        'resinfo': restaurantfo
    }

    return render(request, 'management/management.html', context=context)

@login_required
@permission_required('webpage.add_restaurant') 
def restaurant_edit(request, restaurant_id):
    
    """ แก้ไขร้านอาหาร"""

    try:
        restauranted = restaurant.objects.get(pk=restaurant_id)
        res_type = restaurant_type.objects.all()
        msg = ''
    except restaurant.DoesNotExist:
        return redirect(to='Management')
    
    if request.method == 'POST':
        restauranted.restaurant_name = request.POST.get('restaurant_name')
        restauranted.desc = request.POST.get('desc')
        restauranted.location_address = request.POST.get('location_address'),
        restauranted.restaurant_type_id_id = request.POST.get('restaurant_type_id')
        restauranted.seller_phone = request.POST.get('seller_phone')
        restauranted.picture = request.FILES.get('picture')
        restauranted.restaurant_status = request.POST.get('restaurant_status')
        restauranted.save()
        msg = 'แก้ไขร้านอาหารสำเร็จแล้ว: %s' %(restauranted.restaurant_name)
    
    context = {
        'restauranted': restauranted,
        'res_type': res_type,
        'msg': msg
    }


    return render(request, 'management/edit_restaurant.html', context=context)

@login_required
@permission_required('webpage.add_restaurant') 
def restaurant_delete(request, restaurant_id):

    """ ลบร้านอาหาร """
    restaurantdl = restaurant.objects.get(pk=restaurant_id)
    restaurantdl.delete()

    return redirect(to='Management')
