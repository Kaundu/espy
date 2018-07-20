from .models import Image

# Create your views here.

def index(request):
    images = Image.get_images()
    a = images[0::4]
    b = images[1::4]
    c = images[2::4]
    d = images[3::4]
    return render(request, 'index.html',locals())
def image(request,image_id):
    image = Image.objects.get(id=image_id)
    return render (request, 'image.html', {"image":image})