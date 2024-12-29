from django.contrib import admin
from .models import Movie, Showtime, MovieChain, MovieLocation

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'image_preview', 'cookie_status', 'naver_link')
    search_fields = ('title', 'naver_link')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return "No Image"
    image_preview.allow_tags = True

class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'show_date', 'show_time', 'location', 'end_time')  # end_time을 추가
    list_filter = ('movie', 'location')  # 영화와 장소로 필터링 가능
    search_fields = ('movie__title',)  # 영화 제목으로 검색 가능

    def end_time(self, obj):
        return obj.end_time  # end_time은 프로퍼티로 자동 계산되므로 호출하여 표시

# Movie 모델을 MovieAdmin과 함께 등록
admin.site.register(MovieChain)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(MovieLocation)  # MovieLocation 모델도 등록
