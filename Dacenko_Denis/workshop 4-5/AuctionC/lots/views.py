from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post, Bid
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    data = dict()
    data['title'] = 'My Lots'
    current_user = request.user
    # if Post.objects.get(id=current_user.id):
    # print(Post.objects.get(id=current_user.id))
    # print(current_user.id)
    data['posts'] = Post.objects.all().filter(user=current_user.id)
    return render(request, 'lots/index.html', context=data)

def create(request):
    data = dict()
    data['title'] = 'Add Lots'
    if request.method == "GET":
        data['form'] = PostForm()
        return render(request, 'lots/create.html', context=data)
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/lots')

def check(request, post_id):
    data = dict()
    data['title'] = 'Check Lots'
    if request.method == "GET":
        data['post'] = Post.objects.get(id=post_id)
        try:
            bi = Bid.objects.filter(status='W', auct=post_id)
            data['bigb'] = bi.get()
        except ObjectDoesNotExist:
            data['post'] = Post.objects.get(id=post_id)
        return render(request, 'lots/check.html', context=data)
    if request.user.is_authenticated:
        if request.method == 'POST':
            amount = request.POST['bid']
            try:
                float(amount)
            except:
                data['report_x'] = "You should input digits."
                return render(request, 'accounts/reports.html', context=data)
            auct = Post.objects.filter(id=post_id)
            if auct:
                auct = Post.objects.get(id=post_id)
            if auct.min_price - float(amount) > 0:
                    data['report_x'] = "You have to place bet higher or the same as starting price."
                    return render(request, 'accounts/reports.html', context=data)
            prev_bid_wining = Bid.objects.filter(status='W', auct=auct)
            if prev_bid_wining:
                prev_bid_wining = Bid.objects.filter(status='W', auct=auct).get()
            if prev_bid_wining:
                if prev_bid_wining.user == request.user:
                    data['report_x'] = "You are already wining this auction."
                    return render(request, 'accounts/reports.html', context=data)
                if float(amount) - prev_bid_wining.amount < 1:
                    data['report_x'] = "Bid has to be at least bigger for 1$ than previous bids."
                    return render(request, 'accounts/reports.html', context=data)
                prev_bid_wining.status = 'L'
                prev_bid_wining.save()
            b = Bid(user=request.user, amount=float(amount), auct=auct, status='W')
            b.save()
            user = auct.user
            image = auct.image
            description = auct.description
            title = auct.title
            set = auct.set
            author = auct.author
            lot = Post(id=post_id, user=user, image=image, description=description, title=title, set=set, author=author)
            lot.min_price = float(amount)
            lot.save()
            return redirect(f'/lots/check/{post_id}')
            # bb = Bid.objects.filter(status='W', auct=auct)
            # bigb ={'bb': bb,'au':auct}
            # t = loader.get_template(f'lots/all_lots.html')
            # return HttpResponse(t.render(bigb), content_type="text/html")
    else:
        return redirect('/accounts/sign_in')

def edit(request, post_id):
    data = dict()
    data['title'] = 'Edit lots'
    post = Post.objects.get(id=post_id)
    # del ... ?
    if request.method == 'GET':
        data['form'] = PostForm2(instance=post)
        data['post'] = post
        return render(request, 'lots/edit.html', context=data)
    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        if form2.is_valid():
            post.title = form2.cleaned_data['title']
            post.set = form2.cleaned_data['set']
            post.condition = form2.cleaned_data['condition']
            post.description = form2.cleaned_data['description']
            post.finish_date = form2.cleaned_data['finish_date']
            post.save()
            # update ?
        return redirect('/lots')

def remove(request, post_id):
    data = dict()
    data['title'] = 'Remove Lot'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        data['post'] = post
        return render(request, 'lots/remove.html', context=data)
    elif request.method == 'POST':
        post.delete()
        return redirect('/lots')

def all_lots(request):
    data = dict()
    current_user = request.user
    data['title'] = 'All Lots'
    data['bigb'] = Bid.objects.all()
    data['posts'] = Post.objects.all().exclude(user=current_user.id)
    return render(request, 'lots/all_lots.html', context=data)
