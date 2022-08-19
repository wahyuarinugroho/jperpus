from django import forms
from django.forms import ModelForm, fields, widgets
from jperpustakaan.models import Buku
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        # fungsi exclude - menampilkan data selain yg dipanggil
        # exclude = ['penerbit','jumlah']
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class':'form-control','id':'input judul','placeholder':'input judul'}),
            'penulis': forms.TextInput({'class':'form-control','id':'input penulis','placeholder':'input penulis'}),
            'penerbit': forms.TextInput({'class':'form-control','id':'input penerbit','placeholder':'input penerbit'}),
            'jumlah': forms.NumberInput({'class':'form-control','id':'input jumlah','placeholder':'input jumlah'}),
            'kelompok_id': forms.Select({'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update ({
            'type':'text',
            'name':'username',
            'class':'form-control form-control-user',
            'id':'username',
            'placeholder':'Username'
        })
        self.fields['email'].widget.attrs.update ({
            'type':'email',
            'name':'email',
            'class':'form-control form-control-user',
            'id':'email',
            'placeholder':'Email Address'
        })
        self.fields['password1'].widget.attrs.update ({
            'type':'password',
            'name':'password1',
            'class':'form-control form-control-user',
            'id':'password1',
            'placeholder':'Password'
        })
        self.fields['password2'].widget.attrs.update ({
            'type':'password',
            'name':'password2',
            'class':'form-control form-control-user',
            'id':'password2',
            'placeholder':'Repeat Password'
        })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
