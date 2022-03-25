from django.shortcuts import render
from .models import ClassInfo, Student, StudentPost, PostLike
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import StudentLintSerializer, StudentDetailsSerializer, StudentPostSerializer
from rest_framework.utils import json
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User, Group

def student(requset,class_input):

    data = ClassInfo.objects.filter(Class=class_input)
    # data = Student.objects.filter().all()
    # data = Student.objects.filter().last()  # only last value
    # data = Student.objects.filter().first()  # only first value
    # data = Student.objects.filter(religion='Islam')  #only show islam
    # data = Student.objects.filter().exclude(religion='Hindu') # don't show that data

    return render(requset, 'students.html', {'i': data})

def student_index(requset):
    return render(requset, 'student_index.html')

def student_list(request):
    return render(request, 'student_list.html')

def IsStudentGroup(user):
    user = User.objects.filter(id=user).first()
    return user.groups.filter(name="Student_Group").exists()


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and IsStudentGroup(request.user.id))

class ApiList(ListAPIView):
    permission_classes = [IsStudent]
    def get(self, request):
        name = request.GET.get('name')
        from django.db.models import Q
        # list_data = Student.objects.filter()[0:5]
        # list_data = Student.objects.filter(fee__lt=1700).all()
        list_data = Student.objects.filter()
        if name:
            list_data = list_data.filter(Q(full_name__icontains=name) | Q(father_name__icontains=name) | Q(user__username__icontains=name)).all()
        list_data = StudentLintSerializer(list_data, many=True).data
        return Response(list_data)

def student_details(request, id):
    return render(request, 'student_details.html')

class ApiDetails(ListAPIView):
    permission_classes = []
    def get(self, request, id):
        details_data = Student.objects.filter(id=id).first()
        details_data = StudentDetailsSerializer(details_data).data
        return Response(details_data)

def student_sing_up(request):
    return render(request, "student_sing_up.html")

def student_sing_in(request):
    return render(request, "student_sing_in.html")

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import random

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = '465'
    sender_email = 'django2077@gmail.com'
    sender_password = '2077dj007'
    server = None

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject


        html = """\
        <html>
            <head></head>
            <body>
        """
        html += body.replace('\r\n', '<br/>\r\n')
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg=msg.as_string())
        print("Mail Send")
    except Exception as ex:
        print(str(ex))
    finally:
        if server != None:
            server.quit()

from threading import Thread

def thread_send_email(to, subject, body):
    thread = Thread(target=send_email, args=(to, subject, body))
    thread.start()

class ApiSingUp(CreateAPIView):
    permission_classes = []
    def post(self, request):
        result = {}
        try:
            data = request.data
            if 'full_name' not in data or data['full_name'] == '':
                result['massage'] = "Full name can not be null."
                result['error'] = "Full Name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'father_name' not in data or data['father_name'] == '':
                result['massage'] = "Father name can not be null."
                result['error'] = "Father name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'mother_name' not in data or data['mother_name'] == '':
                result['massage'] = "Mother name can not be null."
                result['error'] = "Mother name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'gender' not in data or data['gender'] == '':
                result['massage'] = "Gender can not be null."
                result['error'] = "Gender"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'religion' not in data or data['religion'] == '':
                result['massage'] = "Religion can not be null."
                result['error'] = "Religion"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'birth_date' not in data or data['birth_date'] == '':
                result['massage'] = "Birth date can not be null."
                result['error'] = "Birth date"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'address' not in data or data['address'] == '':
                result['massage'] = "Address date can not be null."
                result['error'] = "Address"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'blood_group' not in data or data['blood_group'] == '':
                result['massage'] = "Blood group can not be null."
                result['error'] = "Blood group"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'nationality' not in data or data['nationality'] == '':
                result['massage'] = "Nationality can not be null."
                result['error'] = "Nationality"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'phone' not in data or data['phone'] == '':
                result['massage'] = "Phone can not be null."
                result['error'] = "Phone"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            if not user:
                user = User()
                user.username = data['email']
                user.full_name = data['full_name']
                user.father_name = data['father_name']
                user.mother_name = data['mother_name']
                user.gender = data['gender']
                user.religion = data['religion']
                user.birth_date = data['birth_date']
                user.address = data['address']
                user.blood_group = data['blood_group']
                user.nationality = data['nationality']
                user.email = data['email']
                user.phone = data['phone']
                user.password = make_password(data['password'])
                # user.profile_picture = data['profile_picture']
                user.is_active = False
                user.save()
                random_number = random.randint(6000, 9999)
                student = Student()
                student.full_name = data['full_name']
                student.father_name = data['father_name']
                student.mother_name = data['mother_name']
                student.gender = data['gender']
                student.religion = data['religion']
                student.birth_date = data['birth_date']
                student.address = data['address']
                student.blood_group = data['blood_group']
                student.nationality = data['nationality']
                student.email = data['email']
                student.phone = data['phone']
                student.otp = random_number
                student.user = user
                try:
                    if 'profile_picture' in data:
                        print("test")
                        if data['profile_picture']!='' and request.FILES['profile_picture']:
                            student.profile_picture = request.FILES['profile_picture']
                except:
                    return Response("Please prvide a valide image")
                student.save()
                thread_send_email(data['email'], 'your OTP', 'OTP : '+str(random_number))
                result={}
                result['status']=HTTP_200_OK
                result['message']="Success"
                result['email']=data['email']
                return Response(result)

        except Exception as ex:
            return Response(str(ex))
        return Response("True")

class ApiOTPCheck(CreateAPIView):
    permission_classes = []
    def put(self, request):
        result = {}
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            
            if 'otp' not in data or data['otp'] == '':
                result['massage'] = "otp can not be null."
                result['error'] = "OTP"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            if not user:
                
                result['message'] = "Please create a account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            
            elif user.is_active:
                
                result['message'] = "You already created account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            
            else:
                
                student = Student.objects.filter(user=user).first()
                if student.otp==data['otp']:
                    user.is_active=True
                    user.save()
                    student.otp=''
                    student.save()
                    result['message'] = "Success."
                    result['status'] = HTTP_200_OK
                    return Response(result)

                else:
                    
                    result = {}
                    result['status'] = HTTP_400_BAD_REQUEST
                    result['message'] = "OTP did not match."
                    result['Error'] = "OTP"
                    return Response(result)

        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)

from django.contrib.auth.hashers import check_password

class SignInAPI(ListAPIView):
    permission_classes = []
    def post(self, request,*args, **kwargs):
        result={}
        try:
            data = json.loads(request.body)
            print(data)
            if 'email' not in data or data['email'] == '':
                result['message'] = "Email can not be null."
                result['Error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password'] == '':
                result['message'] = "Password can not be null."
                result['Error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            print(user.is_active)
            if not user:
                result['message'] = "Please create a account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            elif not user.is_active:
                result['message'] = "Please active your account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            else:
               if not check_password(data['password'], user.password):
                   result['message'] = "Invalid Credentials"
                   return Response(result, status=HTTP_401_UNAUTHORIZED)
               else:
                student = Student.objects.filter(user=user).first()
                from rest_framework_simplejwt.tokens import RefreshToken
                token = RefreshToken.for_user(user)
                data = {}
                data['user_name'] = user.username
                data['access'] = str(token.access_token)
                data['token'] = str(token)
                data['status'] = HTTP_200_OK

                return Response(data)
        except Exception as e:
            result = {}
            result['message'] = str(e)
            return Response(result)


def student_post(request):
    return render(request, "student_post.html")


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class StudentPostAPI(CreateAPIView):

    permission_classes = [IsUser]

    def post(self, request, *args, **kwargs):

        post_data = request.data
        student_post = StudentPost()
        student_post.user = request.user
        if ("post_text" not in post_data or post_data["post_text"] == "") and ("post_picture" not in request.FILES or request.FILES["post_picture"]):
            return Response("Please enter something")
        if "post_text" in post_data and post_data["post_text"] != "":
            student_post.post_text = post_data["post_text"]
        if "post_picture" in request.FILES and request.FILES["post_picture"] != "":
            student_post.post_picture = request.FILES["post_picture"]
        student_post.save()
        return Response("Success")


class StudentPostlistAPI(ListAPIView):
    permission_classes = []

    def get(self, request):

        post_data = StudentPost.objects.filter().all()
        post_data = StudentPostSerializer(post_data, many=True).data
        return Response(post_data)


class StudentPostLikeAPI(CreateAPIView):
    permission_classes = [IsUser]

    def put(self, request):

        like_data = request.data
        post_like = PostLike()
        post_like.user = request.user
        post_like.post = like_data["id"]
