from django.contrib import admin
from django.db import router
from django.urls import path, include
from jperpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from jperpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    path('user/hapus/<int:id_user>', hapus_user, name='hapus_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('export/xlsx', export_xlsx, name='export_xlsx'),
    path('user/', users, name='users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)