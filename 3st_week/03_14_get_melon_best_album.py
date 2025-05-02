# 1. genre_array 에서 genre 별로 재생횟수를 모두 모아서 비교한다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣는다.
# 2. 많이 재생된 장르 별로 2곡을 넣어줄 때, 많이 재생된 노래 먼저 넣어줘야 한다.
# 3. 장르 내에서 재생횟수가 같다면, 고유 번호가 낮은 노래 먼저 수록해야 한다.


# answer
#
def get_melon_best_album(genre_array, play_array):
    # 1. dict 에 장르별로 얼마나 재생횟수를 가지고 있는가
    # 2. dict 에 장르별로 어느 인덱스에 재생횟수를 가지고 있는가

    n = len(genre_array)
    genre_total_dict = {}
    genre_index_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_dict:
            genre_total_dict[genre] += play
        else:
            genre_total_dict[genre] = play


    return []


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))