""" Class for poker chip objects.

    Used for digital betting purposes in poker game

    """

class Chip(object):

  # Known chip denominations
  denom = [100, 500, 1000, 5000, 10000]

  """ Initialize a chip; chips have one of the values in denom. Default denom
      is the basic chip ($100).

      Note - self.denom is an INDEX for Chip.denom list (above).

      """
  def __init__(self, denomination=0):
    self.denom = denomination

  def __str__(self):
    return("%d" %Chip.denom(self.denom))

  # Basic operations (addition and subtraction)

