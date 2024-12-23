# showtimes/admin.py
from django.contrib import admin
from .models import Movie, Showtime, MovieChain, MovieLocation

# Movie 모델을 Admin에 등록 (중복 제거)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'image_preview', 'naver_link')  # 이미지 미리보기
    search_fields = ('title', 'naver_link')  # 검색 필드에 네이버 링크도 추가


    def cookie_status_display(self, obj):
        return 'O' if obj.cookie_status else 'X'
    cookie_status_display.short_description = '쿠키 여부'  # '쿠키 여부'로 라벨 변경


    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'  # 이미지를 미리보기
        return "No Image"
    image_preview.allow_tags = True  # HTML 태그를 사용할 수 있도록 설정


class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'showtime')  # 'location'을 제거
    list_filter = ('movie',)  # 'location'을 제거


# Movie 모델을 MovieAdmin과 함께 등록
admin.site.register(MovieChain)
admin.site.register(Movie, MovieAdmin)  # MovieAdmin을 사용하여 Movie를 등록
admin.site.register(Showtime, ShowtimeAdmin)
