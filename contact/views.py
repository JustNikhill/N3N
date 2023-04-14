from django.shortcuts import render


# Create your views here.
def contact(request):
    return render(request, 'contact.html')
# def About(request):
#     messageForm = MessageForm(request.POST or None)
#     if messageForm.is_valid():
#         data = messageForm.cleaned_data
#         Message.objects.create(name=data['name'], email=data['email'], text=data['text'])
#         text = f"{data['text']}\nEmail: {data['email']}"
#         send_mail(data['name'], text, 'messages@nimiology.ir', ['nimiologyy@gmail.com'], fail_silently=False)
#         messageForm = MessageForm()
#     context = {
#         'setting': Setting.objects.all().order_by('-id')[0],
#         'form': messageForm
#     }
#     return render(request, "StaticPages/contact.html", context=context)