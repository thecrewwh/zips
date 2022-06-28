class HostedMediaFile():
  def __init__(self, name):
        self.name = name 
     
  def valid_url(self):
     if 'bit.ly' in self.name:
       return False
     else:
       return True
