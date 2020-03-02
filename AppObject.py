class AppObject:

    def on_init(self, postion, surface, hover_func, click_func):
        self.postion = self.x, self.y = postion
        self.surface = surface
        self.hover_func = hover_func
        self.click_func = click_func

    def show(self): pass
    def on_hover(self): pass
    def is_hovered(self): pass
    def is_clicked(self): pass
    def on_click(self): pass