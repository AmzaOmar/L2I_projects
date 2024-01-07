from django.contrib.auth import get_user_model, login ,authenticate ,logout
from django.shortcuts import redirect, render


from Acceuil import views

def menu(request):
    return render(request,'Connexion/menu.html')

User = get_user_model()

def inscription(request):  #la fonction de connexion
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        universite = request.POST.get("universite")
        ufr = request.POST.get("ufr")
        numero_carte = request.POST.get("numero_carte")
        region = request.POST.get("region")
        date_naissance = request.POST.get("date_naissance")
        numero_telephone = request.POST.get("numero_telephone")

        if password1 == password2:  #crreation de l'utilisateur
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                nom=nom,
                prenom=prenom,
                universite=universite,
                ufr=ufr,
                numero_carte=numero_carte,
                region=region,
                date_naissance=date_naissance,
                numero_telephone=numero_telephone
            )
            login(request, user)
            return redirect('acceuil')

    return render(request, 'Connexion/inscription.html')

def connexion(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None and user.is_active:
            login(request, user)
            return redirect("acceuil")
        else:
            error_message = "Identifiants invalides. Veuillez réessayer."
            return render(request, 'Connexion/connexion.html', {'error_message': error_message})
    
    return render(request, 'Connexion/connexion.html')


def deconnexion(request):
    logout(request)
    return redirect("acceuil")