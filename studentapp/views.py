from django.shortcuts import render,redirect
from nouapp.models import Student,Login
from django.views.decorators.cache import cache_control #Used to go out from login session 
from . models import StuResponse,Question,Answer
from datetime import date
from django.contrib import messages
from adminapp.models import Material

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True) #cache cannot be used jitni bhi baar load hoga har baar revalidate hoga aur cache ko store nhi karega
def studenthome(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"studenthome.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
def logout(request):
    try:
        del request.session['rollno']
    except KeyError:
       return redirect('nouapp:login')
    return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno'] #session is used to get all recoords of model from given app
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                responsedate=date.today()
                sr=StuResponse(rollno=stu.rollno,name=stu.name,program=stu.program,branch=stu.branch,year=stu.year,contactno=stu.contactno,emailaddress=stu.emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,responsedate=responsedate)
                sr.save()
                messages.success(request,"Your Response is Submitted")
        return render(request,"response.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postquestion(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=date.today()
                pq=Question(question=question,postedby=postedby,posteddate=posteddate)
                pq.save()
            pq=Question.objects.all()
            return render(request,"postquestion.html",{'stu':stu,'pq':pq})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"postanswer.html",{'stu':stu,'qid':qid})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postans(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answeredby=stu.name
            posteddate=date.today()
            ans=Answer(answer=answer,answeredby=answeredby,posteddate=posteddate,qid=qid)
            ans.save()
            return redirect('studentapp:postquestion')
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)
            return render(request,"viewanswer.html",{'stu':stu,'ans':ans})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def changepassword(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                presentpassword=Login.objects.get(userid=rollno)
                if oldpassword==presentpassword.password:
                    if oldpassword!=newpassword:
                        if newpassword==confirmpassword:
                            Login.objects.filter(userid=rollno).update(password=newpassword)
                            messages.success(request,"Password Changed Successfully!!!")
                            return redirect('studentapp:logout')
                        else:
                            messages.warning(request,"New Password and Confirm Password must be Same")
                    else:
                        messages.warning(request,"Old Password and New Password cannot be same")
                else:
                    messages.warning(request,"Old Password is not Correct")
            return render(request,"changepassword.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def viewprofile(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                return redirect('studentapp:profilemanagement')
            return render(request,"viewprofile.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def profilemanagement(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                contactno=request.POST['contactno']
                emailaddress=request.POST['emailaddress']
                address=request.POST['address']
                Student.objects.filter(rollno=rollno).update(contactno=contactno,emailaddress=emailaddress,address=address)
                return redirect('studentapp:viewprofile')
            return render(request,"profilemanagement.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True) #cache cannot be used jitni bhi baar load hoga har baar revalidate hoga aur cache ko store nhi karega
def viewmat(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            # stu=Student.objects.all()
            mat=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year)
            # mat=Material.objects.all()
            return render(request,"viewmat.html",locals())
    except KeyError:
        return redirect('nouapp:login')