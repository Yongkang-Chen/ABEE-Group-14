# two parameters class for EnergyPlus simulation
class EnergyPlusParameter(object):
    # construction function
    def __init__(self):
        self.window_u_key = None
        self.window_SHGC_key = None
        self.window_u_values = None
        self.window_SHGC_values = None

    # set window U key and values
    def set_window_u_key_and_values(self, window_u_key, window_u_values, val_range):
        valid = True
        # Check whether all values are within the range
        for window_u_value in window_u_values:
            if window_u_value > val_range[1] or window_u_value < val_range[0]:
                valid = False
        if not valid:
            return False
        self.window_u_key = window_u_key
        self.window_u_values = window_u_values
        return True

    # set window SHGC key and values
    def set_window_SHGC_key_and_values(self, window_SHGC_key, window_SHGC_values, val_range):
        valid = True
        # Check whether all values are within the range
        for window_u_value in window_SHGC_values:
            if window_u_value > val_range[1] or window_u_value < val_range[0]:
                valid = False
        if not valid:
            return False
        self.window_SHGC_key = window_SHGC_key
        self.window_SHGC_values = window_SHGC_values
        return True

    # getter method of get U key and values
    def get_window_u_key_and_values(self):
        return self.window_u_key, self.window_u_values

    # getter method of get SHGC key and values
    def get_window_SHGC_key_and_values(self):
        return self.window_SHGC_key, self.window_SHGC_values