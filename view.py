def index(request):

    contact = ContactForm()
    testimony = Testimony()

    all_post = Posts.objects.all()[:3]
    args = {
        'contact':contact,
        'testimony':testimony,
        'post':all_post
    }

    return render(request, 'themes/index.html', context=args)

def detail(request, post_id):
    try:
        detail_post = Posts.objects.get(pk=post_id)
    except Posts.DoesNotExist:
        raise Http404('Posts does not exist')
    return render(request, 'themes/detail.html', {'detail':detail_post})
