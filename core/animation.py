import math


class Animation:

    def __init__(self):

        self.finished = True

        self.elapsed = 0.0

        self.duration = 0.0

        self.start_x = 0
        self.start_y = 0

        self.end_x = 0
        self.end_y = 0

        self.current_x = 0
        self.current_y = 0

        self.callback = None

    # =====================================================

    def start(

        self,

        start_pos,

        end_pos,

        duration=0.3,

        callback=None

    ):

        self.start_x, self.start_y = start_pos

        self.end_x, self.end_y = end_pos

        self.current_x = self.start_x
        self.current_y = self.start_y

        self.duration = duration

        self.elapsed = 0.0

        self.finished = False

        self.callback = callback

    # =====================================================

    def update(self, dt):

        if self.finished:

            return

        self.elapsed += dt

        t = self.elapsed / self.duration

        if t > 1:

            t = 1

        # Ease Out Cubic

        t = 1 - pow(1 - t, 3)

        self.current_x = (

            self.start_x +

            (self.end_x - self.start_x) * t

        )

        self.current_y = (

            self.start_y +

            (self.end_y - self.start_y) * t

        )

        if self.elapsed >= self.duration:

            self.finished = True

            self.current_x = self.end_x
            self.current_y = self.end_y

            if self.callback:

                self.callback()

    # =====================================================

    def position(self):

        return (

            int(self.current_x),

            int(self.current_y)

        )

    # =====================================================

    def is_playing(self):

        return not self.finished

    # =====================================================

    def stop(self):

        self.finished = True

    # =====================================================

    def reset(self):

        self.finished = True

        self.elapsed = 0.0

        self.duration = 0.0

        self.current_x = 0
        self.current_y = 0

    # =====================================================

    @staticmethod
    def ease_in_out(t):

        return -(math.cos(math.pi * t) - 1) / 2

    # =====================================================

    @staticmethod
    def linear(t):

        return t

    # =====================================================

    @staticmethod
    def ease_out(t):

        return 1 - (1 - t) * (1 - t)

    # =====================================================

    @staticmethod
    def ease_in(t):

        return t * t