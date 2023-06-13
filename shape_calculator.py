class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    return

  def __repr__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (self.width + self.height) * 2
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width**2 + self.height**2)**.5)
    return diagonal

  def get_picture(self):
    picture = {}
    res = []
    line = ''
    result = ''
    if self.width > 50:
      return "Too big for picture."
    if self.height > 50:
      return "Too big for picture."
    for i in range(self.height):
      picture[i] = []
      for n in range(self.width):
        picture[i] += ['*']
      res.append(picture[i])

    for x in range(self.height):
      line = ''.join(res[x])
      result += f'{line}\n'
    return result

  def get_amount_inside(self, shape):

    fit_w = self.width / shape.width
    fit_w = int(fit_w)
    if fit_w > 0:
      fit_h = self.height / shape.height
      fit_h = int(fit_h)
      fit = fit_h * fit_w
    else:
      fit = 0
    return fit


class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    super().__init__(side, side)

  def set_side(self, side):
    self.height = side
    self.width = side

  def __repr__(self):
    return f'Square(side={self.width})'
