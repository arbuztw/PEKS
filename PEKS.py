from charm.toolbox.pairinggroup import ZR,G1,G2,pair
from charm.toolbox.hash_module import Hash

class PEKSClient:
   def __init__(self, grpObj):
      global group, h2
      group = grpObj
      h2 = Hash('sha1', group)

   def KeyGen(self):
      g = group.random(G1)
      self.priv = group.random(ZR)
      self.pub = (g, g * self.priv)
      return self.pub

   def PEKS(self, word):
      g, h = self.pub
      r = group.random(ZR)
      t = pair(group.hash(word, G1), h * r)
      return (g * r, h2.hashToZn(t))

   def Trapdoor(self, word):
      return group.hash(word, G1) ** self.priv


class PEKSServer:
   def __init__(self, grpObj, pub):
      global group, h2
      group = grpObj
      h2 = Hash('sha1', group)
      self.pub = pub

   def Test(self, s, tw):
      a, b = s
      return h2.hashToZn(pair(tw, a)) == b

