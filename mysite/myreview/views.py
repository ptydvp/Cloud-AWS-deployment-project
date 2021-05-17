from django.shortcuts import render, redirect
from webpage.models import restaurant
from myreview.models import Review
# Create your views here.

def delete_review(request, review_id):
    """ ลบรีวิว """

    reviewdl = Review.objects.get(pk=review_id)
    reviewdl.delete()

    return redirect(to='/detail/'+ str(reviewdl.restaurant_id))