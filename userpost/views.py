from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter] # SearchFilter를 기반으로 검색할거임
    search_fields = ('title',)  # 어떤 칼럼을 기반으로 검색할것인지 => 튜플이라 무조건 , 넣기


    def get_queryset(self):
        qs = super().get_queryset()
        # 지금 만약 로그인이 되어있다면 -> 로그인한 유저의 글만 필터링
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
            # 만약 로그인이 안되어있다면 -> 비어있는 쿼리셋을 리턴
        else:
            qs = qs.none()
        return qs
    # queryset을 기반으로 조작할 떄 -> 변수에 직접 접근 x
    # get_queryset 메서드를 만들어서 거기서 조작
    # super클래스 = 부모 클래스
    # .filter 또는 .exclude 사용