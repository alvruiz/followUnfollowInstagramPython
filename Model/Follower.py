class InstaInfo:
  def __init__ (self, title, media_list_data, string_list_data):
    self.title = title;
    self.media_lista_data = media_list_data;
    self.string_lista_data = User(**string_list_data[0]);

class User:
  def __init__ (self, href, value, timestamp):
    self.href = href;
    self.value = value;
    self.timestamp = timestamp;

