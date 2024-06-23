class Sports(object):
    def __init__(self,favorite,dislike,college,hobby_sports):
        self.favorite = favorite
        self.dislike = dislike
        self.college = college
        self.hobby_sports = hobby_sports

    def elemental_school(self):
        print(f'小学校の頃は{self.favorite}をやっていました。')
        print(f'{self.dislike}もやっていましたが、続きませんでした。')

    def junior_school(self):
        print(f'中学校の頃は{self.favorite}をやっていました。')

    def high_school(self):
        print(f'高校生の頃は{self.favorite}をやっていました。')

    def college_school(self):
        print(f'大学生は{self.college}をやっていました')

class Hobby(Sports):
    def my_hobby(self):
        print(f'私の趣味は{self.hobby_sports}です。')


sports = Sports('サッカー','野球','ラクロス','筋トレ')

sports.elemental_school()

hobby = Hobby('サッカー','野球','ラクロス','筋トレ')
hobby.my_hobby()


# 属性の参照
print(f"Favorite sport: {sports.favorite}")
print(f"Disliked sport: {sports.dislike}")
print(f"College sport: {sports.college}")
print(f"Hobby sport: {sports.hobby_sports}")

# Hobbyインスタンスからの属性参照
print(f"Favorite sport (Hobby): {hobby.favorite}")
print(f"Disliked sport (Hobby): {hobby.dislike}")
print(f"College sport (Hobby): {hobby.college}")
print(f"Hobby sport (Hobby): {hobby.hobby_sports}")