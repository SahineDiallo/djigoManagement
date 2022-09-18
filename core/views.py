from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms import PatientForm
from core.models import Patient

# Create your views here.


def dashboard(request):
    user = request.user
    context = {"user": user}
    return render(request, "core/index.html", context)


def create_patient(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST":
        print("the request is post")
        if form.is_valid():
            form.save()
            prenom = form.cleaned_data.get("prenom")
            nom = form.cleaned_data.get("nom")
            patient_name = f"{prenom} {nom}"
            messages.success(
                request, f"patient {patient_name}  a ete cree avec succes")
            return redirect("patients")
        else:
            print("the form is not valid")
            print(form.errors)

    context = {"form": form}
    return render(request, "core/create.html", context)


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    print("this is the patient name", patient.nom)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == "POST":
        if form.is_valid():
            if form.has_changed():
                form.save()
                if len(form.changed_data) > 1:
                    changed_fields = ", ".join(form.changed_data)
                    message = f"{changed_fields} ont ete modifies avec succes"
                else:
                    message = f"{form.changed_data[0]} a ete modifie avec succes"
                messages.success(request, message)
                return redirect("patients")
            return redirect("patients")
    context = {"form": form, "patient": patient}
    return render(request, "core/create.html", context)


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    context = {"patient": patient}
    return redirect("patients")


def patients(request):
    patients = Patient.objects.all()

    context = {"patients": patients}
    return render(request, "core/patients.html", context)
