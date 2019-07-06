from django.shortcuts import render

# Create your views here.

def index(request):
    args = {
        'heading' : 'Home Page',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vitae molestiae tenetur rerum vel repudiandae, sint reprehenderit! Perferendis est quaerat esse labore. Nesciunt voluptatibus, in animi velit inventore veniam veritatis dicta.'
    }
    return render(request, 'themes/index.html', context = args)

def about(request):
    args = {
        'heading' : 'About Us',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium at recusandae ut eligendi accusamus et delectus qui reiciendis necessitatibus, cupiditate quis eos blanditiis. Iste, fugit optio aspernatur impedit numquam accusamus.'
    }

    return render(request, 'themes/about.html', context=args)
