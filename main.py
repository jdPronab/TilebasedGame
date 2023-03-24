from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import (Line,
                           Color,
                           Rectangle)
from kivy.properties import NumericProperty

class Tile(Widget):
    def __init__(self, pos, size, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.size  = size
        self.pos = pos
        with self.canvas:
            Color(*self.color)
            Rectangle(pos=self.pos, size=self.size)



class GameWidget(Widget):
    window_equivalent_height = NumericProperty()
    window_equivalent_width = NumericProperty()

    world_size = [50, 50]

    vlines = []
    hlines = []

    tile_colors = [(1, 0, 0), (0, 0, 1)]
    tile_size = 40

    tiles = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"From init - Height: {self.height}, Width: {self.width}")

        self.init_lines()

        self.map = self.generate_tilemap(1, 10)

        #self.update_tile()
        self.render_map()

        #self.prepare_map()
        #self.generate_map()

    def resize(self, *args):
        pass

    def on_size(self, w, t):
        print(self.size)
        print(f"Height: {self.height}, Width: {self.width}")

        self.draw_line(self.width, self.height)
        self.update_tile(self.width, self.height)
        self.render_map()

    def init_lines(self):
        with self.canvas:
            Color(1, 0, 0)
            for i in range(10):
                self.vlines.append(Line())
            for i in range(10):
                self.hlines.append(Line())

    def draw_line(self, width, height):
        for i in range(len(self.vlines)):
            self.vlines[i].points = [ i * 10, height, i * 10, 0]
        for i in range(len(self.hlines)):
            self.hlines[i].points = [ 0, i * 10, width, i * 10 ]

    def prepare_map(self):
        for i in range(world_size[0]):
            if i % 2 == 0:
                color = self.tile_colors[0]
            else:
                color = self.tile_colors[1]
            x = self.x + self.tile_size * i
            y = self.y + self.tile_size * i
            pos = (x, y)
            self.tiles.append(Tile(pos, (self.tile_size, self.tile_size), color))

    def generate_map(self):
        for tile in self.tiles:
            self.add_widget(tile)

    def generate_tilemap(self, width, height):
        map = []
        for x in range(width):
            row = []
            for y in range(height):
                if y % 2 == 0:
                    row.append(0)
                else:
                    row.append(1)
            map.append(row)

        return map

    def update_tile(self, width, height):
        for i in range(len(self.map)):
            row = []
            for j in range(len(self.map[0])):
                x = j * self.tile_size
                y = height -  (i * self.tile_size)
                print(f'y position: {y}')
                pos = (x, y)
                size = (self.tile_size, self.tile_size)
                if self.map[i][j] == 0:
                    row.append(Tile(pos, size, self.tile_colors[0]))
                elif self.map[i][j] == 1:
                    row.append(Tile(pos, size, self.tile_colors[1]))
            self.tiles.append(row)

    def render_map(self):
        self.clear_widgets()
        for row in self.tiles:
            for tile in row:
                self.add_widget(tile)



    def update_map(map):
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 0:
                    color = self.tile_colors[0]
                    map[i][j] = Tile(color)





# Sharon Zeliang
class GameApp(App):
    pass

if __name__ == "__main__":
    game = GameApp()
    game.run()
