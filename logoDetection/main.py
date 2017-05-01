from kivy.app import App
from kivy.lang import Builder

class VisionTest(App):

    def build(self):
        return Builder.load_string('''
BoxLayout
    orientation: 'vertical'
    Camera
        id: camera
        resolution: 800, 600
        play: True
        allow_stretch: True
    Button
        size_hint_y: None
        height: dp(45)
        on_release: app.post_png()
    
''')

    def post_png(self):
        texture = self.root.ids.camera.texture
        texture.save('test.png', flipped=False)
        from detect import run_local
        run_local('test.png')


VisionTest().run()
