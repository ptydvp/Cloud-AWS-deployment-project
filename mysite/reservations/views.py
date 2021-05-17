from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from reservations.models import myreservation, reservation_accepted
from webpage.models import restaurant

# Create your views here.



@permission_required('reservations.add_myreservation')
def start_reservation(request, restaurant_id):
    """ จองร้านอาหาร """
    restaurantrv = restaurant.objects.get(pk=restaurant_id)
    msg = ''
    if request.method == "POST":
        reservationcreat = myreservation.objects.create(
            person=request.POST.get("person"),
            reser_day=request.POST.get("reser_day"),
            reser_time=request.POST.get("reser_time"),
            reser_as=request.POST.get("reser_as"),
            contact=request.POST.get("contact"),
            user=request.user,
            restaurant_id=restaurant_id)
        msg = 'สร้างคำจองเสร็จแล้ว'
        reser_accepted = reservation_accepted.objects.create(reser_status="Pending",reservation=reservationcreat)

    context = {
        'restaurantrv': restaurantrv,
        'msg': msg,
        # 'reservationcreat': reservationcreat,
    }

    return render(request, 'reservations/reservation.html', context=context)


def res_reservation_show(request):
    myreser = myreservation.objects.filter(restaurant__own_by=request.user).order_by('-reservation_date')
    context = {
        'myreser': myreser,
    }
    return render(request, 'reservations/show_reser.html', context=context)

def res_reservation_accepted(request, reservation_id):
    reser_acc = reservation_accepted.objects.get(reservation_id=reservation_id)
    reser_acc.reser_status = "Accepted"
    reser_acc.save()

    return redirect('/show_myreser/')

def res_reservation_rejected(request, reservation_id):
    reser_acc = reservation_accepted.objects.get(reservation_id=reservation_id)
    reser_acc.reser_status = "Rejected"
    reser_acc.save()

    return redirect('/show_myreser/')

def res_reservation_cancel(request, reservation_id):
    reser_acc = reservation_accepted.objects.get(reservation_id=reservation_id)
    reser_acc.reser_status = "Cancel"
    reser_acc.save()

    return redirect('/show_cus_reser/')

def cus_reservation(request):
    myreser = myreservation.objects.filter(user=request.user).order_by('-reservation_date')
    context = {
        'myreser': myreser,
    }
    return render(request, 'reservations/show_cus_reser.html', context=context)
