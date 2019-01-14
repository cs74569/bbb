from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html')
def login(request):
    '''
    Render the Login page
    '''
    return render(request, 'login/login.html')
def connect(request):
    '''
    Render the connect page
    '''
    return render(request, 'connect/connect.html')
def create(request):
    '''
    Render the create page
    '''
    return render(request, 'create/create.html')
def add(request):
    '''
    Render the add page
    '''
    return render(request, 'add/add.html')
def logined(request):
    '''
    Render the logined page
    '''
    return render(request, 'logined/logined.html')
def loginedconnect(request):
    '''
    Render the loginedconnect page
    '''
    return render(request, 'loginedconnect/loginedconnect.html')
