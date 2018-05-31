from django.shortcuts import render
from review_app import forms
from review_app.nlp_model import predict

# Create your views here.

def index(request):
    form = forms.Review()

    if request.method == "POST":
        form = forms.Review(request.POST)
        if form.is_valid():
            prediction = predict(form.cleaned_data['review'])
            label = ""
            if(prediction == 0):
                label = "Hope you like the food next time!"
                Class='red'
            else:
                label = "Thank you for the good review!"
                Class='green'
            return render(request, 'review_app/index.html', {'form': form, 'label': label, 'class': Class})

    return render(request, 'review_app/index.html', {'form': form})
