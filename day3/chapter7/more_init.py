
class Post():

    user_publish = 'admin'

    def __init__(self, post_tile, post_img, post_content):
        self.post_tile = post_tile
        self.post_img = post_img
        self.post_content = post_content

    def site_post(self):
        return 'This is the post heading {} and this is the img {} and also the content {} it is published by {}'.format(self.post_tile, self.post_img, self.post_content, self.user_publish)

p1 = Post('Buhari travels again', 'buhar.jpg', 'loremscafafafafafaac')

print(p1.site_post())

p2 = Post('Osibanjo is VP', 'Osibanjo.png', 'loremipsum afafagagg')
print(p2.site_post())
