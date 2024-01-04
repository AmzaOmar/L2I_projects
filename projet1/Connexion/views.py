from django.contrib.auth import get_user_model, login ,authenticate ,logout
from django.shortcuts import redirect, render


from Acceuil import views

def menu(request):
    return render(request,'Connexion/menu.html')

User = get_user_model()

def inscription(request):
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

        if password1 == password2:  # Vérification des mots de passe
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
            # Redirection vers la page d'accueil
            return redirect( 'acceuil')  # Remplacez 'nom_de_la_vue_accueil' par le nom de votre vue d'accueil

    return render(request, 'Connexion/inscription.html')

def connexion(request):
    if request.method == "POST": # Si la requête est de type POST
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(email=email, password=password)
        
        if user is not None and user.is_active:
            # Si l'utilisateur est actif, le connecter
            login(request, user)
            return redirect("acceuil")  # Redirection vers la vue d'accueil
        else:
            # Gérer les erreurs d'authentification, par exemple afficher un message d'erreur
            error_message = "Identifiants invalides. Veuillez réessayer."
            return render(request, 'Connexion/connexion.html', {'error_message': error_message})
    
    # Si la requête n'est pas de type POST ou si l'authentification échoue, afficher la page de connexion
    return render(request, 'Connexion/connexion.html')


def deconnexion(request):
    logout(request)
    return redirect("acceuil")