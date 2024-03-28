  def __init__(self, message, selected):
        """Initialise color object with specified text and selected color."""
        self._msg = message
        self._color = COLORS[selected]

    def __str__(self):
        return self._color + self._msg + COLORS["end"]

    def __add__(self, other):
        return str(self) + other
#yes
    def __radd__(self, other):
        return other + str(self)

def get_data_directory():
    data_directory = os.getenv("TORBOT_DATA_DIR")
    # if a path is not set, write data to the config directory
    if not data_directory:
        data_directory = project_root_directory

    if data_directory.strip() == "":
        data_directory = project_root_directory

    # create directory if it doesn't exist
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)

    return data_directory
#work
